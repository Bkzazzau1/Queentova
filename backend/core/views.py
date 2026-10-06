from rest_framework import filters, generics, permissions, viewsets

from .models import (
    ContactSubmission,
    FounderAchievement,
    FounderProfile,
    GalleryItem,
    ImpactMetric,
    Partner,
    Program,
    PublishableModel,
    Scholarship,
    Story,
)
from .serializers import (
    ContactSubmissionSerializer,
    FounderAchievementSerializer,
    FounderProfileSerializer,
    GalleryItemSerializer,
    ImpactMetricSerializer,
    PartnerSerializer,
    ProgramSerializer,
    ScholarshipSerializer,
    StorySerializer,
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
    search_fields = ["title", "description"]
    ordering_fields = ["display_order", "title"]


class ContactSubmissionCreateView(generics.CreateAPIView):
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer
    permission_classes = [permissions.AllowAny]
    throttle_scope = "contact"
