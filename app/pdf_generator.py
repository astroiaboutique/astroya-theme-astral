# -*- coding: utf-8 -*-
"""
Générateur de PDF de thème astral personnalisé — Astroya
Construit un HTML mis en page puis le convertit en PDF via WeasyPrint.
Polices : El Messiri (titres) + Poppins (sous-titres) + DejaVu/Arial-like (corps).
"""

import html as html_lib
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

from signs_data import (SIGNS, ELEMENT_THEMES, sign_index, dominant_element,
                        element_counts, modality_counts)
import astro_symbols as sym
import astro_chart as ac

# Palette Astroya (reprise de la page)
VIOLET = "#6b4c8a"
VIOLET_DARK = "#3d2c5a"
ROSE = "#b8849b"
OR = "#c9a96e"
OR_CLAIR = "#e8d4a8"
CREME = "#faf7f2"
CREME_ROSE = "#faf0ea"
TEXTE = "#2b2b3d"
TEXTE_DOUX = "#3a3a4d"

LOGO_URL = "https://www.astroya.fr/cdn/shop/files/logo_astroya_png.png?height=96&v=1721549421"
COLLECTION_URL = "https://www.astroya.fr/collections/collection-astrologie-zodiaque"

COFFRETS = {
    0: "coffret-cadeaux-bougie-bracelet-belier",
    1: "coffret-cadeaux-bougie-bracelet-taureau",
    2: "coffret-cadeaux-bougie-bracelet-gemeaux",
    3: "coffret-cadeaux-bougie-bracelet-cancer",
    4: "coffret-cadeaux-bougie-bracelet-lion",
    5: "coffret-cadeaux-bougie-bracelet-vierge",
    6: "coffret-cadeaux-bougie-bracelet-balance",
    7: "coffret-cadeaux-bougie-et-bracelet-scorpion",
    8: "coffret-cadeaux-bougie-et-bracelet-sagittaire",
    9: "coffret-cadeaux-bougie-bracelet-capricorne",
    10: "coffret-cadeaux-bougie-bracelet-verseau",
    11: "coffret-cadeaux-bougie-bracelet-poisson",
}


def esc(txt):
    return html_lib.escape(str(txt))


def first_stone(stones):
    return stones.split(",")[0].strip()


