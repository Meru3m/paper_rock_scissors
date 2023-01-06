from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, Http404

class ResultView(View):
    def post(self, request, **kwargs):
        print("Sììììì")
        response = HttpResponse(
            # RFC 1123 date format.
            headers={'Content-Type': 'application/json'},
        )
        return response


# Create your views here.
def index(request):
    return render(request, "gamepage/index.html")


def game(request):
    return render(request, "gamepage/game.html")