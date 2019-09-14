from django.db import models
from django.utils.html import mark_safe


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    category = models.ForeignKey(
        Category, related_name="game", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" style="height:auto;" />' % (self.image.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
