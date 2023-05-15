from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja_model
from flask_app import DB
TABLE = 'dojos'

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name= data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.ninjas = data['ninjas']          # Spencer's version appended the attribute dynamically

    # def __repr__(self):
    #     return f'id:{self.id}, name: {self.name}, crt: {self.created_at}, upt: {self.updated_at}, ninjas: {self.ninjas}\n'

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
        query = f"""
                    SELECT * 
                    FROM {TABLE}
                    LEFT JOIN ninjas
                    ON {TABLE}.id = ninjas.dojo_id
                    WHERE {TABLE}.id = %(id)s
                ;"""

        data = { 'id': id }
        rows_from_db = connectToMySQL(DB).query_db(query, data)

        if not rows_from_db:
            return rows_from_db

        dojo = cls(rows_from_db[0])

        ninja_list = []
        for one_row in rows_from_db:
            # Referencing the key []'ninjas.id'] == None
            # Was the trick to NOT displaying None None None for the columns on the Show Dojo page
            if one_row['ninjas.id'] == None:
                return dojo
             
            ninja_dict = {
                'id' : one_row['ninjas.id'],
                'first_name' : one_row['first_name'],
                'last_name' : one_row['last_name'],
                'age' : one_row['age'],
                'created_at' : one_row['ninjas.created_at'],
                'updated_at' : one_row['ninjas.updated_at'],
            }
            instance = ninja_model.Ninja(ninja_dict)
            ninja_list.append(instance)

        dojo.ninjas = ninja_list
        
        return dojo

# Read all
    @classmethod
    def read_all(cls):
        query = f"""SELECT * FROM {TABLE};"""
        data = { 'table': TABLE }
        rows_from_db = connectToMySQL(DB).query_db(query, data)
        # send back objects not rows
        dojos = []

        if not rows_from_db: 
            return dojos 
        for one_row in rows_from_db:
            dojos.append( cls(one_row ))

        # Q for Spencer: do these need to be Objects?
        return dojos

