from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
# DB = 'dojos_and_ninjas_schema'
TABLE = 'dojos'

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name= data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    def __repr__(self):
        return f'id:{self.id}, name: {self.name}, crt: {self.created_at}, upt: {self.updated_at}, ninjas: {self.ninjas}\n'

# CRUD
# Create
    @classmethod
    def create(cls, data):
        query = f"""
            INSERT INTO {TABLE} (name) VALUES (%(name)s)
            """
        return connectToMySQL(DB).query_db(query , data)
# Read
    
# Read 1
    @classmethod
    def read_one(cls, id):
        query = f"SELECT * FROM {TABLE} WHERE id = %(id)s;"
        data = { 'id': id }
        rows_from_db = connectToMySQL(DB).query_db(query, data)
        row = rows_from_db[0]
        ninjas = []
        dict = {
            'id' : row['id'],
            'name' : row['name'],
            'created_at' : row['created_at'],
            'updated_at' : row['updated_at'],
            'ninjas' : ninjas
        }
        # change the query to a join query, then walk its records to reconstruct the list of ninjas in this dojo
        
        # I should handle the case where there is no dojo returned (eg user navigated to the url w/ an invalid id)
        one_dojo = cls(dict)
        return one_dojo

# Read all
    @classmethod
    def read_all(cls):
        query = f"""SELECT * FROM {TABLE};"""
        data = { 'table': TABLE }
        rows_from_db = connectToMySQL(DB).query_db(query, data)

        if not rows_from_db: 
            rows_from_db = [] 

        return rows_from_db

