from django.test import TestCase

from users.models import User

user = User.objects.create_user(username="testuser", email="test@example.com", password="password123")
print(user)

