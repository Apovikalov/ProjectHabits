import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("project",
             broker='redis://redis:6379/0',  # URL брокера
             backend='redis://redis:6379/1'  # URL бэкенда
)

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'cleanup-every-night': {
        'task': 'tasks.cleanup_old_records',
        'schedule': crontab(hour=2, minute=0),  # каждый день в 02:00
    },
    'send-digest-every-hour': {
        'task': 'tasks.send_digest',
        'schedule': crontab(hour='*/1'),  # каждый час
    },
}
