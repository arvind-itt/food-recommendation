from db_connection import DatabaseConnection
from db_config import *

class MenuItem:
    def __init__(self, item_id=None, item_name=None, price=None, availability_status=None, item_category=None):
        self.item_id = item_id
        self.item_name = item_name
        self.price = price
        self.availability_status = availability_status
        self.item_category = item_category

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "item_name": self.item_name,
            "price": self.price,
            "availability_status": self.availability_status,
            "item_category": self.item_category,
        }
    
    @classmethod
    def fetch_complete_menu(cls):
        db = DatabaseConnection(DB_CONFIG)
        db.connect()
        query = "SELECT * FROM menu;"
        menu_items = db.fetch_all(query)
        db.disconnect()
        return menu_items