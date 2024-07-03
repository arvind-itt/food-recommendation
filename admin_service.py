from database.db_config import DB_CONFIG
from database.db_connection import DatabaseConnection

class AdminService:

    def __init__(self):
        self.db = DatabaseConnection(DB_CONFIG)

    def add_menu_item(self, data):
        query = '''
        INSERT INTO menu (item_name, price, availability_status, item_category) 
        VALUES (%s, %s, %s, %s);
        '''
        return self._execute_query(query, (data['item_name'], data['price'], data['availability_status'], data['item_category']), "Item added successfully", "Error adding item")

    def update_item_availability(self, data):
        query = '''
        UPDATE menu SET availability_status = %s WHERE item_id = %s;
        '''
        return self._execute_query(query, (data['availability_status'], data['item_id']), "Availability updated successfully", "Error updating availability")

    def delete_item_from_menu(self, data):
        query = '''
        DELETE FROM menu WHERE item_id = %s;
        '''
        return self._execute_query(query, (data['item_id'],), "Item deleted successfully", "Error deleting item")

    def _execute_query(self, query, values=None, success_msg=None, error_msg=None):
        try:
            self.db.connect()
            self.db.execute_query(query, values)
            self.db.disconnect()
            return success_msg
        except Exception as e:
            print(e)
            return error_msg
