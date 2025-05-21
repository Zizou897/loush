from django.contrib import admin
from .models import Reservation, ContactUs
# Register your models here.


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name_of_reserver', 'phone', 'email', )

    date_hierarchy = "created_at"
    list_per_page = 10
  


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', )

    date_hierarchy = "created_at"
    list_per_page = 10
  