import time
from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

celery_app = Celery('tasks',  broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')


@celery_app.task()
def longtime_add(x, y):
    logger.info('Got Request - Starting work ')
    time.sleep(2)
    logger.info('Work Finished ')
    return x + y