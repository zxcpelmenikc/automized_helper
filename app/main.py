from db.database import init_db
from controllers import employees_controller
from views.employees_view import *
from controllers.auth import register_user, login_user

def auth_menu():
    while True:
        print("\n1. Регистрация")
        print("2. Войти")
        print("3. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            username = input("Введите логин: ")
            password = input("Введите пароль: ")
            if register_user(username, password):
                print("Пользователь успешно зарегистрирован!")
            else:
                print("Пользователь с таким логином уже существует!")
        elif choice == "2":
            username = input("Введите логин: ")
            password = input("Введите пароль: ")
            if login_user(username, password):
                print("Вход выполнен успешно!")
                return True
            else:
                print("Неверный логин или пароль!")
        elif choice == "3":
            print("Выход")
            return False
        else:
            print("Неверный выбор")

def main():
    init_db()
    if not auth_menu():
        return
    while True:
        print("\nМеню:")
        print("1. Добавить работника")
        print("2. Показать всех работников")
        print("3. Изменить дату увольнения")
        print("4. Удалить работника")
        print("5. Показать меню")
        print("6. Показать заказы")
        print("7. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
                id, last_name, first_name, middle_name, tab_number, inn, snils, gender, birth_date, birth_place, address, education, profession, marital_status, hire_date, dismissal_date, is_active=add_employees()
                employees_controller.add_employees(id, last_name, first_name, middle_name, tab_number, inn, snils, gender, birth_date, birth_place, address, education, profession, marital_status, hire_date, dismissal_date, is_active)
        elif choice == "2":
            all_employees_list=employees_controller.get_all_employees()
            show_all_employees(all_employees_list)
        elif choice == "3":
            id, dismissal_date=change_dismissal_date()
            employees_controller.change_dismissal_date(id, dismissal_date)
            
        elif choice == "4":
            id=deleting_employee()
            employees_controller.delete_employee(id)
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "7":
            print("Выход")
            break
        else:
            print("Неверный выбор")
if __name__ == "__main__":
    main()