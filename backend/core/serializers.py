from rest_framework import serializers

from .models import (
    Campaign,
    ContactSubmission,
    Event,
    FounderAchievement,
    FounderProfile,
    GalleryItem,
    ImpactMetric,
    NewsletterSubscriber,
    Partner,
    Program,
    Scholarship,
    SiteProfile,
    Story,
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
