from django.db import models
from django.contrib.auth.models import AbstractUser
from CarDealer.users.choices import RoleChoice
from django.core.exceptions import ValidationError



class User(AbstractUser):
    role = models.CharField(max_length=10, choices=RoleChoice, default=RoleChoice.User)

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Ambil request dari kwargs
        if request and not request.user.is_superuser:
            raise ValidationError("Only superusers can modify this field.")
        super().save(*args, **kwargs)
