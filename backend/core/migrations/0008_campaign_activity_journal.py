from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_founder_media_archive"),
    ]

    operations = [
        migrations.CreateModel(
            name="CampaignUpdate",
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
                ("kind", models.CharField(choices=[("field", "Field update"), ("milestone", "Milestone"), ("delivery", "Delivery / distribution"), ("funding", "Funding update"), ("impact", "Impact update"), ("announcement", "Announcement")], default="field", max_length=20)),
                ("summary", models.TextField()),
                ("body", models.TextField(blank=True)),
                ("occurred_at", models.DateTimeField(db_index=True)),
                ("location_label", models.CharField(blank=True, max_length=180)),
                ("featured", models.BooleanField(default=False)),
                ("video_url", models.URLField(blank=True)),
                ("expenditure_amount", models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
                ("expenditure_currency", models.CharField(default="USD", max_length=8)),
                ("expenditure_note", models.CharField(blank=True, max_length=260)),
                ("expenditure_verified", models.BooleanField(default=False)),
                ("output_value", models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
                ("output_unit", models.CharField(blank=True, max_length=120)),
                ("output_note", models.CharField(blank=True, max_length=260)),
                ("verification_note", models.TextField(blank=True)),
                ("source_reference", models.CharField(blank=True, max_length=260)),
                ("source_url", models.URLField(blank=True)),
                ("display_order", models.PositiveIntegerField(default=0)),
                ("campaign", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name="activity_updates", to="core.campaign")),
                ("program", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="activity_updates", to="core.program")),
            ],
            options={"ordering": ["display_order", "-occurred_at", "-published_at", "title"], "verbose_name": "Campaign / program update", "verbose_name_plural": "Campaign & program activity journal"},
        ),
        migrations.CreateModel(
            name="CampaignUpdateMedia",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("media_type", models.CharField(choices=[("photo", "Photo"), ("document", "Document")], default="photo", max_length=12)),
                ("image", models.ImageField(blank=True, null=True, upload_to="campaign-updates/%Y/%m/")),
                ("file", models.FileField(blank=True, null=True, upload_to="campaign-updates/documents/%Y/%m/")),
                ("external_url", models.URLField(blank=True, max_length=900)),
                ("alt_text", models.CharField(blank=True, max_length=240)),
                ("caption", models.TextField(blank=True)),
                ("credit", models.CharField(blank=True, max_length=220)),
                ("source_url", models.URLField(blank=True, max_length=600)),
                ("reuse_approved", models.BooleanField(default=False, help_text="Required for externally sourced media before public display.")),
                ("featured", models.BooleanField(default=False)),
                ("display_order", models.PositiveIntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("update", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="media", to="core.campaignupdate")),
            ],
            options={"ordering": ["display_order", "-featured", "id"], "verbose_name": "Activity update media", "verbose_name_plural": "Activity update media"},
        ),
    ]
