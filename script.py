import sys
from pymongo import MongoClient
client = MongoClient('mongodb+srv://spend:wise@spendwisedata-gaqmj.mongodb.net/Datas')



db = client.SpendWise
print(db)
collection = db.Datas
print(collection)
for post in collection.find():
        print(post)
client.close()
