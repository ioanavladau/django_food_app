from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # add configuration for user signals
    def ready(self):
        import users.signals