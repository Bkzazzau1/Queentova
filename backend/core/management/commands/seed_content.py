from datetime import date

from django.core.management.base import BaseCommand
from django.utils import timezone

from core.models import FounderAchievement, FounderProfile, Program, SiteProfile, Story


class Command(BaseCommand):
    help = "Seed the current Queen Tovah public website content."

    def handle(self, *args, **options):
        published = {
            "status": "published",
            "published_at": timezone.now(),
        }

        SiteProfile.objects.update_or_create(
            slug="primary",
            defaults={
                "display_name": "Queen Tovah Cares Foundation International",
                "short_description": (
                    "Compassion with dignity. Opportunity with purpose. "
                    "A global outlook rooted in service to people and communities."
                ),
                "volunteer_enabled": True,
                "newsletter_enabled": True,
                **published,
            },
        )

        programs = [
            (
                "Humanitarian Support",
                "humanitarian-support",
                "Practical care for vulnerable people and families, with dignity at the centre of every intervention.",
                "heart",
                1,
            ),
            (
                "Education & Scholarships",
                "education-scholarships",
                "Opening doors to learning for indigent students and people whose potential should not be limited by circumstance.",
                "book",
                2,
            ),
            (
                "Youth Empowerment & Sports",
                "youth-sports",
                "Using sport, mentorship and shared experiences to bring young people together and strengthen communities.",
                "spark",
                3,
            ),
            (
                "Community Development",
                "community-development",
                "Supporting human capital and community-led progress through initiatives designed around real local needs.",
                "people",
                4,
            ),
        ]

        for title, slug, summary, icon, order in programs:
            Program.objects.update_or_create(
                slug=slug,
                defaults={
                    "title": title,
                    "summary": summary,
                    "icon": icon,
                    "display_order": order,
                    "featured": True,
                    **published,
                },
            )

        FounderProfile.objects.update_or_create(
            slug="jessie-ifeoma-udoka-menuba",
            defaults={
                "title": "Founder",
                "primary_name": "Princess Dr. Jessie Joseph",
                "public_record_name": "Princess Dr. Jessie Ifeoma Udoka-Menuba",
                "maiden_name": "Oliobi",
                "headline": "Humanitarian, philanthropist and Founder/CEO in public reporting",
                "biography": (
                    "Public reporting identifies Princess Dr. Jessie Ifeoma Udoka-Menuba "
                    "(née Oliobi) as Founder/CEO of Queen-Tovah Cares Foundation International. "
                    "The Foundation-supplied primary founder name remains Princess Dr. Jessie Joseph "
                    "until the Foundation confirms how the names should be presented together."
                ),
                "motto": "It is good to be good.",
                "faith_line": "God is my strength.",
                "seo_title": "Princess Dr. Jessie Ifeoma Udoka-Menuba | Queen Tovah",
                "seo_description": "Founder public profile for Queen Tovah Cares Foundation International.",
                "seo_keywords": "Jessie Ifeoma Udoka-Menuba, Jessie Joseph, Queen Tovah Cares Foundation International",
                **published,
            },
        )

        achievements = [
            (2024, "Mother General Award", "mother-general-award-2024", "Recognition by Ugosimba Women Association, Amawbia.", "Anambra State Government", "https://anambrastate.gov.ng/ugosimba-women-amawbia-honor-princess-dr-jessie-ifeoma-udoka-menuba-with-prestigious-mother-general-award/"),
            (2025, "Ahaejiejemba1 & Woman of the Decade", "ahaejiejemba1-woman-of-the-decade-2025", "Recognition by Umuigbo United Assembly Worldwide for leadership, service and support for underprivileged people.", "Anambra State Government", "https://anambrastate.gov.ng/founder-queen-tovah-cares-foundation-intl-receives-more-accolades-as-umuigbo-united-assembly-honors-her-with-prestigious-awards/"),
            (2025, "NUJ Anambra Philanthropist of the 21st Century", "nuj-philanthropist-2025", "Publicly listed recognition by NUJ Anambra.", "Anambra State Government", "https://anambrastate.gov.ng/tag/awards/"),
            (2026, "Ada Di Iche 1 Worldwide", "ada-di-iche-1-worldwide-2026", "Recognition for humanitarian work within the community and beyond.", "Anambra State Government", "https://anambrastate.gov.ng/tag/a-shining-light-princess-jessie-udoka-menuba-honoured-with-ada-di-iche-1-worldwide-award/"),
        ]

        for order, (year, title, slug, description, source_name, source_url) in enumerate(achievements, start=1):
            FounderAchievement.objects.update_or_create(
                slug=slug,
                defaults={
                    "year": year,
                    "title": title,
                    "description": description,
                    "source_name": source_name,
                    "source_url": source_url,
                    "display_order": order,
                    **published,
                },
            )

        Story.objects.update_or_create(
            slug="amawbia-august-league-2025",
            defaults={
                "title": "Supporting youth unity through the Amawbia August League",
                "excerpt": "The Foundation supported the 2025 Amawbia August League football tournament to encourage youth engagement and community unity.",
                "category": "youth-sports",
                "event_date": date(2025, 8, 1),
                "featured": True,
                "source_name": "Independent Newspaper Nigeria",
                "source_url": "https://independent.ng/princess-udoka-menuba-kicks-poverty-out-with-amawbia-football-showdown/",
                **published,
            },
        )

        self.stdout.write(self.style.SUCCESS("Queen Tovah seed content is ready."))
