#!/usr/bin/env bash
# ───────────────────────────────────────────────
# ASTROYA — Script de build Render
# Installe les dépendances Python et les polices El Messiri.
# WeasyPrint a besoin de Pango/Cairo : sur Render (runtime Python),
# ces librairies natives sont déjà présentes dans l'image de base.
# ───────────────────────────────────────────────
set -o errexit

# 1. Dépendances Python
pip install --upgrade pip
pip install -r requirements.txt

# 2. Installation des polices El Messiri pour WeasyPrint
#    On les copie dans le dossier de polices utilisateur reconnu par fontconfig.
FONT_DIR="$HOME/.fonts"
mkdir -p "$FONT_DIR"
cp app/fonts/ElMessiri-*.ttf "$FONT_DIR/" || true

# 3. Rafraîchir le cache de polices (si fc-cache dispo)
if command -v fc-cache >/dev/null 2>&1; then
  fc-cache -f "$FONT_DIR" || true
fi

echo "Build terminé : dépendances + polices El Messiri installées."
