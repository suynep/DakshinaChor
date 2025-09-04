from django.shortcuts import render,redirect,
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

card_points=[
    "baje": 900,
    "mama": 800,
    "rakshi": 700,
    "khasi": 600,
    "selroti": 500,
    "paisa": 400,
    "taas": 300,
    "tika+jamara": 200,
    "changa": 100
]

players=["Player 1", "Player 2","Player 3","Player 4","Player 5",]

#homepage
def home(request):
    return render(request, "game/home.html")

#create and join rooms
def create_room(request):
    pass

def join_room(request):
    pass

def calculate_points(request):
    pass