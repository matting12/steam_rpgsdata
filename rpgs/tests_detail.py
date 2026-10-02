from django.test import TestCase

from .models import Game


class DetailTests(TestCase):
    def setUp(self):
        Game.objects.create(rank=1, steam_app_id=1, title="Elden Ring", price="$59.99")

    def test_existing_game_renders(self):
        self.assertContains(self.client.get("/game/1/"), "Elden Ring")

    def test_missing_game_is_404_not_500(self):
        self.assertEqual(self.client.get("/game/99/").status_code, 404)
