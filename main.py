import bot
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']
MONGO_ID = os.environ['MONGO_ID']

if __name__ == "__main__":
    try:
        client = MongoClient('hostname', 27017)
        print("Connected to DB")
        bot.run_bot()

    except Exception:
        print("Could not connect to MongoDB")
