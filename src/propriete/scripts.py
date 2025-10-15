from propriete.models import CaracteristiqueMaison


def importer_caracteristiques(fichier):
    with open(fichier, "r", encoding="utf-8") as file:
        data = file.readlines()

    for ligne in data:
        caracteristique = CaracteristiqueMaison(libele=ligne.strip())
        caracteristique.save()


# Exemple d'utilisation :
fichier = "Caractéristiques_maison.txt"
importer_caracteristiques(fichier)
