from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from . import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ems.settings')

## Get the base REDIS URL, default to redis' default
BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

app = Celery('ems')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.broker_url = BASE_REDIS_URL

app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


