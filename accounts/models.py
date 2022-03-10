from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    created = models.DateTimeField(auto_now_add=True)
    karma = models.IntegerField(default=1)
    about = models.CharField(max_length=400)
    email = models.EmailField()
