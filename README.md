# Astroya — Microservice Thème Astral PDF

Microservice Flask qui génère un thème astral PDF personnalisé, l'héberge sur
Supabase Storage et enregistre la demande en base. Conçu pour Render (plan gratuit).

## Architecture

```
Page Astroya  ──POST /generate──►  Ce service (Render)
                                      │ 1. génère le PDF (WeasyPrint)
                                      │ 2. upload sur Supabase Storage
                                      │ 3. insère la ligne en table Supabase
                                      └─ renvoie { pdf_url }
Page Astroya  ──► Klaviyo (profil + abonnement avec pdf_url)
```

## Structure des fichiers

```
microservice/
├── app/
│   ├── main.py            ← application Flask (endpoint /generate)
│   ├── pdf_generator.py   ← génération du PDF (roue, graphiques, contenu)
│   ├── astro_chart.py     ← roue astrologique + graphiques SVG
│   ├── astro_symbols.py   ← pictogrammes planètes SVG
│   ├── signs_data.py      ← données des 12 signes
│   └── fonts/             ← polices El Messiri (.ttf)
├── requirements.txt
├── build.sh               ← build Render (deps + polices)
├── render.yaml            ← config déploiement Render
└── .gitignore
```

## Endpoint

`POST /generate`

En-tête : `X-Astroya-Key: <ASTROYA_API_KEY>`

Corps JSON :
```json
{
  "prenom": "Claire",
  "sun": "Lion", "moon": "Cancer", "asc": "Balance",
  "venus": "Vierge", "mars": "Scorpion",
  "email": "claire@example.fr",
  "date_naissance": "1990-08-12",
  "heure_naissance": "14:30",
  "ville": "Lyon",
  "newsletter": true
}
```

Réponse : `{ "pdf_url": "https://....pdf", "filename": "theme-astral-xxxx.pdf" }`

## Variables d'environnement (à configurer sur Render)

| Variable | Description |
|---|---|
| `ASTROYA_API_KEY` | Clé secrète partagée page ↔ service |
| `SUPABASE_URL` | https://xxxx.supabase.co |
| `SUPABASE_SERVICE_KEY` | Clé service_role Supabase (secrète) |
| `SUPABASE_BUCKET` | Nom du bucket (def: themes-astraux) |
| `SUPABASE_TABLE` | Nom de la table (def: themes_astraux) |
| `ALLOWED_ORIGIN` | https://www.astroya.fr |

## Table Supabase attendue

```sql
create table themes_astraux (
  id uuid default gen_random_uuid() primary key,
  prenom text,
  email text,
  date_naissance date,
  heure_naissance text,
  ville text,
  signe_soleil text,
  signe_lune text,
  signe_ascendant text,
  signe_venus text,
  signe_mars text,
  newsletter_opt_in boolean default false,
  pdf_url text,
  created_at timestamptz default now()
);
```

Bucket Storage public nommé `themes-astraux`.
