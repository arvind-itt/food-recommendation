import json
from recommendation-engine.recommendation_system import RecommendationSystem
from database.db_config import DB_CONFIG
from database.db_connection import DatabaseConnection

class ChefService:
    
    def get_recommendation(self,num_items):
        recommender = RecommendationSystem()
        recommendations = recommender.get_recommendations(num_items)
        return recommendations
    
    def roll_out_menu(self,items_to_rollout):
        items_to_rollout = ','.join(map(str,items_to_rollout))
        try:
            db = DatabaseConnection(DB_CONFIG)
            db.connect()
            query = f"create or replace view item_for_next_day as select * from menu_item where item_id in ({items_to_rollout});"
            db.execute_query(query)
            db.disconnect()
            status = "Menu rolled out successfully"
        except Exception as e:
            print(e)
            status = "Error while rolling out menu"
        return status
    
    def view_voted_items(self,date):
        try:
            db = DatabaseConnection(DB_CONFIG)
            db.connect()
            query = f"select item_id, user_id from voted_item where selection_date = '{date}';"
            voted_items = db.fetch_all(query)
            db.disconnect()
            return voted_items
        except Exception as e:
            print(e)
            status = "Error in fetching voted items"
        return status