from db_config import DB_CONFIG
from db_connection import DatabaseConnection

class AdminService:

    def add_menu_item(self,data):
        try:
            db = DatabaseConnection(DB_CONFIG)
            db.connect()
            query = '''
            insert into menu (item_name, price, availability_status, item_category) values (%s,%s,%s,%s);
            '''
            values = (data['item_name'], data['price'], data['availability_status'], data['item_category'])
            db.execute_query(query, values)
            db.disconnect()
            status = "Item added successfully"
        except Exception as e:
            status = "Item not added"
        return status
    
    def update_item_availability(self,data):
        try:
            db = DatabaseConnection(DB_CONFIG)
            db.connect()
            query = '''
            update menu set availability_status = %s where item_id = %s;
            '''
            values = (data['availability_status'], data['item_id'])
            db.execute_query(query, values)
            db.disconnect()
            status = "Availability updated successfully"
        except Exception as e:
            print(e)
            status = "Error in updating availability"
        return status
    
    def delete_item_from_menu(self,data):
        try:
            db = DatabaseConnection(DB_CONFIG)
            db.connect()
            query = '''
            delete from menu where item_id = %s;
            '''
            values = (data['item_id'],)
            db.execute_query(query, values)
            db.disconnect()
            status = "Item deleted successfully"
        except Exception as e:
            print(e)
            status = "Error in deleting item"
        return status
