import os
from django.core.management.base import BaseCommand
from propriete.models import Localite
from django.db.models import Count
from django.db import transaction

class Command(BaseCommand):
    help = "Importer des localités depuis un fichier texte (avec ou sans coordonnées)"

    def add_arguments(self, parser):
        parser.add_argument('fichier', type=str, help="Chemin vers le fichier txt")

    def handle(self, *args, **kwargs):
        chemin = kwargs['fichier']
        compteur = 0

        if not os.path.exists(chemin):
            self.stdout.write(self.style.ERROR("Le fichier spécifié n'existe pas."))
            return

        with open(chemin, 'r', encoding='utf-8') as f:
            lignes = f.readlines()

        for ligne in lignes:
            ligne = ligne.strip()
            if not ligne:
                continue

            parts = ligne.split('::')
            name = parts[0].strip()
            longitude = parts[1].strip() if len(parts) > 1 else None
            laltitude = parts[2].strip() if len(parts) > 2 else None

            if not name:
                continue

            existing = Localite.objects.filter(name=name).first()
            if not existing:
                try:
                    with transaction.atomic():
                        loc = Localite.objects.create(name=name, longitude=longitude, laltitude=laltitude)
                        compteur += 1
                        self.stdout.write(self.style.SUCCESS(f"Ajouté : {name}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Erreur lors de l'ajout de {name} : {str(e)}"))
            else:
                self.stdout.write(f"Déjà existant : {name}")

        self.stdout.write(self.style.WARNING(f"{compteur} localité(s) ajoutée(s)"))

        # Nettoyage des doublons par nom
        try:
            doublons = Localite.objects.values('name').annotate(total=Count('id')).filter(total__gt=1)

            for d in doublons:
                doublon_qs = Localite.objects.filter(name=d['name'])
                to_keep = doublon_qs.first()
                deleted_count, _ = doublon_qs.exclude(id=to_keep.id).delete()
                self.stdout.write(self.style.NOTICE(f"{deleted_count} doublon(s) supprimé(s) pour : {d['name']}"))

            self.stdout.write(self.style.SUCCESS("Importation terminée avec nettoyage des doublons."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erreur lors du nettoyage des doublons : {str(e)}"))
