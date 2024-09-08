from celery.schedules import crontab

# Define the schedule for the periodic task
beat_schedule = {
    'transfer-data-every-minute': {
        'task': 'tasks.transfer_data',
        'schedule': crontab(minute='*/1'),  # Run the task every minute
    },
}
