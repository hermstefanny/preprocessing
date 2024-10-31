import json
import os
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv(override=True)


# MongoDB connection settings
mongo_uri = os.environ["DATABASE_URL"]  # Update if your MongoDB is hosted elsewhere
database_name = "cv_tech"      # Replace with your database name
collection_name = "Summary"  # Replace with your collection name

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client[database_name]
collection = db[collection_name]

# Fetch all documents in the collection
documents = list(collection.find({}))

# Convert MongoDB documents to a JSON-compatible format
for doc in documents:
    doc["_id"] = str(doc["_id"])  # Convert ObjectId to string

# Save to JSON file
output_file = "data\depecrated-ish\pilot_summary_data.json"
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(documents, file, indent=4, ensure_ascii=False)

print(f"Collection saved to {output_file}")
