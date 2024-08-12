from django.contrib import admin

from .models import AgencyRealEstate, Searcher, Owner, Newsletters
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
    


@admin.register(Newsletters)
class NewslettersAdmin(admin.ModelAdmin):
    list_display = ('email','created_at')

    date_hierarchy = "created_at"
    list_per_page = 10
    


