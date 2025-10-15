import json
from django.test import TestCase, Client
from .models import AgencyRealEstate

class PartenariatAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_agence_success(self):
        """
        Test that a new agency can be created successfully.
        """
        payload = {
            "name_agency": "Test Agency",
            "phone": "1234567890",
            "email": "test@agency.com",
            "site_web": "https://agency.test",
            "name_representative": "John Doe",
            "address": "123 Test St"
        }
        response = self.client.post(
            "/post/api/agence",
            data=json.dumps(payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertTrue(response_data['success'])
        self.assertEqual(response_data['msg'], "Vous recevrez un mail de la part de Louhsira")

        # Verify the object was created in the database
        self.assertTrue(AgencyRealEstate.objects.filter(email="test@agency.com").exists())

    def test_create_agence_duplicate(self):
        """
        Test that creating an agency with a duplicate email returns the correct message.
        """
        # Create an initial agency
        AgencyRealEstate.objects.create(
            name_agency="Existing Agency",
            phone="0987654321",
            email="duplicate@agency.com"
        )

        payload = {
            "name_agency": "Another Agency",
            "phone": "1122334455",
            "email": "duplicate@agency.com"
        }
        response = self.client.post(
            "/post/api/agence",
            data=json.dumps(payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertTrue(response_data['success'])
        self.assertEqual(response_data['msg'], "ce message est déjà envoyé")

    def test_create_agence_invalid_payload(self):
        """
        Test that the API returns a 422 error for an invalid payload (e.g., missing required fields).
        """
        # Payload missing the 'name_agency' required field
        payload = {
            "phone": "1234567890",
            "email": "invalid@agency.com"
        }
        response = self.client.post(
            "/post/api/agence",
            data=json.dumps(payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 422)
        response_data = response.json()
        # Django-ninja provides detailed error messages
        self.assertIn("detail", response_data)
        self.assertEqual(response_data["detail"][0]["msg"], "Field required")
        self.assertEqual(response_data["detail"][0]["loc"], ["body", "payload", "name_agency"])