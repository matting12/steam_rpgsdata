"""Scrapes Steam's top-selling RPGs from the public store search endpoint.

Note: the Steam *Workshop* has no sales data (it hosts mods, not games),
so the store's "Top Sellers" list filtered by the RPG tag is used instead.
"""
import requests
from bs4 import BeautifulSoup

SEARCH_URL = "https://store.steampowered.com/search/results/"
RPG_TAG_ID = 122


def _app_id(raw):
    try:
        return int((raw or "").split(",")[0])
    except ValueError:
        return None


def parse_results(html, limit=10):
    soup = BeautifulSoup(html, "html.parser")
    games = []
    for rank, row in enumerate(soup.select("a.search_result_row")[:limit], start=1):
        title = row.select_one("span.title")
        img = row.select_one(".search_capsule img")
        price_block = row.select_one(".search_price_discount_combined")
        discount = row.select_one(".discount_pct")
        final = row.select_one(".discount_final_price")

        games.append(
            {
                "rank": rank,
                "steam_app_id": _app_id(row.get("data-ds-appid")),
                "title": title.get_text(strip=True) if title else "Unknown",
                "url": row.get("href", "").split("?")[0],
                "image": img.get("src") if img else "",
                "discount": discount.get_text(strip=True) if discount else "",
                "price": final.get_text(strip=True) if final else "N/A",
                "is_free": bool(
                    price_block and price_block.get("data-price-final") == "0"
                ),
            }
        )
    return games


def fetch_top_rpgs(limit=10):
    resp = requests.get(
        SEARCH_URL,
        params={
            "query": "",
            "start": 0,
            "count": limit,
            "filter": "topsellers",
            "tags": RPG_TAG_ID,
            "category1": 998,  # games only (no DLC/soundtracks)
            "cc": "us",
            "l": "english",
            "infinite": 1,
        },
        headers={"User-Agent": "Mozilla/5.0 (steam-rpgs demo scraper)"},
        timeout=15,
    )
    resp.raise_for_status()
    return parse_results(resp.json().get("results_html", ""), limit)
