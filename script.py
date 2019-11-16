import sys
from pymongo import MongoClient


client = MongoClient('mongodb+srv://spend:wise@spendwisedata-gaqmj.mongodb.net/Datas')
print(client.database_names())
db = client['Datas']
print(db.collection_names())

collection = db.datamodels

for post in collection.find():
        print(post + "\n")
client.close()
