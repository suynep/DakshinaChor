
from django.db import models
from rooms.models import Room
from users.models import Player


# Association table between Room and Player
class RoomPlayer(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    player = models.CharField(max_length=25, blank=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)

# Association table between Player and Card
class PlayerCard(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    player = models.CharField(max_length=25, blank=True, null=True)
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