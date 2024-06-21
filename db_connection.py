import mysql.connector

class DatabaseConnection:
    def __init__(self, config):
        self.host = config['host']
        self.user = config['user']
        self.password = config['password']
        self.database = config['database']
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connection to MySQL database was successful")
        except Exception as e:
            print(f"Error connecting to MySQL database: {e}")
            self.connection = None

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL database connection closed")

    def get_cursor(self):
        return self.connection.cursor()

    def execute_query(self, query, params=None):
        if not self.connection or not self.connection.is_connected():
            print("No database connection available")
            return None
        cursor = self.get_cursor()
        try:
            cursor.execute(query, params)
            self.connection.commit()
            print("Query executed successfully")
            return cursor
        except Exception as e:
            print(f"Error executing query: {e}")
            return None

    def fetch_all(self, query, params=None):
        cursor = self.get_cursor()
        cursor.execute(query, params)
        if cursor:
            result = cursor.fetchall()
            return result
        return []

    def fetch_one(self, query, params=None):
        cursor = self.get_cursor()
        cursor.execute(query)
        if cursor:
            result = cursor.fetchone()
            return result
        return None
