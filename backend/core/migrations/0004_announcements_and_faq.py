from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_support_and_resources"),
    ]

    operations = [
        migrations.CreateModel(
            name="Announcement",
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
                ("title", models.CharField(max_length=180)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                ("message", models.CharField(max_length=360)),
                ("kind", models.CharField(choices=[("info", "Information"), ("event", "Event"), ("opportunity", "Opportunity"), ("appeal", "Appeal"), ("urgent", "Urgent")], default="info", max_length=16)),
                ("link_label", models.CharField(blank=True, max_length=80)),
                ("link_url", models.CharField(blank=True, max_length=300)),
                ("starts_at", models.DateTimeField(blank=True, null=True)),
                ("ends_at", models.DateTimeField(blank=True, null=True)),
                ("dismissible", models.BooleanField(default=True)),
                ("priority", models.PositiveSmallIntegerField(default=0)),
            ],
            options={"ordering": ["-priority", "-published_at", "title"]},
        ),
        migrations.CreateModel(
            name="FAQ",
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
                ("question", models.CharField(max_length=260)),
                ("slug", models.SlugField(max_length=280, unique=True)),
                ("answer", models.TextField()),
                ("category", models.CharField(choices=[("general", "General"), ("support", "Requesting support"), ("giving", "Giving & causes"), ("scholarship", "Scholarships"), ("volunteer", "Volunteering"), ("partnership", "Partnerships")], default="general", max_length=20)),
                ("featured", models.BooleanField(default=False)),
                ("display_order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["display_order", "category", "question"], "verbose_name": "FAQ", "verbose_name_plural": "FAQs"},
        ),
    ]
