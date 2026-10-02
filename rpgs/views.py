from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

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
    games = Game.objects.all()
    return JsonResponse({"games": games})


def game_detail(request, rank):
    game = get_object_or_404(Game, rank=rank)
    return render(request, "rpgs/detail.html", {"game": game})
