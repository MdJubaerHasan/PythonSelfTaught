import os

import psycopg2
from dotenv import load_dotenv
load_dotenv()
class Connect:
    def __init__(self):
        self.conn = None

    def __enter__(self):
        """Auto-creates the connection when entering the 'with' block."""
        try:
            self.conn = psycopg2.connect(
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASS"),
                host=os.getenv("DB_HOST","localhost")
            )
            return self.conn

        except psycopg2.Error as e:
            print(f"Database connection failed: {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()