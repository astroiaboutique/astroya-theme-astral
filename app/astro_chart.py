# -*- coding: utf-8 -*-
"""
Roue astrologique et graphiques (éléments / modalités) dessinés en SVG.
Rendu portable, aux couleurs Astroya. Roue « par signes » : chaque planète
est placée au milieu de son secteur de 30°.
"""
import math

# Glyphes des 12 signes (ordre zodiacal classique, Bélier = secteur 0)
SIGN_GLYPHS = ["\u2648", "\u2649", "\u264a", "\u264b", "\u264c", "\u264d",
               "\u264e", "\u264f", "\u2650", "\u2651", "\u2652", "\u2653"]
SIGN_NAMES = ["Bélier", "Taureau", "Gémeaux", "Cancer", "Lion", "Vierge",
              "Balance", "Scorpion", "Sagittaire", "Capricorne", "Verseau", "Poissons"]

# Couleur par élément (Feu, Terre, Air, Eau) -> teinte de secteur
SIGN_ELEMENT = ["Feu", "Terre", "Air", "Eau"] * 3
ELEMENT_COLORS = {
    "Feu": "#e8c2a8",    # terracotta doux
    "Terre": "#cfc3a0",  # sable doré
    "Air": "#cdbfe0",    # lilas clair
    "Eau": "#b8cfe0",    # bleu doux
}

VIOLET = "#6b4c8a"
VIOLET_DARK = "#3d2c5a"
ROSE = "#b8849b"
OR = "#c9a96e"
OR_FONCE = "#a0825a"


def _pt(cx, cy, r, angle_deg):
    """Point sur un cercle. Angle 0 = haut (12h), sens horaire."""
    a = math.radians(angle_deg - 90)  # -90 pour démarrer en haut
    return cx + r * math.cos(a), cy + r * math.sin(a)


def _glyph_for_planet(kind):
    # symboles dessinés pour Soleil/Lune/Asc en SVG inline ; signes/Vénus/Mars en glyphe texte ok via DejaVu... 
    # mais pour la roue on dessine tout en primitives pour éviter l'emoji.
    return None


