# -*- coding: utf-8 -*-
"""
ASTROYA — Microservice de génération de thème astral PDF
─────────────────────────────────────────────────────────
Reçoit les données depuis la page Astroya, génère le PDF personnalisé,
l'upload sur Supabase Storage, enregistre la demande en table Supabase,
puis renvoie l'URL publique du PDF (que la page transmettra à Klaviyo).

Variables d'environnement attendues (configurées sur Render) :
  - ASTROYA_API_KEY     : clé secrète partagée page <-> service (anti-abus)
  - SUPABASE_URL        : https://xxxx.supabase.co
  - SUPABASE_SERVICE_KEY: clé service_role Supabase (secrète, serveur only)
  - SUPABASE_BUCKET     : nom du bucket Storage (def: themes-astraux)
  - ALLOWED_ORIGIN      : origine autorisée CORS (def: https://www.astroya.fr)
"""

import os
import re
import uuid
import datetime
import requests
from flask import Flask, request, jsonify, make_response

from pdf_generator import generate_pdf_bytes
from signs_data import sign_index

app = Flask(__name__)

# ─── Configuration depuis l'environnement ───
API_KEY = os.environ.get("ASTROYA_API_KEY", "")
SUPABASE_URL = os.environ.get("SUPABASE_URL", "").rstrip("/")
SUPABASE_KEY = os.environ.get("SUPABASE_SERVICE_KEY", "")
SUPABASE_BUCKET = os.environ.get("SUPABASE_BUCKET", "themes-astraux")
ALLOWED_ORIGIN = os.environ.get("ALLOWED_ORIGIN", "https://www.astroya.fr")
TABLE_NAME = os.environ.get("SUPABASE_TABLE", "themes_astraux")

VALID_SIGNS = {
    "Bélier", "Taureau", "Gémeaux", "Cancer", "Lion", "Vierge",
    "Balance", "Scorpion", "Sagittaire", "Capricorne", "Verseau", "Poissons",
}


# ─── CORS : autorise uniquement la boutique Astroya ───
def _cors(resp):
    resp.headers["Access-Control-Allow-Origin"] = ALLOWED_ORIGIN
    resp.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    resp.headers["Access-Control-Allow-Headers"] = "Content-Type, X-Astroya-Key"
    return resp


@app.route("/", methods=["GET"])
def health():
    """Point de santé : Render et vous pouvez vérifier que le service tourne."""
    return jsonify({"status": "ok", "service": "astroya-theme-astral"}), 200


@app.route("/generate", methods=["OPTIONS"])
def generate_options():
    return _cors(make_response("", 204))


@app.route("/generate", methods=["POST"])
def generate():
    # 1. Sécurité : clé partagée
    if API_KEY and request.headers.get("X-Astroya-Key") != API_KEY:
        return _cors(jsonify({"error": "unauthorized"})), 401

    data = request.get_json(silent=True) or {}

    prenom = (data.get("prenom") or "").strip()[:40]
    sun = (data.get("sun") or "").strip()
    moon = (data.get("moon") or "").strip()
    asc = (data.get("asc") or "").strip()
    venus = (data.get("venus") or "").strip()
    mars = (data.get("mars") or "").strip()
    email = (data.get("email") or "").strip().lower()[:120]

    # Données de naissance (pour la table, facultatives mais recommandées)
    date_naissance = (data.get("date_naissance") or "").strip()[:10]
    heure_naissance = (data.get("heure_naissance") or "").strip()[:5]
    ville = (data.get("ville") or "").strip()[:80]
    newsletter = bool(data.get("newsletter", False))

    # 2. Validation
    if not prenom or not re.match(r"^[\w\s'’\-À-ÿ]{1,40}$", prenom):
        return _cors(jsonify({"error": "prenom invalide"})), 400
    for label, s in [("sun", sun), ("moon", moon), ("asc", asc), ("venus", venus), ("mars", mars)]:
        if s not in VALID_SIGNS:
            return _cors(jsonify({"error": f"signe invalide: {label}"})), 400
    if email and not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
        return _cors(jsonify({"error": "email invalide"})), 400

    # 3. Génération du PDF en mémoire
    try:
        pdf_bytes = generate_pdf_bytes(prenom, sun, moon, asc, venus, mars)
    except Exception as e:
        app.logger.error("Erreur génération PDF: %s", e)
        return _cors(jsonify({"error": "echec generation pdf"})), 500

    # 4. Upload sur Supabase Storage
    file_id = uuid.uuid4().hex[:12]
    filename = f"theme-astral-{file_id}.pdf"
    pdf_url = None
    if SUPABASE_URL and SUPABASE_KEY:
        try:
            up = requests.post(
                f"{SUPABASE_URL}/storage/v1/object/{SUPABASE_BUCKET}/{filename}",
                headers={
                    "Authorization": f"Bearer {SUPABASE_KEY}",
                    "Content-Type": "application/pdf",
                    "x-upsert": "true",
                },
                data=pdf_bytes,
                timeout=30,
            )
            if up.status_code not in (200, 201):
                app.logger.error("Upload Supabase echec %s: %s", up.status_code, up.text[:200])
                return _cors(jsonify({"error": "echec upload"})), 502
            # URL publique (bucket public)
            pdf_url = f"{SUPABASE_URL}/storage/v1/object/public/{SUPABASE_BUCKET}/{filename}"
        except Exception as e:
            app.logger.error("Exception upload Supabase: %s", e)
            return _cors(jsonify({"error": "echec upload"})), 502
    else:
        return _cors(jsonify({"error": "supabase non configure"})), 500

    # 5. Enregistrement de la demande en table (best-effort, n'empêche pas le retour)
    try:
        requests.post(
            f"{SUPABASE_URL}/rest/v1/{TABLE_NAME}",
            headers={
                "Authorization": f"Bearer {SUPABASE_KEY}",
                "apikey": SUPABASE_KEY,
                "Content-Type": "application/json",
                "Prefer": "return=minimal",
            },
            json={
                "prenom": prenom,
                "email": email or None,
                "date_naissance": date_naissance or None,
                "heure_naissance": heure_naissance or None,
                "ville": ville or None,
                "signe_soleil": sun,
                "signe_lune": moon,
                "signe_ascendant": asc,
                "signe_venus": venus,
                "signe_mars": mars,
                "newsletter_opt_in": newsletter,
                "pdf_url": pdf_url,
                "created_at": datetime.datetime.utcnow().isoformat() + "Z",
            },
            timeout=15,
        )
    except Exception as e:
        # On loggue mais on ne bloque pas : le PDF existe, c'est l'essentiel
        app.logger.warning("Insertion table echouee (non bloquant): %s", e)

    # 6. Réponse : l'URL du PDF, que la page transmettra à Klaviyo
    return _cors(jsonify({"pdf_url": pdf_url, "filename": filename})), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
