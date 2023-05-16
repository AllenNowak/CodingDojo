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
        print('rg in data?: ', data['under_30'])
        print('rg is on? ', (data['under_30'] == 'on'))
        if('under_30' in data and data['under_30'] == 'True'):
            sub30 = True
            print("found bool to be true")
        else:
            sub30 = False
            print("bool check failed")
        # sub30 = True if ('under_30' in data and data['under_30'] == 'on') else False

        data['under_30'] = sub30

        return connectToMySQL(DB).query_db(query, data)
    
# ----------------------------------------------------  Update
    @classmethod
    def update(cls, data):
        if('under_30' in data and data['under_30'] == 'True'):
            sub30 = True
        else:
            sub30 = False

        data['under_30'] = sub30

        query = f"""
                UPDATE {TABLE} 
                SET name = %(name)s, 
                    description = %(description)s,
                    instructions = %(instructions)s,
                    date_cooked = %(date_cooked)s,
                    under_30 = %(under_30)s
                WHERE id = %(id)s
            ;"""
        
        # data['under_30'] = sub30
        
        return connectToMySQL(DB).query_db(query, data)
    
    





    # @classmethod
    # def save(cls, data):
    #     query = f"""
    #         INSERT INTO {TABLE} 
    #         (name, description, instructions, date_cooked, under_30, user_id)
    #         VALUES 
    #         ( %(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_30)s, %(user_id)s );
    #         ;"""
        
    #     print(data)
    #     print('rg in data?: ', data['under_30'])
    #     print('rg is on? ', (data['under_30'] == 'on'))
    #     if('under_30' in data and data['under_30'] == 'True'):
    #         sub30 = True
    #         print("found bool to be true")
    #     else:
    #         sub30 = False
    #         print("bool check failed")
    #     # sub30 = True if ('under_30' in data and data['under_30'] == 'on') else False

    #     data['under_30'] = sub30

    #     return connectToMySQL(DB).query_db(query, data)
    
    




# ----------------------------------------------------  Read
# Read by email
    @classmethod
    def get_all(cls):
        query = f"""
        SELECT u.first_name as chef, t.*  FROM {TABLE} t 
        JOIN users u ON t.user_id = u.id 
        ;"""
        results = connectToMySQL(DB).query_db(query)
 
        print(results)

        if not results or len(results) == 0 :
            return None
        recipes = []
        for row in results:
            one_recipe = cls(row)
            one_recipe.chef = row['chef']
            recipes.append (one_recipe)
        # For each row in results, build a recipe instance and tack on it's chef's name as done in get_by_id
        # return the list of results

        return recipes

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
    

# ----------------------------------------------------  Delete

    @classmethod
    def delete(cls,data):
        query = f"""DELETE FROM {TABLE} WHERE id = %(id)s;"""
        return connectToMySQL(DB).query_db(query, data)

# ----------------------------------------------------  Validate
    @staticmethod
    def validate(data):
        is_valid = True
        """
            Fields: user_id, name, description, instructions, date_cooked, under_30
        """
        print('\n\n\n\n-----------------> valdate(data): \n', data)
        # -------------- User must be logged in --------------
        # ----------------- Required Fields  -----------------  
        # All fields required
        # ---------------  Minimum len Fields ----------------
        # Name, description & instructions must be >= len 3
        # --------------  Name  --------------  
        if len( data['name'] ) < 1:
            flash( 'Recipe name is required', 'name')
            is_valid = False
        elif len( data['name'] ) < 3:
            flash( 'Recipe name must be at least 3 characters long', 'name')
            is_valid = False

        if len( data['description'] ) < 1:
            flash( 'Recipe description is required', 'description')
            is_valid = False
        elif len( data['description'] ) < 3:
            flash( 'Recipe description must be at least 3 characters long', 'description')
            is_valid = False

        if len( data['instructions'] ) < 1:
            flash( 'Recipe instructions are required', 'instructions')
            is_valid = False
        elif len( data['instructions'] ) < 3:
            flash( 'Recipe instructions must be at least 3 characters long', 'instructions')
            is_valid = False
        
        # ----------------  Require Date -------------------
        if 'date_cooked' not in data:
            flash( 'Date recipe was made is required', 'date_cooked')
            is_valid = False
        elif len( data['date_cooked'] ) < 1:
            flash( 'Date recipe was cooked is required', 'date_cooked')
            is_valid = False
        
        # ----------------  Require Under30 ----------------
        if 'under_30' not in data:
            flash( 'Preparation time is required', 'under_30')
            is_valid = False

        return is_valid


