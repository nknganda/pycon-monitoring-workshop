from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = "core"
    label = "core"

    def ready(self):
        pass
