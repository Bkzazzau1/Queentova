from rest_framework import serializers

from .models import (
    ContactSubmission,
    FounderAchievement,
    FounderProfile,
    GalleryItem,
    ImpactMetric,
    Partner,
    Program,
    Scholarship,
    Story,
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


class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = ["id", "name", "email", "enquiry_type", "message", "created_at"]
        read_only_fields = ["id", "created_at"]
