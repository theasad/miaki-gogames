from django.shortcuts import render
from rest_framework import generics

from apps.game.models import Category, Game
from apps.game.serializers import GameSerializer


class GameView(generics.ListAPIView):
    serializer_class = GameSerializer

    def get_queryset(self):
        category_id = self.request.GET.get('category_id')

        if category_id:
            query_set = Game.objects.filter(category__exact=category_id)
        else:
            query_set = Game.objects.all()

        return query_set
