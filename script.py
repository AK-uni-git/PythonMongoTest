import sys
from pymongo import MongoClient

if (len(sys.argv) > 1): 
        username = sys.argv[1]
else:
        username ="JokuPelle"

client = MongoClient('mongodb+srv://spend:wise@spendwisedata-gaqmj.mongodb.net/Datas')
print(client.database_names())
db = client['Datas']
print(db.collection_names())

collection = db.buymodels

for a in db.datamodels.find():
        print(a)
for user in collection.find( {'username': '{0}'.format(username)} ):
        print(int(user["ean"]) )
        for product in db.datamodels.find( {'ean': user["ean"] } ):
                print(product)
client.close()
