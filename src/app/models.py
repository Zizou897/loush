from django.db import models
from tinymce.models import HTMLField

# Create your models here.

"""_modif sur la partie ventre_

        sur la fonction qui return les 6 1er maison à vendre
"""

from core.constants import (
    BANNER_IMAGE_PATH, 
    LOCATION_PATH,
    ABOUT_PATH,
    WHYCHOOSE,
    LOGO_SITE_PATH,
    DO_TRUSTH_PATH
)


class Convention(models.Model):
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    publish = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Banner(Convention):
    title = models.CharField(max_length = 150)
    picture = models.FileField(upload_to=BANNER_IMAGE_PATH, max_length = 100)
    description = models.TextField()

    class Meta:
        verbose_name = "Bannière"
        verbose_name_plural = "Bannières"
    def __str__(self):
        return self.title

TYPE_HOUSE = (
    ('location', 'location'),
    ('vente', 'vente')
)


class Propriete(Convention):
    title = models.CharField(max_length = 150)
    description = models.TextField()
    author = models.CharField(max_length = 150)
    validators_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    picture = models.FileField(upload_to=LOCATION_PATH, max_length = 100)
    location_or_vendor = models.CharField(choices=TYPE_HOUSE, max_length = 150)
    
    
    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"
    def __str__(self):
        return self.title


class Propriete2(Convention):
    title = models.CharField(max_length = 150)
    description = models.TextField()
    author = models.CharField(max_length = 150)
    validators_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    picture = models.FileField(upload_to=LOCATION_PATH, max_length = 100)
    location_or_vendor = models.CharField(choices=TYPE_HOUSE, max_length = 150)
    
    
    class Meta:
        verbose_name = "Maison à Vendre"
        verbose_name_plural = "Maison à Vendre"
    def __str__(self):
        return self.title



class About(Convention):
    title = models.CharField(max_length = 150)
    description = models.TextField()
    picture = models.FileField(upload_to=ABOUT_PATH, max_length = 100)
    
    class Meta:
        verbose_name = "A propos"
        verbose_name_plural = "A propos"
    def __str__(self):
        return self.title


class Whychoose(Convention):
    title = models.CharField(max_length = 150)
    description = HTMLField()
    picture = models.FileField(upload_to=WHYCHOOSE, max_length = 100)
    
    class Meta:
        verbose_name = "Pourquoi Nous choisir"
        verbose_name_plural = "Pourquoi Nous choisir"
    def __str__(self):
        return self.title



class configuration(Convention):
    name = models.CharField(max_length = 150, blank=True, null=True)
    vendor_title = models.CharField(max_length = 150, blank=True, null=True)
    location_title = models.CharField(max_length = 150, blank=True, null=True)
    about_title = models.CharField(max_length = 150, blank=True, null=True)
    why_choose_title = models.CharField(max_length = 150, blank=True, null=True)
    newsletter_title = models.CharField(max_length = 150, blank=True, null=True)
    newsletter_text = models.TextField()
    newsletter_picture = models.FileField(upload_to=LOGO_SITE_PATH, max_length = 100)
    copy_right = models.CharField(max_length = 150, blank=True, null=True)
    logo = models.FileField(upload_to=LOGO_SITE_PATH , max_length = 100, blank=True, null=True)
    logo2 = models.FileField(upload_to=LOGO_SITE_PATH , max_length = 100, blank=True, null=True)
    
    class Meta:
        verbose_name = "Configuration du site"
        verbose_name_plural = "Configuration du site"
    def __str__(self):
        return self.name
    
    
class DoTrust(Convention):
    title = models.CharField(max_length = 150, blank=True, null=True)
    description = models.TextField()
    picture = models.FileField(upload_to=DO_TRUSTH_PATH, max_length=100)
    
    class Meta:
        verbose_name = "Faire Confiance"
        verbose_name_plural = "Faire Confiance"
        
    def __str__(self):
        return self.title
    