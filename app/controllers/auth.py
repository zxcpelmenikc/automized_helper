import psycopg2
import hashlib

DB_PARAMS = {
    "dbname": "automized_helperistus",
    "user": "postgres",
    "password": "admin",
    "host": "localhost",
    "port": 5432
}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    conn = psycopg2.connect(**DB_PARAMS)
    cursor = conn.cursor()
    password_hash = hash_password(password)
    try:
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (username, password_hash))
        conn.commit()
        return True
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()

def login_user(username, password):
    conn = psycopg2.connect(**DB_PARAMS)
    cursor = conn.cursor()
    password_hash = hash_password(password)
    cursor.execute("SELECT * FROM users WHERE username=%s AND password_hash=%s", (username, password_hash))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user is not None