def build_html(prenom, sun_name, moon_name, asc_name, venus_name, mars_name):
    """Construit le HTML complet du PDF à partir des 5 signes (par nom)."""
    si = sign_index(sun_name)
    mi = sign_index(moon_name)
    ai = sign_index(asc_name)
    vi = sign_index(venus_name)
    mai = sign_index(mars_name)

    sun, moon, asc = SIGNS[si], SIGNS[mi], SIGNS[ai]
    venus, mars = SIGNS[vi], SIGNS[mai]

    dom = dominant_element([si, mi, ai, vi, mai])
    house_text = ELEMENT_THEMES[dom]

    # ── Visuels SVG : roue astrologique + graphiques ──
    wheel_planets = [
        {"sign_index": si,  "kind": "sun",   "color": OR,     "label": "Soleil"},
        {"sign_index": mi,  "kind": "moon",  "color": VIOLET, "label": "Lune"},
        {"sign_index": ai,  "kind": "asc",   "color": ROSE,   "label": "Ascendant"},
        {"sign_index": vi,  "kind": "venus", "color": ROSE,   "label": "Vénus"},
        {"sign_index": mai, "kind": "mars",  "color": VIOLET, "label": "Mars"},
    ]
    wheel_svg = ac.natal_wheel(wheel_planets, 410)
    el_counts = element_counts([si, mi, ai, vi, mai])
    mod_counts = modality_counts([si, mi, ai, vi, mai])
    bars_svg = ac.element_bars(el_counts, 380)
    donut_svg = ac.modality_donut(mod_counts, 170)

    # Texte interprétatif des dominantes
    dom_modality = max(mod_counts, key=mod_counts.get)
    MODALITY_TEXT = {
        "Cardinal": "Vous êtes un profil d'initiative : vous lancez, vous impulsez, vous ouvrez les chemins.",
        "Fixe": "Vous êtes un profil de stabilité : vous ancrez, vous tenez, vous menez les choses jusqu'au bout.",
        "Mutable": "Vous êtes un profil d'adaptation : vous transformez, vous reliez, vous épousez le changement.",
    }

    # Synthèse de cohérence (reprise de la logique buildInterpretation)
    coherence = ""
    if si == mi == ai:
        coherence = (
            f"<p class='synthese'><strong>Triple {esc(sun['name'])}</strong> : votre thème est "
            f"d'une rare cohérence. Ce que vous êtes, ce que vous ressentez et ce que vous montrez "
            f"vibrent à l'unisson. Vous incarnez pleinement l'énergie du {esc(sun['name'])}.</p>"
        )
    elif si == mi:
        coherence = (
            f"<p class='synthese'><strong>Soleil et Lune en {esc(sun['name'])}</strong> : vous êtes "
            f"aligné entre ce que vous êtes consciemment et ce que vous ressentez intimement. "
            f"Une belle harmonie intérieure, que votre Ascendant {esc(asc['name'])} vient nuancer.</p>"
        )

    # Rituels (repris de getRitual)
    rituals = [
        f"<strong>Le matin</strong> — posez une pierre de {esc(first_stone(sun['stones']))} "
        f"(alignée à votre Soleil {esc(sun['name'])}) dans votre main pendant deux minutes en "
        f"visualisant votre intention du jour. C'est le rituel d'ancrage de votre essence.",
        f"<strong>Le soir</strong> — allumez une bougie et tenez une pierre de "
        f"{esc(first_stone(moon['stones']))} (alignée à votre Lune {esc(moon['name'])}) près de "
        f"votre cœur. Laissez remonter les émotions de la journée sans jugement : c'est votre "
        f"rituel de décharge émotionnelle.",
        f"<strong>Une fois par semaine</strong> — portez une pièce en "
        f"{esc(first_stone(asc['stones']))} (alignée à votre Ascendant {esc(asc['name'])}) lors "
        f"d'une rencontre importante. Elle harmonisera la manière dont vous vous présentez au monde.",
    ]
    rituals_html = "".join(f"<li>{r}</li>" for r in rituals)

    # Produits alignés (3 coffrets : Soleil, Lune, Ascendant)
    produits = [
        ("Pour votre Soleil", sym.sun(VIOLET, 26), f"Coffret Bougie &amp; Bracelet {esc(sun['name'])}",
         f"Pierres de {esc(first_stone(sun['stones']))}, alignées à l'essence de votre Soleil.",
         f"https://www.astroya.fr/products/{COFFRETS[si]}"),
        ("Pour votre Lune", sym.moon(VIOLET, 26), f"Coffret Bougie &amp; Bracelet {esc(moon['name'])}",
         f"Pierres de {esc(first_stone(moon['stones']))}, pour honorer votre monde intérieur.",
         f"https://www.astroya.fr/products/{COFFRETS[mi]}"),
        ("Pour votre Ascendant", sym.ascendant(VIOLET, 26), f"Coffret Bougie &amp; Bracelet {esc(asc['name'])}",
         f"Pierres de {esc(first_stone(asc['stones']))}, pour rayonner votre présence sociale.",
         f"https://www.astroya.fr/products/{COFFRETS[ai]}"),
    ]
    produits_html = "".join(
        f"""<div class="prod">
              <div class="prod-badge">{badge}</div>
              <div class="prod-sym">{svg}</div>
              <div class="prod-name">{name}</div>
              <div class="prod-desc">{desc}</div>
            </div>""" for (badge, svg, name, desc, url) in produits
    )

    nom = esc(prenom) if prenom else "Vous"

    return f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><title>Thème astral — {nom}</title></head>
<body>

