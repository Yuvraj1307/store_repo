from flask import Flask
from celery import Celery
from simple_worker.tasks import celery_app
app = Flask(__name__)
# simple_app = Celery('simple_worker',  broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
simple_app = celery_app


@app.route('/simple_start_task')
def call_method():
    app.logger.info("Invoking Method ")
    #                        queue name in task folder.function name
    r = celery_app.send_task('tasks.longtime_add', kwargs={'x': 1, 'y': 2})
    # r = simple_app.send_task('tasks.longtime_add', kwargs={'x': 1, 'y': 2})
    # r = celery_app.apply_async(args=[1, 2], expires=60)
    app.logger.info(r.backend)
    return r.id


@app.route('/simple_task_status/<task_id>')
def get_status(task_id):
    status = celery_app.AsyncResult(task_id, app=celery_app)
    print("Invoking Method ")
    return "Status of the Task " + str(status.state)


@app.route('/simple_task_result/<task_id>')
def task_result(task_id):
    result = celery_app.AsyncResult(task_id).result
    return "Result of the Task " + str(result)


if __name__ == '__main__':
    app.run(debug=True)