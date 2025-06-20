from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.autofilterbot

def save_file(file_id, caption, keywords):
    db.files.insert_one({
        "file_id": file_id,
        "caption": caption,
        "keywords": [kw.strip().lower() for kw in keywords]
    })

def search_files(query):
    return list(db.files.find({"keywords": query.lower()}))
