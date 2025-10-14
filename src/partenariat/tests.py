from django.test import TestCase
from django.urls import reverse
from .models import AgencyRealEstate, Searcher, Owner, Newsletters

class PartenariatModelTest(TestCase):
    """
    Suite de tests pour les modèles de l'application Partenariat.
    """

    def test_creation_agency(self):
        """
        Teste la création d'une instance du modèle AgencyRealEstate.
        """
        agency = AgencyRealEstate.objects.create(
            name_agency="Immo Test",
            email="contact@immotest.com",
            site_web="https://immotest.com"
        )
        self.assertEqual(agency.name_agency, "Immo Test")
        self.assertEqual(str(agency), "Immo Test")

    def test_creation_newsletter(self):
        """
        Teste la création d'une instance du modèle Newsletters.
        """
        newsletter = Newsletters.objects.create(email="test@example.com")
        self.assertEqual(newsletter.email, "test@example.com")
        self.assertEqual(str(newsletter), "test@example.com")


class PartenariatViewTest(TestCase):
    """
    Suite de tests pour les vues de l'application Partenariat.
    """

    def test_post_newsletter_view(self):
        """
        Teste la soumission à la newsletter.
        """
        url = reverse('post-news')
        email = 'newsubscriber@example.com'
        response = self.client.post(url, {'email': email})

        # La vue renvoie une JsonResponse avec un statut 200
        self.assertEqual(response.status_code, 200)

        # Vérifie le contenu de la réponse JSON
        json_response = response.json()
        self.assertTrue(json_response['success'])
        self.assertIn("Vous serrez mis au courant", json_response['msg'])

        # Vérifie que l'email a bien été enregistré en base de données
        self.assertTrue(Newsletters.objects.filter(email=email).exists())