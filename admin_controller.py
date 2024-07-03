from menu_item import MenuItem
import json

class AdminController:
    def get_input(self, prompt, input_type=str):
        return input_type(input(prompt))
    
    def create_item(self, item_name, price, availability_status, item_category):
        return MenuItem(item_name=item_name, price=price, availability_status=availability_status, item_category=item_category)
    
    def create_item_with_id(self, item_id, availability_status=None):
        return MenuItem(item_id=item_id, availability_status=availability_status)
    
    def prepare_payload(self, action, item):
        item_detail_in_json = item.to_dict()
        return json.dumps({'action': action, 'data': item_detail_in_json})
    
    def add_menu_item(self):
        action = "ADD_MENU_ITEM"
        item_name = self.get_input("Please provide the item name: ")
        price = self.get_input("Please provide the item price: ", int)
        availability_status = self.get_input("Enter availability status (1 for available, 0 for not available): ", int)
        item_category = self.get_input("Specify the item category (1 for Breakfast, 2 for Lunch, 3 for Dinner): ", int)
        item = self.create_item(item_name, price, availability_status, item_category)
        return self.prepare_payload(action, item)
    
    def update_item_availability(self):
        action = "UPDATE_AVAILABILITY"
        item_id = self.get_input("Enter the item ID to update: ", int)
        availability_status = self.get_input("Enter new availability status (1 for available, 0 for not available): ", int)
        item = self.create_item_with_id(item_id, availability_status)
        return self.prepare_payload(action, item)
    
    def delete_item_from_menu(self):
        action = "DELETE_ITEM"
        item_id = self.get_input("Enter the item ID to delete: ", int)
        item = self.create_item_with_id(item_id)
        return self.prepare_payload(action, item)
    
    def fetch_complete_menu(self):
        action = "FETCH_COMPLETE_MENU"
        return json.dumps({'action': action})
