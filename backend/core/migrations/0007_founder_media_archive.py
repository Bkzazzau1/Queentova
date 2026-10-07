from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_impact_stories"),
    ]

    operations = [
        migrations.CreateModel(
            name="FounderMediaItem",
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
                ("title", models.CharField(max_length=240)),
                ("slug", models.SlugField(max_length=260, unique=True)),
                ("kind", models.CharField(choices=[("award", "Award & recognition"), ("achievement", "Achievement"), ("news", "News coverage"), ("interview", "Interview"), ("publication", "Publication"), ("community", "Community appearance")], default="news", max_length=20)),
                ("summary", models.TextField()),
                ("body", models.TextField(blank=True)),
                ("event_date", models.DateField(blank=True, db_index=True, null=True)),
                ("publication_date", models.DateField(blank=True, db_index=True, null=True)),
                ("source_name", models.CharField(max_length=180)),
                ("source_url", models.URLField(max_length=600)),
                ("source_domain", models.CharField(blank=True, max_length=180)),
                ("source_reference", models.CharField(blank=True, max_length=220)),
                ("award_title", models.CharField(blank=True, max_length=220)),
                ("awarding_body", models.CharField(blank=True, max_length=220)),
                ("location", models.CharField(blank=True, max_length=180)),
                ("featured", models.BooleanField(default=False)),
                ("verified_source", models.BooleanField(default=False)),
                ("display_order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["display_order", "-event_date", "-publication_date", "-published_at", "title"], "verbose_name": "Founder media item", "verbose_name_plural": "Founder media & recognition"},
        ),
        migrations.CreateModel(
            name="FounderMediaPhoto",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("image", models.ImageField(blank=True, null=True, upload_to="founder-media/%Y/%m/")),
                ("external_image_url", models.URLField(blank=True, max_length=900)),
                ("alt_text", models.CharField(max_length=240)),
                ("caption", models.TextField(blank=True)),
                ("credit", models.CharField(blank=True, max_length=220)),
                ("source_url", models.URLField(blank=True, max_length=600)),
                ("reuse_approved", models.BooleanField(default=False, help_text="Must be enabled before an external/source image can appear publicly.")),
                ("is_primary", models.BooleanField(default=False)),
                ("display_order", models.PositiveIntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("media_item", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="photos", to="core.foundermediaitem")),
            ],
            options={"ordering": ["display_order", "-is_primary", "id"], "verbose_name": "Founder media photo", "verbose_name_plural": "Founder media photos"},
        ),
    ]
