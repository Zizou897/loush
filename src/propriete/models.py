from django.db import models

# Create your models here.
from app.models import Convention
from core.constants import (
    PICTURE_PATH,
)


STATUS_CHOICES = (
    ('VENDRE', 'à vendre'),
    ('LOUER', 'à louer'),
)

class Photo(Convention):
    picture = models.FileField(upload_to=PICTURE_PATH, max_length = 200)
    
    class Meta:
        verbose_name = 'Photo des Proprietes'
        verbose_name_plural = 'Photo des Proprietes'

    def __str__(self):
        return self .id



class Proprietes(Convention):
    
    titre_annonce = models.CharField(max_length=220, blank=True, null=True)
    proprietaire = models.CharField(max_length=220, blank=True, null=True)
    proprietaire_contact = models.CharField(max_length=220, blank=True, null=True)
    type_propriete = models.CharField(max_length=220, blank=True, null=True)
    prix_propriete = models.CharField(max_length=220, blank=True, null=True)
    adresse_propriete = models.CharField(max_length=220, blank=True, null=True)
    localité = models.CharField(max_length=220, blank=True, null=True)
    annee_construction = models.DateField(auto_now=False, auto_now_add=False)
    nbre_chambre = models.IntegerField()
    nbre_salle_bain = models.IntegerField()
    description = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    pictures = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='propriete_picture')
    
    
    class Meta:
        verbose_name = 'Les Propriétés'
        verbose_name_plural = 'Les Propriétés'

    def __str__(self):
        return self.titre_annonce

    