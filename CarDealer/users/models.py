from django.db import models
from django.contrib.auth.models import AbstractUser
from CarDealer.users.choices import RoleChoice


class User(AbstractUser):
    role = models.CharField(max_length=10, choices=RoleChoice, default=RoleChoice.User)
