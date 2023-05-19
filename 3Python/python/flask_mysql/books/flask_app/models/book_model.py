from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DB
from flask_app.utilities import util
TABLE = "books"


class Book:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    def __repr__(self):
        return f'id:{self.id}, tl: {self.title}, num: {self.num_of_pages}'

# ----------------------------------------------------  Create
    @classmethod
    def save(cls, data):
        query = f"""
            INSERT INTO {TABLE} 
            (title, num_of_pages)
            VALUES 
            ( %(title)s, %(num_of_pages)s );
            ;"""
        
        return connectToMySQL(DB).query_db(query, data)
    
# ----------------------------------------------------  Get All Favorites
    # get books with favorites?
    @classmethod
    def get_all_books_favorited_by_author():
        """
            SELECT * FROM books b 
            LEFT JOIN favorites f ON b.id = f.book_id
            LEFT JOIN authors a ON f.author_id = a.id 
            WHERE b.id = 1;
        """
        # TODO: Implement this fully
        pass
    @classmethod
    def get_all_books(cls):
        query = """
            SELECT * FROM books
        """
        row = connectToMySQL(DB).query_db(query)
        if not row:
            return False

        return cls(row[0])        

    @classmethod
    def get_by_id(cls, data):
        query = f"""SELECT *
                FROM {TABLE}
                WHERE id = %(id)s
            ;"""

        row = connectToMySQL(DB).query_db(query, data)
        if not row:
            return False

        return cls(row[0])        
        # instance = cls(row[0])
        # return instance
    

