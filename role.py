from database.db_connection import DatabaseConnection
from database.db_config import *

class Role:
    def __init__(self, role_id, role_name):
        self.role_id = role_id
        self.role_name = role_name

    @classmethod
    def create_role(cls, role_id, role_name):
        db = DatabaseConnection(DB_CONFIG)
        db.connect()
        query = "INSERT INTO Role VALUES (%s,%s)"
        values = (role_id,role_name)
        db.execute_query(query, values)
        db.disconnect()

    @classmethod
    def fetch_roles(cls):
        db = DatabaseConnection(DB_CONFIG)
        db.connect()
        query = "SELECT * FROM Role"
        roles = db.fetch_all(query)
        db.disconnect()
        role_objects = [cls(role[0], role[1]) for role in roles]
        return role_objects