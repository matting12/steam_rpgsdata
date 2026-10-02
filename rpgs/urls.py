from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/top-rpgs/", views.api_top_rpgs, name="api_top_rpgs"),
    path("game/<int:rank>/", views.game_detail, name="game_detail"),
]
