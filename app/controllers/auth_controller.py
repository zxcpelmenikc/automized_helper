import psycopg2
import re
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from db.database import init_db
from config.auth_config import ARGON2_CONFIG, SECURITY_CONFIG, VALIDATION_PATTERNS

# Добавляем путь к конфигурации



# Инициализация хэшера Argon2 с настройками
ph = PasswordHasher(
    time_cost=ARGON2_CONFIG['time_cost'],
    memory_cost=ARGON2_CONFIG['memory_cost'],
    parallelism=ARGON2_CONFIG['parallelism'],
    hash_len=ARGON2_CONFIG['hash_len'],
    salt_len=ARGON2_CONFIG['salt_len']
)

def validate_username(username):
    """Валидация имени пользователя"""
    if not username:
        return False, "Имя пользователя не может быть пустым"
    
    if len(username) < SECURITY_CONFIG['min_username_length']:
        return False, f"Имя пользователя должно содержать минимум {SECURITY_CONFIG['min_username_length']} символов"
    
    if len(username) > SECURITY_CONFIG['max_username_length']:
        return False, f"Имя пользователя не должно превышать {SECURITY_CONFIG['max_username_length']} символов"
    
    if not re.match(VALIDATION_PATTERNS['username'], username):
        return False, "Имя пользователя может содержать только буквы, цифры и подчеркивания"
    
    return True, "OK"

def validate_password(password):
    """Валидация пароля"""
    if not password:
        return False, "Пароль не может быть пустым"
    
    if len(password) < SECURITY_CONFIG['min_password_length']:
        return False, f"Пароль должен содержать минимум {SECURITY_CONFIG['min_password_length']} символов"
    
    if len(password) > SECURITY_CONFIG['max_password_length']:
        return False, f"Пароль не должен превышать {SECURITY_CONFIG['max_password_length']} символов"
    
    return True, "OK"

def register_user(username, password):
    # Валидация входных данных
    username_valid, username_msg = validate_username(username)
    if not username_valid:
        print(f"❌ Ошибка валидации имени пользователя: {username_msg}")
        return False
    
    password_valid, password_msg = validate_password(password)
    if not password_valid:
        print(f"❌ Ошибка валидации пароля: {password_msg}")
        return False
    
    # Получаем соединение с базой данных
    conn, cursor = init_db()
    if not conn or not cursor:
        print("❌ Не удалось подключиться к базе данных")
        return False
    
    try:
        # Хэширование пароля с использованием Argon2
        password_hash = ph.hash(password)
        
        cursor.execute('INSERT INTO users (username, password_hash) VALUES (%s, %s)', 
                      (username, password_hash))
        conn.commit()
        cursor.close()
        conn.close()
        return True
        
    except psycopg2.IntegrityError:
        conn.rollback()
        cursor.close()
        conn.close()
        print("❌ Пользователь с таким именем уже существует")
        return False
        
    except Exception as e:
        print(f"❌ Ошибка при регистрации: {e}")
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        return False
def authorize_user(username, password):
    # Валидация входных данных
    username_valid, username_msg = validate_username(username)
    if not username_valid:
        print(f"❌ Ошибка валидации имени пользователя: {username_msg}")
        return False
    
    password_valid, password_msg = validate_password(password)
    if not password_valid:
        print(f"❌ Ошибка валидации пароля: {password_msg}")
        return False
    
    # Получаем соединение с базой данных
    conn, cursor = init_db()
    if not conn or not cursor:
        print("❌ Не удалось подключиться к базе данных")
        return False
    
    try:
        cursor.execute('SELECT password_hash FROM users WHERE username = %s', (username,))
        result = cursor.fetchone()
        
        if result is None:
            cursor.close()
            conn.close()
            print("❌ Пользователь не найден")
            return False
        
        stored_hash = result[0]
        
        try:
            # Проверяем пароль с помощью Argon2
            is_valid = ph.verify(stored_hash, password)
            cursor.close()
            conn.close()
            
            if is_valid:
                print("✅ Авторизация успешна")
            else:
                print("❌ Неверный пароль")
            
            return is_valid
            
        except VerifyMismatchError:
            cursor.close()
            conn.close()
            print("❌ Неверный пароль")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка при авторизации: {e}")
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        return False