def _draw_planet_marker(cx, cy, color, kind):
    """Dessine un petit pictogramme de planète centré en (cx, cy)."""
    if kind == "sun":
        return (f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="7" fill="none" stroke="{color}" stroke-width="2.2"/>'
                f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="1.8" fill="{color}"/>')
    if kind == "moon":
        # croissant
        x1, y1 = cx + 1.5, cy
        return (f'<path d="M{cx+3:.1f} {cy-7:.1f} a8 8 0 1 0 0 14 6 6 0 0 1 0-14z" fill="{color}"/>')
    if kind == "asc":
        return (f'<line x1="{cx:.1f}" y1="{cy+6:.1f}" x2="{cx:.1f}" y2="{cy-6:.1f}" stroke="{color}" stroke-width="2.2" stroke-linecap="round"/>'
                f'<polyline points="{cx-4:.1f},{cy-2:.1f} {cx:.1f},{cy-7:.1f} {cx+4:.1f},{cy-2:.1f}" fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>')
    if kind == "venus":
        return (f'<circle cx="{cx:.1f}" cy="{cy-2:.1f}" r="5" fill="none" stroke="{color}" stroke-width="2.2"/>'
                f'<line x1="{cx:.1f}" y1="{cy+3:.1f}" x2="{cx:.1f}" y2="{cy+9:.1f}" stroke="{color}" stroke-width="2.2" stroke-linecap="round"/>'
                f'<line x1="{cx-3.5:.1f}" y1="{cy+6:.1f}" x2="{cx+3.5:.1f}" y2="{cy+6:.1f}" stroke="{color}" stroke-width="2.2" stroke-linecap="round"/>')
    if kind == "mars":
        return (f'<circle cx="{cx-2:.1f}" cy="{cy+3:.1f}" r="5" fill="none" stroke="{color}" stroke-width="2.2"/>'
                f'<line x1="{cx+1.5:.1f}" y1="{cy-0.5:.1f}" x2="{cx+7:.1f}" y2="{cy-6:.1f}" stroke="{color}" stroke-width="2.2" stroke-linecap="round"/>'
                f'<polyline points="{cx+3:.1f},{cy-6:.1f} {cx+7:.1f},{cy-6:.1f} {cx+7:.1f},{cy-2:.1f}" fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>')
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="4" fill="{color}"/>'


def natal_wheel(planets, size=420):
    """
    planets : liste de dict {sign_index, kind, color, label}
    Dessine la roue : couronne des 12 signes + planètes placées au milieu de leur secteur.
    Gère les superpositions en décalant légèrement le rayon.
    """
    cx = cy = size / 2
    r_outer = size / 2 - 6
    r_signs = r_outer - 26      # anneau des glyphes de signes
    r_inner = r_signs - 10      # cercle intérieur de l'anneau
    r_planet = r_inner - 34     # rayon de placement des planètes
    r_hub = 30                  # moyeu central

    svg = [f'<svg class="wheel" width="{size}" height="{size}" viewBox="0 0 {size} {size}" '
           f'xmlns="http://www.w3.org/2000/svg">']

    # Cercles de structure
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r_outer}" fill="#fffdfa" stroke="{OR}" stroke-width="1.5"/>')
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r_inner}" fill="#fdfaf5" stroke="{ROSE}" stroke-width="1" opacity="0.7"/>')

    # 12 secteurs colorés (anneau des signes)
    for i in range(12):
        a0 = i * 30
        a1 = (i + 1) * 30
        x0, y0 = _pt(cx, cy, r_outer, a0)
        x1, y1 = _pt(cx, cy, r_outer, a1)
        xi0, yi0 = _pt(cx, cy, r_inner, a0)
        xi1, yi1 = _pt(cx, cy, r_inner, a1)
        col = ELEMENT_COLORS[SIGN_ELEMENT[i]]
        path = (f'<path d="M{xi0:.1f} {yi0:.1f} L{x0:.1f} {y0:.1f} '
                f'A{r_outer:.1f} {r_outer:.1f} 0 0 1 {x1:.1f} {y1:.1f} '
                f'L{xi1:.1f} {yi1:.1f} '
                f'A{r_inner:.1f} {r_inner:.1f} 0 0 0 {xi0:.1f} {yi0:.1f} Z" '
                f'fill="{col}" opacity="0.55" stroke="#fff" stroke-width="0.8"/>')
        svg.append(path)
        # glyphe du signe au milieu du secteur
        gx, gy = _pt(cx, cy, r_signs, a0 + 15)
        svg.append(f'<text x="{gx:.1f}" y="{gy:.1f}" text-anchor="middle" '
                   f'dominant-baseline="central" font-family="DejaVu Sans" '
                   f'font-size="16" fill="{VIOLET_DARK}">{SIGN_GLYPHS[i]}</text>')

    # lignes de séparation des secteurs
    for i in range(12):
        a = i * 30
        x_o, y_o = _pt(cx, cy, r_inner, a)
        x_h, y_h = _pt(cx, cy, r_hub, a)
        svg.append(f'<line x1="{x_h:.1f}" y1="{y_h:.1f}" x2="{x_o:.1f}" y2="{y_o:.1f}" '
                   f'stroke="{ROSE}" stroke-width="0.5" opacity="0.4"/>')

    # moyeu central décoratif
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r_hub}" fill="{VIOLET_DARK}"/>')
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r_hub}" fill="none" stroke="{OR}" stroke-width="1.2"/>')
    svg.append(f'<text x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="central" '
               f'font-family="DejaVu Sans" font-size="13" fill="{OR}">\u2726</text>')

    # Regrouper les planètes par secteur pour gérer les superpositions
    from collections import defaultdict
    by_sector = defaultdict(list)
    for p in planets:
        by_sector[p["sign_index"]].append(p)

    for sign_idx, plist in by_sector.items():
        n = len(plist)
        for j, p in enumerate(plist):
            # répartir dans le secteur : angle centré + petit étalement, rayon alterné
            spread = (j - (n - 1) / 2) * 9  # degrés d'étalement
            ang = sign_idx * 30 + 15 + spread
            rr = r_planet - (j % 2) * 22    # alterne le rayon si plusieurs planètes
            px, py = _pt(cx, cy, rr, ang)
            # disque de fond
            svg.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="13" fill="#fff" '
                       f'stroke="{p["color"]}" stroke-width="1.5"/>')
            svg.append(_draw_planet_marker(px, py, p["color"], p["kind"]))

    svg.append('</svg>')
    return "".join(svg)


