from django.db import models
from app.models import Convention
from propriete.models import Proprietes

# Create your models here.


class Reservation(Convention):
    name_of_reserver = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=254)
    propriete_reserve = models.ForeignKey(
        Proprietes, on_delete=models.DO_NOTHING, related_name="reserve_propriete"
    )

    class Meta:
        verbose_name = "Réservation"
        verbose_name_plural = "Réservations"

    def __str__(self):
        return self.name_of_reserver


class ContactUs(Convention):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Nous Contacter"
        verbose_name_plural = "Nous Contacter"

    def __str__(self):
        return self.name
