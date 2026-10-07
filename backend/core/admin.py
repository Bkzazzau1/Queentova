from django.contrib import admin, messages
from django.core.exceptions import ValidationError
from django.utils import timezone

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


class PublishWorkflowAdmin(admin.ModelAdmin):
    actions = ["move_to_review", "publish_selected", "return_to_draft"]
    readonly_fields = ("created_at", "updated_at", "published_at")

    @admin.action(description="Move selected items to review")
    def move_to_review(self, request, queryset):
        queryset.update(status="review")

    @admin.action(description="Publish selected items")
    def publish_selected(self, request, queryset):
        queryset.update(status="published", published_at=timezone.now())

    @admin.action(description="Return selected items to draft")
    def return_to_draft(self, request, queryset):
        queryset.update(status="draft")


@admin.register(Program)
class ProgramAdmin(PublishWorkflowAdmin):
    list_display = ("title", "status", "featured", "display_order", "updated_at")
    list_filter = ("status", "featured")
    search_fields = ("title", "summary", "body")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Story)
class StoryAdmin(PublishWorkflowAdmin):
    list_display = ("title", "category", "event_date", "status", "featured", "updated_at")
    list_filter = ("status", "category", "featured")
    search_fields = ("title", "excerpt", "body", "source_name")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "event_date"


@admin.register(GalleryItem)
class GalleryItemAdmin(PublishWorkflowAdmin):
    list_display = ("title", "media_type", "category", "event_date", "status", "display_order")
    list_filter = ("status", "media_type", "category")
    search_fields = ("title", "caption", "alt_text")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(FounderProfile)
class FounderProfileAdmin(PublishWorkflowAdmin):
    list_display = ("primary_name", "public_record_name", "status", "updated_at")
    search_fields = ("primary_name", "public_record_name", "biography")
    prepopulated_fields = {"slug": ("primary_name",)}


class FounderMediaPhotoInline(admin.TabularInline):
    model = FounderMediaPhoto
    extra = 0
    fields = (
        "image", "external_image_url", "alt_text", "caption", "credit",
        "source_url", "reuse_approved", "is_primary", "display_order",
    )


@admin.register(FounderMediaItem)
class FounderMediaItemAdmin(PublishWorkflowAdmin):
    list_display = (
        "title", "kind", "event_date", "source_name",
        "verified_source", "featured", "status",
    )
    list_filter = ("status", "kind", "verified_source", "featured", "source_name")
    search_fields = (
        "title", "summary", "body", "award_title",
        "awarding_body", "source_name", "source_url",
    )
    prepopulated_fields = {"slug": ("title",)}
    inlines = [FounderMediaPhotoInline]


@admin.register(FounderAchievement)
class FounderAchievementAdmin(PublishWorkflowAdmin):
    list_display = ("title", "year", "status", "source_name", "display_order")
    list_filter = ("status", "year")
    search_fields = ("title", "description", "source_name")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(HomepageSpotlight)
class HomepageSpotlightAdmin(PublishWorkflowAdmin):
    list_display = ("title", "style", "priority", "display_order", "starts_at", "ends_at", "status")
    list_filter = ("status", "style")
    search_fields = ("eyebrow", "title", "summary", "link_url")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("display_order", "-priority", "-published_at")


