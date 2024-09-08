from celery import Celery

# Initialize Celery application
celery = Celery(__name__, broker='redis://localhost:6379/0',backend='redis://localhost:6379/0')

# Define a Celery task
@celery.task
def add(x, y):
    print(x+y)
    return x + y
