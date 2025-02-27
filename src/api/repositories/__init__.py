from pymongo import MongoClient
from models import Objective

class ObjectiveRepository:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['skillsaga']
        self.collection = self.db['objectives']

    def add(self, objective):
        self.collection.insert_one(objective)

    def delete(self, objective_id):
        self.collection.delete_one({' _id': objective_id})

    def get_all(self):
        items : Objective = []
        cursor = self.collection.find()
        for item in cursor:
            items.append(Objective(item['name'], item['position']))
        return items
    
    def get_by_id(self, objective_id):
        return self.collection.find_one({'_id': objective_id})
    
    def update(self, objective_id, objective):
        self.collection.update_one({'_id': objective_id}, {'$set': objective})

    def sort(self):
        return self.collection.find().sort('position', 1)