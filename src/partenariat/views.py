
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .models import AgencyRealEstate, Searcher, Owner, Newsletters
#from .task import send_costumize_email 
from core.utils import send_costumize_email
from propriete.models import Proprietes, CaracteristiqueMaison, Localite, TypePropriete
from reserves.models import Reservation, ContactUs
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
        all_is_true, msg = True, "ce message est déjà envoyé"
       
        agence, created = AgencyRealEstate.objects.get_or_create(name_agency=name_agency,  phone=phone, email=email, site_web=site_web, name_representative=name_representative, address=address_agency)
        print(created)
        if created:
            msg = 'Vous recevrez un mail de la part de Louhsira'
            # Recuperer les données
            
            template = 'emails/agence_emails/agence.html'
            subjet = "Demande de partenariat"
            message = "Louhsira vous dit merci"
            context = {}
            receivers = [agence.email]
            

            # fichier = '/home/areb/Documents/GitHub/loush/src/partenariat/type_maison.txt' 
            # fichier = 'src/partenariat/Secteurs(Quartiers) de Ouagadougou.txt'
            # src/partenariat/Caractéristiques_maison.txt
            # with open(fichier, 'r', encoding='utf-8') as file:
            #     data = file.readlines()

            # for ligne in data:
            #     lacalite = TypePropriete(libele=ligne.strip())
            #     lacalite.save()
           
            
            # Envoyer l'email
            has_send = send_costumize_email.after_response( 
                subjet=subjet, 
                receivers=receivers, 
                template=template, 
                context=context
            )
            
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
    localisation_souhaite = request.POST.get('select_features_local')
    caract_souhaite = request.POST.get('select_features')
    #-------------------------------------------
    date_demenag_souhaite = "12/13/2023"
    comments_souhaite = request.POST.get('comments_souhaite')
    
    
    if not name or name.isspace() or not email or email.isspace() or not phone or phone.isspace():
        msg = 'Veuillez renseigner les champs vides'
    elif verify_email(email):
        msg = 'veuillez saisir un addresse Mail correct'
    
    else:
        all_is_true, msg = True, "ce message est déjà envoyé"
       
        searcher, created = Searcher.objects.get_or_create(name=name, email=email, phone=phone, type_propriete_rechercher=type_propriete_rechercher, achat_or_location=achat_or_location, nbr_chambre=nbr_chambre, nbr_salle_bain=nbr_salle_bain, surface_habitable=surface_habitable, localisation_souhaite=localisation_souhaite, caract_souhaite=caract_souhaite, date_demenag_souhaite=date_demenag_souhaite, comments_souhaite=comments_souhaite)
        if created:
            msg = 'Vous recevrez un mail de la part de Louhsira'
            
            # Recuperation des données 
            
            template = 'emails/chercheur/chercheur.html'
            subjet = "Demande de partenariat"
            message = "Louhsira vous dit merci"
            context = {}
            receivers = [searcher.email]
            
            # Envoyer l'email
            has_send = send_costumize_email.after_response ( 
                subjet=subjet, 
                receivers=receivers, 
                template=template, 
                context=context
            )
            
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
    caracteris_special = request.POST.get('select_features')
    print("##########")
    print(caracteris_special)
    description = request.POST.get('home_detail')
    
    if verify_email(email):
        msg = 'veuillez saisir un addresse Mail correct'
    else:
       all_is_true, msg = True, "ce message est déjà envoyé" 
       owner, created = Owner.objects.get_or_create(name=name, email=email, phone=phone, type_propriete=type_propriete, status=status, budjet=budjet, address_propriete=address_propriete, annee_construction=annee_construction, surface_habitable=surface_habitable, nbr_chambre=nbr_chambre, nbr_salle_bain=nbr_salle_bain, caracteris_special=caracteris_special, description=description)
       if created:
            msg = "Notre equipe vous contactera dans un bref delai !!! "
       else:
            owner.save()
    print(name)

    data = {
        'success': all_is_true,
        'msg': msg
    }
    return JsonResponse(data,safe=False)



@csrf_exempt
def post_newsletter(request):
    all_is_true = False
    msg = ''
    
    email = request.POST.get('email')
    
    if verify_email(email):
        msg = 'veuillez saisir un addresse Mail correct'
    else:
        all_is_true, msg = True, "Vous etes déjà abonné" 
        news, created = Newsletters.objects.get_or_create(email=email)
        
        if created:
            msg = "Vous serrez mis au courant dès qu'il y a du nouveau !!! "
        else:
            news.save()
        
    data = {
        'success': all_is_true,
        'msg': msg
    }
    
    return JsonResponse(data,safe=False)


@csrf_exempt
def post_reservation(request):
    all_is_true = False
    msg = ''
    
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    property_reserve = request.POST.get('property_reserve')
    print('#####1111#########')
    if not name or name.isspace() or not email or email.isspace() or not phone or phone.isspace():
        msg = 'Veuillez renseigner les champs vides'
    
    elif verify_email(email):
        print('#####2222#########')
        msg = 'veuillez saisir un addresse Mail correct'
        print('#####3333#########')
    else:
        all_is_true = True
        print('#####4444#########')
        property_reserve_obj = Proprietes.objects.get(pk=(property_reserve))
        reserve, created = Reservation.objects.get_or_create(name_of_reserver=name, phone=phone, email=email, propriete_reserve=property_reserve_obj)
        if created:
            reserve.save()
            msg = "Louhsira vous contactera dès que possible !!!"
            
            template = 'emails/reservation/reservation.html'
            subjet = "Demande de réservation"
            message = "Louhsira vous dit merci"
            context = {
                'name_property': property_reserve_obj.titre_annonce,
                'name': name,
            }
            receivers = [reserve.email]
            
            
            # Envoyer l'email
            print('66666666666666666666666')
            # has_send = send_costumize_email.after_response( 
            #     subjet=subjet, 
            #     receivers=receivers, 
            #     template=template, 
            #     context=context
            # )
           
            #print(has_send)
            print('intercepting.....')
        else:
            msg =  "Réservation déjà prise en compte"
        print('#####5555#########')
            
    
    data = {
        'success': all_is_true,
        'msg': msg
    }
    return JsonResponse(data,safe=False)



@csrf_exempt
def contact_us(request):
    
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    
    if not all([name, email, subject]):
        data = {
            'success': False,
            'msg': 'Veuillez renseigner les champs obligatoires'
        }
        return JsonResponse(data, safe=False)
    
    if verify_email(email):
        data = {
            'success': False,
            'msg': 'Veuillez saisir une adresse email valide'
        }
        return JsonResponse(data, safe=False)
    
    contact, created = ContactUs.objects.get_or_create(name=name, email=email, subject=subject, message=message)
   
   
    if created:
        data = {
            'success': True,
            'msg': 'Louhsira vous contactera dans les heures qui suivent'
        }
        
        return JsonResponse(data, safe=False)
    else:
       
        data = {
            'success': True,
            'msg': 'Message déjà envoyé'
        }
        return JsonResponse(data, safe=False)