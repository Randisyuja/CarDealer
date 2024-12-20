# Generated by Django 5.0.4 on 2024-12-03 19:40

import CarDealer.cars.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_cars_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='car_image',
            field=models.ImageField(blank=True, null=True, upload_to='images', validators=[CarDealer.cars.validators.validate_file_size]),
        ),
    ]
