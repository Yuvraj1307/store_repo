from flask import Flask, jsonify, request
# from celery import Celery
import time
from task import add

app = Flask(__name__)

# celery = Celery(__name__, broker='redis://localhost:6379/0')


# @celery.task
# def add(x, y):
#     return x + y

@app.route('/schedule_task', methods=['POST'])
def schedule_task():
    data = request.json
    x = data.get('x')
    y = data.get('y')

    # Schedule the Celery task
    result = add.apply_async(args=(x, y))
    print(result.status)
    # if result.state == 'SUCCESS':
    #   print("Task completed successfully.")
    # elif result.state == 'FAILURE':
    #   print("Task failed.")
    # else:
    #   print("Task is still pending or in progress.")

    return jsonify({"task_id": result.id}), 200


@app.route('/')
def hello():
    return 'Hello, World! This is my Flask server.'


# print(res.state)

if __name__ == '__main__':
    app.run(debug=True)
