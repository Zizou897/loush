import csv
from django.core.management.base import BaseCommand
from src.propriete.models import CaracteristiqueMaison

class Command(BaseCommand):
    help = 'Importer des données depuis un fichier texte'

    def handle(self, *args, **options):
        with open('src/script/Caractéristiques_maison.txt', 'r') as file:
            for ligne in file:
                caracteristique = CaracteristiqueMaison(libele=ligne.strip())
                caracteristique.save()
        self.stdout.write(self.style.SUCCESS('Importation terminée'))
