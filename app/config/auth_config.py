"""
Конфигурация для системы авторизации с Argon2
"""

# Настройки Argon2
ARGON2_CONFIG = {
    'time_cost': 2,
    'memory_cost': 65536,
    'parallelism': 1,
    'hash_len': 32,
    'salt_len': 16,
    'version': 19  
}

# Настройки базы данных
DATABASE_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'dbname': 'a',
    'user': 'postgres',
    'password': 'admin'
}

# Настройки безопасности
SECURITY_CONFIG = {
    'min_password_length': 6,
    'max_password_length': 128,
    'max_username_length': 50,
    'min_username_length': 3,
    'max_login_attempts': 3,
    'account_lockout_duration': 300
}


VALIDATION_PATTERNS = {
   
    'username': r'^[a-zA-Z0-9_]+$',
 
    'password_strength': r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{6,}$'
}
