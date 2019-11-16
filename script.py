import sys
from pymongo import Connection


connection = Connection()
connection = Connection('localhost', 27017)
db = connection.testdb
collection = db.testcollection
for post in collection.find():
        print(post)
connection.close()

dataToSendBack = sys.argv[1] + "\n" + sys.version + "\n" 
print(dataToSendBack)
sys.stdout.flush()