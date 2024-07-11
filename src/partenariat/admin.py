from django.contrib import admin

from .models import AgencyRealEstate, Searcher, Owner
# Register your models here.

@admin.register(AgencyRealEstate)
class AgencyRealEstateAdmin(admin.ModelAdmin):
    list_display = ('name_agency', 'phone', 'site_web', 'address', 'name_representative','created_at','publish')

    date_hierarchy = "created_at"
    list_per_page = 10
    list_editable = ["publish"]
    

@admin.register(Searcher)
class SearcherAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'type_propriete_rechercher', 'achat_or_location','created_at','publish')

    date_hierarchy = "created_at"
    list_per_page = 10
    list_editable = ["publish"]


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'type_propriete', 'status','created_at','publish')

    date_hierarchy = "created_at"
    list_per_page = 10
    list_editable = ["publish"]