# Steam Top 10 RPGs

Tiny Django app that scrapes Steam's top-selling RPGs into a SQLite table and lists them with plain Django templates.
If Steam can't be reached it falls back to hardcoded sample data, so everything works offline.

## Run
```
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Open http://127.0.0.1:8000. "Refresh" re-scrapes; `/api/top-rpgs/` is a JSON endpoint; `/game/<rank>/` is a detail page.

## Known issues (on `main`)


- `/api/top-rpgs/` crashes with a `TypeError` (500): `JsonResponse` is handed a QuerySet, which isn't JSON serializable. Fix: `fix/json-serialize-queryset`.

- Clicking "Refresh" duplicates every row: each scrape calls `Game.objects.create()` instead of `update_or_create()`. Fix: `fix/refresh-duplicates`.

- `/game/99/` raises `Game.DoesNotExist` (500) instead of showing a 404: the view uses `.get()` instead of `get_object_or_404()`. Fix: `fix/detail-404`.
