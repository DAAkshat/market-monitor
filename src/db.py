import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("DB_PASSWORD"),
        database="market_monitor"
    )

def load_price_data(long_data):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO price_history (date, ticker, close_price)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE close_price = VALUES(close_price)
    """
    cursor.executemany(query, list(long_data.itertuples(index=False, name=None)))
    conn.commit()
    cursor.close()
    conn.close()

def load_sector_data(sector_map):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO ticker_sectors (ticker, sector)
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE sector = VALUES(sector)
    """
    cursor.executemany(query, list(sector_map.items()))
    conn.commit()
    cursor.close()
    conn.close()