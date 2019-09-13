import django
from django.db.models import signals
from .commands.sync_plugins import sync_app_plugins

def do_sync(*args, **kwdargs):
    sync_app_plugins(verbosity=kwdargs.get("verbosity", 1))

if django.VERSION >= (1, 7):
    from django.apps import apps
    sender_app = apps.get_app_config('app_plugins')
    signals.post_migrate.connect(do_sync, sender=sender_app)
else:
    from app_plugins import models as sender_app
    signals.post_syncdb.connect(do_sync, sender=sender_app)

if __name__ == "__main__":
    sync_app_plugins()
