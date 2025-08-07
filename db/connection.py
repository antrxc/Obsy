'''
Loads .env.
Creates a single MongoClient instance (singleton pattern).
Defines and exposes:
client
db = client["aXtr-Logs"]
UserData = db["User-table"]
ProjectData = db["Project-Table"]
ClockData = db["Clock-Logs"]
'''

from dotenv import load_dotenv
from pymongo import MongoClient
import os 

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise ValueError("MONGO_URI not found and thus can't connect to db")

try:
    client = MongoClient(MONGO_URI)
    client.admin.command('ping')
    
    db = client["aXtr-Logs"]
    UserData = db["User-Table"]
    ProjectData = db["Project-Table"]
    ClockData = db["Clock-Logs"]
except Exception as e:
    raise ConnectionError(f"Failed to connect to MongoDB: {e}")

