import json
from recommendation_engine.recommendation_system import RecommendationSystem
from database.db_config import DB_CONFIG
from database.db_connection import DatabaseConnection

class ChefService:

    def __init__(self):
        self.db = DatabaseConnection(DB_CONFIG)

    def connect_db(self):
        self.db.connect()

    def disconnect_db(self):
        self.db.disconnect()

    def _prepare_items_list(self, items):
        return ','.join(map(str, items))

    def _create_or_replace_view(self, items_list):
        create_view_query = f"""
        CREATE OR REPLACE VIEW item_for_next_day AS
        SELECT * FROM menu_item WHERE item_id IN ({items_list});
        """
        self.db.execute_query(create_view_query)

    def _fetch_voted_items(self, date):
        fetch_query = f"""
        SELECT item_id, user_id FROM voted_item WHERE selection_date = '{date}';
        """
        return self.db.fetch_all(fetch_query)

    def get_recommendation(self, num_items):
        recommender = RecommendationSystem()
        return recommender.get_recommendations(num_items)
    
    def roll_out_menu(self, items_to_rollout):
        items_list = self._prepare_items_list(items_to_rollout)
        try:
            self.connect_db()
            self._create_or_replace_view(items_list)
            self.disconnect_db()
            result_message = "Menu rolled out successfully."
        except Exception as error:
            print(error)
            result_message = "Error occurred while rolling out the menu."
        return result_message
    
    def view_voted_items(self, date):
        try:
            self.connect_db()
            voted_items = self._fetch_voted_items(date)
            self.disconnect_db()
            return voted_items
        except Exception as error:
            print(error)
            error_message = "Error occurred while fetching voted items."
        return error_message


