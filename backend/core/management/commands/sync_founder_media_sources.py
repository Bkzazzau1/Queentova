from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

from django.core.management.base import BaseCommand

from core.models import FounderMediaItem, FounderMediaPhoto


ALLOWED_SOURCE_DOMAINS = {
    "anambrastate.gov.ng",
    "www.anambrastate.gov.ng",
    "independent.ng",
    "www.independent.ng",
    "odogwublog.com",
    "www.odogwublog.com",
}


class MediaHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.og_image = ""
        self.images = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "meta":
            prop = (attrs.get("property") or attrs.get("name") or "").lower()
            if prop in {"og:image", "twitter:image", "twitter:image:src"}:
                value = attrs.get("content", "").strip()
                if value and not self.og_image:
                    self.og_image = value

        if tag == "img":
            src = (
                attrs.get("src")
                or attrs.get("data-src")
                or attrs.get("data-lazy-src")
                or ""
            ).strip()
            if not src:
                return

            lowered = src.lower()
            if any(
                marker in lowered
                for marker in (
                    "logo",
                    "icon",
                    "avatar",
                    "emoji",
                    "spinner",
                    "placeholder",
                    "gravatar",
                    "favicon",
                )
            ):
                return

            self.images.append(
                {
                    "src": src,
                    "alt": (attrs.get("alt") or "").strip(),
                }
            )


class Command(BaseCommand):
    help = (
        "Collect candidate founder-media images from approved publication sources. "
        "Candidates are never public until reuse_approved is enabled in admin."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--slug",
            help="Only sync one FounderMediaItem slug.",
        )
        parser.add_argument(
            "--limit",
            type=int,
            default=6,
            help="Maximum candidate images to keep per publication.",
        )

    def handle(self, *args, **options):
        queryset = FounderMediaItem.objects.filter(verified_source=True)
        if options.get("slug"):
            queryset = queryset.filter(slug=options["slug"])

        synced = 0
        skipped = 0

        for item in queryset:
            parsed = urlparse(item.source_url)
            domain = parsed.netloc.lower()

            if domain not in ALLOWED_SOURCE_DOMAINS:
                skipped += 1
                self.stdout.write(
                    self.style.WARNING(
                        f"Skipped {item.slug}: source domain {domain!r} is not allowlisted."
                    )
                )
                continue

            if parsed.path.lower().endswith(".pdf"):
                skipped += 1
                self.stdout.write(
                    self.style.WARNING(
                        f"Skipped {item.slug}: PDF source does not expose an HTML photo gallery."
                    )
                )
                continue

            try:
                request = Request(
                    item.source_url,
                    headers={
                        "User-Agent": (
                            "QueenTovahMediaArchive/1.0 "
                            "(official Foundation website media-source review)"
                        )
                    },
                )
                with urlopen(request, timeout=15) as response:
                    content_type = response.headers.get("Content-Type", "")
                    if "text/html" not in content_type:
                        raise ValueError(f"Unexpected content type: {content_type}")
                    html = response.read(2_000_000).decode("utf-8", errors="ignore")
            except Exception as exc:
                self.stdout.write(
                    self.style.ERROR(f"Could not read {item.slug}: {exc}")
                )
                continue

            parser = MediaHTMLParser()
            parser.feed(html)

            candidates = []
            if parser.og_image:
                candidates.append(
                    {
                        "src": parser.og_image,
                        "alt": f"{item.title} — publication preview",
                    }
                )
            candidates.extend(parser.images)

            unique = []
            seen = set()
            for candidate in candidates:
                absolute = urljoin(item.source_url, candidate["src"])
                image_host = urlparse(absolute).netloc.lower()

                if image_host not in ALLOWED_SOURCE_DOMAINS:
                    continue
                if absolute in seen:
                    continue

                seen.add(absolute)
                unique.append(
                    {
                        "url": absolute,
                        "alt": candidate["alt"] or f"{item.title} — source photograph",
                    }
                )

                if len(unique) >= max(1, options["limit"]):
                    break

            for index, candidate in enumerate(unique):
                FounderMediaPhoto.objects.get_or_create(
                    media_item=item,
                    external_image_url=candidate["url"],
                    defaults={
                        "alt_text": candidate["alt"][:240],
                        "caption": (
                            "Candidate image discovered from the linked publication. "
                            "Review rights/permission before enabling public reuse."
                        ),
                        "credit": item.source_name,
                        "source_url": item.source_url,
                        "reuse_approved": False,
                        "is_primary": index == 0,
                        "display_order": index + 1,
                    },
                )

            synced += 1
            self.stdout.write(
                self.style.SUCCESS(
                    f"{item.slug}: collected {len(unique)} candidate image(s). "
                    "They remain private until approved for reuse."
                )
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Founder media source sync finished: {synced} source(s) reviewed, "
                f"{skipped} skipped."
            )
        )
