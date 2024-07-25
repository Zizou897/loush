from .models import (
    Banner,
    Propriete,
    Propriete2,
    About,
    Whychoose,
    configuration,
    DoTrust, 
    Team, 
    Localite,
    TypePropriete,
    Social,
    SectionTriple,
    CGU
)



def get_banner(data=dict()):
    return Banner.objects.filter(**data).first()

def get_some_vendor(data=dict()):
    return Propriete.objects.filter(**data).order_by('created_at')[:6]

def get_some_location(data=dict()):
    return Propriete.objects.filter(**data).order_by('created_at')[:6]

def get_about(data=dict()):
    return About.objects.filter(**data).first()

def get_why_choose(data=dict()):
    return Whychoose.objects.filter(**data).first()

def get_config(data=dict()):
    return configuration.objects.filter(**data).first()

def get_do_trusth(data=dict()):
    return DoTrust.objects.filter(**data)

def get_team(data=dict()):
    return Team.objects.filter(**data)

def get_localite(data=dict()):
    return Localite.objects.filter(**data)

def get_type_propriete(data=dict()):
    return Localite.objects.filter(**data)

def get_social(data=dict()):
    return Social.objects.filter(**data)

def get_section_triple(data=dict()):
    return SectionTriple.objects.filter(**data)

def get_cgu_(data=dict()):
    return CGU.objects.filter(**data)