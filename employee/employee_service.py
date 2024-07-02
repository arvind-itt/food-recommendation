from database.db_config import DB_CONFIG
from database.db_connection import DatabaseConnection
import datetime
from recommendation_engine.sentiment_analyzer import SentimentAnalyzer

class EmployeeService:
    
    def __init__(self):
        self.db = DatabaseConnection(DB_CONFIG)

    def connect_db(self):
        self.db.connect()

    def disconnect_db(self):
        self.db.disconnect()

    def provide_feedback(self, data):
        try:
            self.connect_db()
            feedback_date = self._get_current_date()
            sentiment_score = self._analyze_sentiment(data['comment'])
            self._insert_feedback(data, feedback_date, sentiment_score)
            self.disconnect_db()
            status = "Feedback provided successfully."
        except Exception as error:
            print(error)
            status = "Failed to provide feedback."
        return status

    def view_next_day_menu(self):
        try:
            self.connect_db()
            next_day_menu = self._fetch_next_day_menu()
            self.disconnect_db()
            return next_day_menu
        except Exception as error:
            print(error)
            status = "Error fetching next day menu items."
        return status
    
    def vote_for_food_item(self, item_ids):
        try:
            self.connect_db()
            next_day_menu = self._fetch_next_day_menu()
            self.disconnect_db()
            return next_day_menu
        except Exception as error:
            print(error)
            status = "Error fetching next day menu items."
        return status

    def _get_current_date(self):
        return str(datetime.datetime.today().date())

    def _analyze_sentiment(self, comment):
        sentiment_analyzer = SentimentAnalyzer()
        return sentiment_analyzer.analyze_sentiment(comment)

    def _insert_feedback(self, data, feedback_date, sentiment_score):
        query = '''
        INSERT INTO feedback (user_id, item_id, comment, rating, sentiment_score, feedback_date)
        VALUES (%s, %s, %s, %s, %s, %s);
        '''
        values = (data['user_id'], data['item_id'], data['comment'], data['rating'], sentiment_score, feedback_date)
        self.db.execute_query(query, values)

    def _fetch_next_day_menu(self):
        query = '''
        SELECT item_id, item_name, price, availability_status, item_category
        FROM item_for_next_day;
        '''
        return self.db.fetch_all(query)
