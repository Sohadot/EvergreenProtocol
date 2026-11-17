"""Offline regression checks for the public social-sharing previews.

Run: python3 scripts/check_social_preview.py
No dependencies or network access are required.
"""

from html.parser import HTMLParser
from pathlib import Path
import struct
import unittest
from urllib.parse import urlparse


SITE = Path(__file__).resolve().parents[1] / "assets/evergreenprotocol-com/site"
IMAGE_URL = "https://evergreenprotocol.com/assets/social/evergreen-protocol-card.png"
TITLE = "Evergreen Protocol — Category Standard for AI-Era Digital Continuity"


class MetadataParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.entries = {}

    def handle_starttag(self, tag, attrs):
        if tag != "meta":
            return
        attributes = dict(attrs)
        name = attributes.get("property") or attributes.get("name")
        if name:
            self.entries.setdefault(name, []).append(attributes.get("content", ""))


def read_metadata(file):
    parser = MetadataParser()
    parser.feed(file.read_text(encoding="utf-8"))
    return parser.entries


class SocialPreviewTests(unittest.TestCase):
    def test_both_shared_routes_publish_full_card(self):
        for route, expected_url in [
            ("index.html", "https://evergreenprotocol.com/"),
            ("en/index.html", "https://evergreenprotocol.com/en/"),
        ]:
            with self.subTest(route=route):
                data = read_metadata(SITE / route)
                expected = {
                    "og:type": "website",
                    "og:site_name": "Evergreen Protocol",
                    "og:title": TITLE,
                    "og:url": expected_url,
                    "og:image": IMAGE_URL,
                    "og:image:secure_url": IMAGE_URL,
                    "og:image:type": "image/png",
                    "og:image:width": "1200",
                    "og:image:height": "630",
                    "twitter:card": "summary_large_image",
                    "twitter:title": TITLE,
                    "twitter:image": IMAGE_URL,
                }
                for key, value in expected.items():
                    self.assertEqual(data.get(key), [value], f"{route}: {key}")
                for key in (
                    "description", "og:description", "og:locale",
                    "og:image:alt", "twitter:description", "twitter:image:alt",
                ):
                    self.assertEqual(len(data.get(key, [])), 1, f"{route}: {key}")
                    self.assertTrue(data[key][0].strip(), f"{route}: {key} empty")

    def test_image_is_served_from_the_published_site_tree(self):
        parsed = urlparse(IMAGE_URL)
        self.assertEqual((parsed.scheme, parsed.netloc), ("https", "evergreenprotocol.com"))
        file = SITE / parsed.path.lstrip("/")
        self.assertTrue(file.is_file(), f"Missing published image: {file}")
        self.assertLess(file.stat().st_size, 2_000_000)
        with file.open("rb") as asset:
            header = asset.read(24)
        self.assertEqual(header[:8], b"\x89PNG\r\n\x1a\n")
        self.assertEqual(header[12:16], b"IHDR")
        self.assertEqual(struct.unpack(">II", header[16:24]), (1200, 630))

    def test_vector_source_is_present_for_reproducibility(self):
        self.assertTrue((SITE / "assets/social/evergreen-protocol-card.svg").is_file())


if __name__ == "__main__":
    unittest.main()
