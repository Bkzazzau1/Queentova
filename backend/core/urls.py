from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AnnouncementViewSet,
    CampaignViewSet,
    ContactSubmissionCreateView,
    EventViewSet,
    FAQViewSet,
    FounderAchievementViewSet,
    FounderMediaItemViewSet,
    FounderProfileViewSet,
    GalleryItemViewSet,
    HomepageSpotlightViewSet,
    ImpactMetricViewSet,
    ImpactStoryViewSet,
    NewsletterSubscribeView,
    PartnerViewSet,
    ProgramViewSet,
    ResourceViewSet,
    ScholarshipViewSet,
    SearchView,
    SiteProfileViewSet,
    StoryViewSet,
    SupportRequestCreateView,
    VolunteerApplicationCreateView,
)

router = DefaultRouter()
router.register("announcements", AnnouncementViewSet, basename="announcement")
router.register("faqs", FAQViewSet, basename="faq")
router.register("programs", ProgramViewSet, basename="program")
router.register("stories", StoryViewSet, basename="story")
router.register("gallery", GalleryItemViewSet, basename="gallery")
router.register("homepage-spotlights", HomepageSpotlightViewSet, basename="homepage-spotlight")
router.register("founders", FounderProfileViewSet, basename="founder")
router.register("founder-achievements", FounderAchievementViewSet, basename="founder-achievement")
router.register("founder-media", FounderMediaItemViewSet, basename="founder-media")
router.register("impact", ImpactMetricViewSet, basename="impact")
router.register("impact-stories", ImpactStoryViewSet, basename="impact-story")
router.register("scholarships", ScholarshipViewSet, basename="scholarship")
router.register("partners", PartnerViewSet, basename="partner")
router.register("resources", ResourceViewSet, basename="resource")
router.register("campaigns", CampaignViewSet, basename="campaign")
router.register("events", EventViewSet, basename="event")
router.register("site-profile", SiteProfileViewSet, basename="site-profile")

urlpatterns = [
    path("", include(router.urls)),
    path("contact/", ContactSubmissionCreateView.as_view(), name="contact-create"),
    path("volunteer/", VolunteerApplicationCreateView.as_view(), name="volunteer-create"),
    path("newsletter/", NewsletterSubscribeView.as_view(), name="newsletter-subscribe"),
    path("search/", SearchView.as_view(), name="site-search"),
    path("request-support/", SupportRequestCreateView.as_view(), name="support-request-create"),
]
