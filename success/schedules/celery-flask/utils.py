from pymongo import MongoClient

# from motor.motor_asyncio import AsyncIOMotorClient


def some_async_operation():
    try:
        client = MongoClient('mongodb+srv://yuvraj:yuvraj@cluster0.hhjiny0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        # client = AsyncIOMotorClient('<mongo_connection_string>')
        db = client['celerydatabase']
        collection_a = db['collection_A']
        print("collection_A")
        collection_b = db['collection_C']
        print("collection_B")

        for document in collection_a.find():
             print(document)
             collection_b.insert_one(document)

        return 'Copy completed successfully'
    except Exception as e:
        return f'Error during copy: {str(e)}'
    finally:
        client.close()
