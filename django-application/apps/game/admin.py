from django.contrib import admin

from apps.game.models import Category, Game


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    fields = ['id', 'name']


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'category',)
    list_filter = ('category',)
