import os
from django.core.management.base import BaseCommand
from propriete.models import TypePropriete
from django.db.models import Count

class Command(BaseCommand):
    help = "Importer des types de propriété depuis un fichier texte"

    def add_arguments(self, parser):
        parser.add_argument('fichier', type=str, help="Chemin vers le fichier txt")

    def handle(self, *args, **kwargs):
        chemin = kwargs['fichier']
        compteur = 0

        if not os.path.exists(chemin):
            self.stdout.write(self.style.ERROR("Le fichier n'existe pas."))
            return

        with open(chemin, 'r', encoding='utf-8') as f:
            lignes = f.readlines()

        for ligne in lignes:
            parts = ligne.strip().split('::')  # Par ex. format: Nom::Description
            libele = parts[0].strip()
            description = parts[1].strip() if len(parts) > 1 else ''

            if not libele:
                continue

            existing = TypePropriete.objects.filter(libele=libele).first()
            if not existing:
                TypePropriete.objects.create(libele=libele, description=description)
                compteur += 1
                self.stdout.write(self.style.SUCCESS(f"Ajouté : {libele}"))
            else:
                self.stdout.write(f"Déjà existant : {libele}")

        self.stdout.write(self.style.WARNING(f"{compteur} type(s) ajouté(s)"))

        # === Nettoyage des doublons ===
        doublons = TypePropriete.objects.values('libele').annotate(total=Count('id')).filter(total__gt=1)

        for d in doublons:
            doublon_qs = TypePropriete.objects.filter(libele=d['libele'])
            to_keep = doublon_qs.first()
            deleted_count, _ = doublon_qs.exclude(id=to_keep.id).delete()
            self.stdout.write(self.style.NOTICE(f"{deleted_count} doublon(s) supprimé(s) pour : {d['libele']}"))

        self.stdout.write(self.style.SUCCESS("Importation terminée avec nettoyage des doublons."))
