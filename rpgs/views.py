from django.http import JsonResponse
from django.shortcuts import render

from .models import Game
from .services import refresh_games


def index(request):
    error = None
    if "refresh" in request.GET or not Game.objects.exists():
        error = refresh_games()

    top_pick = Game.objects.filter(rank=1)

    context = {"games": Game.objects.all(), "top_pick": top_pick, "error": error}
    return render(request, "rpgs/index.html", context)


def api_top_rpgs(request):
    games = list(Game.objects.values("rank", "title", "price", "discount", "url"))
    return JsonResponse({"games": games})


def game_detail(request, rank):
    game = Game.objects.get(rank=rank)
    return render(request, "rpgs/detail.html", {"game": game})
