from ninja import NinjaAPI, Schema
from django.http import HttpRequest
from typing import List, Optional

from .models import AgencyRealEstate, Searcher, Owner, Newsletters
from propriete.models import Proprietes
from reserves.models import Reservation, ContactUs

api = NinjaAPI()

# Schemas pour la validation des données

class AgencySchema(Schema):
    name_agency: str
    phone: str
    email: str
    site_web: Optional[str] = None
    name_representative: Optional[str] = None
    address: Optional[str] = None

class SearcherSchema(Schema):
    name: str
    email: str
    phone: str
    type_propriete_rechercher: Optional[str] = None
    achat_or_location: Optional[str] = None
    nbr_chambre: Optional[str] = None
    nbr_salle_bain: Optional[str] = None
    surface_habitable: Optional[str] = None
    localisation_souhaite: Optional[str] = None
    caract_souhaite: Optional[str] = None
    date_demenag_souhaite: str = "12/13/2023" # Gardé pour la compatibilité, mais devrait être un DateField
    comments_souhaite: Optional[str] = None

class OwnerSchema(Schema):
    name: str
    email: str
    phone: str
    type_propriete: Optional[str] = None
    status: Optional[str] = None
    budjet: Optional[str] = None
    address_propriete: Optional[str] = None
    annee_construction: Optional[str] = None
    surface_habitable: Optional[str] = None
    nbr_chambre: Optional[str] = None
    nbr_salle_bain: Optional[str] = None
    caracteris_special: Optional[str] = None
    description: Optional[str] = None

class NewsletterSchema(Schema):
    email: str

class ReservationSchema(Schema):
    name: str
    email: str
    phone: str
    property_reserve: int

class ContactUsSchema(Schema):
    name: str
    email: str
    subject: str
    message: str

class MessageOut(Schema):
    success: bool
    msg: str


# Endpoints de l'API

@api.post("/agence", response=MessageOut)
def create_agence(request: HttpRequest, payload: AgencySchema):
    agence, created = AgencyRealEstate.objects.get_or_create(
        email=payload.email,
        defaults=payload.dict()
    )
    if created:
        # Ici, on pourrait ajouter la logique d'envoi d'email via Celery
        return {"success": True, "msg": "Vous recevrez un mail de la part de Louhsira"}
    return {"success": True, "msg": "ce message est déjà envoyé"}

@api.post("/searcher", response=MessageOut)
def create_searcher(request: HttpRequest, payload: SearcherSchema):
    searcher, created = Searcher.objects.get_or_create(
        email=payload.email,
        defaults=payload.dict()
    )
    if created:
        return {"success": True, "msg": "Vous recevrez un mail de la part de Louhsira"}
    return {"success": True, "msg": "ce message est déjà envoyé"}

@api.post("/owner", response=MessageOut)
def create_owner(request: HttpRequest, payload: OwnerSchema):
    owner, created = Owner.objects.get_or_create(
        email=payload.email,
        defaults=payload.dict()
    )
    if created:
        return {"success": True, "msg": "Notre equipe vous contactera dans un bref delai !!!"}
    return {"success": True, "msg": "ce message est déjà envoyé"}

@api.post("/newsletter", response=MessageOut)
def subscribe_newsletter(request: HttpRequest, payload: NewsletterSchema):
    news, created = Newsletters.objects.get_or_create(email=payload.email)
    if created:
        return {"success": True, "msg": "Vous serrez mis au courant dès qu'il y a du nouveau !!!"}
    return {"success": True, "msg": "Vous etes déjà abonné"}

@api.post("/reservation", response=MessageOut)
def create_reservation(request: HttpRequest, payload: ReservationSchema):
    try:
        property_obj = Proprietes.objects.get(pk=payload.property_reserve)
    except Proprietes.DoesNotExist:
        return {"success": False, "msg": "La propriété spécifiée n'existe pas."}

    reserve, created = Reservation.objects.get_or_create(
        email=payload.email,
        propriete_reserve=property_obj,
        defaults={'name_of_reserver': payload.name, 'phone': payload.phone}
    )
    if created:
        return {"success": True, "msg": "Louhsira vous contactera dès que possible !!!"}
    return {"success": True, "msg": "Réservation déjà prise en compte"}

@api.post("/contact", response=MessageOut)
def create_contact_message(request: HttpRequest, payload: ContactUsSchema):
    contact, created = ContactUs.objects.get_or_create(
        email=payload.email,
        subject=payload.subject,
        defaults={'name': payload.name, 'message': payload.message}
    )
    if created:
        return {"success": True, "msg": "Louhsira vous contactera dans les heures qui suivent"}
    return {"success": True, "msg": "Message déjà envoyé"}