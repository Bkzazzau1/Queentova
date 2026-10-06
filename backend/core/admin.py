from django.contrib import admin
from django.utils import timezone

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


@admin.register(FounderAchievement)
class FounderAchievementAdmin(PublishWorkflowAdmin):
    list_display = ("title", "year", "status", "source_name", "display_order")
    list_filter = ("status", "year")
    search_fields = ("title", "description", "source_name")
    prepopulated_fields = {"slug": ("title",)}


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


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "enquiry_type", "status", "created_at")
    list_filter = ("status", "enquiry_type", "created_at")
    search_fields = ("name", "email", "message")
    readonly_fields = ("name", "email", "enquiry_type", "message", "created_at", "updated_at")
    ordering = ("-created_at",)


admin.site.site_header = "Queen Tovah Foundation Administration"
admin.site.site_title = "Queen Tovah Admin"
admin.site.index_title = "Content, programs and enquiries"
