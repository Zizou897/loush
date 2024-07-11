from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your views here.
from .functions import (
    get_banner,
    get_some_vendor,
    get_some_location,
    get_about,
    get_why_choose,
    get_config,
    get_do_trusth,
    get_team,
    get_localite,
    get_type_propriete,
    get_social
)

def verify_email(email):
    try:
        validate_email(email)
        return False
    except ValidationError:
        return True


def home(request):

    get_socials = get_social({'publish':True})
    get_banners = get_banner({'publish':True})
    get_some_vendors = get_some_vendor({'publish':True,'location_or_vendor': 'vente'})
    get_some_locations = get_some_location({'publish':True,'location_or_vendor': 'location'})
    get_abouts = get_about({'publish':True})
    get_why_chooses = get_why_choose({'publish':True})
    get_configs = get_config({'publish':True})
    get_do_trusths = get_do_trusth({'publish':True})
    get_localites = get_localite({'publish':True})
    get_type_proprietes = get_type_propriete({'publish':True})
    

    template_name = "layout/index.html"
    context = {
        'page': "LOUSHIRA | Accueil",
        'get_socials': get_socials,
        'get_banners': get_banners,
        'get_some_vendors': get_some_vendors,
        'get_some_locations': get_some_locations,
        'get_abouts': get_abouts,
        'get_why_chooses': get_why_chooses,
        'get_configs': get_configs,
        'get_do_trusths': get_do_trusths,
        'get_localites': get_localites,
        'get_type_proprietes': get_type_proprietes
    }
    return render(request, template_name, context)



def search_page(request):
    
    get_socials = get_social({'publish':True})
    get_configs = get_config({'publish':True})
    
    template_name = "layout/home_search.html"
    context = {
        'page': "LOUSHIRA | Chercher-une-maison",
        'get_socials': get_socials,
        'get_configs': get_configs,
    }
    return render(request, template_name, context)


def home_searcher(request):
    
    get_socials = get_social({'publish':True})
    get_configs = get_config({'publish':True})
    get_localites = get_localite({'publish':True})
    get_type_proprietes = get_type_propriete({'publish':True})
    
    template_name = "layout/home_searcher.html"
    context = {
        'page': "LOUSHIRA | chercheur",
        'get_socials': get_socials,
        'get_configs': get_configs,
        'get_localites': get_localites,
        'get_type_proprietes': get_type_proprietes,
    }
    return render(request, template_name, context)


def owner_page(request):
    
    get_socials = get_social({'publish':True})
    get_configs = get_config({'publish':True})
    template_name = "layout/owner.html"
    context = {
        'page': "LOUSHIRA | Proprietaire",
        'get_socials': get_socials,
        'get_configs': get_configs,
    }
    return render(request, template_name, context)



def home_detail(request):

    get_socials = get_social({'publish':True})
    get_configs = get_config({'publish':True})

    template_name = "layout/home_detail.html"
    context = {
        'page': "LOUSHIRA | Home-detail",
        'get_socials': get_socials,
        'get_configs': get_configs,
    }
    return render(request, template_name, context)
    

def catalogue(request):
    
    get_socials = get_social({'publish':True})
    get_configs = get_config({'publish':True})
    get_some_vendors = get_some_vendor({'publish':True,'location_or_vendor': 'vente'})

    template_name = "layout/catalogue.html"
    context = {
        'page': "LOUSHIRA | Catalogue",
        'get_socials': get_socials,
        'get_configs': get_configs,
        'get_some_vendors': get_some_vendors,
    }
    return render(request, template_name, context)
    

def about(request):

    get_socials = get_social({'publish':True})
    get_configs = get_config({'publish':True})
    get_some_vendors = get_some_vendor({'publish':True,'location_or_vendor': 'vente'})
    get_teams = get_team({'publish':True})

    template_name = "layout/about.html"
    context = {
        'page': "LOUSHIRA | A PROPOS",
        'get_socials': get_socials,
        'get_configs': get_configs,
        'get_some_vendors': get_some_vendors,
        'get_teams': get_teams
    }
    return render(request, template_name, context)


def agence(request):

    get_socials = get_social({'publish':True})
    get_configs = get_config({'publish':True})
    get_some_vendors = get_some_vendor({'publish':True,'location_or_vendor': 'vente'})
    
    template_name = "layout/agence.html"
    context = {
        'page': "LOUSHIRA | AGENCE",
        'get_socials': get_socials,
        'get_configs': get_configs,
        'get_some_vendors': get_some_vendors,
        
    }
    return render(request, template_name, context)




def condition_generale(request):
    
    get_socials = get_social({'publish':True})
    get_configs = get_config({'publish':True})
    
    template_name = "layout/condition.html"
    context = {
        'page': "LOUSHIRA | CONDITIONS GENERALE",
        'get_socials': get_socials,
        'get_configs': get_configs,
    }
    return render(request, template_name, context)