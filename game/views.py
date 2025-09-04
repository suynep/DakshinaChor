from django.shortcuts import render,redirect
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

card_points={
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
  

players=["Player 1", "Player 2","Player 3","Player 4","Player 5"]

#homepage
def home(request):
    return render(request, "game/home.html")

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from users.models import Player
from game.models import Card, Move, PlayerCard, RoomPlayer
from rooms.models import Room
from .models import Activity
import uuid

#  Enter Name 
def enter_name(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required"}, status=400)

    username = request.POST.get("username", "").strip()
    if not username:
        return JsonResponse({"error": "Please enter a name."}, status=400)

    player = Player.objects.create(id=uuid.uuid4(), username=username)

    # Log activity
    Activity.objects.create(
        player=player,
        action="entered_name",
        description=f"Guest player {username} entered the game"
    )

    return JsonResponse({"message": f"Welcome {username}", "player_id": str(player.id)})


# Join Room
def join_room(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required"}, status=400)

    player_id = request.POST.get("player_id")
    room_code = request.POST.get("room_code")

    player = get_object_or_404(Player, id=player_id)
    room, created = Room.objects.get_or_create(code=room_code)

   
    RoomPlayer.objects.create(room=room, player=player)

    # Log activity
    Activity.objects.create(
        player=player,
        action="joined_room",
        description=f"{player.username} joined room {room.code}"
    )

    return JsonResponse({"message": f"{player.username} joined room {room.code}", "room_id": str(room.id)})


# Play Card
def play_card(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required"}, status=400)

    player_id = request.POST.get("player_id")
    card_id = request.POST.get("card_id")
    room_code = request.POST.get("room_code")
    round_number = int(request.POST.get("round_number", 1))

    player = get_object_or_404(Player, id=player_id)
    card = get_object_or_404(Card, id=card_id)
    room = get_object_or_404(Room, code=room_code)

    # Log the move (game history)
    Move.objects.create(
        room=room,
        player=player,
        card=card,
        round_number=round_number,
        action="played"
    )

    # Log activity
    Activity.objects.create(
        player=player,
        action="played_card",
        description=f"{player.username} played {card.name} in room {room.code}"
    )

    return JsonResponse({"message": f"{player.username} played {card.name}"})
