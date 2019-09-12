from django.urls import path, re_path
from apps.game.views import GameView
urlpatterns = [
    path('', GameView.as_view(), name="games")
]
