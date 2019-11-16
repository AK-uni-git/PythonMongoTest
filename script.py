import sys
from pymongo import MongoClient


client = MongoClient('mongodb+srv://spend:wise@spendwisedata-gaqmj.mongodb.net/Datas')
print(client.database_names())
db = client['Datas']
print(db.collection_names())
print(db)
collection = db.DataModels
print(collection)
for post in collection.find():
        print(post)
client.close()
