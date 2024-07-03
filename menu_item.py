from database.db_connection import DatabaseConnection
from database.db_config import DB_CONFIG

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
    
    @staticmethod
    def _connect_to_db():
        db = DatabaseConnection(DB_CONFIG)
        db.connect()
        return db
    
    @staticmethod
    def _disconnect_from_db(db):
        db.disconnect()
    
    @classmethod
    def fetch_complete_menu(cls):
        db = cls._connect_to_db()
        query = "SELECT * FROM menu;"
        menu_items = db.fetch_all(query)
        cls._disconnect_from_db(db)
        return menu_items
    
    @classmethod
    def get_item_detail_by_id(cls, item_id):
        db = cls._connect_to_db()
        query = "SELECT * FROM menu WHERE item_id = %s;"
        menu_items = db.fetch_all(query, (item_id,))
        cls._disconnect_from_db(db)
        return menu_items
