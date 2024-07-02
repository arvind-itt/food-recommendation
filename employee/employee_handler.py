import json

class employeeHandler:
    
    def fetch_complete_menu(self):
        action = "FETCH_COMPLETE_MENU"
        item_detail_to_send_to_server = json.dumps({'action': action})
        return item_detail_to_send_to_server
    
    def provide_feedback(self,user_id):
        action = "PROVIDE_FEEDBACK"
        item_id = int(input("Enter the item_id: "))
        comment = input("Enter comment: ")
        rating = int(input("Enter rating out of 5: "))
        item_detail_to_send_to_server = json.dumps({'action': action, 'data': {'user_id':user_id, 'item_id': item_id, 'comment': comment, 'rating': rating}})
        return item_detail_to_send_to_server
    
    def view_next_day_menu(self):
        action = "VIEW_NEXT_DAY_MENU"
        detail_to_send_to_server = json.dumps({'action': action})
        return detail_to_send_to_server
    
    def vote_for_food_item(self,user_id):
        action = "VOTE_FOR_FOOD_ITEM"
        num_items = int(input("Enter how many items you want to vote for: "))
        item_ids = []
        for i in range(num_items):
            item_id = int(input("Enter item id: "))
            item_ids.append(item_id)
        detail_to_send_to_server = json.dumps({'action': action, 'data': {'items_to_vote': item_ids, 'user_id': user_id}})
        return detail_to_send_to_server