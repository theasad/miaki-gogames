from rest_framework import serializers

from apps.game.models import Category, Game


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Game
        fields = ('id', 'name', 'image', 'category',)