<!-- ══════ PAGE DE COUVERTURE ══════ -->
<section class="cover">
  <div class="cover-stars"></div>
  <div class="cover-inner">
    <div class="cover-wordmark">ASTROYA</div>
    <div class="cover-orn">&#10022; &#10022; &#10022;</div>
    <div class="cover-kicker">VOTRE THÈME ASTRAL</div>
    <h1 class="cover-name">{nom}</h1>
    <div class="cover-trio">
      <div class="ct"><span class="ct-sym">{sym.sun("#e8d4a8", 40)}</span><span class="ct-lbl">Soleil</span><span class="ct-val">{esc(sun['name'])}</span></div>
      <div class="ct"><span class="ct-sym">{sym.moon("#e8d4a8", 40)}</span><span class="ct-lbl">Lune</span><span class="ct-val">{esc(moon['name'])}</span></div>
      <div class="ct"><span class="ct-sym">{sym.ascendant("#e8d4a8", 40)}</span><span class="ct-lbl">Ascendant</span><span class="ct-val">{esc(asc['name'])}</span></div>
    </div>
    <p class="cover-sub">Votre signature cosmique, révélée par Astroya</p>
    <div class="cover-orn cover-orn-bottom">&#10022;</div>
  </div>
</section>

<!-- ══════ CARTE DU CIEL (roue + graphiques) ══════ -->
<section class="page">
  <div class="kicker">&#10022; Votre carte du ciel</div>
  <h2>La roue de {nom}</h2>
  <p class="intro-soft">Voici la photographie du ciel au moment de votre naissance. Chaque planète
  est placée dans le signe qu'elle occupait : c'est l'empreinte cosmique unique qui vous accompagne.</p>

  <div class="wheel-wrap">{wheel_svg}</div>

  <div class="wheel-legend">
    <span class="lg"><span class="lg-ico">{sym.sun(OR, 20)}</span>Soleil &middot; {esc(sun['name'])}</span>
    <span class="lg"><span class="lg-ico">{sym.moon(VIOLET, 20)}</span>Lune &middot; {esc(moon['name'])}</span>
    <span class="lg"><span class="lg-ico">{sym.ascendant(ROSE, 20)}</span>Ascendant &middot; {esc(asc['name'])}</span>
    <span class="lg"><span class="lg-ico">{sym.venus(ROSE, 20)}</span>Vénus &middot; {esc(venus['name'])}</span>
    <span class="lg"><span class="lg-ico">{sym.mars(VIOLET, 20)}</span>Mars &middot; {esc(mars['name'])}</span>
  </div>
</section>

<!-- ══════ DOMINANTES (graphiques) ══════ -->
<section class="page">
  <div class="kicker">&#10022; Vos dominantes</div>
  <h2>L'équilibre de vos énergies</h2>
  <p class="intro-soft">La répartition de vos planètes entre les quatre éléments et les trois
  modalités révèle la coloration profonde de votre tempérament.</p>

  <div class="chart-card">
    <div class="chart-title">Vos quatre éléments</div>
    <div class="chart-svg">{bars_svg}</div>
    <p class="chart-note">{esc(ELEMENT_THEMES[dom].split('.')[0])}.</p>
  </div>

  <div class="chart-card">
    <div class="chart-title">Vos trois modalités</div>
    <div class="donut-row">
      <div class="donut-svg">{donut_svg}</div>
      <div class="donut-legend">
        <span class="dl"><span class="dl-sq" style="background:{VIOLET}"></span>Cardinal &middot; {mod_counts['Cardinal']}</span>
        <span class="dl"><span class="dl-sq" style="background:{ROSE}"></span>Fixe &middot; {mod_counts['Fixe']}</span>
        <span class="dl"><span class="dl-sq" style="background:{OR}"></span>Mutable &middot; {mod_counts['Mutable']}</span>
      </div>
    </div>
    <p class="chart-note">{esc(MODALITY_TEXT[dom_modality])}</p>
  </div>
</section>

