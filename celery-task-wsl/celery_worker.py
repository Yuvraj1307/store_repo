from celery import Celery
from tasks import celery

if __name__ == '__main__':
    celery.start()
