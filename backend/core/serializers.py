from django.db.models import Q
from rest_framework import serializers

from .models import (
    Announcement,
    Campaign,
    CampaignUpdate,
    CampaignUpdateMedia,
    ContactSubmission,
    Event,
    FAQ,
    FounderAchievement,
    FounderMediaItem,
    FounderMediaPhoto,
    FounderProfile,
    GalleryItem,
    HomepageSpotlight,
    ImpactMetric,
    ImpactStory,
    NewsletterSubscriber,
    Partner,
    Program,
    Resource,
    Scholarship,
    SiteProfile,
    Story,
    SupportRequest,
    VolunteerApplication,
)


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = [
            "title", "slug", "summary", "body", "icon", "featured",
            "seo_title", "seo_description", "seo_keywords", "published_at",
        ]


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = [
            "title", "slug", "excerpt", "body", "category", "event_date",
            "hero_image", "hero_alt", "featured", "source_name", "source_url",
            "seo_title", "seo_description", "seo_keywords", "published_at",
        ]


class GalleryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryItem
        fields = [
            "title", "slug", "media_type", "image", "video_url", "alt_text",
            "caption", "category", "event_date", "published_at",
        ]


class FounderProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FounderProfile
        fields = [
            "title", "slug", "primary_name", "public_record_name", "maiden_name",
            "headline", "biography", "motto", "faith_line", "portrait", "portrait_alt",
            "seo_title", "seo_description", "seo_keywords", "published_at",
        ]


class FounderAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = FounderAchievement
        fields = [
            "title", "slug", "year", "description", "source_name", "source_url",
            "published_at",
        ]


class ImpactMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImpactMetric
        fields = [
            "title", "slug", "value", "unit", "period", "verification_note",
            "source_reference", "published_at",
        ]


class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholarship
        fields = [
            "title", "slug", "summary", "eligibility", "application_status",
            "opens_at", "closes_at", "application_url", "published_at",
        ]


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ["title", "slug", "description", "website", "logo", "published_at"]


class CampaignSerializer(serializers.ModelSerializer):
    progress_percent = serializers.SerializerMethodField()

    class Meta:
        model = Campaign
        fields = [
            "title", "slug", "summary", "body", "image", "image_alt",
            "goal_amount", "current_amount", "currency", "starts_at", "ends_at",
            "featured", "accepting_support", "cta_label", "progress_percent",
            "seo_title", "seo_description", "seo_keywords", "published_at",
        ]

    def get_progress_percent(self, obj):
        if not obj.goal_amount or obj.goal_amount <= 0:
            return None
        return min(round((obj.current_amount / obj.goal_amount) * 100, 1), 100)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "title", "slug", "summary", "body", "starts_at", "ends_at",
            "venue_name", "address", "city", "country", "online_url",
            "registration_url", "image", "image_alt", "featured",
            "seo_title", "seo_description", "seo_keywords", "published_at",
        ]


class SiteProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteProfile
        fields = [
            "slug", "display_name", "short_description", "contact_email", "phone",
            "whatsapp", "office_address", "country", "facebook_url", "instagram_url",
            "x_url", "linkedin_url", "youtube_url", "donation_url",
            "volunteer_enabled", "newsletter_enabled",
        ]


class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = ["id", "name", "email", "enquiry_type", "message", "created_at"]
        read_only_fields = ["id", "created_at"]


class VolunteerApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerApplication
        fields = [
            "id", "name", "email", "phone", "country", "city",
            "areas_of_interest", "skills", "availability", "message", "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class NewsletterSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscriber
        fields = ["email", "name"]
        extra_kwargs = {"email": {"validators": []}}

    def create(self, validated_data):
        subscriber, _created = NewsletterSubscriber.objects.update_or_create(
            email=validated_data["email"],
            defaults={
                "name": validated_data.get("name", ""),
                "active": True,
                "source": "website",
            },
        )
        return subscriber


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = [
            "title", "slug", "category", "summary", "year", "file",
            "external_url", "thumbnail", "seo_title", "seo_description",
            "seo_keywords", "published_at",
        ]


class SupportRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportRequest
        fields = [
            "id", "name", "email", "phone", "country", "city",
            "assistance_type", "request_summary", "consent_to_contact", "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def validate(self, attrs):
        if not attrs.get("consent_to_contact"):
            raise serializers.ValidationError(
                {"consent_to_contact": "Consent is required so the Foundation can respond."}
            )
        if not attrs.get("email") and not attrs.get("phone"):
            raise serializers.ValidationError(
                "Provide at least an email address or phone number for follow-up."
            )
        return attrs


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = [
            "title", "slug", "message", "kind", "link_label", "link_url",
            "starts_at", "ends_at", "dismissible", "priority", "published_at",
        ]


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = [
            "question", "slug", "answer", "category", "featured",
            "display_order", "published_at",
        ]


class HomepageSpotlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomepageSpotlight
        fields = [
            "eyebrow", "title", "slug", "summary", "image", "image_alt",
            "link_label", "link_url", "secondary_label", "secondary_url",
            "style", "starts_at", "ends_at", "priority", "display_order",
            "published_at",
        ]


class ImpactStorySerializer(serializers.ModelSerializer):
    public_name = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    quote = serializers.SerializerMethodField()
    quote_attribution = serializers.SerializerMethodField()
    shared_with_consent = serializers.SerializerMethodField()

    class Meta:
        model = ImpactStory
        fields = [
            "title", "slug", "excerpt", "body", "program_area", "public_name",
            "age_group", "location_label", "image", "image_alt", "quote",
            "quote_attribution", "featured", "shared_with_consent",
            "seo_title", "seo_description", "seo_keywords", "published_at",
        ]

    def get_public_name(self, obj):
        if obj.identity_mode == ImpactStory.IdentityMode.ANONYMOUS:
            return "Identity protected"
        return obj.approved_display_name.strip()

    def get_image(self, obj):
        if not obj.photo_consent or not obj.image:
            return None
        request = self.context.get("request")
        url = obj.image.url
        return request.build_absolute_uri(url) if request else url

    def get_quote(self, obj):
        return obj.quote if obj.quote_consent else ""

    def get_quote_attribution(self, obj):
        if not obj.quote_consent or not obj.quote:
            return ""
        if obj.quote_attribution.strip():
            return obj.quote_attribution.strip()
        return self.get_public_name(obj)

    def get_shared_with_consent(self, obj):
        return True


class FounderMediaPhotoSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = FounderMediaPhoto
        fields = [
            "image_url", "alt_text", "caption", "credit", "source_url",
            "is_primary", "display_order",
        ]

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image:
            url = obj.image.url
            return request.build_absolute_uri(url) if request else url
        if obj.external_image_url and obj.reuse_approved:
            return obj.external_image_url
        return None


class FounderMediaItemSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()

    class Meta:
        model = FounderMediaItem
        fields = [
            "title", "slug", "kind", "summary", "body", "event_date",
            "publication_date", "source_name", "source_url", "source_domain",
            "source_reference", "award_title", "awarding_body", "location",
            "featured", "verified_source", "photos", "seo_title",
            "seo_description", "seo_keywords", "published_at",
        ]

    def get_photos(self, obj):
        approved = obj.photos.filter(
            (Q(image__isnull=False) & ~Q(image="")) | Q(reuse_approved=True)
        )
        return FounderMediaPhotoSerializer(
            approved,
            many=True,
            context=self.context,
        ).data


class CampaignUpdateMediaSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = CampaignUpdateMedia
        fields = [
            "media_type", "url", "alt_text", "caption", "credit",
            "source_url", "featured", "display_order",
        ]

    def get_url(self, obj):
        request = self.context.get("request")

        if obj.image:
            url = obj.image.url
            return request.build_absolute_uri(url) if request else url

        if obj.file:
            url = obj.file.url
            return request.build_absolute_uri(url) if request else url

        if obj.external_url and obj.reuse_approved:
            return obj.external_url

        return None


class CampaignUpdateSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField()
    campaign_slug = serializers.CharField(source="campaign.slug", read_only=True, allow_null=True)
    campaign_title = serializers.CharField(source="campaign.title", read_only=True, allow_null=True)
    program_slug = serializers.CharField(source="program.slug", read_only=True, allow_null=True)
    program_title = serializers.CharField(source="program.title", read_only=True, allow_null=True)

    class Meta:
        model = CampaignUpdate
        fields = [
            "title", "slug", "kind", "summary", "body", "occurred_at",
            "location_label", "featured", "video_url",
            "campaign_slug", "campaign_title", "program_slug", "program_title",
            "expenditure_amount", "expenditure_currency", "expenditure_note",
            "expenditure_verified", "output_value", "output_unit", "output_note",
            "verification_note", "source_reference", "source_url", "media",
            "seo_title", "seo_description", "seo_keywords", "published_at",
        ]

    def get_media(self, obj):
        approved = obj.media.filter(
            Q(reuse_approved=True)
            | (Q(image__isnull=False) & ~Q(image=""))
            | (Q(file__isnull=False) & ~Q(file=""))
        )
        return CampaignUpdateMediaSerializer(
            approved,
            many=True,
            context=self.context,
        ).data
