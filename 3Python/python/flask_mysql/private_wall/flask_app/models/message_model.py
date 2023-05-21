from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DB
from flask_app.models import user_model
TABLE = "messages"


class Message:
    def __init__(self,data):
        self.id = data['id']
        self.sender_id = data['sender_id']
        self.receiver_id = data['receiver_id']
        self.message = data['message']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    def __repr__(self):
        return f'id:{self.id}, s_id: {self.sender_id}, r_ic: {self.receiver_id}, msg: {self.message}'


# CURD

# ----------------------------------------------------  Create
    @classmethod
    def save(cls, data):
        query = f"""
            INSERT INTO {TABLE} 
            (sender_id, receiver_id, message)
            VALUES 
            ( %(sender_id)s,  %(receiver_id)s,  %(message)s);
            ;"""
        
        print('Saving data: ', data)

        return connectToMySQL(DB).query_db(query, data)
# ----------------------------------------------------  Read
    @classmethod
    # Current user's outbox length
    def get_sent_message_count_for_user(cls, data):
        # print('Data is : ', data)
        query = f"""
            SELECT COUNT(*) as count FROM {TABLE} t
            WHERE t.sender_id = %(id)s
        ;"""
        result = connectToMySQL(DB).query_db(query, data)[0]
        return result['count']


    @classmethod
    # Current user's inbox
    def get_all_by_recipient_id(cls, data):
        print('Data is : ', data)
        query = f"""
            SELECT t.*, receiver.*, sender.* FROM {TABLE} t
            JOIN users AS receiver 
            ON receiver.id = t.receiver_id
            JOIN users AS sender
            ON sender.id = t.sender_id
            WHERE t.receiver_id = %(id)s
            ORDER BY t.created_at DESC
        ;"""

        results = connectToMySQL(DB).query_db(query, data)
 
        print(results)

        if not results or len(results) == 0 :
            return None
        
        messages = []
        for row in results:
            instance = cls(row)
            instance.sent_how_long_ago = Message.pretty_date(row['created_at'])

            rcvrData = {
                **row,
                'id' : row['receiver.id'],
                'full_name' :  row['first_name'] + " " +  row['last_name'],
                # 'first_name' : row['first_name'],
                # 'last_name' : row['last_name'],
                # 'password' : row['password'],
                # 'email' : row['email'],
                # 'created_at' : row['created_at'],
                # 'updated_at' : row['updated_at']
            }
            receiver = user_model.User(rcvrData)
            instance.receiver = receiver
            print('Receiver -----------------> ', receiver)

            senderData = {
                'id' : row['sender.id'],
                'first_name' : row['sender.first_name'],
                'last_name' : row['sender.last_name'],
                'full_name' :  row['sender.first_name'] + " " +  row['sender.last_name'],
                'password' : row['sender.password'],
                'email' : row['sender.email'],
                'created_at' : row['sender.created_at'],
                'updated_at' : row['sender.updated_at']
            }
            sender = user_model.User(senderData)
            instance.sender = sender
            print('Sender   -----------------> ', sender)
            
            messages.append(instance)

        # For each row in results, build a message instance and tack on it's chef's name as done in get_by_id
        # return the list of messages

        return messages


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
        # # -------------- User must be logged in --------------
        # # ----------------- Required Fields  -----------------  
        # # All fields required
        # # ---------------  Minimum len Fields ----------------
        # # Name, description & instructions must be >= len 3
        # # --------------  Name  --------------  
        # if len( data['location'] ) < 1:
        #     flash( 'Location is required', 'location')
        #     is_valid = False

        # if len( data['description'] ) < 1:
        #     flash( 'Description is required', 'description')
        #     is_valid = False

        # # ----------------  How Many  -------------------
        # if 'how_many' not in data:
        #     flash( 'Number of Sasquatches is required', 'how_many')
        #     is_valid = False
        # elif len( data['how_many'] ) < 1:
        #     flash( 'Number of Sasquatches is required', 'how_many')
        #     is_valid = False
        # # ----------------  Require Date -------------------
        # if 'date' not in data:
        #     flash( 'Date sighting was made is required', 'date')
        #     is_valid = False
        # elif len( data['date'] ) < 1:
        #     flash( 'Date sighting was made is required', 'date')
        #     is_valid = False
        
        return is_valid



# ----------------------------------------------------  Pretty Date
# Attribution: StackOverflow:
# https://stackoverflow.com/questions/1551382/user-friendly-time-format-in-python/1551394#1551394
    # @staticmethod
    def pretty_date(time=False):
        """
        Get a datetime object or a int() Epoch timestamp and return a
        pretty string like 'an hour ago', 'Yesterday', '3 months ago',
        'just now', etc
        """
        from datetime import datetime
        now = datetime.now()
        if type(time) is int:
            diff = now - datetime.fromtimestamp(time)
        elif isinstance(time, datetime):
            diff = now - time
        elif not time:
            diff = 0
        second_diff = diff.seconds
        day_diff = diff.days

        if day_diff < 0:
            return ''

        if day_diff == 0:
            if second_diff < 10:
                return "just now"
            if second_diff < 60:
                return str(second_diff) + " seconds ago"
            if second_diff < 120:
                return "a minute ago"
            if second_diff < 3600:
                return str(second_diff // 60) + " minutes ago"
            if second_diff < 7200:
                return "an hour ago"
            if second_diff < 86400:
                return str(second_diff // 3600) + " hours ago"
        if day_diff == 1:
            return "Yesterday"
        if day_diff < 7:
            return str(day_diff) + " days ago"
        if day_diff < 31:
            return str(day_diff // 7) + " weeks ago"
        if day_diff < 365:
            return str(day_diff // 30) + " months ago"
        return str(day_diff // 365) + " years ago"



