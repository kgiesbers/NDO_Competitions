import sqlite3

def create_database():
    conn = sqlite3.connect('data_access/database/competitions.db')
    cursor = conn.cursor()

    cursor.execute()