<!-- ══════ INTERPRÉTATION ══════ -->
<section class="page">
  <div class="kicker">&#10022; Votre signature cosmique</div>
  <h2>L'essence de {nom}</h2>

  <p>{nom}, votre signature cosmique se dessine autour de trois axes puissants : un
  <strong>Soleil en {esc(sun['name'])}</strong> qui éclaire votre essence, une
  <strong>Lune en {esc(moon['name'])}</strong> qui nourrit votre vie intérieure, et un
  <strong>Ascendant en {esc(asc['name'])}</strong> qui façonne votre présence au monde.</p>

  <div class="planet-block sun-block">
    <div class="pb-head"><span class="pb-sym">{sym.sun(OR, 30)}</span>
      <div><div class="pb-title">Soleil en {esc(sun['name'])}</div>
      <div class="pb-sub">Ce que vous êtes &middot; {esc(sun['keywords'])}</div></div></div>
    <p>{esc(sun['sun'])}</p>
  </div>

  <div class="planet-block moon-block">
    <div class="pb-head"><span class="pb-sym">{sym.moon(VIOLET, 30)}</span>
      <div><div class="pb-title">Lune en {esc(moon['name'])}</div>
      <div class="pb-sub">Ce que vous ressentez &middot; {esc(moon['keywords'])}</div></div></div>
    <p>{esc(moon['moon'])}</p>
  </div>

  <div class="planet-block asc-block">
    <div class="pb-head"><span class="pb-sym">{sym.ascendant(ROSE, 30)}</span>
      <div><div class="pb-title">Ascendant en {esc(asc['name'])}</div>
      <div class="pb-sub">Ce que vous montrez &middot; {esc(asc['keywords'])}</div></div></div>
    <p>{esc(asc['asc'])}</p>
  </div>

  {coherence}
</section>

<!-- ══════ VÉNUS & MARS ══════ -->
<section class="page">
  <div class="kicker">&#10022; Vos planètes intimes</div>
  <h2>Comment vous aimez, comment vous agissez</h2>

  <div class="planet-block venus-block">
    <div class="pb-head"><span class="pb-sym">{sym.venus(ROSE, 28)}</span>
      <div><div class="pb-title">Vénus en {esc(venus['name'])}</div>
      <div class="pb-sub">Amour, séduction, lien</div></div></div>
    <p>{esc(venus['venus'])}</p>
    <p class="stones-note">Pierres alignées à votre Vénus : <em>{esc(venus['stones'])}</em>.</p>
  </div>

  <div class="planet-block mars-block">
    <div class="pb-head"><span class="pb-sym">{sym.mars(VIOLET, 28)}</span>
      <div><div class="pb-title">Mars en {esc(mars['name'])}</div>
      <div class="pb-sub">Action, désir, élan vital</div></div></div>
    <p>{esc(mars['mars'])}</p>
    <p class="stones-note">Pierres alignées à votre Mars : <em>{esc(mars['stones'])}</em>.</p>
  </div>

  <div class="house-box">
    <div class="house-title">Vos thématiques de vie dominantes</div>
    <p>{esc(house_text)}</p>
  </div>
</section>

<!-- ══════ RITUEL ══════ -->
<section class="page">
  <div class="kicker">&#10022; Votre rituel personnel</div>
  <h2>Trois pratiques alignées à votre signature</h2>
  <p class="intro-soft">Voici trois gestes simples, pensés pour honorer votre trépied cosmique
  au quotidien. À adapter à votre rythme et à votre ressenti.</p>
  <ul class="ritual">{rituals_html}</ul>

  <div class="kicker" style="margin-top:30px">&#10022; Pierres &amp; objets alignés</div>
  <h3 class="prod-h3">La sélection Astroya pour {nom}</h3>
  <div class="prod-grid">{produits_html}</div>
  <div class="cta">
    <p>Incarnez votre thème au quotidien avec la Collection Astrologie &amp; Zodiaque.</p>
    <div class="cta-url">astroya.fr &middot; Livraison offerte dès 69&euro;</div>
  </div>
</section>

<!-- ══════ PAGE FINALE / DISCLAIMER ══════ -->
<section class="page final">
  <div class="final-orn">&#10022; &#10022; &#10022;</div>
  <p class="final-quote">« L'astrologie ne décide pas de votre vie.<br>Elle vous offre un miroir
  pour mieux vous comprendre, et la liberté d'en faire ce que vous voulez. »</p>
  <div class="disclaimer">
    <p>Ce thème astral est établi à partir des cinq planètes majeures (Soleil, Lune, Ascendant,
    Vénus, Mars), qui révèlent l'essentiel de votre profil. Il est proposé à des fins de
    développement personnel et de bien-être. La lithothérapie est une pratique de bien-être
    qui ne se substitue en aucun cas à un avis ou un traitement médical.</p>
  </div>
  <div class="final-wordmark">ASTROYA</div>
  <p class="final-sign">L'astrologie incarnée dans des objets qui ont du sens</p>
