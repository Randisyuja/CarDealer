# Generated by Django 5.0.4 on 2024-12-15 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brands',
            name='description',
        ),
    ]