def element_bars(counts, size_w=420):
    """
    Graphique en barres horizontales de la répartition des éléments.
    counts : dict {Feu:int, Terre:int, Air:int, Eau:int}
    """
    order = ["Feu", "Terre", "Air", "Eau"]
    total = sum(counts.values()) or 1
    bar_h = 26
    gap = 16
    label_w = 70
    track_w = size_w - label_w - 60
    height = len(order) * (bar_h + gap) + 10

    svg = [f'<svg class="chart" width="{size_w}" height="{height}" viewBox="0 0 {size_w} {height}" '
           f'xmlns="http://www.w3.org/2000/svg" font-family="DejaVu Sans">']
    for i, el in enumerate(order):
        y = 8 + i * (bar_h + gap)
        val = counts.get(el, 0)
        pct = val / total
        w = max(track_w * pct, 2)
        col = {
            "Feu": "#d98c6a", "Terre": "#bfa86a", "Air": "#9b86c4", "Eau": "#6a9bc4"
        }[el]
        # label
        svg.append(f'<text x="0" y="{y + bar_h/2:.1f}" dominant-baseline="central" '
                   f'font-size="12" fill="{VIOLET_DARK}" font-weight="bold">{el}</text>')
        # track
        svg.append(f'<rect x="{label_w}" y="{y}" width="{track_w}" height="{bar_h}" '
                   f'rx="{bar_h/2}" fill="#efe6f0"/>')
        # barre
        svg.append(f'<rect x="{label_w}" y="{y}" width="{w:.1f}" height="{bar_h}" '
                   f'rx="{bar_h/2}" fill="{col}"/>')
        # valeur
        svg.append(f'<text x="{label_w + track_w + 12}" y="{y + bar_h/2:.1f}" '
                   f'dominant-baseline="central" font-size="12" fill="{OR_FONCE}" '
                   f'font-weight="bold">{val}/{total}</text>')
    svg.append('</svg>')
    return "".join(svg)


def modality_donut(counts, size=200):
    """
    Donut des modalités (Cardinal / Fixe / Mutable).
    counts : dict {Cardinal:int, Fixe:int, Mutable:int}
    """
    order = ["Cardinal", "Fixe", "Mutable"]
    colors = {"Cardinal": VIOLET, "Fixe": ROSE, "Mutable": OR}
    total = sum(counts.values()) or 1
    cx = cy = size / 2
    r = size / 2 - 10
    rin = r - 30
    svg = [f'<svg class="donut" width="{size}" height="{size}" viewBox="0 0 {size} {size}" '
           f'xmlns="http://www.w3.org/2000/svg" font-family="DejaVu Sans">']
    start = 0.0
    for m in order:
        val = counts.get(m, 0)
        if val == 0:
            continue
        frac = val / total
        end = start + frac * 360
        large = 1 if (end - start) > 180 else 0
        x0, y0 = _pt(cx, cy, r, start)
        x1, y1 = _pt(cx, cy, r, end)
        xi0, yi0 = _pt(cx, cy, rin, start)
        xi1, yi1 = _pt(cx, cy, rin, end)
        svg.append(f'<path d="M{x0:.1f} {y0:.1f} A{r:.1f} {r:.1f} 0 {large} 1 {x1:.1f} {y1:.1f} '
                   f'L{xi1:.1f} {yi1:.1f} A{rin:.1f} {rin:.1f} 0 {large} 0 {xi0:.1f} {yi0:.1f} Z" '
                   f'fill="{colors[m]}" stroke="#fff" stroke-width="1.5"/>')
        start = end
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{rin-2:.1f}" fill="#fffdfa"/>')
    svg.append('</svg>')
    return "".join(svg)
