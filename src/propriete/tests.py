from django.test import TestCase, Client
from django.urls import reverse
from datetime import date
from .models import Proprietes, TypePropriete, Localite, CaracteristiqueMaison, Photo

class ProprieteModelTest(TestCase):
    """
    Suite de tests pour les modèles de l'application Propriete.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Configure les objets non modifiés utilisés par toutes les méthodes de test.
        """
        cls.localite = Localite.objects.create(name="Cocody Angré")
        cls.type_propriete = TypePropriete.objects.create(libele="Appartement")

    def test_creation_propriete(self):
        """
        Teste la création d'une instance du modèle Proprietes.
        """
        propriete = Proprietes.objects.create(
            titre_annonce="Appartement moderne à Angré",
            proprietaire="M. Dupont",
            proprietaire_contact="0123456789",
            type_propriete=self.type_propriete,
            prix_propriete=50000000,
            adresse_propriete="Près du nouveau pont",
            localite=self.localite,
            annee_construction=date(2021, 5, 10),
            nbre_chambre=3,
            nbre_salle_bain=2,
            description="<p>Un bel appartement lumineux.</p>",
            status='à vendre'
        )

        # Vérifie que l'objet a été créé et que les champs sont corrects
        self.assertEqual(propriete.titre_annonce, "Appartement moderne à Angré")
        self.assertEqual(str(propriete), "Appartement moderne à Angré")
        self.assertEqual(propriete.nbre_chambre, 3)
        self.assertEqual(propriete.status, "à vendre")
        self.assertTrue(propriete.is_new) # Le bien a été créé récemment

    def test_relations_many_to_many(self):
        """
        Teste les relations ManyToMany (caractéristiques et photos).
        """
        propriete = Proprietes.objects.create(
            titre_annonce="Test ManyToMany",
            type_propriete=self.type_propriete,
            localite=self.localite,
            annee_construction=date(2020, 1, 1),
            nbre_chambre=1,
            nbre_salle_bain=1,
            status='à louer'
        )

        # Ajout de caractéristiques
        caracteristique1 = CaracteristiqueMaison.objects.create(libele="Piscine")
        caracteristique2 = CaracteristiqueMaison.objects.create(libele="Jardin")
        propriete.caracteristique_speciale.add(caracteristique1, caracteristique2)

        self.assertEqual(propriete.caracteristique_speciale.count(), 2)
        self.assertIn(caracteristique1, propriete.caracteristique_speciale.all())

        # Ajout de photos
        photo1 = Photo.objects.create(title="Façade")
        photo2 = Photo.objects.create(title="Salon")
        propriete.pictures.add(photo1, photo2)

        self.assertEqual(propriete.pictures.count(), 2)
        self.assertIn(photo2, propriete.pictures.all())


class ProprieteViewTest(TestCase):
    """
    Suite de tests pour les vues liées aux propriétés.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Configure les objets nécessaires pour les tests des vues.
        """
        cls.client = Client()
        cls.localite = Localite.objects.create(name="Testville")
        cls.type_propriete = TypePropriete.objects.create(libele="Maison")
        cls.propriete = Proprietes.objects.create(
            titre_annonce="Maison à Testville",
            type_propriete=cls.type_propriete,
            localite=cls.localite,
            annee_construction=date(2022, 1, 1),
            nbre_chambre=4,
            nbre_salle_bain=3,
            status='à vendre'
        )
        cls.catalogue_url = reverse('catalogue')
        cls.detail_url = reverse('home-detail', args=[cls.propriete.id])
        cls.invalid_detail_url = reverse('home-detail', args=[999])

    def test_catalogue_view(self):
        """
        Teste que la page du catalogue se charge correctement.
        """
        response = self.client.get(self.catalogue_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/layout/catalogue.html')

    def test_home_detail_view_success(self):
        """
        Teste que la page de détail d'une propriété se charge correctement.
        """
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/layout/home_detail.html')
        self.assertContains(response, self.propriete.titre_annonce)

    def test_home_detail_view_not_found(self):
        """
        Teste que la page de détail renvoie une erreur 404 pour un ID invalide.
        """
        response = self.client.get(self.invalid_detail_url)
        self.assertEqual(response.status_code, 404)