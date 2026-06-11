# -*- coding: utf-8 -*-
"""
Symboles astrologiques dessinés en SVG inline.
Garantit un rendu identique partout (pas de dépendance à une police emoji).
Chaque fonction retourne un <svg> dont la couleur est pilotée par `color`.
"""


def _wrap(inner, color, size):
    return (
        f'<svg class="zsym" width="{size}" height="{size}" viewBox="0 0 100 100" '
        f'xmlns="http://www.w3.org/2000/svg" fill="none" '
        f'stroke="{color}" stroke-width="6" stroke-linecap="round" '
        f'stroke-linejoin="round">{inner}</svg>'
    )


def sun(color="#c9a96e", size=34):
    # Cercle + point central + rayons (symbole du Soleil ☉)
    inner = (
        '<circle cx="50" cy="50" r="30"/>'
        f'<circle cx="50" cy="50" r="5" fill="{color}" stroke="none"/>'
    )
    return _wrap(inner, color, size)


def moon(color="#c9a96e", size=34):
    # Croissant de lune
    inner = (
        '<path d="M62 18a36 36 0 1 0 0 64 30 30 0 0 1 0-64z" '
        f'fill="{color}" stroke="none"/>'
    )
    return _wrap(inner, color, size)


def ascendant(color="#c9a96e", size=34):
    # Flèche montante (Ascendant)
    inner = (
        '<line x1="50" y1="80" x2="50" y2="24"/>'
        '<polyline points="32,42 50,22 68,42"/>'
    )
    return _wrap(inner, color, size)


def venus(color="#6b4c8a", size=30):
    # Cercle + croix dessous (♀)
    inner = (
        '<circle cx="50" cy="36" r="22"/>'
        '<line x1="50" y1="58" x2="50" y2="86"/>'
        '<line x1="36" y1="72" x2="64" y2="72"/>'
    )
    return _wrap(inner, color, size)


def mars(color="#6b4c8a", size=30):
    # Cercle + flèche oblique (♂)
    inner = (
        '<circle cx="42" cy="58" r="22"/>'
        '<line x1="58" y1="42" x2="82" y2="18"/>'
        '<polyline points="62,18 82,18 82,38"/>'
    )
    return _wrap(inner, color, size)


# Map signe -> dessin de la constellation/glyphe simplifié (point + nom suffit en pratique,
# mais on fournit une pastille élégante par élément pour les 12 signes si besoin)
def element_dot(element, color, size=30):
    symbols = {
        "Feu": '<path d="M50 20 C40 40 30 50 50 80 C70 50 60 40 50 20 Z" fill="{c}" stroke="none"/>',
        "Terre": '<rect x="28" y="28" width="44" height="44" rx="6" fill="{c}" stroke="none"/>',
        "Air": '<circle cx="50" cy="50" r="24" fill="none" stroke="{c}" stroke-width="7"/>',
        "Eau": '<path d="M50 22 C30 50 30 70 50 80 C70 70 70 50 50 22 Z" fill="{c}" stroke="none"/>',
    }
    inner = symbols.get(element, symbols["Air"]).format(c=color)
    return _wrap(inner, color, size)
