from django.db import models

# Create your models here.

class Player(models.Model):
    id = models.UUIDField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username or str(self.id)