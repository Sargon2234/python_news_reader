from pymongo import MongoClient


class Database:
    def __init__(self, address, port):
        self.client = MongoClient(address, port)

    def buildConnection(self, database):
        self.db = self.client[database]

    def getData(self, collection, data):
        return self.db[collection].find_one(data)

    def insertData(self, collection, data):
        result = self.db[collection].insert_one(data)
        return result.inserted_id

    def insertBulk(self, collection, data):
        result = self.db[collection].insert_many(data)
        return result.inserted_ids
