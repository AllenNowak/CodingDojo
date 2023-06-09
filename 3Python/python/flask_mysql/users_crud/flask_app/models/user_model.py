from flask_app.config.mysqlconnection import connectToMySQL
DB = 'users_crud'

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name= data['first_name']
        self.last_name= data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    def __repr__(self):
        return f'id:{self.id}, fn: {self.first_name}, ln: {self.last_name}, crt: {self.created_at}, upt: {self.updated_at}'

# CRUD
# Create
    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO users (first_name,last_name,email) 
            VALUES (%(first_name)s,%(last_name)s,%(email)s)
            """
        return connectToMySQL(DB).query_db(query , data)
# Read
# Read 1
# Read all
    @classmethod
    def read_all(cls):
        query = "SELECT * FROM users;"
        users_from_db =  connectToMySQL(DB).query_db(query)
        users =[]
        for u in users_from_db:
            users.append(cls(u))
        # print('\n'*2 + users + '\n'*2)
        # print('='*10)
        return users
    
# for comparison
    @classmethod
    def get_user_by_id(cls, id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = { 'id': id }
        users_from_db = connectToMySQL(DB).query_db(query, data)
        user = users_from_db[0]
        return user

# Update
    @classmethod
    def update(cls, data):
        query = """
            UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
            WHERE id = %(id)s;
            """
        return connectToMySQL(DB).query_db(query , data)

# Delete
    @classmethod
    def destroy_user_by_id(cls,id):
        data = { 'id': id }
        query = "DELETE FROM users WHERE id = %(id)s;"
        print('\n'*2 + '-'*20)
        print(f'\nTrying to Destroy user.\nQuery:')
        print(data)
        print('-'*20 + '\n'*2)
        # print(query + f'id: {data["id"]}\n\n')
        return connectToMySQL(DB).query_db(query,data)

