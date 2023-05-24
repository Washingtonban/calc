import os
import sqlite3
from dotenv import load_dotenv


# Carrega as variáveis do arquivo .env
load_dotenv()


def get_conn():
    database_url = os.getenv("DATABASE_URL")
    conn = sqlite3.connect(database_url)
    return conn.cursor()


if __name__ == '__main__':
    get_conn()
