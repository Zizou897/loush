from django.db import models

# Create your models here.

from app.models import Convention

class AgencyRealEstate(Convention):
    name_agency = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=150)
    site_web = models.URLField(max_length = 200)
    name_representative = models.CharField(max_length=150, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    
    class Meta:
        verbose_name = "Agence Immobilière"
        verbose_name_plural = "Agence Immobilière"
        

    def __str__(self):
        return self.name_agency

  
class Searcher(Convention):
    name = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(max_length=150)
    #------------------------------------------------------------
    type_propriete_rechercher = models.CharField(max_length=150, blank=True, null=True)
    achat_or_location = models.CharField(max_length=150, blank=True, null=True)
    nbr_chambre = models.CharField(max_length=150, blank=True, null=True)
    nbr_salle_bain = models.CharField(max_length=150, blank=True, null=True)
    surface_habitable = models.CharField(max_length=150, blank=True, null=True)
    localisation_souhaite = models.CharField(max_length=150, blank=True, null=True)
    caract_souhaite = models.CharField(max_length=150, blank=True, null=True)
    #------------------------------------------------------------
    date_demenag_souhaite = models.CharField(max_length=150, blank=True, null=True)
    comments_souhaite = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = "Chercheur"
        verbose_name_plural = "Chercheurs"
        
    def __str__(self):
        return self.name



class Owner(Convention):
    name = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(max_length=150)
    #-----------------------------------------------------
    type_propriete = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    budjet = models.CharField(max_length=250, blank=True, null=True)
    address_propriete = models.CharField(max_length=200, blank=True, null=True)
    annee_construction = models.CharField(max_length=200, blank=True, null=True)
    surface_habitable = models.CharField(max_length=100, blank=True, null=True)
    nbr_chambre = models.CharField(max_length=100, blank=True, null=True)
    nbr_salle_bain = models.CharField(max_length=100, blank=True, null=True)
    caracteris_special = models.CharField(max_length=200, blank=True, null=True)
    #---------------------------------------------------------------------
    description = models.TextField()
    #---------------------------------------------------------------------
   
    class Meta:
        verbose_name = "Proprietaire"
        verbose_name_plural = "Proprietaires"
        
    def __str__(self):
        return self.name


class Newsletters(Convention):
    email = models.EmailField(max_length=254)
    
    class Meta:
        verbose_name = "Newsletters"
        verbose_name_plural = "Newsletters"
        
    def __str__(self):
        return self.email

    