from unittest.mock import patch

from django.test import TestCase

from .models import Game
from .services import refresh_games


def _game(rank, app_id, title):
    return {"rank": rank, "steam_app_id": app_id, "title": title, "url": "", "image": "",
            "discount": "", "price": "$1.00", "is_free": False}


@patch("rpgs.services.fetch_top_rpgs")
class RefreshTests(TestCase):
    def test_refreshing_twice_does_not_duplicate(self, fetch):
        fetch.return_value = [_game(1, 1, "A"), _game(2, 2, "B")]
        refresh_games()
        refresh_games()
        self.assertEqual(Game.objects.count(), 2)

    def test_games_that_drop_out_are_removed(self, fetch):
        fetch.return_value = [_game(1, 1, "A"), _game(2, 2, "B")]
        refresh_games()
        fetch.return_value = [_game(1, 2, "B")]
        refresh_games()
        self.assertEqual(list(Game.objects.values_list("title", flat=True)), ["B"])
