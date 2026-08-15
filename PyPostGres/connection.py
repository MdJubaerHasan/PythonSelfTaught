"""
Before running this script, you must do the following:
1. Install PG4Admin
2. Create Database
3. Install psycopg2-binary
4. Install dotenv
5. Create an .env file in your side of the project
"""

import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

try:
    # Connection attempt
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASS"),
        host = "localhost"
    )
    print("Connected Successfully!")

    curs = conn.cursor()
    curs.execute('SELECT * FROM books;')
    data = curs.fetchall()

    for row in data:
        print(row)

    # 4. Clean up the evidence
    curs.close()
    conn.close()

except Exception as e:
    print(f"Failed to connect:{e}")




