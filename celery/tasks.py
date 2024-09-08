from celery import Celery
from pymongo import MongoClient
# from motor.motor_asyncio import AsyncIOMotorClient

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
@celery.task
async def copy_collection():
    # Connect to MongoDB using Motor
    client = MongoClient('mongodb+srv://yuvraj:yuvraj@cluster0.hhjiny0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    db = client['celerydatabase']
    collection_a = db['collection_A']
    print("collection_a")
    collection_b = db['collection_B']
    print("collection_b")

    # Read from collection A and insert into collection B
    async for document in collection_a.find():
        await collection_b.insert_one(document)

    # Close the Motor client
    client.close()
    return 'Copy completed successfully'



# dfvsdfvsdfvsdfvsdfgsdfgsdfssd