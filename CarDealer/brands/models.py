from django.db import models


class Brands(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=False,
    )

    year_established = models.IntegerField(
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name
