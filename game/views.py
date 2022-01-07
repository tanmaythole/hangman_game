from django.shortcuts import render
import requests
import random

from game.models import Game

# Create your views here.
def get_word():
    word = requests.get("https://random-word-api.herokuapp.com/word?number=1").json()[0]
    return word


def get_guessed_word(word):
    hint = random.choice(word) + "" + random.choice(word)
    guessed_word = ""
    for c in word:
        if c in hint:
            guessed_word += c
        else:
            guessed_word += "_"
    return guessed_word



def index(request):
    if request.method=='GET':
        word = get_word()
        guessed_word = get_guessed_word(word)
        game = Game(word=word, guessed_word=guessed_word)
        game.save()
        game.image = 6 - game.lives
        return render(request, 'index.html', { 'game':game })
    elif request.method=='POST':
        return 