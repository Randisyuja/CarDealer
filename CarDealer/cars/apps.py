from django.apps import AppConfig


class CarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CarDealer.cars'

    def ready(self):
        import CarDealer.cars.signals  # Impor signals
