from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_campaign_activity_journal"),
    ]

    operations = [
        migrations.AddField(
            model_name="partner",
            name="partner_type",
            field=models.CharField(
                choices=[
                    ("corporate", "Corporate"),
                    ("nonprofit", "Nonprofit / NGO"),
                    ("government", "Government / public institution"),
                    ("education", "Education / research"),
                    ("media", "Media"),
                    ("community", "Community organisation"),
                    ("professional", "Professional body"),
                    ("other", "Other"),
                ],
                default="other",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="partner",
            name="relationship_status",
            field=models.CharField(
                choices=[
                    ("strategic", "Strategic partner"),
                    ("active", "Active partner"),
                    ("project", "Project partner"),
                    ("supporter", "Supporter / sponsor"),
                    ("completed", "Completed collaboration"),
                ],
                default="active",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="partner",
            name="tagline",
            field=models.CharField(blank=True, max_length=240),
        ),
        migrations.AddField(
            model_name="partner",
            name="body",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="partner",
            name="hero_image",
            field=models.ImageField(blank=True, null=True, upload_to="partners/hero/%Y/%m/"),
        ),
        migrations.AddField(
            model_name="partner",
            name="hero_alt",
            field=models.CharField(blank=True, max_length=220),
        ),
        migrations.AddField(
            model_name="partner",
            name="city",
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name="partner",
            name="country",
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name="partner",
            name="relationship_since",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="partner",
            name="relationship_ended",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="partner",
            name="verified_relationship",
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AddField(
            model_name="partner",
            name="verification_note",
            field=models.TextField(
                blank=True,
                help_text="Internal/public-safe note explaining how the relationship was verified.",
            ),
        ),
        migrations.AddField(
            model_name="partner",
            name="reference_url",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="partner",
            name="featured",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="partner",
            name="logo",
            field=models.ImageField(blank=True, null=True, upload_to="partners/logos/"),
        ),
        migrations.CreateModel(
            name="PartnerCollaboration",
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
                ("summary", models.TextField()),
                ("body", models.TextField(blank=True)),
                ("collaboration_status", models.CharField(choices=[("planned", "Planned"), ("active", "Active"), ("completed", "Completed"), ("ongoing", "Ongoing")], default="active", max_length=16)),
                ("starts_at", models.DateField(blank=True, null=True)),
                ("ends_at", models.DateField(blank=True, null=True)),
                ("location_label", models.CharField(blank=True, max_length=180)),
                ("featured", models.BooleanField(default=False)),
                ("verified_record", models.BooleanField(db_index=True, default=False)),
                ("verification_note", models.TextField(blank=True)),
                ("source_url", models.URLField(blank=True)),
                ("display_order", models.PositiveIntegerField(default=0)),
                ("campaign", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="partner_collaborations", to="core.campaign")),
                ("partner", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="collaborations", to="core.partner")),
                ("program", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="partner_collaborations", to="core.program")),
            ],
            options={"ordering": ["display_order", "-starts_at", "-published_at", "title"]},
        ),
        migrations.AddField(
            model_name="campaignupdate",
            name="partners",
            field=models.ManyToManyField(blank=True, related_name="activity_updates", to="core.partner"),
        ),
    ]
