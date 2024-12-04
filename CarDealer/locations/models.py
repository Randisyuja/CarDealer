from django.db import models


class Location(models.Model):
    location = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.location
