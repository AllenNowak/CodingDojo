from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DB
TABLE = "sightings"


class Sighting:
    def __init__(self,data):
        self.id = data['id']
        self.location = data['location']
        self.description = data['description']
        self.date = data['date']
        self.how_many = data['how_many']
        self.reported_by_id = data['reported_by_id']
        self.reported_by_name = data['reported_by_name']
        self.reporter = None                    # User Instance?
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    def __repr__(self):
        return f'id:{self.id}, loc: {self.location}, dscr: {self.description}, dt: {self.date}, num: {self.how_many}, uid: {self.reported_by_id}, unm: {self.reported_by_name}'


# CURD

# ----------------------------------------------------  Create
    @classmethod
    def save(cls, data):
        query = f"""
            INSERT INTO {TABLE} 
            (location, description, date, how_many, user_id)
            VALUES 
            ( %(location)s, %(description)s, %(date)s, %(how_many)s, %(reported_by_id)s );
            ;"""
        
        # print(data)

        return connectToMySQL(DB).query_db(query, data)
    
# ----------------------------------------------------  Update
    @classmethod
    def update(cls, data):
        query_perhaps = f"""
                UPDATE {TABLE} 
                SET location = %(location)s, 
                    description = %(description)s,
                    date = %(date)s,
                    user_id = %(reported_by_id)s,
                    how_many = %(how_many)s
                WHERE id = %(id)s
            ;"""
        
        # Rreporter's id seems to be immutable post creation
        query = f"""
                UPDATE {TABLE} 
                SET location = %(location)s, 
                    description = %(description)s,
                    date = %(date)s,
                    how_many = %(how_many)s
                WHERE id = %(id)s
            ;"""
        
        return connectToMySQL(DB).query_db(query, data)
    


# ----------------------------------------------------  Read
    @classmethod
    def get_all(cls):
        query = f"""
        SELECT  concat(u.first_name, ' ', u.last_name) as reported_by_name, 
                u.id as reported_by_id, 
                t.*  
        FROM {TABLE} t 
        JOIN users u ON t.user_id = u.id 
        ;"""

        results = connectToMySQL(DB).query_db(query)
 
        print(results)

        if not results or len(results) == 0 :
            return None
        
        sightings = []
        for row in results:
            instance = cls(row)
            instance.reporter = None    # Why create a full user for a read-only property? It's easy enough to do, but wasteful
            sightings.append(instance)

        # For each row in results, build a sighting instance and tack on it's chef's name as done in get_by_id
        # return the list of sightings

        return sightings

    @classmethod
    def get_by_sighting_id(cls, data):
        print('Getting one by id:', data)
        # query = f"SELECT * FROM {TABLE} WHERE id = %(id)s;"
        query = f"""SELECT 
                s.*, 
                concat(u.first_name, ' ', u.last_name) as reported_by_name, 
                u.id as reported_by_id 
                FROM {TABLE} s
                JOIN users u 
                ON u.id = s.user_id
                WHERE s.id = %(id)s
            ;"""

        row = connectToMySQL(DB).query_db(query, data)
        print('Row from db resultset is: ', row)

        if not row:
            print('Row was empty')
            return False
        
        sighting = cls(row[0])
        print(sighting)
        return sighting
        # return cls (row[0])

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
            Req'd Fields: location, description, date, how_many, user_id
        """
        print('\n\n\n\n-----------------> valdate(data): \n', data)
        # -------------- User must be logged in --------------
        # ----------------- Required Fields  -----------------  
        # All fields required
        # ---------------  Minimum len Fields ----------------
        # Name, description & instructions must be >= len 3
        # --------------  Name  --------------  
        if len( data['location'] ) < 1:
            flash( 'Location is required', 'location')
            is_valid = False

        if len( data['description'] ) < 1:
            flash( 'Description is required', 'description')
            is_valid = False

        # ----------------  How Many  -------------------
        if 'how_many' not in data:
            flash( 'Number of Sasquatches is required', 'how_many')
            is_valid = False
        elif len( data['how_many'] ) < 1:
            flash( 'Number of Sasquatches is required', 'how_many')
            is_valid = False
        # ----------------  Require Date -------------------
        if 'date' not in data:
            flash( 'Date sighting was made is required', 'date')
            is_valid = False
        elif len( data['date'] ) < 1:
            flash( 'Date sighting was made is required', 'date')
            is_valid = False
        
        return is_valid


