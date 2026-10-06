from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import Program


class PublicApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        Program.objects.create(
            title="Published Program",
            slug="published-program",
            summary="Visible",
            status="published",
        )
        Program.objects.create(
            title="Draft Program",
            slug="draft-program",
            summary="Hidden",
            status="draft",
        )

    def test_program_api_exposes_only_published_content(self):
        response = self.client.get("/api/v1/programs/")
        self.assertEqual(response.status_code, 200)
        titles = [item["title"] for item in response.data["results"]]
        self.assertEqual(titles, ["Published Program"])

    def test_contact_submission_can_be_created(self):
        response = self.client.post(
            "/api/v1/contact/",
            {
                "name": "Test Person",
                "email": "test@example.com",
                "enquiry_type": "partnership",
                "message": "We would like to discuss a partnership.",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)
