from django.db import models
from rooms.models import Room
from users.models import Player

# Association table between Room and Player
class RoomPlayer(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

# Association table between Player and Card
class PlayerCard(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    card = models.ForeignKey('Card', on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

class Card(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    CATEGORY_CHOICES = [
        ("food", "Food"),
        ("people", "People"),
        ("miscellaneous", "Miscellaneous"),
    ]
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="miscellaneous",
    )
    points = models.IntegerField()
    image = models.URLField(blank=True, null=True)

# 🔹 Activity model (top-level, not inside Card)
class Activity(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)  # e.g., "entered_name", "joined_room", "played_card"
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.username} -> {self.action} at {self.timestamp}"
