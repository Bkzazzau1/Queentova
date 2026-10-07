from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_announcements_and_faq"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomepageSpotlight",
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
                ("eyebrow", models.CharField(blank=True, max_length=100)),
                ("title", models.CharField(max_length=220)),
                ("slug", models.SlugField(max_length=240, unique=True)),
                ("summary", models.TextField()),
                ("image", models.ImageField(blank=True, null=True, upload_to="spotlights/%Y/%m/")),
                ("image_alt", models.CharField(blank=True, max_length=220)),
                ("link_label", models.CharField(default="Explore", max_length=80)),
                ("link_url", models.CharField(max_length=300)),
                ("secondary_label", models.CharField(blank=True, max_length=80)),
                ("secondary_url", models.CharField(blank=True, max_length=300)),
                ("style", models.CharField(choices=[("editorial", "Editorial"), ("impact", "Impact"), ("campaign", "Campaign"), ("opportunity", "Opportunity")], default="editorial", max_length=20)),
                ("starts_at", models.DateTimeField(blank=True, null=True)),
                ("ends_at", models.DateTimeField(blank=True, null=True)),
                ("priority", models.PositiveSmallIntegerField(default=0)),
                ("display_order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["display_order", "-priority", "-published_at", "title"]},
        ),
    ]
