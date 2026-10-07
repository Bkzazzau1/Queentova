from django.db.models import Q
from django.utils import timezone
from rest_framework import filters, generics, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

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
    NewsletterSubscriber,
    Partner,
    PartnerCollaboration,
    Program,
    PublishableModel,
    Resource,
    Scholarship,
    SiteProfile,
    Story,
    SupportRequest,
    VolunteerApplication,
)
from .serializers import (
    AnnouncementSerializer,
    CampaignSerializer,
    CampaignUpdateSerializer,
    ContactSubmissionSerializer,
    EventSerializer,
    FAQSerializer,
    FounderAchievementSerializer,
    FounderMediaItemSerializer,
    FounderProfileSerializer,
    GalleryItemSerializer,
    HomepageSpotlightSerializer,
    ImpactMetricSerializer,
    ImpactStorySerializer,
    NewsletterSubscriberSerializer,
    PartnerSerializer,
    PartnerCollaborationSerializer,
    ProgramSerializer,
    ResourceSerializer,
    ScholarshipSerializer,
    SiteProfileSerializer,
    StorySerializer,
    SupportRequestSerializer,
    VolunteerApplicationSerializer,
)


class PublishedReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    lookup_field = "slug"
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    def get_queryset(self):
        return super().get_queryset().filter(status=PublishableModel.PublicationStatus.PUBLISHED)


