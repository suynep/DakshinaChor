from django.urls import path
import game.views as views

urlpatterns = [
    path("", views.home_view, name='home'),
    path("play/", views.play, name='play'),
    path("create/", views.create_room, name='create room'),
]