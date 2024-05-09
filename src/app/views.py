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
    get_do_trusth
)

def verify_email(email):
    try:
        validate_email(email)
        return False
    except ValidationError:
        return True


def home(request):

    get_banners = get_banner({'publish':True})
    get_some_vendors = get_some_vendor({'publish':True,'location_or_vendor': 'vente'})
    get_some_locations = get_some_location({'publish':True,'location_or_vendor': 'location'})
    get_abouts = get_about({'publish':True})
    get_why_chooses = get_why_choose({'publish':True})
    get_configs = get_config({'publish':True})
    get_do_trusths = get_do_trusth({'publish':True})
    

    template_name = "layout/index.html"
    context = {
        'get_banners': get_banners,
        'get_some_vendors': get_some_vendors,
        'get_some_locations': get_some_locations,
        'get_abouts': get_abouts,
        'get_why_chooses': get_why_chooses,
        'get_configs': get_configs,
        'get_do_trusths': get_do_trusths
    }
    return render(request, template_name, context)



def search_page(request):
    
    get_configs = get_config({'publish':True})
    
    template_name = "layout/home_search.html"
    context = {
        'get_configs': get_configs,
    }
    return render(request, template_name, context)


def home_searcher(request):
    
    get_configs = get_config({'publish':True})
    
    template_name = "layout/home_searcher.html"
    context = {
        'get_configs': get_configs,
    }
    return render(request, template_name, context)


def owner_page(request):
    
    
    get_configs = get_config({'publish':True})
    template_name = "layout/owner.html"
    context = {
        'get_configs': get_configs,
    }
    return render(request, template_name, context)


@csrf_exempt
def post_ask_home(request):
    
    all_is_true = False
    msg = ''
    
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    
    if not name or name.isspace() or not email or email.isspace() or not phone or phone.isspace():
        msg = 'Veuillez renseigner les champs vides'
    elif len(phone) < 10:
        msg = 'Le numéro de téléphone doit etre e 10 chiffres'
    elif verify_email(email):
        msg = 'veuillez saisir un addresse Mail correct'
    
    else:
       all_is_true, msg = True, 'Vous recevrez un mail de la part de Louhsira'
       
    
    data = {
        'success': all_is_true,
        'msg': msg
    }
    return JsonResponse(data,safe=False)