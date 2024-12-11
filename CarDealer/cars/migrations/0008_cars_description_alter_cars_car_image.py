# Generated by Django 5.0.4 on 2024-12-10 20:18

import CarDealer.cars.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_cars_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='description',
            field=models.TextField(default=1, validators=[CarDealer.cars.validators.validate_description]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cars',
            name='car_image',
            field=models.ImageField(default=2, upload_to='images/', validators=[CarDealer.cars.validators.validate_file_size]),
            preserve_default=False,
        ),
    ]