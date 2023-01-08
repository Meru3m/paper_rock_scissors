import json
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

class ResultView(View):
    def post(self, request, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        user_choise = body.get("user_choice")
        opponent_choise = body.get("opponent_choice")
        user_choise_mod = user_choise % 2
        opponent_choise_mod = opponent_choise % 2

        winner = 0
        if user_choise < opponent_choise:
            winner = 2
            if opponent_choise - user_choise == 2:
                winner = 1
        elif opponent_choise < user_choise:
            winner = 1
            if user_choise - opponent_choise == 2:
                winner = 2

        response = JsonResponse({"winner": winner})

        return response


# Create your views here.
def index(request):
    return render(request, "gamepage/index.html")


def game(request):
    return render(request, "gamepage/game.html")