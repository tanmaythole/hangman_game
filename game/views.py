from django.shortcuts import render
import requests
import random
from django.http.response import JsonResponse

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


def update_guessed_word(word, guessed_word, inp):
    new_guess = ""
    if inp in word:
        for i in range(len(word)):
            if word[i] in inp:
                new_guess += inp
            else:
                new_guess += guessed_word[i]
    else:
        return 0
    return new_guess 


def index(request):

    if request.method=='GET':
        word = get_word()
        guessed_word = get_guessed_word(word)
        game = Game(word=word, guessed_word=guessed_word)
        game.save()
        game.image = 6 - game.lives
        return render(request, 'index.html', { 'game':game })
        
    elif request.method=='POST':
        game = Game.objects.filter(id=request.POST['game_id'])[0]
        inp = request.POST['inp'].lower()
        new_guess = update_guessed_word(game.word, game.guessed_word, inp)

        if new_guess == 0:
            game.lives = game.lives - 1
            if game.lives == 0 or game.lives<0:
                game.status = "lose"
            game.save()
            return JsonResponse({"ans":False, "lives":game.lives, "status":game.status}, status=200)
            
        else:
            game.guessed_word = new_guess

            if new_guess.lower() == game.word.lower() and game.lives>0:
                game.status = "win"
            game.save()

            return JsonResponse({"ans":True, "guessed_word":game.guessed_word, "status":game.status}, status=200)
        
        return JsonResponse({}, 401)
        