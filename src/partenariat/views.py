from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .models import AgencyRealEstate, Searcher, Owner
# Create your views here.
def verify_email(email):
    try:
        validate_email(email)
        return False
    except ValidationError:
        return True


@csrf_exempt
def post_agence(request):
    all_is_true = False
    msg = ''
    
    
    name_agency = request.POST.get('name_agency')
    phone =  request.POST.get('phone')
    site_web =  request.POST.get('site_web')
    email = request.POST.get('email')
    name_representative =  request.POST.get('name_representative')
    address_agency =  request.POST.get('address_agency')
    
    if not name_agency or name_agency.isspace() or not email or email.isspace() or not phone or phone.isspace():
        msg = 'Veuillez renseigner les champs vides'
    elif len(phone) < 10:
        msg = 'Le numéro de téléphone doit etre de 10 chiffres'
    elif verify_email(email):
        msg = 'veuillez saisir un addresse Mail correct'
    
    else:
        all_is_true, msg = True, 'Vous recevrez un mail de la part de Louhsira'
       
        agence, created = AgencyRealEstate.objects.get_or_create(name_agency=name_agency,  phone=phone, email=email, site_web=site_web, name_representative=name_representative, address=address_agency)
        print(created)
        if created:
            msg = "ce message est déjà envoyé"
        else:
            agence.save()
       
    
    data = {
        'success': all_is_true,
        'msg': msg
    }
    return JsonResponse(data,safe=False)


@csrf_exempt
def post_searcher(request):
    
    all_is_true = False
    msg = ''
    
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    #--------------------------------------
    type_propriete_rechercher = request.POST.get('type_propriete_rechercher')
    achat_or_location = request.POST.get('achat_or_location')
    nbr_chambre = request.POST.get('nbr_chambre')
    nbr_salle_bain = request.POST.get('nbr_salle_bain')
    surface_habitable = request.POST.get('surface_habitable')
    localisation_souhaite = request.POST.get('localisation_souhaite')
    caract_souhaite = request.POST.get('caract_souhaite')
    #-------------------------------------------
    date_demenag_souhaite = request.POST.get('date_demenag_souhaite')
    comments_souhaite = request.POST.get('comments_souhaite')
    
    
    if not name or name.isspace() or not email or email.isspace() or not phone or phone.isspace():
        msg = 'Veuillez renseigner les champs vides'
    elif len(phone) < 10:
        msg = 'Le numéro de téléphone doit etre e 10 chiffres'
    elif verify_email(email):
        msg = 'veuillez saisir un addresse Mail correct'
    
    else:
       all_is_true, msg = True, 'Vous recevrez un mail de la part de Louhsira'
       
       searcher, created = Searcher.objects.get_or_create(name=name, email=email, phone=phone, type_propriete_rechercher=type_propriete_rechercher, achat_or_location=achat_or_location, nbr_chambre=nbr_chambre, nbr_salle_bain=nbr_salle_bain, surface_habitable=surface_habitable, localisation_souhaite=localisation_souhaite, caract_souhaite=caract_souhaite, date_demenag_souhaite=date_demenag_souhaite, comments_souhaite=comments_souhaite)
       if created:
            msg = "ce message est déjà envoyé"
       else:
            searcher.save()
    
    data = {
        'success': all_is_true,
        'msg': msg
    }
    return JsonResponse(data,safe=False)


@csrf_exempt
def post_owner(request):
    all_is_true = False
    msg = ''
    
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    
    type_propriete = request.POST.get('type_propriete_for_owner')
    status = request.POST.get('status_buy_sell')
    budjet = request.POST.get('home_price')
    address_propriete = request.POST.get('home_address')
    annee_construction = request.POST.get('year_building')
    surface_habitable = request.POST.get('living_space')
    nbr_chambre = request.POST.get('nbr_room')
    nbr_salle_bain = request.POST.get('nbr_bath_room')
    caracteris_special = request.POST.get('other_detail')
    
    description = request.POST.get('home_detail')
    
    if not name or name.isspace() or not email or email.isspace() or not phone or phone.isspace():
        msg = 'Veuillez renseigner les champs vides'
    elif verify_email(email):
        msg = 'veuillez saisir un addresse Mail correct'
    else:
       all_is_true, msg = True, "Notre equipe vous contactera dans un bref delai !!! "
       owner, created = Owner.objects.get_or_create(name=name, email=email, phone=phone, type_propriete=type_propriete, status=status, budjet=budjet, address_propriete=address_propriete, annee_construction=annee_construction, surface_habitable=surface_habitable, nbr_chambre=nbr_chambre, nbr_salle_bain=nbr_salle_bain, caracteris_special=caracteris_special, description=description)
       if created:
            msg = "ce message est déjà envoyé"
       else:
            owner.save()
       

    data = {
        'success': all_is_true,
        'msg': msg
    }
    return JsonResponse(data,safe=False)