from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    ContactSubmissionCreateView,
    FounderAchievementViewSet,
    FounderProfileViewSet,
    GalleryItemViewSet,
    ImpactMetricViewSet,
    PartnerViewSet,
    ProgramViewSet,
    ScholarshipViewSet,
    StoryViewSet,
)

router = DefaultRouter()
router.register("programs", ProgramViewSet, basename="program")
router.register("stories", StoryViewSet, basename="story")
router.register("gallery", GalleryItemViewSet, basename="gallery")
router.register("founders", FounderProfileViewSet, basename="founder")
router.register("founder-achievements", FounderAchievementViewSet, basename="founder-achievement")
router.register("impact", ImpactMetricViewSet, basename="impact")
router.register("scholarships", ScholarshipViewSet, basename="scholarship")
router.register("partners", PartnerViewSet, basename="partner")

urlpatterns = [
    path("", include(router.urls)),
    path("contact/", ContactSubmissionCreateView.as_view(), name="contact-create"),
]
