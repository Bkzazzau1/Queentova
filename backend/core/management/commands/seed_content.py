from datetime import date, datetime

from django.core.management.base import BaseCommand
from django.utils import timezone

from core.models import CampaignUpdate, FAQ, FounderAchievement, FounderMediaItem, FounderProfile, HomepageSpotlight, Program, SiteProfile, Story


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






        founder_media = [
            {
                "slug": "professorship-award-crown-matron",
                "title": "Professorship Award and Crown Matron recognition",
                "kind": "award",
                "summary": (
                    "Anambra State Government reporting says Princess Dr. Jessie Ifeoma Udoka-Menuba "
                    "received a Professorship Award from Crown Prince Ministerial College of Bishops "
                    "and was installed as Crown Matron in recognition of humanitarian and ministerial service."
                ),
                "event_date": date(2024, 3, 30),
                "publication_date": date(2024, 4, 3),
                "source_name": "Anambra State Government",
                "source_url": "https://anambrastate.gov.ng/founder-queen-tovah-cares-foundation-intl-recieves-professorship-award-installed-patroness-of-crown-princess-college-of-bishops/",
                "source_domain": "anambrastate.gov.ng",
                "award_title": "Professorship Award / Crown Matron",
                "awarding_body": "Crown Prince Ministerial College of Bishops Inc. Nigeria",
                "location": "Amawbia, Anambra State",
                "featured": False,
                "display_order": 1,
            },
            {
                "slug": "mother-general-award-ugosimba-women",
                "title": "Ugosimba Women honour her with Mother General Award",
                "kind": "award",
                "summary": (
                    "Ugosimba Women Association, Amawbia recognised her leadership and humanitarian "
                    "service with the Mother General Award."
                ),
                "event_date": date(2024, 12, 30),
                "publication_date": date(2024, 12, 30),
                "source_name": "Anambra State Government",
                "source_url": "https://anambrastate.gov.ng/ugosimba-women-amawbia-honor-princess-dr-jessie-ifeoma-udoka-menuba-with-prestigious-mother-general-award/",
                "source_domain": "anambrastate.gov.ng",
                "award_title": "Mother General Award",
                "awarding_body": "Ugosimba Women Association, Amawbia",
                "location": "Amawbia, Anambra State",
                "featured": True,
                "display_order": 2,
            },
            {
                "slug": "woman-of-the-decade-ahaejiejemba1",
                "title": "Woman of the Decade and Ahaejiejemba1 honours",
                "kind": "award",
                "summary": (
                    "Umuigbo United Assembly Worldwide conferred the Woman of the Decade and "
                    "Ahaejiejemba1 honours, citing leadership, service and support for vulnerable people."
                ),
                "event_date": date(2025, 1, 11),
                "publication_date": date(2025, 1, 11),
                "source_name": "Anambra State Government",
                "source_url": "https://anambrastate.gov.ng/founder-queen-tovah-cares-foundation-intl-receives-more-accolades-as-umuigbo-united-assembly-honors-her-with-prestigious-awards/",
                "source_domain": "anambrastate.gov.ng",
                "award_title": "Woman of the Decade / Ahaejiejemba1",
                "awarding_body": "Umuigbo United Assembly Worldwide",
                "location": "Enugu, Enugu State",
                "featured": True,
                "display_order": 3,
            },
            {
                "slug": "nuj-philanthropist-of-the-21st-century",
                "title": "NUJ Anambra Philanthropist of the 21st Century",
                "kind": "award",
                "summary": (
                    "NUJ Anambra materials publicly identify Princess Dr. Jessie Ifeoma Udoka-Menuba "
                    "as the 2025 Philanthropist of the 21st Century award recipient."
                ),
                "event_date": None,
                "publication_date": date(2025, 8, 1),
                "source_name": "NUJ Anambra / The WatchDog Magazine",
                "source_url": "https://www.odogwublog.com/wp-content/uploads/2025/10/The-WatchDog-Magazine-Of-The-NUJ-Anambra-2025-1.pdf",
                "source_domain": "odogwublog.com",
                "award_title": "Philanthropist of the 21st Century",
                "awarding_body": "Nigeria Union of Journalists, Anambra State Council",
                "location": "Anambra State",
                "featured": True,
                "display_order": 4,
            },
            {
                "slug": "amawbia-august-league-youth-empowerment",
                "title": "National media covers Amawbia August League youth empowerment",
                "kind": "news",
                "summary": (
                    "Independent Newspaper Nigeria reported on her sponsorship of the 2025 Amawbia "
                    "August League football tournament as part of youth empowerment and community development."
                ),
                "event_date": date(2025, 8, 15),
                "publication_date": date(2025, 8, 19),
                "source_name": "Independent Newspaper Nigeria",
                "source_url": "https://independent.ng/princess-udoka-menuba-kicks-poverty-out-with-amawbia-football-showdown/",
                "source_domain": "independent.ng",
                "award_title": "",
                "awarding_body": "",
                "location": "Amawbia, Anambra State",
                "featured": False,
                "display_order": 5,
            },
            {
                "slug": "new-yam-and-birthday-public-profile",
                "title": "Public profile highlighted during 2025 New Yam celebration",
                "kind": "news",
                "summary": (
                    "Anambra State Government coverage of the 2025 New Yam celebration highlighted "
                    "her philanthropy, community-development work and widely reported recognitions."
                ),
                "event_date": date(2025, 9, 29),
                "publication_date": date(2025, 10, 2),
                "source_name": "Anambra State Government",
                "source_url": "https://anambrastate.gov.ng/rtd-air-commodore-udoka-menuba-celebrates-new-yam-festival-cum-wifes-birthday-in-grand-style/",
                "source_domain": "anambrastate.gov.ng",
                "award_title": "",
                "awarding_body": "",
                "location": "Amawbia, Anambra State",
                "featured": False,
                "display_order": 6,
            },
            {
                "slug": "ada-di-iche-1-worldwide",
                "title": "Ada Di Iche 1 Worldwide Award",
                "kind": "award",
                "summary": (
                    "Umuada Nimo married to Amawbia conferred the Ada Di Iche 1 Worldwide Award "
                    "for humanitarian work within the community and beyond."
                ),
                "event_date": date(2026, 4, 12),
                "publication_date": date(2026, 4, 12),
                "source_name": "Anambra State Government",
                "source_url": "https://anambrastate.gov.ng/tag/a-shining-light-princess-jessie-udoka-menuba-honoured-with-ada-di-iche-1-worldwide-award/",
                "source_domain": "anambrastate.gov.ng",
                "award_title": "Ada Di Iche 1 Worldwide",
                "awarding_body": "Umuada Nimo married to Amawbia",
                "location": "Amawbia, Anambra State",
                "featured": True,
                "display_order": 7,
            },
        ]

        for item in founder_media:
            FounderMediaItem.objects.update_or_create(
                slug=item["slug"],
                defaults={
                    **item,
                    "verified_source": True,
                    **published,
                },
            )


        youth_program = Program.objects.get(slug="youth-sports")
        CampaignUpdate.objects.update_or_create(
            slug="amawbia-august-league-2025-field-update",
            defaults={
                "title": "Amawbia August League youth engagement update",
                "program": youth_program,
                "kind": "milestone",
                "summary": (
                    "Independent Newspaper Nigeria reported the Foundation's sponsorship of the "
                    "2025 Amawbia August League football tournament as part of youth empowerment "
                    "and community-development efforts."
                ),
                "body": (
                    "The activity journal records this as a source-linked program milestone. "
                    "No expenditure or beneficiary figure is published here because the current "
                    "public source does not provide a verified figure suitable for this website."
                ),
                "occurred_at": timezone.make_aware(datetime(2025, 8, 15, 12, 0)),
                "location_label": "Amawbia, Anambra State",
                "featured": True,
                "verification_note": (
                    "Public activity record linked to Independent Newspaper Nigeria coverage."
                ),
                "source_reference": "Independent Newspaper Nigeria — Amawbia football showdown",
                "source_url": "https://independent.ng/princess-udoka-menuba-kicks-poverty-out-with-amawbia-football-showdown/",
                "display_order": 1,
                **published,
            },
        )

        HomepageSpotlight.objects.update_or_create(
            slug="amawbia-youth-sports-spotlight",
            defaults={
                "eyebrow": "Youth & community",
                "title": "Sport as a meeting point for youth, unity and community.",
                "summary": (
                    "The Foundation's support for the 2025 Amawbia August League reflects a wider "
                    "commitment to constructive youth engagement and stronger community life."
                ),
                "link_label": "Read the story",
                "link_url": "/news/amawbia-august-league-2025",
                "secondary_label": "Explore youth programs",
                "secondary_url": "/programs/youth-sports",
                "style": "editorial",
                "priority": 10,
                "display_order": 1,
                **published,
            },
        )

        faqs = [
            (
                "How can I request humanitarian support?",
                "request-humanitarian-support",
                "support",
                "Use the private Request Support page. The initial form asks only for a brief description and a way to contact you. Submitting a request does not guarantee assistance; it allows the Foundation to review the situation privately.",
                1,
            ),
            (
                "How do I know a donation or payment link is official?",
                "official-donation-links",
                "giving",
                "Use only giving links published on the official Queen Tovah Cares Foundation International website. If the website does not show an approved payment channel, contact the Foundation before sending money.",
                2,
            ),
            (
                "Where are scholarship opportunities published?",
                "where-scholarships-are-published",
                "scholarship",
                "Verified scholarship opportunities are published on the Scholarships page with their application status, eligibility information and official application link when available.",
                3,
            ),
            (
                "How can I volunteer?",
                "how-to-volunteer",
                "volunteer",
                "Use the Get Involved page to submit your interests, skills and availability. Volunteer applications are reviewed privately by authorised Foundation administrators.",
                4,
            ),
            (
                "Can an organisation partner with the Foundation?",
                "organisation-partnerships",
                "partnership",
                "Yes. Organisations and institutions can contact the Foundation to discuss humanitarian, education, youth, community-development, sponsorship or professional collaborations.",
                5,
            ),
            (
                "Is the Foundation politically motivated?",
                "political-independence",
                "general",
                "Public reporting describes Queen Tovah Cares Foundation International as humanitarian in focus and not politically motivated. Its stated work centres on vulnerable people, education, empowerment and community development.",
                6,
            ),
        ]

        for question, slug, category, answer, order in faqs:
            FAQ.objects.update_or_create(
                slug=slug,
                defaults={
                    "question": question,
                    "category": category,
                    "answer": answer,
                    "display_order": order,
                    "featured": order <= 3,
                    **published,
                },
            )

        self.stdout.write(self.style.SUCCESS("Queen Tovah seed content is ready."))
