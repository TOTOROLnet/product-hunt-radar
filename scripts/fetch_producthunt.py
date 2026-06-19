import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

FEED_URL = "https://www.producthunt.com/feed"
OUTPUT = Path(__file__).resolve().parents[1] / "data" / "latest.json"

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        text = data.strip()
        if text:
            self.parts.append(text)

    def value(self):
        return re.sub(r"\s+", " ", " ".join(self.parts)).strip()

def local(tag):
    return tag.rsplit("}", 1)[-1]

def clean_html(s):
    p = TextExtractor()
    p.feed(s or "")
    return p.value()

def child_text(node, names):
    for c in list(node):
        if local(c.tag) in names and c.text:
            return c.text.strip()
    return ""

def entry_link(entry):
    for c in list(entry):
        if local(c.tag) == "link":
            return c.attrib.get("href") or (c.text or "")
    return child_text(entry, ("guid",))

req = urllib.request.Request(
    FEED_URL,
    headers={"User-Agent": "Mozilla/5.0 ProductHuntRadar/1.0"}
)

with urllib.request.urlopen(req, timeout=30) as r:
    xml = r.read()

root = ET.fromstring(xml)
entries = [n for n in root.iter() if local(n.tag) in ("entry", "item")]

products = []
for e in entries:
    name = clean_html(child_text(e, ("title",)))
    desc = clean_html(child_text(e, ("content", "summary", "description")))
    link = entry_link(e)
    published = child_text(e, ("published", "pubDate", "updated"))
    if name and link:
        products.append({
            "name": name,
            "tagline_or_description": desc,
            "product_hunt_url": link,
            "published_at": published
        })

OUTPUT.parent.mkdir(exist_ok=True)
OUTPUT.write_text(json.dumps({
    "source": FEED_URL,
    "fetched_at": datetime.now(timezone.utc).isoformat(),
    "count": len(products),
    "products": products
}, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"Saved {len(products)} products to {OUTPUT}")
