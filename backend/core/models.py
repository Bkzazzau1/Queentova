from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class PublishableModel(models.Model):
    class PublicationStatus(models.TextChoices):
        DRAFT = "draft", "Draft"
        REVIEW = "review", "In review"
        PUBLISHED = "published", "Published"

    status = models.CharField(
        max_length=12,
        choices=PublicationStatus.choices,
        default=PublicationStatus.DRAFT,
        db_index=True,
    )
    published_at = models.DateTimeField(blank=True, null=True, db_index=True)
    seo_title = models.CharField(max_length=180, blank=True)
    seo_description = models.CharField(max_length=320, blank=True)
    seo_keywords = models.CharField(max_length=500, blank=True)
    og_image = models.ImageField(upload_to="seo/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.status == self.PublicationStatus.PUBLISHED and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)


class Program(PublishableModel):
    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True)
    summary = models.TextField()
    body = models.TextField(blank=True)
    icon = models.CharField(max_length=40, blank=True)
    featured = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "title"]

    def __str__(self):
        return self.title


class Story(PublishableModel):
    class Category(models.TextChoices):
        HUMANITARIAN = "humanitarian", "Humanitarian"
        EDUCATION = "education", "Education"
        YOUTH = "youth-sports", "Youth & Sports"
        COMMUNITY = "community", "Community Development"
        FOUNDATION = "foundation", "Foundation"
        PARTNERSHIP = "partnership", "Partnership"

    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=240, unique=True)
    excerpt = models.TextField()
    body = models.TextField(blank=True)
    category = models.CharField(max_length=24, choices=Category.choices, default=Category.FOUNDATION)
    event_date = models.DateField(blank=True, null=True)
    hero_image = models.ImageField(upload_to="stories/%Y/%m/", blank=True, null=True)
    hero_alt = models.CharField(max_length=220, blank=True)
    featured = models.BooleanField(default=False)
    source_name = models.CharField(max_length=180, blank=True)
    source_url = models.URLField(blank=True)

    class Meta:
        ordering = ["-event_date", "-published_at", "-created_at"]
        verbose_name_plural = "Stories"

    def __str__(self):
        return self.title


class GalleryItem(PublishableModel):
    class MediaType(models.TextChoices):
        IMAGE = "image", "Image"
        VIDEO = "video", "Video"

    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True)
    media_type = models.CharField(max_length=12, choices=MediaType.choices, default=MediaType.IMAGE)
    image = models.ImageField(upload_to="gallery/%Y/%m/", blank=True, null=True)
    video_url = models.URLField(blank=True)
    alt_text = models.CharField(max_length=220, blank=True)
    caption = models.TextField(blank=True)
    category = models.CharField(max_length=120, blank=True)
    event_date = models.DateField(blank=True, null=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "-event_date", "-created_at"]

    def __str__(self):
        return self.title


class FounderProfile(PublishableModel):
    title = models.CharField(max_length=180, default="Founder")
    slug = models.SlugField(max_length=180, unique=True)
    primary_name = models.CharField(max_length=220)
    public_record_name = models.CharField(max_length=260, blank=True)
    maiden_name = models.CharField(max_length=180, blank=True)
    headline = models.CharField(max_length=260, blank=True)
    biography = models.TextField()
    motto = models.CharField(max_length=180, blank=True)
    faith_line = models.CharField(max_length=180, blank=True)
    portrait = models.ImageField(upload_to="founder/", blank=True, null=True)
    portrait_alt = models.CharField(max_length=220, blank=True)

    class Meta:
        ordering = ["primary_name"]

    def __str__(self):
        return self.primary_name


