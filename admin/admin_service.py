from database.db_config import DB_CONFIG
from database.db_connection import DatabaseConnection

class AdminService:
    def __init__(self):
        self.db = DatabaseConnection(DB_CONFIG)
    
    def connect_db(self):
        self.db.connect()
    
    def disconnect_db(self):
        self.db.disconnect()

    def add_menu_item(self, data):
        try:
            self.connect_db()
            insert_query = '''
            INSERT INTO menu (item_name, price, availability_status, item_category) VALUES (%s, %s, %s, %s);
            '''
            params = (data['item_name'], data['price'], data['availability_status'], data['item_category'])
            self.db.execute_query(insert_query, params)
            self.disconnect_db()
            response = "Item has been added successfully."
        except Exception as error:
            print(error)
            response = "Failed to add item."
        return response
    
    def update_item_availability(self, data):
        try:
            self.connect_db()
            update_query = '''
            UPDATE menu SET availability_status = %s WHERE item_id = %s;
            '''
            params = (data['availability_status'], data['item_id'])
            self.db.execute_query(update_query, params)
            self.disconnect_db()
            response = "Availability status updated successfully."
        except Exception as error:
            print(error)
            response = "Failed to update availability."
        return response
    
    def delete_item_from_menu(self, data):
        try:
            self.connect_db()
            delete_query = '''
            DELETE FROM menu WHERE item_id = %s;
            '''
            params = (data['item_id'],)
            self.db.execute_query(delete_query, params)
            self.disconnect_db()
            response = "Item deleted successfully."
        except Exception as error:
            print(error)
            response = "Failed to delete item."
        return response
