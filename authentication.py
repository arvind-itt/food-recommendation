from db_connection import DatabaseConnection
from db_config import *

class AuthService:
    def login(self, email):
        user = self.get_user_details_from_email(email)
        if len(user) == 1:
            print(f"Authentication successfull Welcome {user[0][0]}..!")
            return user
        else:
            print("Authentication failed user not present.")
            return user
        return user
    
    def get_user_details_from_email(self, email):
        db = DatabaseConnection(DB_CONFIG)
        db.connect()
        query = "select Name, email, role_name from users u join role r on u.role_id = r.role_id where email = %s;"
        values = (email,)
        user_details = db.fetch_all(query, values)
        return user_details
