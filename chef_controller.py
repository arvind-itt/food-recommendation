import json
from datetime import datetime, timedelta

class ChefController:
    
    def _get_input_number(self, message):
        return int(input(message))
    
    def _get_item_ids(self, number_of_items):
        item_ids = []
        for i in range(number_of_items):
            item_id = self._get_input_number(f"Enter item id no. {i+1}: ")
            item_ids.append(item_id)
        return item_ids
    
    def _create_json_payload(self, action, data=None):
        payload = {'action': action}
        if data:
            payload.update(data)
        return json.dumps(payload)
    
    def get_recommendation(self):
        action = "GET_RECOMMENDATION"
        number_of_items_chef_want = self._get_input_number("Enter number of items you want from recommendation system: ")
        return self._create_json_payload(action, {'number_of_items_chef_want': number_of_items_chef_want})
    
    def roll_out_menu(self):
        action = "ROLL_OUT_MENU"
        number_of_items_to_rollout = self._get_input_number("Enter number of items you want to roll out for each meal type: ")
        print("Enter all the item_ids you want to roll out: ")
        item_ids = self._get_item_ids(number_of_items_to_rollout * 3)
        return self._create_json_payload(action, {'items_to_rollout': item_ids})
    
    def fetch_complete_menu(self):
        action = "FETCH_COMPLETE_MENU"
        return self._create_json_payload(action)
    
    def view_voted_items(self):
        action = "VIEW_VOTED_ITEMS"
        yesterday = (datetime.today() - timedelta(days=1)).date()
        return self._create_json_payload(action, {'date': str(yesterday)})
