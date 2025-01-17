from .sqlite import SQLiteDataBase

file: str = "example.db"
sql_database: SQLiteDataBase = SQLiteDataBase(file_name=file)
sql_database.connect()

create_table_query: str = """"
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL, 
        email TEXT NOT NULL
    );
    """

sql_database.run_query(create_table_query)

sql_database.disconnect()
