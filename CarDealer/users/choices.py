from django.db import models


class RoleChoice(models.TextChoices):
    User = 'User', 'User'
    Staff = 'Staff', 'Staff'
    Admin = 'Admin', 'Admin'
