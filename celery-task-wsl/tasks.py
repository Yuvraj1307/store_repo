from celery import Celery

celery = Celery('tasks', broker='redis://localhost:6379/0',backend='redis://localhost:6379/0')

@celery.task
def long_task(x,y):
    # Simulate a long-running task
    import time
    time.sleep(10)
    res=x+y
    return res
# @celery.task
# def long_task():
#     # Simulate a long-running task
#     import time
#     time.sleep(10)
#     return 'Task completed!'
