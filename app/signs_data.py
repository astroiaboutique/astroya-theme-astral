# -*- coding: utf-8 -*-
"""
Données des 12 signes du zodiaque — Astroya
Reprises À L'IDENTIQUE du JavaScript de la page /pages/theme-astral-gratuit
pour garantir que le PDF dit exactement la même chose que la page.
"""

SIGNS = [
    {
        "name": "Bélier", "symbol": "\u2648", "element": "Feu",
        "stones": "jaspe rouge, hématite, cornaline",
        "keywords": "action, courage, initiative",
        "sun": "Vous êtes un moteur, un initiateur. Vous vivez dans l'instant, aimez les défis et refusez la monotonie. Votre essence est celle du feu qui s'allume et met le monde en mouvement.",
        "moon": "Vos émotions sont intenses, rapides, directes. Vous avez besoin d'espace et de liberté pour vous ressourcer. La colère éclate vite mais retombe aussi vite. Vous êtes émotionnellement courageux.",
        "asc": "Vous projetez dynamisme, franchise, allure conquérante. Les gens vous trouvent audacieux, parfois impulsif. Votre démarche est assurée, votre regard direct.",
        "venus": "En amour, vous aimez la conquête. Vous tombez amoureux vite et fort, aimez l'intensité des débuts. La routine vous pèse. Vous séduisez par votre énergie brute et votre sincérité sans détour.",
        "mars": "Votre énergie d'action est pure et immédiate. Vous foncez, vous n'attendez pas. La stratégie vous ennuie, vous préférez les résultats rapides. Excellent sprinter, moins bon marathonien.",
    },
    {
        "name": "Taureau", "symbol": "\u2649", "element": "Terre",
        "stones": "aventurine verte, quartz rose, émeraude",
        "keywords": "ancrage, sensualité, stabilité",
        "sun": "Vous êtes solide, patient, connecté au concret. Vous aimez ce qui dure, ce qui se touche, ce qui nourrit. Votre essence est celle de la terre qui porte et fait grandir.",
        "moon": "Vos émotions sont stables, lentes, profondes. Vous avez besoin de confort matériel, de rituels, de beauté autour de vous pour vous sentir bien. La sécurité affective est vitale.",
        "asc": "Vous projetez calme, sensualité, présence rassurante. Les gens se sentent en sécurité près de vous. Votre port est posé, votre voix souvent mélodieuse.",
        "venus": "En amour, vous êtes sensuel et fidèle. Le contact physique, la nourriture partagée, les beaux moments ensemble comptent pour vous. Vous prenez votre temps et construisez dans la durée.",
        "mars": "Votre énergie d'action est lente à se déclencher mais puissante une fois lancée. Vous êtes endurant, patient, obstiné. Vous finissez ce que vous commencez. Résistant aux pressions extérieures.",
    },
    {
        "name": "Gémeaux", "symbol": "\u264a", "element": "Air",
        "stones": "citrine, aigue-marine, agate",
        "keywords": "curiosité, échange, vivacité",
        "sun": "Vous êtes curieux, vif, pluriel. Vous avez mille intérêts, mille facettes. Votre essence est celle du vent qui circule et relie les idées entre elles.",
        "moon": "Vos émotions passent par la pensée avant d'être ressenties. Vous avez besoin de parler, d'échanger, de comprendre ce que vous vivez. Le silence prolongé vous pèse.",
        "asc": "Vous projetez vivacité, curiosité, gestes rapides. Les gens vous trouvent sociable, drôle, stimulant intellectuellement. Votre regard pétille.",
        "venus": "En amour, vous aimez par l'esprit. La conversation, l'humour, la complicité mentale priment sur le reste. Vous séduisez par vos mots et votre légèreté. La jalousie vous ennuie.",
        "mars": "Votre énergie d'action est dispersée mais rapide. Vous agissez par impulsions successives, menez plusieurs projets en parallèle. Excellent à improviser, moins à planifier.",
    },
    {
        "name": "Cancer", "symbol": "\u264b", "element": "Eau",
        "stones": "pierre de lune, quartz rose, calcédoine",
        "keywords": "sensibilité, intuition, tendresse",
        "sun": "Vous êtes sensible, intuitif, protecteur. Votre vie intérieure est riche et vos émotions guident vos choix. Votre essence est celle de l'eau qui nourrit et enveloppe.",
        "moon": "Vos émotions sont profondes, fluctuantes, comme les marées. Vous ressentez tout intensément, absorbez l'ambiance des lieux et des gens. Votre cocon est sacré.",
        "asc": "Vous projetez douceur, émotivité, regard rêveur et protecteur. Les gens se confient à vous. Votre présence invite à la tendresse.",
        "venus": "En amour, vous êtes tendre, enveloppant, fidèle. Vous cherchez la sécurité émotionnelle, le partage intime, le foyer. Vous aimez prendre soin et être pris en charge.",
        "mars": "Votre énergie d'action passe par l'émotion. Vous agissez pour protéger, pour nourrir, pour défendre les vôtres. Vous avez du mal à vous mettre en colère sans en pleurer.",
    },
    {
        "name": "Lion", "symbol": "\u264c", "element": "Feu",
        "stones": "citrine, œil de tigre, pierre de soleil",
        "keywords": "rayonnement, générosité, charisme",
        "sun": "Vous êtes chaleureux, généreux, né pour rayonner. Vous avez besoin d'être reconnu et célébré. Votre essence est celle du soleil qui illumine et réchauffe tout ce qu'il touche.",
        "moon": "Vos émotions sont théâtrales et généreuses. Vous avez besoin d'être aimé, admiré, remarqué. Votre cœur est grand mais votre orgueil aussi. Blessé, vous pleurez royalement.",
        "asc": "Vous projetez charisme, prestance, rayonnement naturel. Les regards se tournent vers vous sans effort. Votre port de tête est noble, votre voix porte.",
        "venus": "En amour, vous êtes généreux, passionné, exclusif. Vous aimez grandement, offrez grandement. Vous avez besoin d'être admiré par celui ou celle que vous aimez. Fidèle tant qu'on vous nourrit de reconnaissance.",
        "mars": "Votre énergie d'action est chaleureuse et créative. Vous agissez avec panache, aimez les beaux gestes, refusez la médiocrité. Vous êtes un leader naturel.",
    },
    {
        "name": "Vierge", "symbol": "\u264d", "element": "Terre",
        "stones": "amazonite, cornaline, aventurine",
        "keywords": "discernement, précision, service",
        "sun": "Vous êtes précis, méthodique, analytique. Vous voyez les détails que les autres ratent. Votre essence est celle de la terre fertile qui trie et organise le vivant.",
        "moon": "Vos émotions passent par l'analyse. Vous vous sentez bien quand tout est à sa place, planifié, maîtrisé. Le chaos vous stresse profondément.",
        "asc": "Vous projetez discrétion, élégance sobre, attitude méthodique. Les gens remarquent votre souci du détail, votre tenue soignée, votre propos précis.",
        "venus": "En amour, vous êtes délicat, attentif, parfois trop critique. Vous aimez dans les petits gestes du quotidien plus que dans les grandes déclarations. La fidélité est un réflexe chez vous.",
        "mars": "Votre énergie d'action est méthodique et efficace. Vous planifiez, décomposez, exécutez avec précision. Vous excellez dans le travail bien fait et détaillé.",
    },
    {
        "name": "Balance", "symbol": "\u264e", "element": "Air",
        "stones": "quartz rose, jade, sodalite",
        "keywords": "harmonie, diplomatie, beauté",
        "sun": "Vous êtes harmonieux, diplomate, esthète. Vous cherchez naturellement l'équilibre en toute chose. Votre essence est celle de l'air léger qui cherche l'équilibre parfait.",
        "moon": "Vos émotions ont besoin d'harmonie pour s'exprimer. Les conflits vous minent, la beauté vous ressource. Vous avez besoin de relations équilibrées pour vous sentir bien.",
        "asc": "Vous projetez charme, diplomatie, esthétisme naturel. Les gens vous trouvent agréable, élégant, conciliant. Votre sourire désarme.",
        "venus": "En amour, vous êtes romantique, raffiné, en quête de l'idéal. Vous aimez la beauté des gestes, les attentions poétiques. La relation elle-même compte plus que le défi passionnel.",
        "mars": "Votre énergie d'action passe par la négociation. Vous agissez en concertation, cherchez le consensus, détestez les conflits frontaux. Excellent médiateur.",
    },
    {
        "name": "Scorpion", "symbol": "\u264f", "element": "Eau",
        "stones": "malachite, obsidienne noire, labradorite",
        "keywords": "intensité, transformation, magnétisme",
        "sun": "Vous êtes intense, profond, transformateur. Vous allez jusqu'au bout de ce que vous entreprenez. Votre essence est celle de l'eau souterraine qui creuse et révèle.",
        "moon": "Vos émotions sont extrêmes, secrètes, puissantes. Vous ressentez en profondeur et rarement à moitié. Vous avez besoin d'intimité totale pour vous dévoiler.",
        "asc": "Vous projetez intensité magnétique, regard perçant, présence qui ne laisse pas indifférent. Les gens vous trouvent mystérieux, profond, parfois intimidant.",
        "venus": "En amour, vous êtes passionné, exclusif, possessif. Vous aimez tout ou rien. La fusion émotionnelle et physique est votre norme. Vous êtes un amant mémorable.",
        "mars": "Votre énergie d'action est souterraine et tenace. Vous avancez en stratège, frappez au bon moment, ne lâchez jamais. Résistant à toute épreuve.",
    },
    {
        "name": "Sagittaire", "symbol": "\u2650", "element": "Feu",
        "stones": "lapis-lazuli, améthyste, sodalite",
        "keywords": "expansion, liberté, quête",
        "sun": "Vous êtes enthousiaste, aventurier, en quête de sens. Vous avez besoin de vastes horizons. Votre essence est celle du feu qui voyage et éclaire de nouveaux territoires.",
        "moon": "Vos émotions ont besoin de liberté et d'aventure. Vous vous ressourcez dans le voyage, la philosophie, les grandes idées. L'enfermement émotionnel vous étouffe.",
        "asc": "Vous projetez enthousiasme, optimisme, allure voyageuse. Les gens vous trouvent chaleureux, généreux, inspirant. Votre rire est communicatif.",
        "venus": "En amour, vous aimez la liberté avant tout. Vous cherchez un partenaire de voyage intellectuel et physique. La routine conjugale vous pèse. Vous aimez grandement quand vous vous sentez libre.",
        "mars": "Votre énergie d'action est expansive et généreuse. Vous visez grand, osez l'impossible, fuyez les petits calculs. Excellent meneur de grands projets.",
    },
    {
        "name": "Capricorne", "symbol": "\u2651", "element": "Terre",
        "stones": "quartz fumé, malachite, onyx noir",
        "keywords": "structure, ambition, discipline",
        "sun": "Vous êtes ambitieux, discipliné, stratégique. Vous construisez pour durer. Votre essence est celle de la montagne qui s'élève patiemment au-dessus des nuages.",
        "moon": "Vos émotions sont contenues, maîtrisées, exprimées en privé. Vous avez besoin de cadre, de respect, de stabilité pour vous sentir bien. La vulnérabilité se mérite.",
        "asc": "Vous projetez sérieux, maturité, autorité naturelle. Les gens vous trouvent structuré, fiable, réservé. Votre maintien est digne.",
        "venus": "En amour, vous êtes loyal, réservé, engagé. Vous prenez le temps d'aimer et quand vous aimez, c'est pour longtemps. Vous cherchez un partenaire solide plus qu'une passion éphémère.",
        "mars": "Votre énergie d'action est stratégique et patiente. Vous construisez dans la durée, gravissez les échelons, ne prenez pas de raccourcis. Votre persévérance est légendaire.",
    },
    {
        "name": "Verseau", "symbol": "\u2652", "element": "Air",
        "stones": "améthyste, aigue-marine, lapis-lazuli",
        "keywords": "originalité, liberté, vision",
        "sun": "Vous êtes original, visionnaire, indépendant. Vous pensez autrement que les autres. Votre essence est celle du vent libre qui souffle où il veut.",
        "moon": "Vos émotions sont cérébrales, prises avec distance. Vous vous ressourcez dans les idées, les causes collectives, les amitiés fidèles. L'exclusivité affective vous oppresse.",
        "asc": "Vous projetez originalité, indépendance, style décalé. Les gens vous trouvent unique, atypique, en avance sur votre temps.",
        "venus": "En amour, vous aimez la liberté mutuelle. Vous cherchez un ami-amant, un complice intellectuel. Les relations conventionnelles vous ennuient. Vous êtes fidèle mais à votre manière.",
        "mars": "Votre énergie d'action est innovante et collective. Vous agissez pour des causes, des groupes, des idéaux. Les combats égoïstes ne vous motivent pas.",
    },
    {
        "name": "Poissons", "symbol": "\u2653", "element": "Eau",
        "stones": "améthyste, pierre de lune, turquoise",
        "keywords": "rêverie, empathie, spiritualité",
        "sun": "Vous êtes sensible, rêveur, spirituel. Vous ressentez le monde plus que vous ne le pensez. Votre essence est celle de l'océan qui contient tout et reflète tout.",
        "moon": "Vos émotions sont océaniques, empathiques, poreuses. Vous absorbez les émotions des autres sans distinction. Vous avez besoin de solitude régulière pour vous décharger.",
        "asc": "Vous projetez douceur, rêverie, empathie naturelle. Les gens se sentent compris par vous avant même d'avoir parlé. Votre regard est flou et bienveillant.",
        "venus": "En amour, vous aimez en fusion totale. Vous idéalisez vos partenaires, vous donnez sans compter, pardonnez beaucoup. Vous êtes un amoureux romantique et poétique.",
        "mars": "Votre énergie d'action est diffuse et intuitive. Vous agissez par vagues, suivez votre ressenti plus qu'un plan. Créatif et imprévisible.",
    },
]