class FounderAchievement(PublishableModel):
    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=240, unique=True)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField()
    source_name = models.CharField(max_length=180, blank=True)
    source_url = models.URLField(blank=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-year", "display_order", "title"]

    def __str__(self):
        return self.title


class ImpactStory(PublishableModel):
    class ConsentStatus(models.TextChoices):
        PENDING = "pending", "Pending"
        ACTIVE = "active", "Active"
        WITHDRAWN = "withdrawn", "Withdrawn"

    class IdentityMode(models.TextChoices):
        ANONYMOUS = "anonymous", "Identity protected"
        FIRST_NAME = "first-name", "Approved first name"
        APPROVED_NAME = "approved-name", "Approved public name"

    class AgeGroup(models.TextChoices):
        NOT_STATED = "not-stated", "Not stated"
        CHILD = "child", "Child"
        YOUTH = "youth", "Youth"
        ADULT = "adult", "Adult"
        OLDER_ADULT = "older-adult", "Older adult"

    class ProgramArea(models.TextChoices):
        HUMANITARIAN = "humanitarian", "Humanitarian support"
        EDUCATION = "education", "Education & scholarships"
        YOUTH = "youth", "Youth & sports"
        COMMUNITY = "community", "Community development"
        LIVELIHOOD = "livelihood", "Livelihood & empowerment"
        OTHER = "other", "Other"

    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=240, unique=True)
    excerpt = models.TextField()
    body = models.TextField()
    program_area = models.CharField(
        max_length=20,
        choices=ProgramArea.choices,
        default=ProgramArea.HUMANITARIAN,
    )
    identity_mode = models.CharField(
        max_length=20,
        choices=IdentityMode.choices,
        default=IdentityMode.ANONYMOUS,
    )
    approved_display_name = models.CharField(max_length=120, blank=True)
    age_group = models.CharField(
        max_length=20,
        choices=AgeGroup.choices,
        default=AgeGroup.NOT_STATED,
    )
    location_label = models.CharField(
        max_length=160,
        blank=True,
        help_text="Use only a broad approved location, such as city/state/country.",
    )
    image = models.ImageField(upload_to="impact-stories/%Y/%m/", blank=True, null=True)
    image_alt = models.CharField(max_length=220, blank=True)
    quote = models.TextField(blank=True)
    quote_attribution = models.CharField(max_length=120, blank=True)
    featured = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)

    consent_status = models.CharField(
        max_length=12,
        choices=ConsentStatus.choices,
        default=ConsentStatus.PENDING,
        db_index=True,
    )
    story_consent = models.BooleanField(default=False)
    photo_consent = models.BooleanField(default=False)
    quote_consent = models.BooleanField(default=False)
    privacy_reviewed = models.BooleanField(default=False)
    is_minor = models.BooleanField(default=False)
    guardian_consent = models.BooleanField(default=False)
    consent_reference = models.CharField(
        max_length=160,
        blank=True,
        help_text="Internal reference only. Never exposed through the public API.",
    )
    consent_recorded_at = models.DateTimeField(blank=True, null=True)
    consent_withdrawn_at = models.DateTimeField(blank=True, null=True)
    consent_review_note = models.TextField(
        blank=True,
        help_text="Internal privacy/consent review notes. Never exposed publicly.",
    )

    class Meta:
        ordering = ["display_order", "-published_at", "title"]
        verbose_name = "Impact story"
        verbose_name_plural = "Impact stories"

    def __str__(self):
        return self.title

    def clean(self):
        errors = {}

        if self.identity_mode != self.IdentityMode.ANONYMOUS and not self.approved_display_name.strip():
            errors["approved_display_name"] = "An approved public display name is required for this identity mode."

        if self.image and not self.photo_consent:
            errors["photo_consent"] = "Photo consent is required before an image can be attached to this story."

        if self.quote and not self.quote_consent:
            errors["quote_consent"] = "Quote consent is required before a beneficiary quote can be published."

        if self.status == self.PublicationStatus.PUBLISHED:
            if self.consent_status != self.ConsentStatus.ACTIVE:
                errors["consent_status"] = "Active consent is required before publication."
            if not self.story_consent:
                errors["story_consent"] = "Story publication consent is required."
            if not self.privacy_reviewed:
                errors["privacy_reviewed"] = "A privacy review is required before publication."
            if not self.consent_recorded_at:
                errors["consent_recorded_at"] = "Record when consent was obtained before publication."
            if not self.consent_reference.strip():
                errors["consent_reference"] = "An internal consent reference is required before publication."
            if self.is_minor and not self.guardian_consent:
                errors["guardian_consent"] = "Guardian consent is required for a minor."

        if errors:
            raise ValidationError(errors)


class ImpactMetric(PublishableModel):
    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True)
    value = models.CharField(max_length=80)
    unit = models.CharField(max_length=80, blank=True)
    period = models.CharField(max_length=120, blank=True)
    verification_note = models.TextField()
    source_reference = models.CharField(max_length=240, blank=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "title"]

    def __str__(self):
        return f"{self.title}: {self.value}"


