from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# from flask_bcrypt import Bcrypt        
# bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
#                          # which is made by invoking the function Bcrypt with our app as an argument

from flask_app import DB
TABLE = "users"

import re
ALPHAONLY = re.compile(r"^[a-zA-Z]+$")
ALPHANUMERIC = re.compile(r"^[a-zA-Z0-9]+$")
# Attribution: https://uibakery.io/regex-library/email-regex-python
ISVALIDEMAIL = re.compile(r"^\S+@\S+\.\S+$")
# Password regex Based upon
# Attribution: https://stackoverflow.com/questions/46582497/python-regex-for-password-validation
# Attribution: https://www.geeksforgeeks.org/password-validation-in-python/
ISVALIDPASSWORD = re.compile(r"^(?=.*[\d])(?=.*[a-z])(?=.*[A-Z])[A-Za-z\d]{8,20}$")

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
        return f'id:{self.id}, fn: {self.first_name}, ln: {self.last_name}, em: {self.email}, pw: {self.password}'

# CRUD
# Create
    @classmethod
    def save(cls, data):
        query = f"""
            INSERT INTO {TABLE} (first_name,last_name, password, email) 
            VALUES (%(first_name)s,%(last_name)s,%(password)s,%(email)s)
            """

        return connectToMySQL(DB).query_db(query , data)

# Read
# Read by id
    @classmethod
    def get_by_id(cls, id):
        query = f"SELECT * FROM {TABLE} WHERE id = %(id)s;"
        row = connectToMySQL(DB).query_db(query, { 'id': id })

        if not row:
            return False

        return cls(row[0])

# Read by email
    @classmethod
    def get_by_email(cls, data):
        query = f"SELECT * FROM {TABLE} WHERE email = %(email)s;"
        results = connectToMySQL(DB).query_db(query, data)
 
        if not results or len(results) == 0 :
            return None
        
        user = results[0]
        return cls(user)

    # TODO: Maybe implement helper function to modularize simple queries 

    @classmethod
    def get_by_field_name(cls, data):
        if data.keys | len > 1:
            return 'I need to raise an exception or handle multi-key select'
        for i in data:
            col = i
            val = data[i]
        query = f"SELECT * FROM {TABLE} WHERE {col} = %({col})s;"

        users_from_db = connectToMySQL(DB).query_db(query, data)
        user = users_from_db[0]
        return cls(user)
        
# ----------------------   Validations   ----------------------
    @staticmethod
    def validate_registration(data):
        already_registered_user = User.get_by_email({'email' : data['email']})
        print(f'Found user: {already_registered_user}')
        print(f'From request form data: {data}')
        is_valid = True

        # --------------  Required Fields  --------------  
        # This is here w/ the intention of possibly building out helper methods
        # Build a dict of Validation Rules 
        # { 'field' : field_name, 'Display' : 'display_name', 'group' : 'error_group', 'rules' : [REQUIRED, MINLEN, MAXLEN, EMAIL, etc]}
        # 
        required_fields = [
            {'first_name': 'First name'},
            {'last_name': 'Last name'},
            {'email': 'email'},
            {'password': 'Password'},
            {'confirm_pass': 'Password'}
            ]

        # --------------  First Name  --------------  data
        if len( data["first_name"] ) < 1:
            flash("First name required", "first_name")
            is_valid = False
        elif len( data["first_name"] ) < 3:
            flash("First name must be at least 3 characters", "first_name")
            is_valid = False
        elif not ALPHAONLY.match(data['first_name']):
            flash("Name can only contain letters from the alphabet", "first_name")
            is_valid = False

        # --------------  Last Name  --------------  
        if len( data["last_name"] ) < 1:
            flash("Last name required", "last_name")
            is_valid = False
        elif len( data["last_name"] ) < 3:
            flash("Last name must be at least 3 characters", "last_name")
            is_valid = False
        elif not ALPHAONLY.match(data['last_name']):
            flash("Name can only contain letters from the alphabet", "last_name")
            is_valid = False

        # --------------  Email  --------------  
        if len( data['email'] ) < 1:
            flash("Email required", "email")
            is_valid = False
        # --------------  Email in valid format  --------------  
        elif not ISVALIDEMAIL.match(data['email']):
            flash("Invalid email address", "email")
            is_valid = False
        # --------------  Email not previously registered  --------------  
        else:
            print('Verifying email conflicts')
            is_conflicted = User.get_by_email({'email' : data['email']})
            if is_conflicted:
                flash("Invalid email address: Address already registered.", "email")
                is_valid = False

        # --------------  Password lengths  --------------  
        if len( data["password"] ) < 1:
            flash("Password required", "password")
            is_valid = False
        # elif len( data['password'] ) < 8:
        #     flash("Password must be at least 8 characters", "password")
        #     is_valid = False
        elif len( data['password'] ) > 20:
            flash("Password must not exceed 20 characters", "password")
            is_valid = False

        # REDUNDANT
        # if len( data['confirm_pass'] ) < 1:
        #     flash("Password confirmation required", "confirm_pass")
        #     is_valid = False
        # elif len( data['confirm_pass'] ) < 8:
        #     flash("Password must be at least 8 characters", "confirm_pass")
        #     is_valid = False

        # --------------  Password === Confirmed PW --------------  
        if data['password'] != data['confirm_pass']:
            flash("Passwords must be identical", "password")
            # flash("Passwords must be identical", "confirm_pass") # Desired IFF providing error feedback paired to the specific input?
            is_valid = False

        # --------------  Ninja Bonus: Password  --------------  
        if not ISVALIDPASSWORD.match(data['password']):
            flash("Password requires at least one lowercase & uppercase letter & a digit", "password")
            is_valid = False

        return is_valid

