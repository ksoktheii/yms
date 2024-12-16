from django.apps import AppConfig


class YouthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'youth'

    def ready(self):
        import youth.signals
