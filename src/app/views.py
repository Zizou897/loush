from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import Q
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from propriete.models import Proprietes, TypePropriete

# Create your views here.
from .functions import (
    get_banner,
    get_about,
    get_why_choose,
    get_config,
    get_do_trusth,
    get_team,
    get_localite,
    get_type_propriete,
    get_social,
    get_section_triple,
    get_cgu_,
    get_all_properties,
    get_property_vendor,
    get_property_location,
    get_property_id,
    get_all_type_propriete,
    get_about_banner,
    get_partenaire,
    get_caracteristique_home,
    get_all_properties_for_index,
    get_vision,
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
    get_property_vendors = get_all_properties_for_index({'publish':True})
    get_property_locations = get_property_location({'publish':True, 'status': 'à louer'})
    get_abouts = get_about({'publish':True})
    get_why_chooses = get_why_choose({'publish':True})
    get_configs = get_config({'publish':True})
    get_do_trusths = get_do_trusth({'publish':True})
    get_localites = get_localite({'publish':True})
    get_type_proprietes = get_type_propriete({'publish':True})
    get_partenaires = get_partenaire({'publish':True})
    
    
    template_name = "app/layout/index.html"
    context = {
        'page': "LOUSHIRA | Accueil",
        'get_socials': get_socials,
        'get_banners': get_banners,
        'get_abouts': get_abouts,
        'get_why_chooses': get_why_chooses,
        'get_configs': get_configs,
        'get_do_trusths': get_do_trusths,
        'get_localites': get_localites,
        'get_type_proprietes': get_type_proprietes,
        'get_property_vendors': get_property_vendors,
        'get_property_locations': get_property_locations,
        'get_partenaires': get_partenaires,
        'get_caracteristique_homes': get_caracteristique_home,
    }
    return render(request, template_name, context)



def search_page(request):
    
    get_socials = get_social({'publish':True})
    get_configs = get_config({'publish':True})
    
    template_name = "app/layout/home_search.html"
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
    
    template_name = "app/layout/home_searcher.html"
    context = {
        'page': "LOUSHIRA | chercheur",
        'get_socials': get_socials,
        'get_configs': get_configs,
        'get_localites': get_localites,
        'get_type_proprietes': get_type_propriete,
        'get_caracteristique_homes': get_caracteristique_home,
    }
    return render(request, template_name, context)


def owner_page(request):
    
    get_socials = get_social({'publish':True})
    get_configs = get_config({'publish':True})
    get_type_proprietes = get_type_propriete({'publish':True})
    get_caracteristique_homes = get_caracteristique_home({'publish': True})
    template_name = "app/layout/owner.html"
    context = {
        'page': "LOUSHIRA | Proprietaire",
        'get_socials': get_socials,
        'get_configs': get_configs,
        'get_type_proprietes': get_type_proprietes,
        'get_caracteristique_homes': get_caracteristique_homes,
    }
    return render(request, template_name, context)

def data_caract(request):
    from django.http import JsonResponse
    data = list(get_caracteristique_home().values_list('libele', flat=True))
    return JsonResponse({'features': data})

def home_detail(request, id):

    get_socials = get_social({'publish':True})
    get_configs = get_config({'publish':True})
    get_property_ids = get_property_id(id)
    template_name = "app/layout/home_detail.html"
    context = {
        'page': "LOUSHIRA | Home-detail",
        'get_socials': get_socials,
        'get_configs': get_configs,
        'get_property_ids': get_property_ids
    }
    return render(request, template_name, context)
    

def catalogue(request):
    get_all__properties = get_all_properties({'publish': True, })
    
    
    if request.GET:
        print("##################ok######################")
        type_propriete = request.GET.get('type_propriete')  
        status = request.GET.get('status')
        prix_propriete = request.GET.get('prix_propriete')
        localite = request.GET.get('localite')
        
        print("intercepting...")
        print(type_propriete)
        print(status)
        print(prix_propriete)
        print(localite)
        
    
        filters = Q(publish=True)  # on affiche seulement les propriétés publiées

        if localite and localite != "Zone":
            filters &= Q(localite=int(localite))

        if type_propriete and type_propriete != "Type de propriété":
            filters &= Q(type_propriete=int(type_propriete))

        if status and status != "Status (A louer / A vendre)":
            filters &= Q(status=status)

        if prix_propriete and prix_propriete != "Prix":
            filters &= Q(prix_propriete=prix_propriete)

        get_all__properties = Proprietes.objects.filter(filters)

       
    get_socials = get_social({'publish':True})
    get_configs = get_config({'publish':True})
    get_localites = get_localite({'publish':True})
    get_type_proprietes = get_all_type_propriete({'publish':True})


    template_name = "app/layout/catalogue.html"
    context = {
        'page': "LOUSHIRA | Catalogue",
        'get_socials': get_socials,
        'get_configs': get_configs,
        'get_all__properties': get_all__properties,
        'get_localites': get_localites,
        'get_type_proprietes': get_type_proprietes
    }
    return render(request, template_name, context)
    

def about(request):
    liste = [1,3,5]
    get_socials = get_social({'publish':True})
    get_configs = get_config({'publish':True})
    get_about_banners = get_about_banner({'publish':True})
    get_teams = get_team({'publish':True})
    get_section_triples = get_section_triple({'publish':True})
    get_visions = get_vision({'publish':True})
    template_name = "app/layout/about.html"
    context = {
        'listes': liste,
        'page': "LOUSHIRA | A PROPOS",
        'get_socials': get_socials,
        'get_configs': get_configs,
        'get_about_banners': get_about_banners,
        'get_teams': get_teams,
        'get_section_triples': get_section_triples,
        'get_visions': get_visions
    }
    return render(request, template_name, context)


def agence(request):

    get_socials = get_social({'publish':True})
    get_configs = get_config({'publish':True})
   
    
    template_name = "app/layout/agence.html"
    context = {
        'page': "LOUSHIRA | AGENCE",
        'get_socials': get_socials,
        'get_configs': get_configs,
        
        
    }
    return render(request, template_name, context)




def condition_generale(request):
    
    get_socials = get_social({'publish':True})
    get_configs = get_config({'publish':True})
    get_cgu_s = get_cgu_({'publish': True})
    
    template_name = "app/layout/condition.html"
    context = {
        'page': "LOUSHIRA | CONDITIONS GENERALE",
        'get_socials': get_socials,
        'get_configs': get_configs,
        'get_cgu_s': get_cgu_s,
    }
    return render(request, template_name, context)


def contact(request):
    
    get_socials = get_social({'publish':True})
    get_configs = get_config({'publish':True})
    
    
    template_name = "app/layout/contact.html"
    context = {
        'page': "LOUSHIRA | Contact",
        'get_socials': get_socials,
        'get_configs': get_configs,
        
    }
    return render(request, template_name, context)