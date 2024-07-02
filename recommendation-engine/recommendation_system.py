from database.db_config import DB_CONFIG
from database.db_connection import DatabaseConnection
from datetime import datetime, timedelta
from menu.menu_item import MenuItem

class RecommendationSystem:

    def __init__(self):
        self.db = DatabaseConnection(DB_CONFIG)

    def connect_db(self):
        self.db.connect()

    def disconnect_db(self):
        self.db.disconnect()

    def _extract_item_ids(self, items):
        return [item[0] for item in items]

    def _calculate_item_scores(self, feedback_data, exclude_items):
        items = {}
        for item in feedback_data:
            if item[0] not in exclude_items:
                if item[0] not in items:
                    items[item[0]] = {'total_score': 0, 'count': 0}
                items[item[0]]['total_score'] += item[1] * item[2]
                items[item[0]]['count'] += 1
        return items

    def _get_top_recommended_ids(self, items, num_items):
        sorted_items = sorted(items.items(), key=lambda x: x[1]['total_score'] / x[1]['count'], reverse=True)
        top_ids = [item[0] for item in sorted_items[:num_items]]
        return ','.join(map(str, top_ids))


    def fetch_feedback_data(self, item_category):
        self.connect_db()
        query = """
        SELECT DISTINCT f.item_id, rating, sentiment_score
        FROM feedback f
        LEFT JOIN menu_item m ON f.item_id = m.item_id
        WHERE m.item_category = %s
        """
        values = (item_category,)
        feedback_data = self.db.fetch_all(query, values)
        self.disconnect_db()
        return feedback_data

    def get_yesterdays_items(self, item_category):
        self.connect_db()
        yesterday = datetime.now() - timedelta(1)
        query = """
        SELECT DISTINCT f.item_id
        FROM feedback f
        LEFT JOIN menu_item m ON f.item_id = m.item_id
        WHERE feedback_date >= %s AND feedback_date < %s AND m.item_category = %s
        """
        values = (yesterday.date(), datetime.now().date(), item_category)
        yesterdays_items = self.db.fetch_all(query, values)
        self.disconnect_db()
        return yesterdays_items

    def recommend_items(self, item_category, num_items):
        feedback_data = self.fetch_feedback_data(item_category)
        exclude_items = self._extract_item_ids(self.get_yesterdays_items(item_category))
        item_scores = self._calculate_item_scores(feedback_data, exclude_items)
        recommended_ids = self._get_top_recommended_ids(item_scores, num_items)
        return recommended_ids

    def get_recommendations(self, num_items):
        menu_item = MenuItem()
        recommendations = {
            'breakfast': menu_item.get_item_detail_by_id(self.recommend_items(1, num_items)),
            'lunch': menu_item.get_item_detail_by_id(self.recommend_items(2, num_items)),
            'dinner': menu_item.get_item_detail_by_id(self.recommend_items(3, num_items))
        }
        return recommendations