class ProgramViewSet(PublishedReadOnlyViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    search_fields = ["title", "summary", "body"]
    ordering_fields = ["display_order", "published_at", "title"]


class StoryViewSet(PublishedReadOnlyViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    search_fields = ["title", "excerpt", "body", "category"]
    ordering_fields = ["event_date", "published_at", "title"]


class GalleryItemViewSet(PublishedReadOnlyViewSet):
    queryset = GalleryItem.objects.all()
    serializer_class = GalleryItemSerializer
    search_fields = ["title", "caption", "category"]
    ordering_fields = ["display_order", "event_date", "published_at"]


class FounderProfileViewSet(PublishedReadOnlyViewSet):
    queryset = FounderProfile.objects.all()
    serializer_class = FounderProfileSerializer
    search_fields = ["primary_name", "public_record_name", "biography"]


class FounderAchievementViewSet(PublishedReadOnlyViewSet):
    queryset = FounderAchievement.objects.all()
    serializer_class = FounderAchievementSerializer
    search_fields = ["title", "description", "source_name"]
    ordering_fields = ["year", "display_order", "published_at"]


class ImpactMetricViewSet(PublishedReadOnlyViewSet):
    queryset = ImpactMetric.objects.all()
    serializer_class = ImpactMetricSerializer
    search_fields = ["title", "verification_note", "source_reference"]
    ordering_fields = ["display_order", "published_at", "title"]


class ScholarshipViewSet(PublishedReadOnlyViewSet):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer
    search_fields = ["title", "summary", "eligibility"]
    ordering_fields = ["opens_at", "closes_at", "published_at"]


class PartnerViewSet(PublishedReadOnlyViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    search_fields = ["title", "tagline", "description", "body", "country", "city"]
    ordering_fields = ["display_order", "relationship_since", "title"]

    def get_queryset(self):
        return super().get_queryset().filter(verified_relationship=True)


class PartnerCollaborationViewSet(PublishedReadOnlyViewSet):
    queryset = PartnerCollaboration.objects.select_related("partner", "program", "campaign").all()
    serializer_class = PartnerCollaborationSerializer
    search_fields = [
        "title", "summary", "body", "partner__title",
        "program__title", "campaign__title", "location_label",
    ]
    ordering_fields = ["display_order", "starts_at", "published_at", "title"]

    def get_queryset(self):
        queryset = super().get_queryset().filter(verified_record=True)
        partner_slug = self.request.query_params.get("partner", "").strip()
        if partner_slug:
            queryset = queryset.filter(partner__slug=partner_slug)
        return queryset


class CampaignViewSet(PublishedReadOnlyViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    search_fields = ["title", "summary", "body"]
    ordering_fields = ["display_order", "ends_at", "published_at", "title"]


class EventViewSet(PublishedReadOnlyViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    search_fields = ["title", "summary", "body", "venue_name", "city", "country"]
    ordering_fields = ["starts_at", "published_at", "title"]


class SiteProfileViewSet(PublishedReadOnlyViewSet):
    queryset = SiteProfile.objects.all()
    serializer_class = SiteProfileSerializer
    search_fields = ["display_name", "short_description"]


class ContactSubmissionCreateView(generics.CreateAPIView):
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer
    permission_classes = [permissions.AllowAny]
    throttle_scope = "contact"


class VolunteerApplicationCreateView(generics.CreateAPIView):
    queryset = VolunteerApplication.objects.all()
    serializer_class = VolunteerApplicationSerializer
    permission_classes = [permissions.AllowAny]
    throttle_scope = "volunteer"


class NewsletterSubscribeView(generics.CreateAPIView):
    queryset = NewsletterSubscriber.objects.all()
    serializer_class = NewsletterSubscriberSerializer
    permission_classes = [permissions.AllowAny]
    throttle_scope = "newsletter"

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"status": "subscribed", "email": response.data.get("email")},
            status=status.HTTP_200_OK,
        )


class SearchView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        query = request.query_params.get("q", "").strip()
        if len(query) < 2:
            return Response({"query": query, "results": []})

        published = PublishableModel.PublicationStatus.PUBLISHED
        results = []

        for item in Program.objects.filter(status=published).filter(
            Q(title__icontains=query) | Q(summary__icontains=query) | Q(body__icontains=query)
        )[:8]:
            results.append({
                "type": "program",
                "title": item.title,
                "excerpt": item.summary,
                "url": f"/programs/{item.slug}",
            })

        for item in Story.objects.filter(status=published).filter(
            Q(title__icontains=query) | Q(excerpt__icontains=query) | Q(body__icontains=query)
        )[:8]:
            results.append({
                "type": "story",
                "title": item.title,
                "excerpt": item.excerpt,
                "url": f"/news/{item.slug}",
            })

        for item in Campaign.objects.filter(status=published).filter(
            Q(title__icontains=query) | Q(summary__icontains=query) | Q(body__icontains=query)
        )[:8]:
            results.append({
                "type": "campaign",
                "title": item.title,
                "excerpt": item.summary,
                "url": f"/causes/{item.slug}",
            })

        for item in Partner.objects.filter(
            status=published,
            verified_relationship=True,
        ).filter(
            Q(title__icontains=query) | Q(tagline__icontains=query) |
            Q(description__icontains=query) | Q(body__icontains=query)
        )[:8]:
            results.append({
                "type": "partner",
                "title": item.title,
                "excerpt": item.tagline or item.description,
                "url": f"/partners/{item.slug}",
            })

        for item in CampaignUpdate.objects.filter(status=published).filter(
            Q(title__icontains=query) | Q(summary__icontains=query) |
            Q(body__icontains=query) | Q(location_label__icontains=query)
        )[:8]:
            results.append({
                "type": "activity-update",
                "title": item.title,
                "excerpt": item.summary,
                "url": f"/activity/{item.slug}",
            })

        for item in Event.objects.filter(status=published).filter(
            Q(title__icontains=query) | Q(summary__icontains=query) | Q(body__icontains=query)
        )[:8]:
            results.append({
                "type": "event",
                "title": item.title,
                "excerpt": item.summary,
                "url": f"/events/{item.slug}",
            })

        for item in FAQ.objects.filter(status=published).filter(
            Q(question__icontains=query) | Q(answer__icontains=query) | Q(category__icontains=query)
        )[:8]:
            results.append({
                "type": "faq",
                "title": item.question,
                "excerpt": item.answer[:220],
                "url": f"/faq#{item.slug}",
            })

        for item in FounderMediaItem.objects.filter(status=published).filter(
            Q(title__icontains=query) | Q(summary__icontains=query) |
            Q(award_title__icontains=query) | Q(awarding_body__icontains=query)
        )[:8]:
            results.append({
                "type": "founder-media",
                "title": item.title,
                "excerpt": item.summary,
                "url": f"/founder/media/{item.slug}",
            })

        for item in ImpactStory.objects.filter(
            status=published,
            consent_status=ImpactStory.ConsentStatus.ACTIVE,
            story_consent=True,
            privacy_reviewed=True,
        ).filter(Q(is_minor=False) | Q(guardian_consent=True)).filter(
            Q(title__icontains=query) | Q(excerpt__icontains=query) | Q(body__icontains=query)
        )[:8]:
            results.append({
                "type": "impact-story",
                "title": item.title,
                "excerpt": item.excerpt,
                "url": f"/impact-stories/{item.slug}",
            })

        for item in Resource.objects.filter(status=published).filter(
            Q(title__icontains=query) | Q(summary__icontains=query) | Q(category__icontains=query)
        )[:8]:
            results.append({
                "type": "resource",
                "title": item.title,
                "excerpt": item.summary or item.get_category_display(),
                "url": f"/resources/{item.slug}",
            })

        return Response({"query": query, "results": results[:24]})


class AnnouncementViewSet(PublishedReadOnlyViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    search_fields = ["title", "message", "kind"]
    ordering_fields = ["priority", "published_at", "title"]

    def get_queryset(self):
        now = timezone.now()
        return (
            super()
            .get_queryset()
            .filter(Q(starts_at__isnull=True) | Q(starts_at__lte=now))
            .filter(Q(ends_at__isnull=True) | Q(ends_at__gte=now))
        )


class FAQViewSet(PublishedReadOnlyViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    search_fields = ["question", "answer", "category"]
    ordering_fields = ["display_order", "category", "question"]


class ResourceViewSet(PublishedReadOnlyViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    search_fields = ["title", "summary", "category"]
    ordering_fields = ["display_order", "year", "published_at", "title"]


class SupportRequestCreateView(generics.CreateAPIView):
    queryset = SupportRequest.objects.all()
    serializer_class = SupportRequestSerializer
    permission_classes = [permissions.AllowAny]
    throttle_scope = "support_request"


class HomepageSpotlightViewSet(PublishedReadOnlyViewSet):
    queryset = HomepageSpotlight.objects.all()
    serializer_class = HomepageSpotlightSerializer
    search_fields = ["eyebrow", "title", "summary", "style"]
    ordering_fields = ["display_order", "priority", "published_at", "title"]

    def get_queryset(self):
        now = timezone.now()
        return (
            super()
            .get_queryset()
            .filter(Q(starts_at__isnull=True) | Q(starts_at__lte=now))
            .filter(Q(ends_at__isnull=True) | Q(ends_at__gte=now))
        )


class ImpactStoryViewSet(PublishedReadOnlyViewSet):
    queryset = ImpactStory.objects.all()
    serializer_class = ImpactStorySerializer
    search_fields = ["title", "excerpt", "body", "program_area", "location_label"]
    ordering_fields = ["display_order", "published_at", "title"]

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(
                consent_status=ImpactStory.ConsentStatus.ACTIVE,
                story_consent=True,
                privacy_reviewed=True,
            )
            .filter(Q(is_minor=False) | Q(guardian_consent=True))
        )


class FounderMediaItemViewSet(PublishedReadOnlyViewSet):
    queryset = FounderMediaItem.objects.prefetch_related("photos").all()
    serializer_class = FounderMediaItemSerializer
    search_fields = [
        "title", "summary", "body", "award_title", "awarding_body",
        "source_name", "location",
    ]
    ordering_fields = [
        "display_order", "event_date", "publication_date",
        "published_at", "title",
    ]


class CampaignUpdateViewSet(PublishedReadOnlyViewSet):
    queryset = CampaignUpdate.objects.select_related("campaign", "program").prefetch_related("media").all()
    serializer_class = CampaignUpdateSerializer
    search_fields = [
        "title", "summary", "body", "kind", "location_label",
        "campaign__title", "program__title", "verification_note",
    ]
    ordering_fields = ["display_order", "occurred_at", "published_at", "title"]

    def get_queryset(self):
        queryset = super().get_queryset()
        campaign_slug = self.request.query_params.get("campaign", "").strip()
        program_slug = self.request.query_params.get("program", "").strip()
        kind = self.request.query_params.get("kind", "").strip()

        if campaign_slug:
            queryset = queryset.filter(campaign__slug=campaign_slug)
        if program_slug:
            queryset = queryset.filter(program__slug=program_slug)
        partner_slug = self.request.query_params.get("partner", "").strip()

        if kind:
            queryset = queryset.filter(kind=kind)
        if partner_slug:
            queryset = queryset.filter(partners__slug=partner_slug).distinct()

        return queryset
