from pymongo import MongoClient

MONGO_URI = "mongodb+srv://Vivek:Motabhai242@vivek.jv7ju.mongodb.net/notes?retryWrites=true&w=majority"

con = MongoClient(MONGO_URI)