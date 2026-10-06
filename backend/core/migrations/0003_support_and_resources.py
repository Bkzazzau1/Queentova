from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_premium_engagement"),
    ]

    operations = [
        migrations.CreateModel(
            name="Resource",
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
                ("category", models.CharField(choices=[("annual-report", "Annual report"), ("impact-report", "Impact report"), ("policy", "Policy"), ("press-kit", "Press kit"), ("publication", "Publication")], default="publication", max_length=24)),
                ("summary", models.TextField(blank=True)),
                ("year", models.PositiveSmallIntegerField(blank=True, null=True)),
                ("file", models.FileField(blank=True, null=True, upload_to="resources/%Y/")),
                ("external_url", models.URLField(blank=True)),
                ("thumbnail", models.ImageField(blank=True, null=True, upload_to="resources/thumbnails/")),
                ("display_order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["display_order", "-year", "title"]},
        ),
        migrations.CreateModel(
            name="SupportRequest",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=180)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("phone", models.CharField(blank=True, max_length=60)),
                ("country", models.CharField(max_length=120)),
                ("city", models.CharField(blank=True, max_length=120)),
                ("assistance_type", models.CharField(choices=[("general", "General humanitarian support"), ("education", "Education"), ("family", "Family support"), ("shelter", "Shelter / housing"), ("livelihood", "Livelihood / empowerment"), ("other", "Other")], default="general", max_length=20)),
                ("request_summary", models.TextField()),
                ("consent_to_contact", models.BooleanField(default=False)),
                ("status", models.CharField(choices=[("new", "New"), ("reviewing", "Reviewing"), ("follow-up", "Follow up"), ("closed", "Closed")], db_index=True, default="new", max_length=16)),
                ("internal_notes", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
