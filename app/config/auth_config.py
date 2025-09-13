"""
Конфигурация для системы авторизации с Argon2
"""

# Настройки Argon2
ARGON2_CONFIG = {
    # Время выполнения (в миллисекундах)
    'time_cost': 2,
    # Использование памяти (в кибибайтах)
    'memory_cost': 65536,  # 64 MB
    # Количество параллельных потоков
    'parallelism': 1,
    # Длина хэша (в байтах)
    'hash_len': 32,
    # Тип соли
    'salt_len': 16,
    # Версия Argon2
    'version': 19  # Argon2id
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
    # Минимальная длина пароля
    'min_password_length': 6,
    # Максимальная длина пароля
    'max_password_length': 128,
    # Максимальная длина имени пользователя
    'max_username_length': 50,
    # Минимальная длина имени пользователя
    'min_username_length': 3,
    # Максимальное количество попыток входа
    'max_login_attempts': 3,
    # Блокировка аккаунта (в секундах)
    'account_lockout_duration': 300  # 5 минут
}

# Регулярные выражения для валидации
VALIDATION_PATTERNS = {
    # Имя пользователя: только буквы, цифры и подчеркивания
    'username': r'^[a-zA-Z0-9_]+$',
    # Пароль: минимум одна буква, одна цифра
    'password_strength': r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{6,}$'
}
