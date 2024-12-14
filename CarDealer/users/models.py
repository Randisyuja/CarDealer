from django.db import models
from django.contrib.auth.models import AbstractUser
from CarDealer.users.choices import RoleChoice
from django.core.exceptions import ValidationError



class User(AbstractUser):
    role = models.CharField(max_length=10, choices=RoleChoice, default=RoleChoice.User)

    def save(self, *args, **kwargs):
        # Pastikan hanya superuser yang dapat mengubah peran
        if self.pk and not self.is_superuser and self.role != self.__class__.objects.get(pk=self.pk).role:
            raise ValidationError("You are not allowed to change the user role.")
        super().save(*args, **kwargs)
