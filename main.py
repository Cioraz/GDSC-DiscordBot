# Main file to run the bot
# Importing the required libraries
import bot
from dotenv import load_dotenv
from pymongo import MongoClient
import os

# Loading the environment variables
load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

# Main function to run the bot
if __name__ == "__main__":
    try:
        db_connection = MongoClient(MONGODB_URI)
        print("Connected to DB")
        db = db_connection["GDSC_Bot"]
        bot.run_bot(db)

    except Exception as e:
        print(e)
        print("Could not connect to MongoDB")
