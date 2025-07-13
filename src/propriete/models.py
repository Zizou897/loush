from datetime import timedelta
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

# Create your models here.
from app.models import Convention
from core.constants import (
    PICTURE_PATH,
)


STATUS_CHOICES = (  
    ('à vendre', 'à vendre'),
    ('à louer', 'à louer'),
)

class Photo(Convention):
    title = models.CharField(max_length=220, blank=True, null=True)
    picture = models.FileField(upload_to=PICTURE_PATH, max_length = 200, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Photo des Proprietes'
        verbose_name_plural = 'Photo des Proprietes'

    def __str__(self):
        return self.title

class TypePropriete(Convention):
    libele =  models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Type de Propriété"
        verbose_name_plural = "Type de Propriétés"
    def __str__(self):
        return self.libele


class Localite(Convention):
    name = models.CharField(max_length=150, blank=True, null=True)
    longitude =  models.CharField(max_length=150, blank=True, null=True)
    laltitude =  models.CharField(max_length=150, blank=True, null=True)
    
    class Meta:
        verbose_name = "Localité"
        verbose_name_plural = "Localités"
        
    def __str__(self):
        return self.name

class CaracteristiqueMaison(Convention):
    libele = models.CharField(max_length=220, blank=True, null=True)
    
    class Meta:
        verbose_name = "Caratéristiques des Maisons"
        verbose_name_plural = "Caratéristiques des Maisons"

    def __str__(self):
        return self.libele

    



class Proprietes(Convention):
    titre_annonce = models.CharField(max_length=220, blank=True, null=True)
    proprietaire = models.CharField(max_length=220, blank=True, null=True)
    proprietaire_contact = models.CharField(max_length=220, blank=True, null=True)
    type_propriete = models.ForeignKey(TypePropriete, on_delete=models.DO_NOTHING, related_name="type_propriete_related")
    prix_propriete = models.PositiveIntegerField(max_length=220, blank=True, null=True)
    adresse_propriete = models.CharField(max_length=220, blank=True, null=True)
    localite = models.ForeignKey(Localite, on_delete=models.DO_NOTHING, related_name="localite_propriete")
    annee_construction = models.DateField(auto_now=False, auto_now_add=False)
    nbre_chambre = models.IntegerField()
    nbre_salle_bain = models.IntegerField()
    description = HTMLField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    caracteristique_speciale = models.ManyToManyField(CaracteristiqueMaison)
    pictures = models.ManyToManyField(Photo)
    
    @property
    def is_new(self):
        return self.created_at >= timezone.now() - timedelta(days=7)
    
    class Meta:
        verbose_name = 'Les Propriétés'
        verbose_name_plural = 'Les Propriétés'

    def __str__(self):
        return self.titre_annonce

    