@admin.register(ImpactStory)
class ImpactStoryAdmin(PublishWorkflowAdmin):
    list_display = (
        "title", "program_area", "identity_mode", "consent_status",
        "privacy_reviewed", "featured", "status", "updated_at",
    )
    list_filter = (
        "status", "consent_status", "privacy_reviewed", "story_consent",
        "photo_consent", "quote_consent", "is_minor", "featured", "program_area",
    )
    search_fields = (
        "title", "excerpt", "body", "approved_display_name",
        "location_label", "consent_reference",
    )
    prepopulated_fields = {"slug": ("title",)}
    actions = ["move_to_review", "publish_selected", "return_to_draft", "withdraw_consent"]
    fieldsets = (
        (
            "Public story",
            {
                "fields": (
                    "title", "slug", "excerpt", "body", "program_area",
                    "identity_mode", "approved_display_name", "age_group",
                    "location_label", "image", "image_alt", "quote",
                    "quote_attribution", "featured", "display_order",
                )
            },
        ),
        (
            "Consent & privacy review — internal only",
            {
                "fields": (
                    "consent_status", "story_consent", "photo_consent",
                    "quote_consent", "privacy_reviewed", "is_minor",
                    "guardian_consent", "consent_reference",
                    "consent_recorded_at", "consent_withdrawn_at",
                    "consent_review_note",
                )
            },
        ),
        (
            "Publishing & SEO",
            {
                "fields": (
                    "status", "published_at", "seo_title",
                    "seo_description", "seo_keywords", "og_image",
                    "created_at", "updated_at",
                )
            },
        ),
    )

    @admin.action(description="Publish selected impact stories after consent validation")
    def publish_selected(self, request, queryset):
        published = 0
        rejected = []

        for obj in queryset:
            obj.status = obj.PublicationStatus.PUBLISHED
            if not obj.published_at:
                obj.published_at = timezone.now()
            try:
                obj.full_clean()
            except ValidationError as exc:
                rejected.append(f"{obj.title}: {exc.message_dict}")
                continue
            obj.save()
            published += 1

        if published:
            self.message_user(
                request,
                f"{published} impact stor{'y' if published == 1 else 'ies'} published.",
                level=messages.SUCCESS,
            )
        if rejected:
            self.message_user(
                request,
                "Not published because consent/privacy requirements were incomplete: "
                + " | ".join(rejected),
                level=messages.WARNING,
            )

    @admin.action(description="Withdraw consent and unpublish selected impact stories")
    def withdraw_consent(self, request, queryset):
        count = queryset.update(
            consent_status=ImpactStory.ConsentStatus.WITHDRAWN,
            consent_withdrawn_at=timezone.now(),
            status=ImpactStory.PublicationStatus.DRAFT,
            published_at=None,
        )
        self.message_user(
            request,
            f"Consent withdrawn and {count} stor{'y' if count == 1 else 'ies'} unpublished.",
            level=messages.SUCCESS,
        )


@admin.register(ImpactMetric)
class ImpactMetricAdmin(PublishWorkflowAdmin):
    list_display = ("title", "value", "unit", "period", "status", "display_order")
    list_filter = ("status",)
    search_fields = ("title", "verification_note", "source_reference")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Scholarship)
class ScholarshipAdmin(PublishWorkflowAdmin):
    list_display = ("title", "application_status", "opens_at", "closes_at", "status")
    list_filter = ("status", "application_status")
    search_fields = ("title", "summary", "eligibility")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Partner)
class PartnerAdmin(PublishWorkflowAdmin):
    list_display = ("title", "status", "display_order", "updated_at")
    list_filter = ("status",)
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Campaign)
class CampaignAdmin(PublishWorkflowAdmin):
    list_display = ("title", "status", "featured", "accepting_support", "current_amount", "goal_amount", "currency")
    list_filter = ("status", "featured", "accepting_support", "currency")
    search_fields = ("title", "summary", "body")
    prepopulated_fields = {"slug": ("title",)}


class CampaignUpdateMediaInline(admin.TabularInline):
    model = CampaignUpdateMedia
    extra = 0
    fields = (
        "media_type", "image", "file", "external_url", "alt_text",
        "caption", "credit", "source_url", "reuse_approved",
        "featured", "display_order",
    )


