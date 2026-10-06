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
