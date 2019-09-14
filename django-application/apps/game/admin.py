from django.contrib import admin

from apps.game.models import Category, Game


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'category',)
    list_filter = ('category',)
    fields = ('name', 'image_tag', 'image', 'category',)
    readonly_fields = ('image_tag',)
