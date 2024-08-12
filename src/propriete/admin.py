from django.contrib import admin


# Register your models here.
from propriete.models import Proprietes, Photo, TypePropriete, Localite, CaracteristiqueMaison



@admin.register(TypePropriete)
class TypeProprieteAdmin(admin.ModelAdmin):
    list_display = ("libele","created_at", "publish")
    date_hierarchy = "created_at"
    list_per_page = 10
    list_editable = ["publish"]


@admin.register(Localite)
class LocaliteAdmin(admin.ModelAdmin):
    list_display = ("name", "longitude", "laltitude","created_at", "publish")
    date_hierarchy = "created_at"
    list_per_page = 10
    list_editable = ["publish"]
    

@admin.register(Proprietes)
class ProprietesAdmin(admin.ModelAdmin):
    list_display = ('titre_annonce','proprietaire','type_propriete', 'prix_propriete', 'adresse_propriete', 'status', 'publish')
    date_hierarchy = "created_at"   
    list_per_page = 10
 

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title',)
    date_hierarchy = "created_at"   
    list_per_page = 10
 

@admin.register(CaracteristiqueMaison)
class CaracteristiqueMaisonAdmin(admin.ModelAdmin):
    list_display = ("libele","created_at", "publish")
    date_hierarchy = "created_at"
    list_per_page = 10
    list_editable = ["publish"]
