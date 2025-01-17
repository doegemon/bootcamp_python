import sqlite3

class SQLiteDataBase:
    def __init__(self, file_name):
        self.file_name = file_name
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.file_name)
            print("Successfully connected!")
        except sqlite3.Error as e:
            print("Database connection error: ", e)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected")

    def run_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except sqlite3.Error as e:
            print("Query execution error: ", e)
