from flask_app.config.mysqlconnection import connectToMySQL
DB = 'users_crud'

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name= data['first_name']
        self.last_name= data['last_name']
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
# Delete



# Vestigial below here
    @classmethod
    def save_burgers(cls,data):
        query = "INSERT INTO burgers (name,bun,meat,calories,created_at,updated_at) VALUES (%(name)s,%(bun)s,%(meat)s,%(calories)s,NOW(),NOW())"
        return connectToMySQL('burgers').query_db(query,data)

    @classmethod
    def get_all_burgers(cls):
        query = "SELECT * FROM burgers;"
        burgers_from_db =  connectToMySQL('burgers').query_db(query)
        burgers =[]
        for b in burgers_from_db:
            burgers.append(cls(b))
        return burgers

    @classmethod
    def get_one_burgers(cls,data):
        query = "SELECT * FROM burgers WHERE burgers.id = %(id)s;"
        burger_from_db = connectToMySQL('burgers').query_db(query,data)

        return cls(burger_from_db[0])

    @classmethod
    def update_burgers(cls,data):
        query = "UPDATE burgers SET name=%(name)s, bun=%(bun)s, meat=%(meat)s, calories=%(calories)s,updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('burgers').query_db(query,data)

    @classmethod
    def destroy_burgers(cls,data):
        query = "DELETE FROM burgers WHERE id = %(id)s;"
        return connectToMySQL('burgers').query_db(query,data)
