from database.db_config import DB_CONFIG
from database.db_connection import DatabaseConnection
from datetime import datetime, timedelta
from menu_item import MenuItem

class RecommendationSystem:
    
    def __init__(self):
        self.db = DatabaseConnection(DB_CONFIG)

    def _connect_to_db(self):
        self.db.connect()

    def _disconnect_from_db(self):
        self.db.disconnect()

    def _fetch_feedback_data(self, item_category):
        self._connect_to_db()
        query = """
        SELECT DISTINCT f.item_id, rating, sentiment_score
        FROM feedback f LEFT JOIN menu m ON f.item_id = m.item_id WHERE m.item_category = %s
        """
        values = (item_category,)
        data = self.db.fetch_all(query, values)
        self._disconnect_from_db()
        return data

    def _get_yesterdays_items(self, item_category):
        self._connect_to_db()
        yesterday = datetime.now() - timedelta(1)
        query = """
        SELECT DISTINCT f.item_id
        FROM feedback f LEFT JOIN menu m ON f.item_id = m.item_id
        WHERE feedback_date >= %s AND feedback_date < %s AND m.item_category = %s
        """
        values = (yesterday.date(), datetime.now().date(), item_category)
        data = self.db.fetch_all(query, values)
        self._disconnect_from_db()
        return data

    def _recommend_items(self, item_category, num_items):
        feedback_data = self._fetch_feedback_data(item_category)
        exclude_items = self._get_yesterdays_items(item_category)
        items = {}
        exclude_items = [item[0] for item in exclude_items]
        for item in feedback_data:
            if item[0] not in exclude_items:
                if item[0] not in items:
                    items[item[0]] = {
                        'total_score': 0,
                        'count': 0,
                    }
                items[item[0]]['total_score'] += item[1] * item[2]
                items[item[0]]['count'] += 1

        recommendations = sorted(
            items.items(),
            key=lambda x: x[1]['total_score'] / x[1]['count'],
            reverse=True
        )
        recommended_ids = [item[0] for item in recommendations[:num_items]]
        recommended_ids_str = ','.join(map(str, recommended_ids))
        return recommended_ids_str

    def get_recommendations(self, num_items):
        menu_item = MenuItem()
        breakfast_recommendations = menu_item.get_item_detail_by_id(self._recommend_items(1, num_items))
        lunch_recommendations = menu_item.get_item_detail_by_id(self._recommend_items(2, num_items))
        dinner_recommendations = menu_item.get_item_detail_by_id(self._recommend_items(3, num_items))

        return {
            'breakfast': breakfast_recommendations,
            'lunch': lunch_recommendations,
            'dinner': dinner_recommendations
        }
