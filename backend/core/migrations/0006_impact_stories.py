from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_homepage_spotlights"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImpactStory",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("status", models.CharField(choices=[("draft", "Draft"), ("review", "In review"), ("published", "Published")], db_index=True, default="draft", max_length=12)),
                ("published_at", models.DateTimeField(blank=True, db_index=True, null=True)),
                ("seo_title", models.CharField(blank=True, max_length=180)),
                ("seo_description", models.CharField(blank=True, max_length=320)),
                ("seo_keywords", models.CharField(blank=True, max_length=500)),
                ("og_image", models.ImageField(blank=True, null=True, upload_to="seo/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=220)),
                ("slug", models.SlugField(max_length=240, unique=True)),
                ("excerpt", models.TextField()),
                ("body", models.TextField()),
                ("program_area", models.CharField(choices=[("humanitarian", "Humanitarian support"), ("education", "Education & scholarships"), ("youth", "Youth & sports"), ("community", "Community development"), ("livelihood", "Livelihood & empowerment"), ("other", "Other")], default="humanitarian", max_length=20)),
                ("identity_mode", models.CharField(choices=[("anonymous", "Identity protected"), ("first-name", "Approved first name"), ("approved-name", "Approved public name")], default="anonymous", max_length=20)),
                ("approved_display_name", models.CharField(blank=True, max_length=120)),
                ("age_group", models.CharField(choices=[("not-stated", "Not stated"), ("child", "Child"), ("youth", "Youth"), ("adult", "Adult"), ("older-adult", "Older adult")], default="not-stated", max_length=20)),
                ("location_label", models.CharField(blank=True, help_text="Use only a broad approved location, such as city/state/country.", max_length=160)),
                ("image", models.ImageField(blank=True, null=True, upload_to="impact-stories/%Y/%m/")),
                ("image_alt", models.CharField(blank=True, max_length=220)),
                ("quote", models.TextField(blank=True)),
                ("quote_attribution", models.CharField(blank=True, max_length=120)),
                ("featured", models.BooleanField(default=False)),
                ("display_order", models.PositiveIntegerField(default=0)),
                ("consent_status", models.CharField(choices=[("pending", "Pending"), ("active", "Active"), ("withdrawn", "Withdrawn")], db_index=True, default="pending", max_length=12)),
                ("story_consent", models.BooleanField(default=False)),
                ("photo_consent", models.BooleanField(default=False)),
                ("quote_consent", models.BooleanField(default=False)),
                ("privacy_reviewed", models.BooleanField(default=False)),
                ("is_minor", models.BooleanField(default=False)),
                ("guardian_consent", models.BooleanField(default=False)),
                ("consent_reference", models.CharField(blank=True, help_text="Internal reference only. Never exposed through the public API.", max_length=160)),
                ("consent_recorded_at", models.DateTimeField(blank=True, null=True)),
                ("consent_withdrawn_at", models.DateTimeField(blank=True, null=True)),
                ("consent_review_note", models.TextField(blank=True, help_text="Internal privacy/consent review notes. Never exposed publicly.")),
            ],
            options={"ordering": ["display_order", "-published_at", "title"], "verbose_name": "Impact story", "verbose_name_plural": "Impact stories"},
        ),
    ]