# Thématiques de vie dominantes selon l'élément majoritaire (repris du JS getHouseTheme)
ELEMENT_THEMES = {
    "Feu": "Votre thème astral révèle une dominante de Feu. Les maisons de l'action, de la créativité et de l'ambition sont particulièrement animées chez vous. Vous vous épanouissez dans les contextes où vous pouvez initier, créer, rayonner. Les domaines de vie qui vous appellent : carrière visible, projets créatifs, leadership, sports, aventures. Vous avez besoin de défis réguliers pour vous sentir vivant.",
    "Terre": "Votre thème astral révèle une dominante de Terre. Les maisons du concret, de la matière et de la construction durable sont dominantes. Vous cherchez le tangible, le stable, ce qui se mesure et se palpe. Les domaines de vie qui vous appellent : foyer, finances, carrière stable, santé corporelle, plaisirs sensuels. Vous excellez à bâtir patiemment ce qui dure.",
    "Air": "Votre thème astral révèle une dominante d'Air. Les maisons de la communication, du social et des idées dominent. Vous vivez à travers les échanges, les concepts, les réseaux. Les domaines de vie qui vous appellent : communication, enseignement, écriture, amitiés, engagement collectif, voyages intellectuels. Vous avez besoin de conversations stimulantes pour vous nourrir.",
    "Eau": "Votre thème astral révèle une dominante d'Eau. Les maisons de l'intime, de l'émotionnel et du spirituel dominent. Votre vie se joue d'abord à l'intérieur avant de se manifester dehors. Les domaines de vie qui vous appellent : relations intimes profondes, arts, spiritualité, accompagnement d'autrui, ressourcement dans la solitude.",
}


def sign_index(name):
    """Retrouve l'index d'un signe par son nom (insensible à la casse/accents superflus)."""
    for i, s in enumerate(SIGNS):
        if s["name"].lower() == name.lower():
            return i
    return None


def dominant_element(indices):
    """Détermine l'élément dominant à partir d'une liste d'index de signes."""
    counts = {"Feu": 0, "Terre": 0, "Air": 0, "Eau": 0}
    for i in indices:
        counts[SIGNS[i]["element"]] += 1
    return max(counts, key=counts.get)


# Modalité de chaque signe (ordre zodiacal : Bélier=Cardinal, Taureau=Fixe, Gémeaux=Mutable...)
SIGN_MODALITY = ["Cardinal", "Fixe", "Mutable"] * 4


def element_counts(indices):
    counts = {"Feu": 0, "Terre": 0, "Air": 0, "Eau": 0}
    for i in indices:
        counts[SIGNS[i]["element"]] += 1
    return counts


def modality_counts(indices):
    counts = {"Cardinal": 0, "Fixe": 0, "Mutable": 0}
    for i in indices:
        counts[SIGN_MODALITY[i]] += 1
    return counts
