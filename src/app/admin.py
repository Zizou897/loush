from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import (
    Banner, 
    Propriete,
    About,
    Whychoose,
    configuration,
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