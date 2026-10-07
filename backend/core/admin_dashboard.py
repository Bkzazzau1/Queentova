from datetime import timedelta
from decimal import Decimal

from django.db.models import Count, Q
from django.urls import reverse
from django.utils import timezone

from .models import (
    Announcement,
    Campaign,
    CampaignUpdate,
    ContactSubmission,
    Event,
    FAQ,
    FounderAchievement,
    FounderMediaItem,
    FounderProfile,
    GalleryItem,
    HomepageSpotlight,
    ImpactMetric,
    ImpactStory,
    Partner,
    PartnerCollaboration,
    Program,
    PublishableModel,
    Resource,
    Scholarship,
    ScholarshipApplication,
    SiteProfile,
    Story,
    SupportRequest,
    VolunteerApplication,
)


CONTENT_MODELS = (
    Program,
    Story,
    GalleryItem,
    FounderProfile,
    FounderAchievement,
    FounderMediaItem,
    ImpactMetric,
    ImpactStory,
    Scholarship,
    Partner,
    PartnerCollaboration,
    Campaign,
    CampaignUpdate,
    Event,
    HomepageSpotlight,
    Announcement,
    FAQ,
    Resource,
    SiteProfile,
)


def admin_url(model, action="changelist"):
    return reverse(
        f"admin:{model._meta.app_label}_{model._meta.model_name}_{action}"
    )


def filtered_admin_url(model, **filters):
    base = admin_url(model)
    query = "&".join(f"{key}={value}" for key, value in filters.items())
    return f"{base}?{query}" if query else base


def _content_overview():
    counts = {"draft": 0, "review": 0, "published": 0}
    review_items = []

    for model in CONTENT_MODELS:
        status_rows = model.objects.values("status").annotate(total=Count("id"))
        for row in status_rows:
            if row["status"] in counts:
                counts[row["status"]] += row["total"]

        for obj in model.objects.filter(
            status=PublishableModel.PublicationStatus.REVIEW
        ).order_by("-updated_at")[:3]:
            title = (
                getattr(obj, "title", None)
                or getattr(obj, "question", None)
                or getattr(obj, "display_name", None)
                or str(obj)
            )
            review_items.append(
                {
                    "title": title,
                    "model": model._meta.verbose_name.title(),
                    "updated_at": obj.updated_at,
                    "url": reverse(
                        f"admin:{model._meta.app_label}_{model._meta.model_name}_change",
                        args=[obj.pk],
                    ),
                }
            )

    review_items.sort(key=lambda item: item["updated_at"], reverse=True)
    return counts, review_items[:8]


def _campaign_progress(campaign):
    if not campaign.goal_amount or campaign.goal_amount <= 0:
        return None
    progress = (campaign.current_amount / campaign.goal_amount) * Decimal("100")
    return min(round(progress, 1), Decimal("100.0"))


