"""Offline guardrails for the bounded commercial-validation entry point.

Run: python3 scripts/check_commercial_validation.py
"""

from html.parser import HTMLParser
from pathlib import Path
import json
import unittest
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "assets/evergreenprotocol-com/site"
ROUTE = "/engagements/reference-continuity-evidence-brief/"
PAGE = SITE / ROUTE.lstrip("/") / "index.html"


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.meta = {}
        self.forms = 0
        self.inputs = 0
        self.ldjson = []
        self.in_ldjson = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a":
            self.links.append(attrs.get("href", ""))
        if tag == "meta":
            key = attrs.get("name") or attrs.get("property")
            if key:
                self.meta.setdefault(key, []).append(attrs.get("content", ""))
        if tag == "form":
            self.forms += 1
        if tag == "input":
            self.inputs += 1
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self.in_ldjson = True

    def handle_endtag(self, tag):
        if tag == "script":
            self.in_ldjson = False

    def handle_data(self, data):
        if self.in_ldjson:
            self.ldjson.append(data)


def parse(path):
    parsed = PageParser()
    parsed.feed(path.read_text(encoding="utf-8"))
    return parsed


class CommercialValidationTests(unittest.TestCase):
    def test_bounded_page_has_real_contact_and_no_form(self):
        self.assertTrue(PAGE.is_file())
        p = parse(PAGE)
        canonical = "https://evergreenprotocol.com" + ROUTE
        self.assertEqual(p.meta.get("og:url"), [canonical])
        self.assertEqual(p.meta.get("twitter:card"), ["summary_large_image"])
        self.assertEqual(p.forms, 0)
        self.assertEqual(p.inputs, 0)
        self.assertTrue(any(h.startswith("mailto:agent@sohadot.com?subject=") for h in p.links))
        self.assertTrue((SITE / "assets/social/evergreen-protocol-card.png").is_file())

    def test_public_limits_are_explicit(self):
        html = PAGE.read_text(encoding="utf-8")
        for phrase in (
            "Up to ten sources", "public", "written proposal", "no live checkout",
            "No numerical readiness score", "certification", "confidential",
            "No purchase, deadline, or acceptance is implied",
        ):
            self.assertIn(phrase.casefold(), html.casefold())
        obj = json.loads("".join(parse(PAGE).ldjson))
        self.assertEqual(obj["@type"], "WebPage")
        self.assertNotIn('"@type":"Offer"', html)
        self.assertNotIn('"@type":"Service"', html)

    def test_navigation_and_sitemap_are_coherent(self):
        self.assertIn(ROUTE, parse(SITE / "operator-brief/index.html").links)
        self.assertIn(ROUTE, parse(SITE / "strategic-operating-partnership/index.html").links)
        root = ElementTree.parse(SITE / "sitemap.xml").getroot()
        ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locs = [n.text for n in root.findall("s:url/s:loc", ns)]
        self.assertEqual(locs.count("https://evergreenprotocol.com" + ROUTE), 1)
        for href in parse(PAGE).links:
            if href.startswith("/"):
                self.assertTrue((SITE / href.lstrip("/") / "index.html").is_file(), href)


if __name__ == "__main__":
    unittest.main()
