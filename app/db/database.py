import psycopg2
from argon2 import PasswordHasher


ph = PasswordHasher()

def init_db():
    try:
        conn = psycopg2.connect(
            dbname='a',
            user='postgres',
            password='admin',
            host='localhost',
            port=5432
        )
        cursor = conn.cursor()
        
        # Создаем таблицу users если она не существует
        create_users_table(cursor)
        conn.commit()
        
        print('База данных инициализирована успешно!')
        return conn, cursor

    except psycopg2.Error as e:
        print(f"Ошибка инициализации базы данных: {e}")
        return None, None

def create_users_table(cursor):
    """Создает таблицу users для хранения данных пользователей"""
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        print("Таблица users создана или уже существует")
    except psycopg2.Error as e:
        print(f"Ошибка создания таблицы users: {e}")

def get_password_hasher():
    """Возвращает экземпляр PasswordHasher для использования в других модулях"""
    return ph