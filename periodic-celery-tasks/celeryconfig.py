# celeryconfig.py

from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'copy-data-task': {
        'task': 'app.copy_data_task',
        'schedule': crontab(minute='*'),  
    },
}
