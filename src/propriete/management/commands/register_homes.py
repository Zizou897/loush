from django.core.management.base import BaseCommand
from propriete.models import CaracteristiqueMaison
from unidecode import unidecode

class Command(BaseCommand):
    help = 'Ajoute les types de maisons depuis un fichier texte.'

    def add_arguments(self, parser):
        parser.add_argument('fichier', type=str, help='Chemin vers le fichier contenant les types de maisons.')

    def handle(self, *args, **options):
        chemin_fichier = options['fichier']
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
                lignes = fichier.readlines()
                for ligne in lignes:
                    libele = ligne.strip()
                    if not libele:
                        continue
                    
                    libele_normalise = unidecode(libele.strip().lower())
                    existant = CaracteristiqueMaison.objects.filter(
                        libele__iexact=libele_normalise
                    ).first()

                    if not existant:
                        CaracteristiqueMaison.objects.create(libele=libele)
                        self.stdout.write(self.style.SUCCESS(f"✅ Ajouté : {libele}"))
                    else:
                        self.stdout.write(self.style.WARNING(f"⚠️ Déjà présent : {libele}"))

        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"❌ Fichier non trouvé : {chemin_fichier}"))
