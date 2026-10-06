from django.test import TestCase
from rest_framework.test import APIClient

from .models import Campaign, NewsletterSubscriber, Program, VolunteerApplication


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
        Campaign.objects.create(
            title="Published Cause",
            slug="published-cause",
            summary="Visible cause",
            status="published",
        )
        Campaign.objects.create(
            title="Draft Cause",
            slug="draft-cause",
            summary="Hidden cause",
            status="draft",
        )

    def test_program_api_exposes_only_published_content(self):
        response = self.client.get("/api/v1/programs/")
        self.assertEqual(response.status_code, 200)
        titles = [item["title"] for item in response.data["results"]]
        self.assertEqual(titles, ["Published Program"])

    def test_campaign_api_exposes_only_published_content(self):
        response = self.client.get("/api/v1/campaigns/")
        self.assertEqual(response.status_code, 200)
        titles = [item["title"] for item in response.data["results"]]
        self.assertEqual(titles, ["Published Cause"])

    def test_search_ignores_draft_content(self):
        response = self.client.get("/api/v1/search/?q=Program")
        self.assertEqual(response.status_code, 200)
        titles = [item["title"] for item in response.data["results"]]
        self.assertIn("Published Program", titles)
        self.assertNotIn("Draft Program", titles)

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

    def test_volunteer_application_can_be_created(self):
        response = self.client.post(
            "/api/v1/volunteer/",
            {
                "name": "Volunteer Person",
                "email": "volunteer@example.com",
                "areas_of_interest": "Education",
                "skills": "Mentoring",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(VolunteerApplication.objects.count(), 1)

    def test_newsletter_subscription_is_idempotent(self):
        payload = {"email": "reader@example.com", "name": "Reader"}
        first = self.client.post("/api/v1/newsletter/", payload, format="json")
        second = self.client.post("/api/v1/newsletter/", payload, format="json")
        self.assertEqual(first.status_code, 200)
        self.assertEqual(second.status_code, 200)
        self.assertEqual(NewsletterSubscriber.objects.count(), 1)