def build_admin_dashboard_context(request):
    now = timezone.now()
    week_ago = now - timedelta(days=7)

    content_counts, content_review_items = _content_overview()

    active_scholarship_statuses = [
        ScholarshipApplication.ReviewStatus.SUBMITTED,
        ScholarshipApplication.ReviewStatus.SCREENING,
        ScholarshipApplication.ReviewStatus.ELIGIBLE,
        ScholarshipApplication.ReviewStatus.SHORTLISTED,
    ]
    scholarship_queue = (
        ScholarshipApplication.objects.select_related(
            "scholarship", "assigned_reviewer"
        )
        .filter(review_status__in=active_scholarship_statuses)
        .order_by("-submitted_at")[:6]
    )

    support_queue = SupportRequest.objects.exclude(
        status=SupportRequest.Status.CLOSED
    ).order_by("-created_at")[:6]

    enquiry_queue = ContactSubmission.objects.exclude(
        status=ContactSubmission.Status.CLOSED
    ).order_by("-created_at")[:6]

    volunteer_queue = VolunteerApplication.objects.filter(
        status__in=[
            VolunteerApplication.Status.NEW,
            VolunteerApplication.Status.REVIEWING,
        ]
    ).order_by("-created_at")[:6]

    active_campaigns = (
        Campaign.objects.filter(
            status=PublishableModel.PublicationStatus.PUBLISHED,
            accepting_support=True,
        )
        .filter(Q(ends_at__isnull=True) | Q(ends_at__gte=now))
        .order_by("display_order", "-published_at")[:5]
    )

    campaign_cards = [
        {
            "title": campaign.title,
            "currency": campaign.currency,
            "current_amount": campaign.current_amount,
            "goal_amount": campaign.goal_amount,
            "progress": _campaign_progress(campaign),
            "url": reverse(
                "admin:core_campaign_change",
                args=[campaign.pk],
            ),
        }
        for campaign in active_campaigns
    ]

    upcoming_events = list(
        Event.objects.filter(
            status=PublishableModel.PublicationStatus.PUBLISHED,
            starts_at__gte=now,
        ).order_by("starts_at")[:5]
    )

    open_scholarships = list(
        Scholarship.objects.filter(
            status=PublishableModel.PublicationStatus.PUBLISHED,
            application_status=Scholarship.ApplicationStatus.OPEN,
        )
        .filter(Q(opens_at__isnull=True) | Q(opens_at__lte=now))
        .filter(Q(closes_at__isnull=True) | Q(closes_at__gte=now))
        .order_by("closes_at", "-opens_at")[:5]
    )

    metrics = [
        {
            "label": "Scholarship pipeline",
            "value": ScholarshipApplication.objects.filter(
                review_status__in=active_scholarship_statuses
            ).count(),
            "hint": "Submitted through shortlisted",
            "url": filtered_admin_url(
                ScholarshipApplication,
                review_status__in=",".join(active_scholarship_statuses),
            ),
            "tone": "gold",
        },
        {
            "label": "New support requests",
            "value": SupportRequest.objects.filter(
                status=SupportRequest.Status.NEW
            ).count(),
            "hint": "Private humanitarian cases",
            "url": filtered_admin_url(
                SupportRequest,
                status__exact=SupportRequest.Status.NEW,
            ),
            "tone": "plum",
        },
        {
            "label": "New enquiries",
            "value": ContactSubmission.objects.filter(
                status=ContactSubmission.Status.NEW
            ).count(),
            "hint": "General, media & partnership",
            "url": filtered_admin_url(
                ContactSubmission,
                status__exact=ContactSubmission.Status.NEW,
            ),
            "tone": "neutral",
        },
        {
            "label": "Volunteer queue",
            "value": VolunteerApplication.objects.filter(
                status__in=[
                    VolunteerApplication.Status.NEW,
                    VolunteerApplication.Status.REVIEWING,
                ]
            ).count(),
            "hint": "New or under review",
            "url": admin_url(VolunteerApplication),
            "tone": "green",
        },
        {
            "label": "Content in review",
            "value": content_counts["review"],
            "hint": "Editorial approval queue",
            "url": "#content-review",
            "tone": "purple",
        },
        {
            "label": "Recent field updates",
            "value": CampaignUpdate.objects.filter(
                created_at__gte=week_ago
            ).count(),
            "hint": "Created in the last 7 days",
            "url": admin_url(CampaignUpdate),
            "tone": "blue",
        },
    ]

    quick_actions = [
        {
            "label": "New activity update",
            "description": "Add a reviewed field or campaign update.",
            "url": admin_url(CampaignUpdate, "add"),
        },
        {
            "label": "New scholarship",
            "description": "Configure an opportunity and application channel.",
            "url": admin_url(Scholarship, "add"),
        },
        {
            "label": "New story",
            "description": "Draft Foundation news or a program story.",
            "url": admin_url(Story, "add"),
        },
        {
            "label": "New campaign",
            "description": "Create a public cause or fundraising campaign.",
            "url": admin_url(Campaign, "add"),
        },
        {
            "label": "New announcement",
            "description": "Schedule a site-wide notice or opportunity.",
            "url": admin_url(Announcement, "add"),
        },
        {
            "label": "New partner",
            "description": "Prepare a partner profile for verification.",
            "url": admin_url(Partner, "add"),
        },
    ]

    return {
        "dashboard_generated_at": now,
        "dashboard_metrics": metrics,
        "dashboard_content_counts": content_counts,
        "dashboard_content_review_items": content_review_items,
        "dashboard_scholarship_queue": scholarship_queue,
        "dashboard_support_queue": support_queue,
        "dashboard_enquiry_queue": enquiry_queue,
        "dashboard_volunteer_queue": volunteer_queue,
        "dashboard_campaigns": campaign_cards,
        "dashboard_upcoming_events": upcoming_events,
        "dashboard_open_scholarships": open_scholarships,
        "dashboard_quick_actions": quick_actions,
        "dashboard_urls": {
            "scholarships": admin_url(ScholarshipApplication),
            "support": admin_url(SupportRequest),
            "enquiries": admin_url(ContactSubmission),
            "volunteers": admin_url(VolunteerApplication),
            "content_activity": admin_url(CampaignUpdate),
            "events": admin_url(Event),
            "scholarship_programs": admin_url(Scholarship),
        },
        "dashboard_assigned_to_me": ScholarshipApplication.objects.filter(
            assigned_reviewer=request.user,
            review_status__in=active_scholarship_statuses,
        ).count(),
    }
