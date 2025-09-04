from django.urls import path
import game.views as views

urlpatterns = [
    path("", views.home_view, name='home'),
    path("play/", views.play, name='play'),
    path("join/", views.join_room, name='join room'),
    # path("play-2/", views.play2, name='play2'),
    path("createuser/", views.create_user, name='create user'),
    path("create/", views.create_room, name='create room'),
]