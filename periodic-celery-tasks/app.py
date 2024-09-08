# app.py

from flask import Flask
from celery import Celery
from pymongo import MongoClient
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

app = Flask(__name__)

# MongoDB connection
mongo_client = MongoClient('mongodb+srv://yuvraj:yuvraj@cluster0.hhjiny0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = mongo_client['celerydatabase']

# Celery configuration
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task
def copy_data_task():
    logger.info('got request from copy_data_task')
    try:
        # Get data from collection A
        collection_a = db['collection_A']
        data = collection_a.find()

        # Insert data into collection B
        collection_b = db['collection_B']
        collection_b.insert_many(data)
        logger.info('request completed successfully')
        # Log success
        app.logger.info("Data copied successfully from collection A to collection B.")
    except Exception as e:
        # Log error
        logger.error(f'Error {str(e)}')
        app.logger.error(f"Error copying data: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