@admin.register(CampaignUpdate)
class CampaignUpdateAdmin(PublishWorkflowAdmin):
    list_display = (
        "title", "kind", "campaign", "program", "occurred_at",
        "expenditure_verified", "featured", "status",
    )
    list_filter = (
        "status", "kind", "featured", "expenditure_verified",
        "campaign", "program",
    )
    search_fields = (
        "title", "summary", "body", "location_label",
        "campaign__title", "program__title", "verification_note",
        "source_reference",
    )
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "occurred_at"
    inlines = [CampaignUpdateMediaInline]
    actions = ["move_to_review", "publish_selected", "return_to_draft"]
    fieldsets = (
        (
            "Activity update",
            {
                "fields": (
                    "title", "slug", "campaign", "program", "kind",
                    "summary", "body", "occurred_at", "location_label",
                    "featured", "video_url", "display_order",
                )
            },
        ),
        (
            "Verified expenditure",
            {
                "fields": (
                    "expenditure_amount", "expenditure_currency",
                    "expenditure_note", "expenditure_verified",
                )
            },
        ),
        (
            "Reported output",
            {
                "fields": (
                    "output_value", "output_unit", "output_note",
                )
            },
        ),
        (
            "Verification & source",
            {
                "fields": (
                    "verification_note", "source_reference", "source_url",
                )
            },
        ),
        (
            "Publishing & SEO",
            {
                "fields": (
                    "status", "published_at", "seo_title",
                    "seo_description", "seo_keywords", "og_image",
                    "created_at", "updated_at",
                )
            },
        ),
    )

    @admin.action(description="Publish selected updates after verification checks")
    def publish_selected(self, request, queryset):
        published = 0
        rejected = []

        for obj in queryset:
            obj.status = obj.PublicationStatus.PUBLISHED
            if not obj.published_at:
                obj.published_at = timezone.now()
            try:
                obj.full_clean()
            except ValidationError as exc:
                rejected.append(f"{obj.title}: {exc.message_dict}")
                continue
            obj.save()
            published += 1

        if published:
            self.message_user(
                request,
                f"{published} activity update{'s' if published != 1 else ''} published.",
                level=messages.SUCCESS,
            )
        if rejected:
            self.message_user(
                request,
                "Not published because verification requirements were incomplete: "
                + " | ".join(rejected),
                level=messages.WARNING,
            )


@admin.register(Event)
class EventAdmin(PublishWorkflowAdmin):
    list_display = ("title", "starts_at", "city", "country", "status", "featured")
    list_filter = ("status", "featured", "country")
    search_fields = ("title", "summary", "body", "venue_name", "city", "country")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "starts_at"


@admin.register(SiteProfile)
class SiteProfileAdmin(PublishWorkflowAdmin):
    list_display = ("display_name", "contact_email", "phone", "status", "updated_at")
    search_fields = ("display_name", "contact_email", "phone", "office_address")


@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "country", "areas_of_interest", "status", "created_at")
    list_filter = ("status", "country", "created_at")
    search_fields = ("name", "email", "phone", "areas_of_interest", "skills", "message")
    readonly_fields = ("name", "email", "phone", "country", "city", "areas_of_interest", "skills", "availability", "message", "created_at", "updated_at")
    ordering = ("-created_at",)


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "active", "source", "consent_at")
    list_filter = ("active", "source", "consent_at")
    search_fields = ("email", "name")
    readonly_fields = ("consent_at", "updated_at")
    ordering = ("-consent_at",)


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "enquiry_type", "status", "created_at")
    list_filter = ("status", "enquiry_type", "created_at")
    search_fields = ("name", "email", "message")
    readonly_fields = ("name", "email", "enquiry_type", "message", "created_at", "updated_at")
    ordering = ("-created_at",)


@admin.register(Announcement)
class AnnouncementAdmin(PublishWorkflowAdmin):
    list_display = ("title", "kind", "priority", "starts_at", "ends_at", "status")
    list_filter = ("status", "kind", "dismissible")
    search_fields = ("title", "message")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(FAQ)
class FAQAdmin(PublishWorkflowAdmin):
    list_display = ("question", "category", "featured", "display_order", "status")
    list_filter = ("status", "category", "featured")
    search_fields = ("question", "answer")
    prepopulated_fields = {"slug": ("question",)}


@admin.register(Resource)
class ResourceAdmin(PublishWorkflowAdmin):
    list_display = ("title", "category", "year", "status", "display_order")
    list_filter = ("status", "category", "year")
    search_fields = ("title", "summary")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(SupportRequest)
class SupportRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "assistance_type", "country", "status", "created_at")
    list_filter = ("status", "assistance_type", "country", "created_at")
    search_fields = ("name", "email", "phone", "country", "city", "request_summary")
    readonly_fields = (
        "name", "email", "phone", "country", "city", "assistance_type",
        "request_summary", "consent_to_contact", "created_at", "updated_at"
    )
    ordering = ("-created_at",)


admin.site.site_header = "Queen Tovah Foundation Administration"
admin.site.site_title = "Queen Tovah Admin"
admin.site.index_title = "Content, programs and engagement"
