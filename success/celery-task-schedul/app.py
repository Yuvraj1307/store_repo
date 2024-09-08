from flask import Flask, jsonify, request
from task import transfer_data
from task import db
# Initialize Flask application
app = Flask(__name__)

@app.route("/insert",methods=["POST"])
def add_data():
    print(request.json)
    collection_a = db['collection_A']
    print(list(collection_a.find()))
    collection_a.insert_one(request.json)
    return {"message": "Added data"}

# Define a route to schedule the Celery task
@app.route('/schedule_transfer_data', methods=['POST'])
def schedule_transfer_data():
    # You can receive any data needed to trigger the task
    # For example, you could receive parameters in the request
    # and pass them to the Celery task
    transfer_data.apply_async()

    return jsonify({"message": "Data transfer task scheduled"}), 200

if __name__ == '__main__':
    app.run(debug=True)
