from .demo import DEMO_GAMES
from .models import Game
from .scraper import fetch_top_rpgs


def save_games(scraped):
    ids = [g["steam_app_id"] for g in scraped]
    for g in scraped:
        defaults = {k: v for k, v in g.items() if k != "steam_app_id"}
        Game.objects.update_or_create(steam_app_id=g["steam_app_id"], defaults=defaults)
    # Drop games that fell out of the top 10 so ranks stay unique.
    Game.objects.exclude(steam_app_id__in=ids).delete()


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
