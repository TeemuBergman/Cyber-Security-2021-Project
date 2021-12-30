from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Message(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sender")
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipient")
    content = models.TextField(max_length=256, default="")
    timestamp = models.DateTimeField(default=timezone.now)
    opened = models.BooleanField(default=False)
