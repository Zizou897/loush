from django.shortcuts import get_object_or_404
from .models import (
    Banner,
    AboutBanner,
    About,
    Whychoose,
    configuration,
    DoTrust,
    Team,
    Social,
    SectionTriple,
    CGU,
    Partenaire,
    Vision,
    Valeur,
)

from propriete.models import TypePropriete, Localite, Proprietes, CaracteristiqueMaison


def get_banner(data=dict()):
    return Banner.objects.filter(**data).first()


def get_about_banner(data=dict()):
    return AboutBanner.objects.filter(**data).first()


def get_about(data=dict()):
    return About.objects.filter(**data).first()


def get_why_choose(data=dict()):
    return Whychoose.objects.filter(**data).first()


def get_config(data=dict()):
    return configuration.objects.filter(**data).first()


def get_do_trusth(data=dict()):
    return DoTrust.objects.filter(**data)


def get_vision(data=dict()):
    return Vision.objects.filter(**data).first()


def get_team(data=dict()):
    return Team.objects.filter(**data)


def get_localite(data=dict()):
    return Localite.objects.filter(**data)


def get_localisation(data=dict()):
    return Localite.objects.all()


def get_caracteristique_home(data=dict()):
    return CaracteristiqueMaison.objects.all()


def get_type_propriete(data=dict()):
    return TypePropriete.objects.filter(**data)


def get_all_type_propriete(data=dict()):
    return TypePropriete.objects.all()


def get_social(data=dict()):
    return Social.objects.filter(**data)


def get_section_triple(data=dict()):
    return SectionTriple.objects.filter(**data)


def get_cgu_(data=dict()):
    return CGU.objects.filter(**data)


def get_partenaire(data=dict()):
    return Partenaire.objects.filter(**data)


def get_nos_valeur(data=dict()):
    return Valeur.objects.filter(**data)


##------------------CATALOGUE------------------------------


def get_all_properties(data=dict()):
    return Proprietes.objects.filter(**data)


def get_all_properties_for_index(data=dict()):
    return Proprietes.objects.filter(**data).order_by("-created_at")[:6]


def get_property_vendor(data=dict()):
    return Proprietes.objects.filter(**data).order_by("created_at")[:6]


def get_property_location(data=dict()):
    return Proprietes.objects.filter(**data).order_by("created_at")[:6]


##--------------------HOME-DETAIL-----------------------------


def get_property_id(id):
    return get_object_or_404(Proprietes, id=id)
