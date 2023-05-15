from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DB
TABLE = "recipes"


class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions  = data['instructions']
        self.date_cooked = data['date_cooked']
        self.under_30 = data['under_30']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    def __repr__(self):
        return f'id:{self.id}, nm: {self.name}, dt: {self.date_cooked}, 30: {self.under_30}, uid: {self.user_id}'

# ----------------------------------------------------  Create
    @classmethod
    def save(cls, data):
        query = f"""
            INSERT INTO {TABLE} 
            (name, description, instructions, date_cooked, under_30, user_id)
            VALUES 
            ( %(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_30)s, %(user_id)s );
            ;"""
        
        print(data)
        print('rg in data?: ', data['radio_group'])
        print('rg is on? ', (data['radio_group'] == 'on'))
        if('radio_group' in data and data['radio_group'] == 'on'):
            sub30 = True
            print("found bool to be true")
        else:
            sub30 = False
            print("bool check failed")
        # sub30 = True if ('radio_group' in data and data['radio_group'] == 'on') else False

        data['under_30'] = sub30

        return connectToMySQL(DB).query_db(query, data)

# ----------------------------------------------------  Read
# Read by email
    @classmethod
    def get_all(cls):
        query = f"""
        SELECT u.first_name as chef, t.*  FROM {TABLE} t 
        JOIN users u ON t.user_id = u.id 
        ;"""
        results = connectToMySQL(DB).query_db(query)
 
        if not results or len(results) == 0 :
            return None
        
        # For each row in results, build a recipe instance and tack on it's chef's name as done in get_by_id
        # return the list of results

        return results

    @classmethod
    def get_by_id(cls, data):
        # query = f"SELECT * FROM {TABLE} WHERE id = %(id)s;"
        query = f"""SELECT r.*, u.first_name as chef 
                FROM {TABLE} r
                JOIN users u 
                ON u.id = r.user_id
                WHERE r.id = %(id)s
            ;"""

        row = connectToMySQL(DB).query_db(query, data)

        if not row:
            return False
        
        recipe = cls(row[0])
        recipe.chef = row[0]['chef']

        return recipe
    
    @classmethod
    def get_by_user(cls, data):
        # id = data['id']
        query = f"SELECT * FROM {TABLE} WHERE id = %(id)s;"
        row = connectToMySQL(DB).query_db(query, data)

        if not row:
            return False

        return cls(row[0])
    





# ----------------------------------------------------  Update


# ----------------------------------------------------  Delete



# ----------------------------------------------------  Validate
    @staticmethod
    def validate(data):
        # TODO: Implement validation
        return True


