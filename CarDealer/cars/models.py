from django.db import models

from CarDealer.brands.models import Brands
from CarDealer.cars.validators import validate_file_size, validate_description
from CarDealer.categories.models import Category
from CarDealer.locations.models import Location



class Cars(models.Model):
    id_cars = models.AutoField(
        primary_key=True
    )

    car_image = models.ImageField(
        upload_to='images/',
        validators=[validate_file_size],
        null=False,
        blank=False,
    )

    cars_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )

    brand = models.ForeignKey(
        Brands,
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    warna = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )

    tahun = models.IntegerField(
        null=False,
        blank=False,
    )

    CC = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )

    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE
    )

    description = models.TextField(
        validators=[validate_description],
        null=False,
        blank=False,
    )
