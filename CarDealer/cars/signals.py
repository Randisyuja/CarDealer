import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Cars


@receiver(post_delete, sender=Cars)
def delete_car_image(sender, instance, **kwargs):
    """
    Menghapus file gambar saat instance Cars dihapus.
    """
    if instance.car_image:
        car_image_path = instance.car_image.path
        if os.path.isfile(car_image_path):
            try:
                os.remove(car_image_path)
            except Exception as e:
                print(f"Error deleting image: {e}")
