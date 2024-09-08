# from fastapi import FastAPI, BackgroundTasks
# from motor.motor_asyncio import AsyncIOMotorClient
# from pydantic import BaseModel
# import schedule
# import asyncio
# import time
# import tracemalloc 
# import threading

# class User(BaseModel):
#     name: str
#     age: int
#     job: str

# app = FastAPI()

# async def connect_to_mongodb():
#     client = AsyncIOMotorClient("mongodb+srv://yuvraj:yuvraj@cluster0.hhjiny0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#     return client["test_db"]

# @app.get("/")
# async def read_root():
#     return {"message": "Hello, World"}

# @app.get("/start")

# @app.post("/users/")
# async def create_user(user: User):
#     db = await connect_to_mongodb()
#     collection = db["users"]
#     result = await collection.insert_one(user.dict())
#     return {"inserted_id": str(result.inserted_id)}


# async def process_users_data():
#     db = await connect_to_mongodb()
#     users_collection = db["users"]
#     modified_data_collection = db["main_data"]
#     users=users_collection.find()
#     print("hello")
#     print(users)
#     async for user in users:
#         modified_user = {
#             "name": f"readed {user['name']}",
#             "age": f"readed {user['age']}",
#             "job": f"readed {user['job']}"
#         }
#         await modified_data_collection.insert_one(modified_user)
#     # return {"message": "all set"}



# # process_users_data()

# async def print_hi():
#     print("Hi")

# def run_print_hi():
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(process_users_data())# Schedule the job to run every second

# schedule.every(1).seconds.do(lambda: threading.Thread(target=run_print_hi).start())

# # Keep the script running so that scheduled jobs can execute
# while True:
#     schedule.run_pending()
#     time.sleep(1)









from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
import asyncio

class User(BaseModel):
    name: str
    age: int
    job: str

app = FastAPI()

async def connect_to_mongodb():
    client = AsyncIOMotorClient("mongodb+srv://yuvraj:yuvraj@cluster0.hhjiny0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    return client["test_db"]

@app.get("/")
async def read_root():
    return {"message": "Hello, World"}

@app.post("/users/")
async def create_user(user: User):
    db = await connect_to_mongodb()
    collection = db["users"]
    result = await collection.insert_one(user.dict())
    return {"inserted_id": str(result.inserted_id)}

async def process_users_data():
    db = await connect_to_mongodb()
    users_collection = db["users"]
    modified_data_collection = db["main_data4"]
    async for user in users_collection.find():
        modified_user = {
            "name": f"readed {user['name']}",
            "age": f"readed {user['age']}",
            "job": f"readed {user['job']}"
        }
        await modified_data_collection.insert_one(modified_user)
        print("hi")

async def schedule_task():
    while True:
        await asyncio.sleep(1)  # Sleep for 1 second
        await process_users_data()

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(schedule_task())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)




# schedule.every(1).seconds.do(process_users_data)
# while True:
#     tracemalloc.start()
#     schedule.run_pending()
#     time.sleep(1)

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
# async def scheduled_task():
#     while True:
#         await asyncio.sleep(1)
#         schedule.run_pending()

# async def main():
#     await asyncio.gather(
#         app(),
#         scheduled_task(),
#         process_users_data()
#     )

# if __name__ == "__main__":
#     asyncio.run(main())