class Scholarship(PublishableModel):
    class ApplicationStatus(models.TextChoices):
        UPCOMING = "upcoming", "Upcoming"
        OPEN = "open", "Open"
        CLOSED = "closed", "Closed"

    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=240, unique=True)
    summary = models.TextField()
    eligibility = models.TextField(blank=True)
    application_status = models.CharField(
        max_length=12,
        choices=ApplicationStatus.choices,
        default=ApplicationStatus.UPCOMING,
    )
    opens_at = models.DateTimeField(blank=True, null=True)
    closes_at = models.DateTimeField(blank=True, null=True)
    application_url = models.URLField(blank=True)

    class Meta:
        ordering = ["-opens_at", "-created_at"]

    def __str__(self):
        return self.title


class Partner(PublishableModel):
    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to="partners/", blank=True, null=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "title"]

    def __str__(self):
        return self.title


class Campaign(PublishableModel):
    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=240, unique=True)
    summary = models.TextField()
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to="campaigns/%Y/%m/", blank=True, null=True)
    image_alt = models.CharField(max_length=220, blank=True)
    goal_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    current_amount = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    currency = models.CharField(max_length=8, default="USD")
    starts_at = models.DateTimeField(blank=True, null=True)
    ends_at = models.DateTimeField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    accepting_support = models.BooleanField(default=False)
    cta_label = models.CharField(max_length=80, default="Support this cause")
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "-published_at", "title"]

    def __str__(self):
        return self.title


class Event(PublishableModel):
    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=240, unique=True)
    summary = models.TextField()
    body = models.TextField(blank=True)
    starts_at = models.DateTimeField(db_index=True)
    ends_at = models.DateTimeField(blank=True, null=True)
    venue_name = models.CharField(max_length=180, blank=True)
    address = models.CharField(max_length=260, blank=True)
    city = models.CharField(max_length=120, blank=True)
    country = models.CharField(max_length=120, blank=True)
    online_url = models.URLField(blank=True)
    registration_url = models.URLField(blank=True)
    image = models.ImageField(upload_to="events/%Y/%m/", blank=True, null=True)
    image_alt = models.CharField(max_length=220, blank=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["starts_at", "title"]

    def __str__(self):
        return self.title


class SiteProfile(PublishableModel):
    slug = models.SlugField(max_length=80, unique=True, default="primary")
    display_name = models.CharField(max_length=220, default="Queen Tovah Cares Foundation International")
    short_description = models.TextField(blank=True)
    contact_email = models.EmailField(blank=True)
    phone = models.CharField(max_length=60, blank=True)
    whatsapp = models.CharField(max_length=60, blank=True)
    office_address = models.TextField(blank=True)
    country = models.CharField(max_length=120, blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    x_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    donation_url = models.URLField(blank=True)
    volunteer_enabled = models.BooleanField(default=True)
    newsletter_enabled = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Site profile"
        verbose_name_plural = "Site profile"

    def __str__(self):
        return self.display_name


class HomepageSpotlight(PublishableModel):
    class Style(models.TextChoices):
        EDITORIAL = "editorial", "Editorial"
        IMPACT = "impact", "Impact"
        CAMPAIGN = "campaign", "Campaign"
        OPPORTUNITY = "opportunity", "Opportunity"

    eyebrow = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=240, unique=True)
    summary = models.TextField()
    image = models.ImageField(upload_to="spotlights/%Y/%m/", blank=True, null=True)
    image_alt = models.CharField(max_length=220, blank=True)
    link_label = models.CharField(max_length=80, default="Explore")
    link_url = models.CharField(max_length=300)
    secondary_label = models.CharField(max_length=80, blank=True)
    secondary_url = models.CharField(max_length=300, blank=True)
    style = models.CharField(max_length=20, choices=Style.choices, default=Style.EDITORIAL)
    starts_at = models.DateTimeField(blank=True, null=True)
    ends_at = models.DateTimeField(blank=True, null=True)
    priority = models.PositiveSmallIntegerField(default=0)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "-priority", "-published_at", "title"]

    def __str__(self):
        return self.title


