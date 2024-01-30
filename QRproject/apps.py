from django.apps import AppConfig


class QrprojectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'QRproject'
    def ready(self):
        import QRproject.signals
