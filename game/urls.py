from django.urls import path
import game.views as views

urlpatterns = [
    path("", views.home_view, name='home'),
    path("play/", views.play, name='play'),
    path("play-1/", views.play1, name='play1'),
    path("play-2/", views.play2, name='play2'),
    path("enter-name/", views.enter_name, name='enter name'),
    path("game-play/", views.game_play, name='game play'),
    path("create/", views.create_room, name='create room'),
]