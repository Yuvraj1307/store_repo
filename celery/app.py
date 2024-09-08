# from flask import Flask, jsonify
# from tasks import long_task
# from celery import Celery

# app = Flask(__name__)
# app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
# app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

# celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
# celery.conf.update(app.config)

# @app.route('/runtask')
# def run_task():
#     task = long_task.delay()
#     return f'Task {task.id} started!'

# @app.route('/getstatus/<task_id>')
# def get_status(task_id):
#     task = long_task.AsyncResult(task_id)
#     return jsonify({'status': task.state})
# cgsdfgf




# app.py
from flask import Flask, jsonify
from celery import Celery
from tasks import long_task, copy_collection

app = Flask(__name__)
# app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
# app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

# celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
# celery.conf.update(app.config)

# @celery.task
# def long_task():
#     # Simulate a long-running task
#     import time
#     time.sleep(10)
#     return 'Task completed!'


@app.route('/')
def base():
    return 'Hello World!'

@app.route('/runtask')
def run_task():
    # task = long_task.delay(5,6)
    task=copy_collection.delay()
    return f'Task {task.id} started!'

@app.route('/getstatus/<task_id>')
def get_status(task_id):
    task = copy_collection.AsyncResult(task_id)
    return jsonify({'status': task.state})


@app.route('/getres/<task_id>')
def get_result(task_id):
    task = copy_collection.AsyncResult(task_id)
    return jsonify({'status': task.result})

if __name__ == '__main__':
    app.run()