from django.test import TestCase

from .models import Game


class JsonApiTests(TestCase):
    def test_api_returns_serialized_games(self):
        Game.objects.create(rank=1, steam_app_id=1, title="Elden Ring", price="$59.99")
        resp = self.client.get("/api/top-rpgs/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["games"][0]["title"], "Elden Ring")
