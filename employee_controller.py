import json

class EmployeeController:
    
    def get_input(self, prompt, input_type=str):
        return input_type(input(prompt))
    
    def prepare_payload(self, action, data=None):
        payload = {'action': action}
        if data:
            payload.update(data)
        return json.dumps(payload)
    

    
    def provide_feedback(self, user_id):
        action = "PROVIDE_FEEDBACK"
        item_id = self.get_input("Please enter the item ID: ", int)
        comment = self.get_input("Please provide your comment: ")
        rating = self.get_input("Please rate the item out of 5: ", int)
        feedback_data = {'user_id': user_id, 'item_id': item_id, 'comment': comment, 'rating': rating}
        return self.prepare_payload(action, {'data': feedback_data})
    
    def view_next_day_menu(self):
        action = "VIEW_NEXT_DAY_MENU"
        return self.prepare_payload(action)
    
    def vote_for_food_item(self, user_id):
        action = "VOTE_FOR_FOOD_ITEM"
        num_items = self.get_input("How many items would you like to vote for? ", int)
        item_ids = [self.get_input(f"Please enter item ID {i + 1}: ", int) for i in range(num_items)]
        vote_data = {'items_to_vote': item_ids, 'user_id': user_id}
        return self.prepare_payload(action, {'data': vote_data})

    def fetch_complete_menu(self):
        action = "FETCH_COMPLETE_MENU"
        return self.prepare_payload(action)
