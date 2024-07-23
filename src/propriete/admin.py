from django.contrib import admin

# Register your models here.
from propriete.models import Proprietes, Photo





@admin.register(Proprietes)
class ProprietesAdmin(admin.ModelAdmin):
    list_display = ('titre_annonce','proprietaire','type_propriete', 'prix_propriete', 'adresse_propriete',)
    date_hierarchy = "created_at"   
    list_per_page = 10
 


