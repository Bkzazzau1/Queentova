from datetime import timedelta

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIClient

from .models import Announcement, Campaign, CampaignUpdate, CampaignUpdateMedia, FAQ, FounderMediaItem, FounderMediaPhoto, HomepageSpotlight, ImpactStory, NewsletterSubscriber, Partner, PartnerCollaboration, Program, Scholarship, ScholarshipApplication, ScholarshipApplicationDocument, SupportRequest, VolunteerApplication


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


    def test_homepage_spotlight_api_hides_inactive_items(self):
        now = timezone.now()
        HomepageSpotlight.objects.create(
            eyebrow="Featured",
            title="Live Spotlight",
            slug="live-spotlight",
            summary="Visible on the homepage.",
            link_url="/programs",
            starts_at=now - timedelta(hours=1),
            ends_at=now + timedelta(hours=1),
            status="published",
        )
        HomepageSpotlight.objects.create(
            eyebrow="Future",
            title="Future Spotlight",
            slug="future-spotlight",
            summary="Not visible yet.",
            link_url="/events",
            starts_at=now + timedelta(hours=1),
            status="published",
        )
        response = self.client.get("/api/v1/homepage-spotlights/")
        self.assertEqual(response.status_code, 200)
        slugs = [item["slug"] for item in response.data["results"]]
        self.assertEqual(slugs, ["live-spotlight"])


    def test_impact_story_api_exposes_only_active_consented_stories(self):
        now = timezone.now()
        visible = ImpactStory.objects.create(
            title="A consented impact story",
            slug="consented-impact-story",
            excerpt="A verified story shared with consent.",
            body="The public body.",
            consent_status=ImpactStory.ConsentStatus.ACTIVE,
            story_consent=True,
            privacy_reviewed=True,
            consent_reference="CONSENT-001",
            consent_recorded_at=now,
            status="published",
        )
        hidden = ImpactStory.objects.create(
            title="A story later withdrawn",
            slug="withdrawn-impact-story",
            excerpt="This should disappear.",
            body="Private after withdrawal.",
            consent_status=ImpactStory.ConsentStatus.ACTIVE,
            story_consent=True,
            privacy_reviewed=True,
            consent_reference="CONSENT-002",
            consent_recorded_at=now,
            status="published",
        )
        ImpactStory.objects.filter(pk=hidden.pk).update(
            consent_status=ImpactStory.ConsentStatus.WITHDRAWN
        )

        response = self.client.get("/api/v1/impact-stories/")
        self.assertEqual(response.status_code, 200)
        slugs = [item["slug"] for item in response.data["results"]]
        self.assertIn(visible.slug, slugs)
        self.assertNotIn(hidden.slug, slugs)

    def test_impact_story_public_serializer_hides_identity_by_default(self):
        now = timezone.now()
        ImpactStory.objects.create(
            title="Protected identity",
            slug="protected-identity",
            excerpt="Identity is protected.",
            body="A public-safe narrative.",
            approved_display_name="Private Full Name",
            identity_mode=ImpactStory.IdentityMode.ANONYMOUS,
            consent_status=ImpactStory.ConsentStatus.ACTIVE,
            story_consent=True,
            privacy_reviewed=True,
            consent_reference="CONSENT-003",
            consent_recorded_at=now,
            status="published",
        )

        response = self.client.get("/api/v1/impact-stories/protected-identity/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["public_name"], "Identity protected")
        self.assertNotIn("consent_reference", response.data)
        self.assertNotIn("approved_display_name", response.data)

    def test_minor_impact_story_requires_guardian_consent_before_publication(self):
        story = ImpactStory(
            title="Minor story",
            slug="minor-story",
            excerpt="Protected.",
            body="Protected narrative.",
            is_minor=True,
            consent_status=ImpactStory.ConsentStatus.ACTIVE,
            story_consent=True,
            privacy_reviewed=True,
            consent_reference="CONSENT-004",
            consent_recorded_at=timezone.now(),
            status="published",
        )

        with self.assertRaises(ValidationError):
            story.full_clean()


    def test_founder_media_api_keeps_unapproved_external_photos_private(self):
        item = FounderMediaItem.objects.create(
            title="Verified award coverage",
            slug="verified-award-coverage",
            kind="award",
            summary="A verified source-linked recognition.",
            source_name="Anambra State Government",
            source_url="https://anambrastate.gov.ng/example/",
            source_domain="anambrastate.gov.ng",
            verified_source=True,
            status="published",
        )
        FounderMediaPhoto.objects.create(
            media_item=item,
            external_image_url="https://anambrastate.gov.ng/wp-content/uploads/example.jpg",
            alt_text="Candidate publication photograph",
            credit="Anambra State Government",
            source_url=item.source_url,
            reuse_approved=False,
            is_primary=True,
        )

        response = self.client.get("/api/v1/founder-media/verified-award-coverage/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["source_url"], item.source_url)
        self.assertTrue(response.data["verified_source"])
        self.assertEqual(response.data["photos"], [])

    def test_founder_media_api_exposes_approved_external_photo(self):
        item = FounderMediaItem.objects.create(
            title="Approved media photo",
            slug="approved-media-photo",
            kind="news",
            summary="A publication with an approved source image.",
            source_name="Independent Newspaper Nigeria",
            source_url="https://independent.ng/example/",
            source_domain="independent.ng",
            verified_source=True,
            status="published",
        )
        FounderMediaPhoto.objects.create(
            media_item=item,
            external_image_url="https://independent.ng/wp-content/uploads/example.jpg",
            alt_text="Approved publication photograph",
            credit="Independent Newspaper Nigeria",
            source_url=item.source_url,
            reuse_approved=True,
            is_primary=True,
        )

        response = self.client.get("/api/v1/founder-media/approved-media-photo/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["photos"]), 1)
        self.assertEqual(
            response.data["photos"][0]["image_url"],
            "https://independent.ng/wp-content/uploads/example.jpg",
        )


    def test_activity_update_api_filters_by_campaign(self):
        campaign = Campaign.objects.create(
            title="Water Relief",
            slug="water-relief",
            summary="Emergency water relief.",
            status="published",
        )
        other_campaign = Campaign.objects.create(
            title="Education Relief",
            slug="education-relief",
            summary="Education support.",
            status="published",
        )
        now = timezone.now()

        CampaignUpdate.objects.create(
            title="Water delivery completed",
            slug="water-delivery-completed",
            campaign=campaign,
            kind="delivery",
            summary="A verified field delivery update.",
            occurred_at=now,
            status="published",
        )
        CampaignUpdate.objects.create(
            title="School materials delivered",
            slug="school-materials-delivered",
            campaign=other_campaign,
            kind="delivery",
            summary="A separate campaign update.",
            occurred_at=now,
            status="published",
        )

        response = self.client.get("/api/v1/activity-updates/?campaign=water-relief")
        self.assertEqual(response.status_code, 200)
        slugs = [item["slug"] for item in response.data["results"]]
        self.assertEqual(slugs, ["water-delivery-completed"])

    def test_activity_update_rejects_unverified_public_expenditure(self):
        campaign = Campaign.objects.create(
            title="Food Relief",
            slug="food-relief",
            summary="Food assistance.",
            status="published",
        )
        update = CampaignUpdate(
            title="Food purchase",
            slug="food-purchase",
            campaign=campaign,
            kind="funding",
            summary="A financial field update.",
            occurred_at=timezone.now(),
            expenditure_amount="5000.00",
            expenditure_currency="USD",
            expenditure_verified=False,
            verification_note="",
            status="published",
        )

        with self.assertRaises(ValidationError):
            update.full_clean()

    def test_activity_update_hides_unapproved_external_media(self):
        program = Program.objects.create(
            title="Youth Program",
            slug="youth-program",
            summary="Youth empowerment.",
            status="published",
        )
        update = CampaignUpdate.objects.create(
            title="Youth field update",
            slug="youth-field-update",
            program=program,
            kind="field",
            summary="A program activity update.",
            occurred_at=timezone.now(),
            status="published",
        )
        CampaignUpdateMedia.objects.create(
            update=update,
            media_type="photo",
            external_url="https://example.com/photo.jpg",
            alt_text="Candidate photo",
            reuse_approved=False,
        )

        response = self.client.get("/api/v1/activity-updates/youth-field-update/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["media"], [])


    def test_partner_api_exposes_only_verified_published_relationships(self):
        Partner.objects.create(
            title="Verified Partner",
            slug="verified-partner",
            description="A verified relationship.",
            verified_relationship=True,
            verification_note="Confirmed by Foundation administration.",
            status="published",
        )
        Partner.objects.create(
            title="Unverified Partner",
            slug="unverified-partner",
            description="Should not be public.",
            verified_relationship=False,
            status="published",
        )

        response = self.client.get("/api/v1/partners/")
        self.assertEqual(response.status_code, 200)
        slugs = [item["slug"] for item in response.data["results"]]
        self.assertIn("verified-partner", slugs)
        self.assertNotIn("unverified-partner", slugs)

    def test_partner_requires_verification_before_publication(self):
        partner = Partner(
            title="Unverified Publish Attempt",
            slug="unverified-publish-attempt",
            description="Should fail validation.",
            verified_relationship=False,
            status="published",
        )

        with self.assertRaises(ValidationError):
            partner.full_clean()

    def test_partner_collaboration_api_requires_verified_record_and_partner(self):
        partner = Partner.objects.create(
            title="Institution Partner",
            slug="institution-partner",
            description="Verified partner.",
            verified_relationship=True,
            verification_note="Relationship confirmed.",
            status="published",
        )
        visible = PartnerCollaboration.objects.create(
            partner=partner,
            title="Education collaboration",
            slug="education-collaboration",
            summary="A verified collaboration.",
            verified_record=True,
            verification_note="Confirmed collaboration record.",
            status="published",
        )
        hidden = PartnerCollaboration.objects.create(
            partner=partner,
            title="Unverified collaboration",
            slug="unverified-collaboration",
            summary="Should stay hidden.",
            verified_record=False,
            status="published",
        )

        response = self.client.get("/api/v1/partner-collaborations/?partner=institution-partner")
        self.assertEqual(response.status_code, 200)
        slugs = [item["slug"] for item in response.data["results"]]
        self.assertIn(visible.slug, slugs)
        self.assertNotIn(hidden.slug, slugs)

    def test_activity_update_hides_unverified_partner_links(self):
        verified = Partner.objects.create(
            title="Verified Activity Partner",
            slug="verified-activity-partner",
            verified_relationship=True,
            verification_note="Confirmed.",
            status="published",
        )
        hidden = Partner.objects.create(
            title="Hidden Activity Partner",
            slug="hidden-activity-partner",
            verified_relationship=False,
            status="published",
        )
        program = Program.objects.create(
            title="Partner Program",
            slug="partner-program",
            summary="Program linked to partners.",
            status="published",
        )
        update = CampaignUpdate.objects.create(
            title="Partner-supported delivery",
            slug="partner-supported-delivery",
            program=program,
            kind="delivery",
            summary="A public update.",
            occurred_at=timezone.now(),
            status="published",
        )
        update.partners.add(verified, hidden)

        response = self.client.get("/api/v1/activity-updates/partner-supported-delivery/")
        self.assertEqual(response.status_code, 200)
        partner_slugs = [item["slug"] for item in response.data["partners"]]
        self.assertEqual(partner_slugs, ["verified-activity-partner"])


    def test_internal_scholarship_application_returns_private_receipt_only(self):
        scholarship = Scholarship.objects.create(
            title="Private Scholarship",
            slug="private-scholarship",
            summary="Apply privately.",
            application_status=Scholarship.ApplicationStatus.OPEN,
            internal_applications_enabled=True,
            opens_at=timezone.now() - timedelta(days=1),
            closes_at=timezone.now() + timedelta(days=7),
            status="published",
        )
        transcript = SimpleUploadedFile(
            "transcript.pdf",
            b"%PDF-1.4 private academic record",
            content_type="application/pdf",
        )

        response = self.client.post(
            f"/api/v1/scholarships/{scholarship.slug}/apply/",
            {
                "first_name": "Ada",
                "last_name": "Applicant",
                "email": "ada@example.com",
                "phone": "+2348000000000",
                "country": "Nigeria",
                "city": "Awka",
                "institution": "Example University",
                "course_of_study": "Engineering",
                "current_level": "300",
                "academic_summary": "Strong academic performance.",
                "financial_need_statement": "I need support to continue my education.",
                "personal_statement": "Education will help me contribute to my community.",
                "consent_to_processing": True,
                "declaration_true": True,
                "academic_document": transcript,
            },
            format="multipart",
        )

        self.assertEqual(response.status_code, 201)
        self.assertIn("reference_code", response.data)
        self.assertEqual(response.data["status"], "submitted")
        self.assertNotIn("email", response.data)
        self.assertNotIn("first_name", response.data)
        self.assertNotIn("academic_document", response.data)

        application = ScholarshipApplication.objects.get(email="ada@example.com")
        self.assertEqual(application.scholarship, scholarship)
        self.assertEqual(application.documents.count(), 1)
        document = ScholarshipApplicationDocument.objects.get(application=application)
        self.assertEqual(document.document_type, "academic")

    def test_scholarship_application_is_rejected_outside_open_window(self):
        scholarship = Scholarship.objects.create(
            title="Closed Internal Scholarship",
            slug="closed-internal-scholarship",
            summary="Applications closed.",
            application_status=Scholarship.ApplicationStatus.OPEN,
            internal_applications_enabled=True,
            opens_at=timezone.now() - timedelta(days=10),
            closes_at=timezone.now() - timedelta(days=1),
            status="published",
        )

        response = self.client.post(
            f"/api/v1/scholarships/{scholarship.slug}/apply/",
            {
                "first_name": "Late",
                "last_name": "Applicant",
                "email": "late@example.com",
                "country": "Nigeria",
                "financial_need_statement": "Need.",
                "personal_statement": "Statement.",
                "consent_to_processing": True,
                "declaration_true": True,
            },
            format="multipart",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(ScholarshipApplication.objects.count(), 0)

    def test_duplicate_scholarship_email_is_rejected(self):
        scholarship = Scholarship.objects.create(
            title="One Application Scholarship",
            slug="one-application-scholarship",
            summary="One application per email.",
            application_status=Scholarship.ApplicationStatus.OPEN,
            internal_applications_enabled=True,
            status="published",
        )
        payload = {
            "first_name": "One",
            "last_name": "Applicant",
            "email": "same@example.com",
            "country": "Nigeria",
            "financial_need_statement": "Need statement.",
            "personal_statement": "Personal statement.",
            "consent_to_processing": True,
            "declaration_true": True,
        }

        first = self.client.post(
            f"/api/v1/scholarships/{scholarship.slug}/apply/",
            payload,
            format="multipart",
        )
        second = self.client.post(
            f"/api/v1/scholarships/{scholarship.slug}/apply/",
            payload,
            format="multipart",
        )

        self.assertEqual(first.status_code, 201)
        self.assertEqual(second.status_code, 400)
        self.assertEqual(ScholarshipApplication.objects.count(), 1)

    def test_application_status_lookup_does_not_expose_scores_or_documents(self):
        scholarship = Scholarship.objects.create(
            title="Status Scholarship",
            slug="status-scholarship",
            summary="Track privately.",
            status="published",
        )
        application = ScholarshipApplication.objects.create(
            scholarship=scholarship,
            first_name="Status",
            last_name="Applicant",
            email="status@example.com",
            country="Nigeria",
            financial_need_statement="Need",
            personal_statement="Statement",
            consent_to_processing=True,
            declaration_true=True,
            review_status=ScholarshipApplication.ReviewStatus.SHORTLISTED,
            eligibility_score="88.00",
            overall_score="85.00",
        )

        response = self.client.post(
            "/api/v1/scholarship-application-status/",
            {
                "reference_code": application.reference_code,
                "email": "status@example.com",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["status"], "shortlisted")
        self.assertNotIn("eligibility_score", response.data)
        self.assertNotIn("overall_score", response.data)
        self.assertNotIn("documents", response.data)

        wrong_email = self.client.post(
            "/api/v1/scholarship-application-status/",
            {
                "reference_code": application.reference_code,
                "email": "wrong@example.com",
            },
            format="json",
        )
        self.assertEqual(wrong_email.status_code, 404)

    def test_public_scholarship_results_are_aggregate_and_release_controlled(self):
        scholarship = Scholarship.objects.create(
            title="Results Scholarship",
            slug="results-scholarship",
            summary="Aggregate results only.",
            max_awards=2,
            public_results_released=False,
            status="published",
        )
        ScholarshipApplication.objects.create(
            scholarship=scholarship,
            first_name="Selected",
            last_name="Applicant",
            email="selected@example.com",
            country="Nigeria",
            financial_need_statement="Need",
            personal_statement="Statement",
            consent_to_processing=True,
            declaration_true=True,
            review_status=ScholarshipApplication.ReviewStatus.APPROVED,
        )

        hidden = self.client.get("/api/v1/scholarships/results-scholarship/")
        self.assertEqual(hidden.status_code, 200)
        self.assertIsNone(hidden.data["results_summary"])

        scholarship.public_results_released = True
        scholarship.public_results_note = "Selection has concluded."
        scholarship.save()

        released = self.client.get("/api/v1/scholarships/results-scholarship/")
        self.assertEqual(released.status_code, 200)
        self.assertEqual(released.data["results_summary"]["selected"], 1)
        self.assertEqual(released.data["results_summary"]["applications_received"], 1)
        self.assertNotIn("applications", released.data)

    def test_scholarship_rejects_mixed_internal_and_external_application_channels(self):
        scholarship = Scholarship(
            title="Ambiguous Channel",
            slug="ambiguous-channel",
            summary="Invalid configuration.",
            internal_applications_enabled=True,
            application_url="https://example.com/apply",
        )

        with self.assertRaises(ValidationError):
            scholarship.full_clean()
