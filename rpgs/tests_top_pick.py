from django.test import TestCase

from .models import Game


class TopPickTests(TestCase):
    def setUp(self):
        Game.objects.create(rank=1, steam_app_id=1, title="Divinity Original Sin 2", price="$22.49")
        Game.objects.create(rank=2, steam_app_id=2, title="Elden Ring", price="$59.99")

    def test_top_pick_banner_shows_rank_one_game(self):
        html = self.client.get("/").content.decode()
        self.assertIn("Top pick: <strong>Divinity Original Sin 2</strong> $22.49", html)
