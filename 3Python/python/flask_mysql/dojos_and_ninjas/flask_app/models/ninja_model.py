from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB

# Trying to make it easier to copy/past CRUD queries from this model into 
# a future implementation w fewer freplacements, this isn't perfect tho when JOINing
TABLE = 'ninjas'        

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name= data['first_name']
        self.last_name= data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # include the dojo_id field
    def __repr__(self):
        return f'id:{self.id}, fname: {self.first_name}, lname: {self.last_name}, crt: {self.created_at}, upt: {self.updated_at}'

# CRUD
# Create
    @classmethod
    def create(cls, data):
        query = f"""
            INSERT INTO {TABLE} (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s )
            """
        return connectToMySQL(DB).query_db(query , data)
# Read
# Read all
    @classmethod
    def read_all(cls):
        query = f"""SELECT * FROM {TABLE};"""
        rows_from_db = connectToMySQL(DB).query_db(query)
        rows =[]
        for one_row in rows_from_db:
            rows.append(cls(one_row))

        return rows
    
# Read 1
    @classmethod
    def read_one(cls, id):
        query = "SELECT * FROM {TABLE} WHERE id = %(id)s;"
        data = { 'id': id }
        rows_from_db = connectToMySQL(DB).query_db(query, data)
        row = rows_from_db[0]

        return cls(row)


# Unused, what are you doing here?  Nothing to see. Move along.
# Update
    @classmethod
    def update(cls, data):
        # data.table = TABLE
        query = f"""
            UPDATE {TABLE} SET 
            first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
            WHERE id = %(id)s;
            """
        return connectToMySQL(DB).query_db(query , data)

# Delete
    @classmethod
    def delete_by_id(cls,id):
        data = { 'id': id }
        query = "DELETE FROM {TABLE}  WHERE id = %(id)s;"
        print('\n'*2 + '-'*20)
        print(f'\nTrying to Destroy record.\nQuery:')
        print(data)
        print('-'*20 + '\n'*2)
        
        return connectToMySQL(DB).query_db(query,data)

