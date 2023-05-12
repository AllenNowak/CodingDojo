from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja_model
from flask_app import DB
# DB = 'dojos_and_ninjas_schema'
TABLE = 'dojos'

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name= data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.ninjas = data['ninjas']

    def __repr__(self):
        return f'id:{self.id}, name: {self.name}, crt: {self.created_at}, upt: {self.updated_at}, ninjas: {self.ninjas}\n'

    # Should make this a static method
    # @classmethod
    # def prnt(data):
    #     print('\n'*3 + '-'*10)
    #     print(data)
    #     print('-'*10 + '\n'*3)

# CRUD
# Create
    # @classmethod
    def create(cls, data):
        query = f"""
            INSERT INTO {TABLE} (name) VALUES (%(name)s)
            """
        return connectToMySQL(DB).query_db(query , data)
# Read
    
# Read 1
    @classmethod
    def read_one(cls, id):
        # query = f"SELECT * FROM {TABLE} WHERE id = %(id)s;"
        query = f"""
                    SELECT * 
                    FROM {TABLE}
                    JOIN ninjas
                    ON {TABLE}.id = ninjas.dojo_id
                    WHERE {TABLE}.id = %(id)s
                ;"""

        data = { 'id': id }
        rows_from_db = connectToMySQL(DB).query_db(query, data)

        if not rows_from_db:
            return rows_from_db

        dojo = cls(rows_from_db[0])

        # ninjas = []
        # dict = {
        #     'id' : dojo['id'],
        #     'name' : dojo['name'],
        #     'created_at' : dojo['created_at'],
        #     'updated_at' : dojo['updated_at'],
        #     'ninjas' : ninjas
        # }

        # # I should handle the case where there is no dojo returned (eg user navigated to the url w/ an invalid id)
        # one_dojo = cls(dict)


        ninja_list = []
        for one_row in rows_from_db:
            if one_row == None:
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
        # print("\n\n\n" + "-"*10)
        # print(f'The ninjas list is: {ninja_list}')
        # dict['ninjas'] = ninja_list
        # print(f'The full dict is: {dict}')
        # print("-"*10 + "\n\n\n")
        
        return dojo

# Read all
    @classmethod
    def read_all(cls):
        query = f"""SELECT * FROM {TABLE};"""
        data = { 'table': TABLE }
        rows_from_db = connectToMySQL(DB).query_db(query, data)

        if not rows_from_db: 
            rows_from_db = [] 

        return rows_from_db

