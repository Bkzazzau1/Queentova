from datetime import timedelta

from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIClient

from .models import Announcement, Campaign, FAQ, NewsletterSubscriber, Program, SupportRequest, VolunteerApplication


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


    def test_support_request_requires_consent_and_contact(self):
        response = self.client.post(
            "/api/v1/request-support/",
            {
                "name": "Applicant",
                "country": "Nigeria",
                "assistance_type": "education",
                "request_summary": "I need support to continue my education.",
                "consent_to_contact": True,
                "phone": "+2348000000000",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(SupportRequest.objects.count(), 1)


    def test_faq_api_exposes_only_published_questions(self):
        FAQ.objects.create(
            question="Published question?",
            slug="published-question",
            answer="Published answer.",
            status="published",
        )
        FAQ.objects.create(
            question="Draft question?",
            slug="draft-question",
            answer="Draft answer.",
            status="draft",
        )
        response = self.client.get("/api/v1/faqs/")
        self.assertEqual(response.status_code, 200)
        slugs = [item["slug"] for item in response.data["results"]]
        self.assertIn("published-question", slugs)
        self.assertNotIn("draft-question", slugs)

    def test_announcement_api_hides_expired_and_future_items(self):
        now = timezone.now()
        Announcement.objects.create(
            title="Active",
            slug="active-announcement",
            message="Visible now",
            starts_at=now - timedelta(hours=1),
            ends_at=now + timedelta(hours=1),
            priority=10,
            status="published",
        )
        Announcement.objects.create(
            title="Expired",
            slug="expired-announcement",
            message="No longer visible",
            ends_at=now - timedelta(minutes=1),
            status="published",
        )
        Announcement.objects.create(
            title="Future",
            slug="future-announcement",
            message="Not yet visible",
            starts_at=now + timedelta(hours=1),
            status="published",
        )
        response = self.client.get("/api/v1/announcements/")
        self.assertEqual(response.status_code, 200)
        slugs = [item["slug"] for item in response.data["results"]]
        self.assertEqual(slugs, ["active-announcement"])
