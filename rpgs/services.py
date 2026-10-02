from .demo import DEMO_GAMES
from .models import Game
from .scraper import fetch_top_rpgs


def save_games(scraped):
    for g in scraped:
        Game.objects.create(**g)


def refresh_games(limit=10):
    """Scrape Steam and store the results. Returns an error message, or None on success."""
    try:
        scraped = fetch_top_rpgs(limit)
        if not scraped:
            raise ValueError("no results parsed")
        error = None
    except Exception as exc:  # network down, Steam changed markup, etc.
        scraped = DEMO_GAMES
        error = f"Couldn't reach Steam ({exc}); showing sample data."
    save_games(scraped)
    return error