</section>

</body></html>"""


CSS_TEMPLATE = f"""
@page {{
  size: A4;
  margin: 0;
}}
@page :first {{ margin: 0; }}

* {{ margin: 0; padding: 0; box-sizing: border-box; }}

body {{
  font-family: 'DejaVu Sans', sans-serif;
  color: {TEXTE};
  font-size: 11pt;
  line-height: 1.65;
}}

/* Symboles astrologiques dessinés en SVG : alignement vertical propre */
.zsym {{ display: inline-block; vertical-align: middle; }}
.ct-sym {{ display: flex; justify-content: center; align-items: center; height: 44px; margin-bottom: 8px; }}
.pb-sym {{ display: flex; justify-content: center; align-items: center; width: 44px; height: 40px; }}
.prod-sym {{ display: flex; justify-content: center; align-items: center; height: 32px; margin-bottom: 6px; }}

/* ════ COUVERTURE ════ */
.cover {{
  height: 297mm; width: 210mm;
  background: linear-gradient(160deg, {VIOLET_DARK} 0%, {VIOLET} 55%, {ROSE} 100%);
  color: #fff;
  position: relative;
  page-break-after: always;
  overflow: hidden;
}}
.cover-inner {{
  position: absolute; top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  width: 80%; text-align: center;
}}
.cover-wordmark {{
  font-family: 'El Messiri', serif; font-weight: 700;
  font-size: 17pt; letter-spacing: 9px; color: #fff;
  margin-bottom: 22px; opacity: 0.95;
}}
.cover-orn {{ color: {OR_CLAIR}; letter-spacing: 8px; font-size: 13pt; margin-bottom: 18px; }}
.cover-orn-bottom {{ margin-top: 32px; margin-bottom: 0; font-size: 16pt; }}
.cover-kicker {{
  font-family: 'El Messiri', serif; font-weight: 500;
  letter-spacing: 7px; font-size: 12pt; color: {OR_CLAIR};
  text-transform: uppercase; margin-bottom: 10px;
}}
.cover-name {{
  font-family: 'El Messiri', serif; font-weight: 700;
  font-size: 46pt; line-height: 1.05; margin-bottom: 34px; color: #fff;
}}
.cover-trio {{ display: flex; justify-content: center; gap: 14px; margin-bottom: 30px; }}
.ct {{
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.25);
  border-radius: 10px; padding: 16px 10px; width: 30%;
  display: flex; flex-direction: column; align-items: center;
}}
.ct-sym {{ font-size: 30pt; line-height: 1; margin-bottom: 8px; color: {OR_CLAIR}; }}
.ct-lbl {{
  font-family: 'El Messiri', serif; font-size: 8.5pt; letter-spacing: 2px;
  text-transform: uppercase; color: rgba(255,255,255,0.8); margin-bottom: 3px;
}}
.ct-val {{ font-family: 'El Messiri', serif; font-size: 14pt; font-weight: 600; }}
.cover-sub {{ font-style: italic; font-size: 12pt; color: rgba(255,255,255,0.9); }}

/* ════ PAGES INTÉRIEURES ════ */
.page {{
  width: 210mm; min-height: 297mm;
  padding: 26mm 22mm;
  background: {CREME};
  page-break-after: always;
  position: relative;
}}
.kicker {{
  font-family: 'El Messiri', serif; font-weight: 500;
  letter-spacing: 4px; font-size: 9.5pt; color: {OR};
  text-transform: uppercase; text-align: center; margin-bottom: 8px;
}}
h2 {{
  font-family: 'Poppins', sans-serif; font-weight: 600;
  font-size: 21pt; color: {VIOLET_DARK}; text-align: center;
  margin-bottom: 22px; line-height: 1.2;
}}
h3.prod-h3 {{
  font-family: 'Poppins', sans-serif; font-weight: 600;
  font-size: 15pt; color: {VIOLET_DARK}; text-align: center; margin-bottom: 16px;
}}
p {{ margin-bottom: 11px; color: {TEXTE_DOUX}; }}
strong {{ color: {VIOLET}; font-weight: 700; }}
em {{ color: {ROSE}; font-style: italic; }}