class Announcement(PublishableModel):
    class Kind(models.TextChoices):
        INFO = "info", "Information"
        EVENT = "event", "Event"
        OPPORTUNITY = "opportunity", "Opportunity"
        APPEAL = "appeal", "Appeal"
        URGENT = "urgent", "Urgent"

    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True)
    message = models.CharField(max_length=360)
    kind = models.CharField(max_length=16, choices=Kind.choices, default=Kind.INFO)
    link_label = models.CharField(max_length=80, blank=True)
    link_url = models.CharField(max_length=300, blank=True)
    starts_at = models.DateTimeField(blank=True, null=True)
    ends_at = models.DateTimeField(blank=True, null=True)
    dismissible = models.BooleanField(default=True)
    priority = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["-priority", "-published_at", "title"]

    def __str__(self):
        return self.title


class FAQ(PublishableModel):
    class Category(models.TextChoices):
        GENERAL = "general", "General"
        SUPPORT = "support", "Requesting support"
        GIVING = "giving", "Giving & causes"
        SCHOLARSHIP = "scholarship", "Scholarships"
        VOLUNTEER = "volunteer", "Volunteering"
        PARTNERSHIP = "partnership", "Partnerships"

    question = models.CharField(max_length=260)
    slug = models.SlugField(max_length=280, unique=True)
    answer = models.TextField()
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.GENERAL)
    featured = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "category", "question"]
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question


class VolunteerApplication(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "New"
        REVIEWING = "reviewing", "Reviewing"
        ACCEPTED = "accepted", "Accepted"
        DECLINED = "declined", "Declined"

    name = models.CharField(max_length=180)
    email = models.EmailField()
    phone = models.CharField(max_length=60, blank=True)
    country = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=120, blank=True)
    areas_of_interest = models.CharField(max_length=260)
    skills = models.TextField(blank=True)
    availability = models.CharField(max_length=180, blank=True)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.NEW, db_index=True)
    internal_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — volunteer"


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=160, blank=True)
    active = models.BooleanField(default=True, db_index=True)
    source = models.CharField(max_length=80, default="website")
    consent_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-consent_at"]

    def __str__(self):
        return self.email


class Resource(PublishableModel):
    class Category(models.TextChoices):
        ANNUAL_REPORT = "annual-report", "Annual report"
        IMPACT_REPORT = "impact-report", "Impact report"
        POLICY = "policy", "Policy"
        PRESS_KIT = "press-kit", "Press kit"
        PUBLICATION = "publication", "Publication"

    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=240, unique=True)
    category = models.CharField(max_length=24, choices=Category.choices, default=Category.PUBLICATION)
    summary = models.TextField(blank=True)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    file = models.FileField(upload_to="resources/%Y/", blank=True, null=True)
    external_url = models.URLField(blank=True)
    thumbnail = models.ImageField(upload_to="resources/thumbnails/", blank=True, null=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "-year", "title"]

    def __str__(self):
        return self.title


class SupportRequest(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "New"
        REVIEWING = "reviewing", "Reviewing"
        FOLLOW_UP = "follow-up", "Follow up"
        CLOSED = "closed", "Closed"

    class AssistanceType(models.TextChoices):
        GENERAL = "general", "General humanitarian support"
        EDUCATION = "education", "Education"
        FAMILY = "family", "Family support"
        SHELTER = "shelter", "Shelter / housing"
        LIVELIHOOD = "livelihood", "Livelihood / empowerment"
        OTHER = "other", "Other"

    name = models.CharField(max_length=180)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=60, blank=True)
    country = models.CharField(max_length=120)
    city = models.CharField(max_length=120, blank=True)
    assistance_type = models.CharField(max_length=20, choices=AssistanceType.choices, default=AssistanceType.GENERAL)
    request_summary = models.TextField()
    consent_to_contact = models.BooleanField(default=False)
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.NEW, db_index=True)
    internal_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.get_assistance_type_display()}"


class ContactSubmission(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "New"
        IN_PROGRESS = "in-progress", "In progress"
        CLOSED = "closed", "Closed"

    class EnquiryType(models.TextChoices):
        GENERAL = "general", "General enquiry"
        PARTNERSHIP = "partnership", "Partnership"
        HUMANITARIAN = "humanitarian", "Humanitarian support"
        SCHOLARSHIP = "scholarship", "Scholarship"
        MEDIA = "media", "Media"

    name = models.CharField(max_length=160)
    email = models.EmailField()
    enquiry_type = models.CharField(max_length=20, choices=EnquiryType.choices, default=EnquiryType.GENERAL)
    message = models.TextField()
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.NEW, db_index=True)
    internal_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.get_enquiry_type_display()}"
