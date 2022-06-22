from django.apps import AppConfig
from django.core.signals import request_started


class JdmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jdm'

    def ready(self):
        from . import signals
        request_started.connect(signals.request_start_handler)