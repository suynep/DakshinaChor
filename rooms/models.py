from django.db import models

# Create your models here.

class Room(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(max_length=5, unique=True, blank=True, null=True)

    def __str__(self):
        return self.code or str(self.id)
