from django.db import models

# Create your models here.

class Game(models.Model):
    word = models.CharField(max_length=20)
    guessed_word = models.CharField(max_length=20)
    status = models.CharField(max_length=10, default="ongoing")
    lives = models.IntegerField(default=6)