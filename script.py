import sys
from pymongo import MongoClient
client = MongoClient('mongodb+srv://spend:wise@spendwisedata-gaqmj.mongodb.net/Datas')



db = client.SpendWise
collection = db.Datas
for post in collection.find():
        print(post)
client.close()
