import sys
from pymongo import MongoClient
client = MongoClient('mongodb+srv://spend:wise@spendwisedata-gaqmj.mongodb.net/Datas')



db = client.SpendWise
collection = db.Datas
for post in collection.find():
        print(post)
client.close()

dataToSendBack = sys.argv[1] + "\n" + sys.version + "\n" 
print(dataToSendBack)
sys.stdout.flush()