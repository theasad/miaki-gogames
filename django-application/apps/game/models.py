from django.db import models


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
