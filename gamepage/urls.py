from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt
from . import views

app_name = 'rps_game'
urlpatterns = [
    path("", views.index, name='index'),
    path("play/", views.game),
    path("result/", csrf_exempt(views.ResultView.as_view()), name="status"),
]