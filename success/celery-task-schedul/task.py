from celery import Celery, current_task
from pymongo import MongoClient

from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


# Initialize Celery application
app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

# Load Celery configuration from celeryconfig.py
app.config_from_object('celeryconfig')

# Define the MongoDB connection
client = MongoClient('mongodb+srv://yuvraj:yuvraj@cluster0.hhjiny0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['celerydatabase']

# Define the Celery task
@app.task()
def transfer_data():
    logger.info('got request from copy_data_task')
    current_task.update_state(state='PROGRESS', meta={'status': 'Task started: Transfer data from collection A to collection B'})

    try:
      # Connect to MongoDB and retrieve data from collection A
      collection_a = db['collection_A']
      data_to_transfer = list(collection_a.find())

      current_task.update_state(state='PROGRESS', meta={'status': f'Retrieved {len(data_to_transfer)} documents from collection A'})

      print(data_to_transfer)
      # Insert data into collection B
      collection_b = db['collection_B']
      result=collection_b.insert_many(data_to_transfer)
      logger.info('request completed successfully')
      current_task.update_state(state='PROGRESS', meta={'status': f'Transferred {len(result.inserted_ids)} documents from collection A to collection B'})

    except Exception as e:
       logger.error(f'Error {str(e)}')
       current_task.update_state(state='FAILURE', meta={'status': f'An error occurred: {str(e)}'})

    return f"Transferred {len(data_to_transfer)} documents from collection A to collection B"
