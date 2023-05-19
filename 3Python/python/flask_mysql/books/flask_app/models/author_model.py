from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import DB
from flask_app.utilities import util
TABLE = "authors"


class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    def __repr__(self):
        return f'id:{self.id}, nm: {self.name}'

# Create
    @classmethod
    def save(cls, data):
        query = f"""
            INSERT INTO {TABLE} (name) VALUES (%(name)s);
            """

        return connectToMySQL(DB).query_db(query , data)

# Read
    @classmethod
    def get_by_id(cls, id):
        query = f"SELECT * FROM {TABLE} WHERE id = %(id)s;"
        row = connectToMySQL(DB).query_db(query, { 'id': id })

        if not row:
            return False

        return cls(row[0])
    
    @classmethod
    def get_all_favorites_by_authors():
        pass

    @classmethod
    def get_all(cls):
        print('\n\n\n\n\n Tryinna call callout ---------------------')
        util.callout("testing callout in author model")
        query = f"SELECT * FROM {TABLE};"

        rows = connectToMySQL(DB).query_db(query)
        if not rows or len(rows) == 0 :
            return False
        
        authors = []
        for row in rows:
            author = cls(row)
            authors.append(author)

        return authors
        
