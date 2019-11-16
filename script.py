import sys
from pymongo import MongoClient
import datetime

class Product:
        def __init__(self, name, purchaseDate, price, usage):
                self.name = name
                self.purchaseDate = purchaseDate
                self.price = price
                self.usage = usage
                print(datetime.datetime.now() - purchaseDate)

        def __str__(self):
                return("name {0}\ndate {1}\nprice {2}\nusage {3}".format(self.name, self.purchaseDate, self.price, self.usage))


products = []

if (len(sys.argv) > 1): 
        username = sys.argv[1]
else:
        username ="JokuPelle"

client = MongoClient('mongodb+srv://spend:wise@spendwisedata-gaqmj.mongodb.net/Datas')
print(client.database_names())
db = client['Datas']
print(db.collection_names())

collection = db.buymodels


for user in collection.find( {'username': '{0}'.format(username)} ):
        print(user)
        for product in db.datamodels.find( {'ean': user["ean"] } ):
                print(product)
                products.append(Product(product["name"], user["buydate"], product["price"], product["usage"]))

#debug
for product in products:
        print(product)
        print()
client.close()
