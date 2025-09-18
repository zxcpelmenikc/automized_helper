from controllers.auth_controller import register_user, authorize_user, validate_username, validate_password
import getpass
import sys
import os

# Добавляем путь к конфигурации
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'config'))
from config.auth_config import SECURITY_CONFIG

def get_user_input():
    """Получает ввод пользователя с валидацией"""
    username = input("Введите логин: ").strip()
    password = getpass.getpass("Введите пароль: ")
    
    return username, password

def get_secure_password():
    """Получает подтверждение пароля при регистрации"""
    password = getpass.getpass("Введите пароль: ")
    password_confirm = getpass.getpass("Подтвердите пароль: ")
    
    if password != password_confirm:
        print(" Пароли не совпадают!")
        return None
    
    return password

def auth_menu():
    print("=== Система авторизации ===")
    print("Используется Argon2 для безопасного хэширования паролей")
    
    while True:
        print("\n1. Регистрация")
        print("2. Войти")
        print("3. Выход")
        
        try:
            choice = input("Выберите действие: ").strip()
            
            if choice == "1":
                print("\n--- Регистрация нового пользователя ---")
                print(f"Требования к имени пользователя: {SECURITY_CONFIG['min_username_length']}-{SECURITY_CONFIG['max_username_length']} символов, только буквы, цифры и подчеркивания")
                print(f"Требования к паролю: минимум {SECURITY_CONFIG['min_password_length']} символов")
                
                username, _ = get_user_input()
                password = get_secure_password()
                
                if username and password:
                    if register_user(username, password):
                        print(" Пользователь успешно зарегистрирован!")
                    # Ошибки уже выводятся в register_user
                        
            elif choice == "2":
                print("\n--- Вход в систему ---")
                username, password = get_user_input()
                
                if username and password:
                    if authorize_user(username, password):
                        print(" Вход выполнен успешно!")
                        return True
                    else:
                        print(" Неверный логин или пароль!")
                        
            elif choice == "3":
                print(" Выход из программы")
                return False
            else:
                print(" Неверный выбор. Попробуйте снова.")
                
        except KeyboardInterrupt:
            print("\n\n Программа прервана пользователем")
            return False
        except Exception as e:
            print(f" Произошла ошибка: {e}")
            continue
