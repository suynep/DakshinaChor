from django.shortcuts import render, redirect
from django.urls import reverse
from .models import RoomPlayer,PlayerCard,Card
from rooms.models import Room
from users.models import Player
import random
import uuid

alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
    'y', 'z',
]

ROOM_CODE_LENGTH = 8

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
    # railguard
    if not request.session.get('username'):
        return redirect("create user")
    
    if request.session.get('room_code'):
        return render(request, "game/play.html", {'room': True})

    return render(request, "game/play.html")

def join_room(request):
    # railguard
    if not request.session.get('username'):
        return redirect("create user")
    return render(request, "game/joinroom.html")

def create_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        if not username:
            return render(request, "game/createuser.html", {"error": "username cannot be empty!"})
        else:
            request.session['username'] = username
            print(request.session['username'])
            return redirect('play')

    return render(request, "game/createuser.html")

def create_room(request):
    # railguard
    if not request.session.get('username'):
        return redirect("create user")

    room_code = ''
    for _ in range(ROOM_CODE_LENGTH):
        room_code += random.choice(alphabets)

    if request.method == "POST":
        code = request.POST.get("room_code")
        if not code:
            return render(request, "game/createroom.html", {"error": "code cannot be empty!"})
        
        new_room = Room(id=uuid.uuid4(), code=room_code)
        new_room.save()
        request.session['room_code'] = room_code
        RoomPlayer(room=new_room, player=request.session.get("username")).save()
        print(f"new room `{room_code}` created successfully")




    return render(request, "game/createroom.html", {'room_code': room_code})

def calculate_points(request):
    pass