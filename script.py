import sys
from pymongo import MongoClient
client = MongoClient('mongodb+srv://spend:wise@spendwisedata-gaqmj.mongodb.net/Datas')



db = client.Datas
print(db)
collection = db.DataModels
print(collection)
for post in collection.find():
        print(post)
client.close()
