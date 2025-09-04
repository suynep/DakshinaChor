from django.shortcuts import render, redirect
from .models import RoomPlayer,PlayerCard,Card
from rooms.models import Room
from users.models import Player
import random

cards=[
    "baje","baje","baje","baje",
    "mama","mama","mama","mama",
    "raksi","raksi","raksi","raksi",
    "selroti","selroti","selroti","selroti",
    "paisa", "paisa", "paisa", "paisa",
    "taas", "taas", "taas", "taas",
    "tika+jamara", "tika+jamara", "tika+jamara", "tika+jamara",
    "changa", "changa", "changa", "changa"
]

card_points= {
    "baje": 900,
    "mama": 800,
    "rakshi": 700,
    "khasi": 600,
    "selroti": 500,
    "paisa": 400,
    "taas": 300,
    "tika+jamara": 200,
    "changa": 100
}

players=["Player 1", "Player 2","Player 3","Player 4","Player 5",]

#homepage
def home_view(request):
    return render(request, "game/index.html")

#create and join rooms
def play(request):
    return render(request, "game/play.html")

def play1(request):
    return render(request, "game/play-1.html")

def play2(request):
    return render(request, "game/play-2.html")

def enter_name(request):
    return render(request, "game/enter-name.html")

def create_room(request):
    return render(request, "game/createroom.html")

def calculate_points(request):
    pass