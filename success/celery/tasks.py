# from fastapi import FastAPI, BackgroundTasks
# import schedule
# import time

# app = FastAPI()

# # Define a global variable to store the scheduled job identifier
# scheduled_job = None

# def print_hi():
#     print("Hi")

# # Schedule the job to run every second
# schedule.every(1).seconds.do(print_hi)

# @app.get('/')
# def read_root():
#     return {"message":"wanna schedule a job"}

# # Define a FastAPI endpoint to start the scheduled job
# @app.get("/start")
# async def start_scheduled_job(background_tasks: BackgroundTasks):
#     global scheduled_job

#     def run_scheduled_job():
#         while True:
#             schedule.run_pending()
#             time.sleep(1)

#     scheduled_job = background_tasks.add_task(run_scheduled_job)
#     return {"message": "Scheduled job started"}

# # Define a FastAPI endpoint to stop the scheduled job
# @app.get("/stop")
# async def stop_scheduled_job():
#     global scheduled_job
#     if scheduled_job:
#         scheduled_job.cancel()
#         return {"message": "Scheduled job stopped"}
#     else:
#         return {"message": "No scheduled job running"}


# # # dfsdffg
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000).reload()







# from fastapi import FastAPI, BackgroundTasks
# from motor.motor_asyncio import AsyncIOMotorClient
# import schedule
# import asyncio

# app = FastAPI()

# # MongoDB Atlas connection settings
# MONGO_URI = "mongodb+srv://yuvraj:yuvraj@cluster0.hhjiny0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# MONGO_DB = "test_db"
# COLLECTION_A = "collection_a"
# COLLECTION_B = "collection_b"

# # Connect to MongoDB Atlas
# client = AsyncIOMotorClient(MONGO_URI)
# db = client[MONGO_DB]


# # Define the job function
# async def get_data_and_insert():
#     collection_a = db[COLLECTION_A]
#     collection_b = db[COLLECTION_B]

#     async for document in collection_a.find({}):
#         # Modify fields
#         modified_document = {
#             "name": f"readed {document['name']}",
#             "age": f"readed {document['age']}",
#             "job": f"readed {document['job']}"
#         }

#         # Insert modified data into Collection B
#         await collection_b.insert_one(modified_document)

# # Schedule the job to run every minute
# schedule.every(1).minutes.do(get_data_and_insert)
# # Run scheduled job function
# async def run_scheduled_job():
#     while True:
#         schedule.run_pending()
#         await asyncio.sleep(1)

# @app.on_event("startup")
# async def startup_event():
#     # Start running the scheduled job
#     asyncio.create_task(run_scheduled_job())

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)




from fastapi import FastAPI, BackgroundTasks
from motor.motor_asyncio import AsyncIOMotorClient
from celery import Celery
# import schedule
# import asyncio

app = FastAPI()
celery = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
MONGO_URI = "mongodb+srv://yuvraj:yuvraj@cluster0.hhjiny0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
MONGO_DB = "test_db"
COLLECTION_A = "collection_a"
COLLECTION_B = "collection_b"

# Connect to MongoDB Atlas
# client = AsyncIOMotorClient(MONGO_URI)
# db = client[MONGO_DB]
@celery.task
def process_task(x, y):
    print("task started")
    return x + y
@app.get("/")
def start_server():
    return {"message": "connection established"}

@app.post("/add")
async def add(x: int, y: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_task, x, y)
    return {"message": "Task added to the background queue."}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)