from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import (
    Banner, 
    Propriete,
    About,
    Whychoose,
    configuration,
    DoTrust,
    Team,
    Localite,
    TypePropriete,
    Social,
    SectionTriple,
    ClassButton,
    Links,
    CGU,
)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("image_view", "title", "created_at", "publish")
    date_hierarchy = "created_at"
    list_per_page = 10
    list_editable = ["publish"]

    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"


@admin.register(Propriete)
class ProprieteAdmin(admin.ModelAdmin):
    list_display = ("image_view", "title", "author", "location_or_vendor","created_at", "publish",)
    date_hierarchy = "created_at"
    list_per_page = 10
    list_editable = ["publish"]

    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"



@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("image_view", "title", "created_at", "publish")
    date_hierarchy = "created_at"
    list_per_page = 10
    list_editable = ["publish"]

    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"



@admin.register(Whychoose)
class WhychooseAdmin(admin.ModelAdmin):
    list_display = ("image_view", "title", "created_at", "publish")
    date_hierarchy = "created_at"
    list_per_page = 10
    list_editable = ["publish"]

    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"


@admin.register(configuration)
class configurationAdmin(admin.ModelAdmin):
    list_display = ("logo_view", "name", "created_at", "publish")
    date_hierarchy = "created_at"
    list_per_page = 10
    list_editable = ["publish"]

    def logo_view(self, obj):
        return mark_safe(f'<img src="{obj.logo.url}" style="height:100px; width:150px">')
    logo_view.short_description = "Aperçu des images"
    

@admin.register(DoTrust)
class DoTrustAdmin(admin.ModelAdmin):
    list_display = ("logo_view", "title", "created_at", "publish")
    date_hierarchy = "created_at"
    list_per_page = 10
    list_editable = ["publish"]

    def logo_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    logo_view.short_description = "Aperçu des images"
    

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("image_view", "name", "created_at", "publish")
    date_hierarchy = "created_at"
    list_per_page = 10
    list_editable = ["publish"]

    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"
    

@admin.register(Localite)
class LocaliteAdmin(admin.ModelAdmin):
    list_display = ("name", "longitude", "laltitude","created_at", "publish")
    date_hierarchy = "created_at"
    list_per_page = 10
    list_editable = ["publish"]
    

@admin.register(TypePropriete)
class TypeProprieteAdmin(admin.ModelAdmin):
    list_display = ("libele","created_at", "publish")
    date_hierarchy = "created_at"
    list_per_page = 10
    list_editable = ["publish"]
    

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ("name", "link","created_at", "publish")
    date_hierarchy = "created_at"
    list_per_page = 10
    list_editable = ["publish"]
    

@admin.register(ClassButton)
class ClassButtonAdmin(admin.ModelAdmin):
    list_display = ("name","created_at", "publish")
    date_hierarchy = "created_at"
    list_per_page = 10
    list_editable = ["publish"]


@admin.register(SectionTriple)
class SectionTripleAdmin(admin.ModelAdmin):
    list_display = ("order", "title","created_at", "publish")
    date_hierarchy = "created_at"
    list_per_page = 10
    list_editable = ["publish"]



@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "publish")
    date_hierarchy = "created_at"
    list_per_page = 10
    list_editable = ["publish"]
    

@admin.register(CGU)
class CGUAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "publish")
    date_hierarchy = "created_at"
    list_per_page = 10
    list_editable = ["publish"]
