from django import template

register = template.Library()

@register.filter
def format_with_dot(value):
    try:
        number = int(value)
        return '{:,}'.format(number).replace(',', '.')
    except (ValueError, TypeError):
        return value

@register.simple_tag
def my_enumerate(queryset):
    for index, item in enumerate(queryset):
        yield index, item 


ICONE_CARACTERISTIQUES = {
    "abri de jardin": "fa-tree",
    "aire de barbecue": "fa-fire",
    "balcon": "fa-building",
    "bibliothèque": "fa-book",
    "bureau": "fa-briefcase",
    "buanderie": "fa-boxes-stacked",
    "cave à vin": "fa-wine-glass",
    "cellier": "fa-boxes-packing",
    "chambre": "fa-bed",
    "chauffage": "fa-temperature-high",
    "cheminée": "fa-fire",
    "climatisation": "fa-fan",
    "cuisine": "fa-utensils",
    "douche": "fa-shower",
    "dressing": "fa-person-dress",
    "garage": "fa-car",
    "jardin": "fa-seedling",
    "jacuzzi": "fa-hot-tub-person",
    "panneaux solaires": "fa-solar-panel",
    "piscine": "fa-water-ladder",
    "salle à manger": "fa-chair",
    "salle de bains": "fa-bath",
    "salle de cinéma": "fa-film",
    "salle de jeux": "fa-gamepad",
    "salle de sport": "fa-dumbbell",
    "salon": "fa-couch",
    "salon extérieur": "fa-umbrella-beach",
    "sauna": "fa-hot-tub-person",
    "domotique": "fa-house-signal",
    "purification": "fa-droplet",
    "sécurité": "fa-shield-halved",
    "terrain de sport": "fa-basketball",
    "terrasse": "fa-sun",
    "véranda": "fa-house-chimney-window",
}

@register.filter
def icone_caracteristique(nom):
    key = nom.lower()
    for mot, icone in ICONE_CARACTERISTIQUES.items():
        if mot in key:
            return icone
    return "fa-circle-info"