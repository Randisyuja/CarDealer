from django.db import models

from CarDealer.brands.models import Brands
from CarDealer.cars.validators import validate_file_size, validate_description
from CarDealer.categories.models import Category
from CarDealer.locations.models import Location
from CarDealer.users.models import User



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

    price = models.IntegerField(
        null=False,
        blank=False
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

    def __str__(self):
        return self.cars_name


class TestDrive(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_drive_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Test Drive {self.id} for {self.car} by {self.user}"

