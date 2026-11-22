from django.shortcuts import render
from rest_framework import generics

from apps.game.models import Category, Game
from apps.game.serializers import GameSerializer


class GameView(generics.ListAPIView):
    serializer_class = GameSerializer

    def get_queryset(self):
        return (
            Game.objects.filter(category__exact=category_id)
            if (category_id := self.request.GET.get('category_id'))
            else Game.objects.all()
        )
