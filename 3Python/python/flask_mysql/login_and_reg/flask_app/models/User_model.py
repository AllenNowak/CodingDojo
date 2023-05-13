from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
TABLE = "users"

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.password  = data['password']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    def __repr__(self):
        return f'id:{self.id}, fn: {self.first_name}, ln: {self.last_name}, em: {self.email}, pw: {self.pw}'

# CRUD
# Create
    @classmethod
    def save(cls, data):
        query = f"""
            INSERT INTO {TABLE} (first_name,last_name, password, email) 
            VALUES (%(first_name)s,%(last_name)s,%(password)s,%(email)s)
            """
        # password already INSIDE the data dictionary better be hashed or we're doing it here
        return connectToMySQL(DB).query_db(query , data)
# Read
# Read by id
    @classmethod
    def get_by_id(cls, id):
        query = f"SELECT * FROM {TABLE} WHERE id = %(id)s;"
        users_from_db = connectToMySQL(DB).query_db(query, { 'id': id })
        user = users_from_db[0]
        return cls(user)

# Read by email
    @classmethod
    def get_by_email(cls, email):
        query = f"SELECT * FROM {TABLE} WHERE email = %(email)s;"
        users_from_db = connectToMySQL(DB).query_db(query, {'email': email})
        user = users_from_db[0]
        return cls(user)

# Helper function
    @classmethod
    def get_by_field_name(cls, data):
        if data.keys | len > 1:
            return 'I need to raise an exception or handle the multi-key select'
        for i in data:
            col = i
            val = data[i]
        query = f"SELECT * FROM {TABLE} WHERE {col} = %({col})s;"

        users_from_db = connectToMySQL(DB).query_db(query, data)
        user = users_from_db[0]
        return cls(user)
        



