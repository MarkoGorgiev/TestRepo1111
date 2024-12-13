from pymongo.mongo_client import MongoClient


uri = "mongodb+srv://admin:admin@cluster0.agqtnax.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

print(client.list_database_names())
# db = client.test
db = client["test"]
# print(db)

# collection = db.product_list
collection = db["product_list"]
# print(collection)
print(collection.find_one())
print(type(collection.find_one()))
print(collection.find_one({"price": "10"}))

# print(collection.find({"price": "10"}))
# print(price_10_collenctions.explain())

price_10_collections = collection.find({"price": "10"})
for element in price_10_collections:
    print(element)

# print(collection.find({"name": "TEST_PRODUCT"}))

# collection.insert_one({"price": 1000000, "name": "Hello"})
# collection.insert_many([{"price": 1000000, "name": "Hello"}, {"price": 1000000, "name": "Hello"}])
collection.delete_one({"price": 1000000, "name": "Hello"})