.planet-block {{
  background: #fff; border-radius: 8px;
  border: 1px solid rgba(184,132,155,0.25);
  border-left: 4px solid {ROSE};
  padding: 16px 20px; margin-bottom: 14px;
}}
.sun-block {{ border-left-color: {OR}; }}
.moon-block {{ border-left-color: {VIOLET}; }}
.asc-block {{ border-left-color: {ROSE}; }}
.venus-block {{ border-left-color: {ROSE}; }}
.mars-block {{ border-left-color: {VIOLET}; }}
.pb-head {{ display: flex; align-items: center; gap: 12px; margin-bottom: 8px; }}
.pb-sym {{
  font-size: 22pt; line-height: 1; color: {VIOLET};
  width: 40px; text-align: center;
}}
.pb-title {{ font-family: 'Poppins', sans-serif; font-weight: 600; font-size: 13pt; color: {VIOLET_DARK}; }}
.pb-sub {{ font-style: italic; font-size: 9.5pt; color: #8a7a9a; }}
.stones-note {{ font-size: 9.5pt; color: #7a6a8a; margin-bottom: 0; }}
.synthese {{
  background: {CREME_ROSE}; border-radius: 8px; padding: 14px 18px;
  margin-top: 6px; font-size: 10.5pt;
}}

.house-box {{
  background: linear-gradient(135deg, {CREME_ROSE}, {CREME});
  border-left: 4px solid {VIOLET};
  border-radius: 0 8px 8px 0; padding: 18px 22px; margin-top: 18px;
}}
.house-title {{
  font-family: 'Poppins', sans-serif; font-weight: 600;
  font-size: 12pt; color: {VIOLET_DARK}; margin-bottom: 8px;
}}

.intro-soft {{ font-style: italic; color: #6a6080; text-align: center; margin-bottom: 18px; }}

/* ── Carte du ciel ── */
.wheel-wrap {{ text-align: center; margin: 10px 0 18px; }}
.wheel-wrap .wheel {{ display: inline-block; }}
.wheel-legend {{
  display: flex; flex-wrap: wrap; justify-content: center; gap: 10px 20px;
  margin-top: 8px;
}}
.wheel-legend .lg {{
  font-size: 10pt; color: {TEXTE_DOUX};
  display: inline-flex; align-items: center; gap: 7px;
}}
.lg-dot {{
  width: 12px; height: 12px; border-radius: 50%;
  border: 2.5px solid {VIOLET}; background: #fff; display: inline-block;
}}

/* ── Graphiques dominantes ── */
.chart-card {{
  background: #fff; border: 1px solid rgba(184,132,155,0.22);
  border-radius: 8px; padding: 20px 24px; margin-bottom: 16px;
}}
.chart-title {{
  font-family: 'Poppins', sans-serif; font-weight: 600;
  font-size: 12.5pt; color: {VIOLET_DARK}; text-align: center; margin-bottom: 14px;
}}
.chart-svg {{ text-align: center; }}
.chart-note {{
  font-size: 10pt; font-style: italic; color: #6a6080;
  text-align: center; margin: 12px 0 0;
}}
.donut-row {{ display: flex; align-items: center; justify-content: center; gap: 30px; }}
.donut-svg {{ flex-shrink: 0; }}
.donut-legend {{ display: flex; flex-direction: column; gap: 10px; }}
.donut-legend .dl {{
  font-size: 10.5pt; color: {TEXTE_DOUX};
  display: inline-flex; align-items: center; gap: 8px;
}}
.dl-sq {{ width: 13px; height: 13px; border-radius: 3px; display: inline-block; }}
ul.ritual {{ list-style: none; }}
ul.ritual li {{
  background: #fff; border: 1px solid rgba(184,132,155,0.2);
  border-radius: 8px; padding: 13px 18px 13px 36px;
  margin-bottom: 10px; position: relative; font-size: 10.5pt; color: {TEXTE_DOUX};
}}
ul.ritual li:before {{
  content: '\\2726'; position: absolute; left: 14px; top: 13px; color: {OR}; font-size: 11pt;
}}

.prod-grid {{ display: flex; gap: 12px; margin-bottom: 20px; }}
.prod {{
  flex: 1; background: #fff; border: 1px solid rgba(184,132,155,0.22);
  border-radius: 8px; padding: 16px 12px; text-align: center;
}}
.prod-badge {{
  display: inline-block; background: rgba(107,76,138,0.08); color: {VIOLET};
  font-family: 'El Messiri', serif; font-size: 7.5pt; letter-spacing: 1.5px;
  text-transform: uppercase; padding: 3px 9px; border-radius: 10px; margin-bottom: 8px;
}}
.prod-sym {{ font-size: 24pt; line-height: 1; margin-bottom: 6px; color: {VIOLET}; }}
.prod-name {{ font-weight: 700; font-size: 10pt; color: {VIOLET_DARK}; margin-bottom: 6px; }}
.prod-desc {{ font-size: 9pt; font-style: italic; color: #6a6080; line-height: 1.45; }}

.cta {{
  background-color: {VIOLET_DARK};
  background-image: linear-gradient(135deg, {VIOLET_DARK}, {VIOLET});
  color: #fff;
  border-radius: 8px; padding: 18px 22px; text-align: center;
}}
.cta p {{ color: #ffffff !important; font-style: italic; margin-bottom: 6px; }}
.cta-url {{ font-family: 'El Messiri', serif; font-size: 10pt; letter-spacing: 1px; color: {OR_CLAIR} !important; font-weight: 600; }}

/* ════ PAGE FINALE ════ */
.final {{ text-align: center; }}
.final-orn {{ color: {OR}; letter-spacing: 8px; font-size: 14pt; margin-top: 40mm; margin-bottom: 30px; }}
.final-quote {{
  font-family: 'El Messiri', serif; font-size: 16pt; font-style: italic;
  color: {VIOLET_DARK}; line-height: 1.5; max-width: 70%; margin: 0 auto 40px;
}}
.disclaimer {{
  background: #fff; border: 1px solid rgba(184,132,155,0.25);
  border-radius: 8px; padding: 16px 22px; max-width: 80%; margin: 0 auto 40px;
}}
.disclaimer p {{ font-size: 9pt; color: #7a6a8a; margin-bottom: 0; line-height: 1.6; }}
.final-wordmark {{
  font-family: 'El Messiri', serif; font-weight: 700;
  font-size: 15pt; letter-spacing: 7px; color: {VIOLET}; margin-bottom: 8px;
}}
.final-sign {{ font-style: italic; color: #6a6080; font-size: 10pt; }}
"""


def generate_pdf(prenom, sun, moon, asc, venus, mars, output_path):
    """Génère le PDF et l'écrit sur disque. Retourne le chemin."""
    font_config = FontConfiguration()
    html_content = build_html(prenom, sun, moon, asc, venus, mars)
    HTML(string=html_content).write_pdf(
        output_path,
        stylesheets=[CSS(string=CSS_TEMPLATE, font_config=font_config)],
        font_config=font_config,
        full_fonts=True,  # évite le subsetting (bug fontTools sur les symboles astro d'El Messiri)
    )
    return output_path


def generate_pdf_bytes(prenom, sun, moon, asc, venus, mars):
    """Génère le PDF en mémoire et retourne les octets (pour upload Supabase)."""
    font_config = FontConfiguration()
    html_content = build_html(prenom, sun, moon, asc, venus, mars)
    pdf_bytes = HTML(string=html_content).write_pdf(
        stylesheets=[CSS(string=CSS_TEMPLATE, font_config=font_config)],
        font_config=font_config,
        full_fonts=True,
    )
    return pdf_bytes


if __name__ == "__main__":
    # Démo : Claire, Soleil Lion / Lune Cancer / Ascendant Balance / Vénus Vierge / Mars Scorpion
    generate_pdf(
        "Claire", "Lion", "Cancer", "Balance", "Vierge", "Scorpion",
        "/home/claude/astroya/theme-astral-pdf/demo_claire.pdf",
    )
    print("PDF généré : demo_claire.pdf")
