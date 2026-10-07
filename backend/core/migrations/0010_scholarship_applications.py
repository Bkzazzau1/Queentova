from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.core.validators
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_verified_partner_profiles"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="scholarship",
            name="application_instructions",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="scholarship",
            name="required_documents",
            field=models.TextField(
                blank=True,
                help_text="Public description of the documents applicants should prepare.",
            ),
        ),
        migrations.AddField(
            model_name="scholarship",
            name="internal_applications_enabled",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="scholarship",
            name="max_awards",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="scholarship",
            name="public_results_released",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="scholarship",
            name="public_results_note",
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name="ScholarshipApplication",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("reference_code", models.CharField(db_index=True, default=core.models.scholarship_application_reference, editable=False, max_length=20, unique=True)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(blank=True, max_length=40)),
                ("country", models.CharField(max_length=120)),
                ("city", models.CharField(blank=True, max_length=120)),
                ("institution", models.CharField(blank=True, max_length=220)),
                ("course_of_study", models.CharField(blank=True, max_length=220)),
                ("current_level", models.CharField(blank=True, max_length=120)),
                ("academic_summary", models.TextField(blank=True)),
                ("financial_need_statement", models.TextField()),
                ("personal_statement", models.TextField()),
                ("consent_to_processing", models.BooleanField(default=False)),
                ("declaration_true", models.BooleanField(default=False)),
                ("review_status", models.CharField(choices=[("submitted", "Submitted"), ("screening", "Screening"), ("eligible", "Eligible"), ("shortlisted", "Shortlisted"), ("approved", "Approved"), ("rejected", "Rejected"), ("withdrawn", "Withdrawn")], db_index=True, default="submitted", max_length=16)),
                ("eligibility_score", models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ("merit_score", models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ("need_score", models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ("overall_score", models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ("eligibility_note", models.TextField(blank=True)),
                ("reviewer_notes", models.TextField(blank=True)),
                ("reviewed_at", models.DateTimeField(blank=True, null=True)),
                ("submitted_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("assigned_reviewer", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="assigned_scholarship_applications", to=settings.AUTH_USER_MODEL)),
                ("reviewed_by", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="reviewed_scholarship_applications", to=settings.AUTH_USER_MODEL)),
                ("scholarship", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="applications", to="core.scholarship")),
            ],
            options={"ordering": ["-submitted_at"]},
        ),
        migrations.CreateModel(
            name="ScholarshipApplicationDocument",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("document_type", models.CharField(choices=[("academic", "Academic record / transcript"), ("identity", "Identity document"), ("admission", "Admission / enrolment evidence"), ("recommendation", "Recommendation"), ("supporting", "Other supporting document")], default="supporting", max_length=20)),
                ("file", models.FileField(upload_to=core.models.scholarship_document_path)),
                ("original_name", models.CharField(max_length=260)),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                ("application", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="documents", to="core.scholarshipapplication")),
            ],
            options={"ordering": ["document_type", "uploaded_at"]},
        ),
        migrations.AddConstraint(
            model_name="scholarshipapplication",
            constraint=models.UniqueConstraint(fields=("scholarship", "email"), name="unique_scholarship_application_email"),
        ),
    ]
