from db.database import init_db
from controllers import employees_controller
from views.employees_view import *
from views.auth_view import auth_menu

def main_menu():
    """Главное меню приложения после авторизации"""
    while True:
        print("\n=== Главное меню ===")
        print("1. Добавить работника")
        print("2. Показать всех работников")
        print("3. Изменить дату увольнения")
        print("4. Удалить работника")
        print("5. Выход")
        
        choice = input("Выберите действие: ").strip()

        if choice == "1":
                
            employee_data = add_employees()
            if employee_data is not None:
                id, last_name, first_name, middle_name, tab_number, inn, snils, gender, birth_date, birth_place, address, education, profession, marital_status, hire_date, dismissal_date, is_active = employee_data
                if employees_controller.add_employees(id, last_name, first_name, middle_name, tab_number, inn, snils, gender, birth_date, birth_place, address, education, profession, marital_status, hire_date, dismissal_date, is_active):
                    print("Работник успешно добавлен!")
                        
                    
        elif choice == "2":
                
            all_employees_list = employees_controller.get_all_employees()
            show_all_employees(all_employees_list)
                
        elif choice == "3":
               
            change_data = change_dismissal_date()
            if change_data is not None:
                id, dismissal_date = change_data
                if employees_controller.change_dismissal_date(id, dismissal_date):
                    print(" Дата увольнения изменена!")
                       
                
                    
        elif choice == "4":
               
            employee_id = deleting_employee()
            if employee_id is not None:
                if employees_controller.delete_employee(employee_id):
                    print(" Работник удален!")
                  
              
                    
        elif choice == "5":
                print(" Выход из программы")
                break
            

def main():
    """Основная функция приложения"""
    print("=== Система управления персоналом ===")
    print("С защищенной авторизацией через Argon2")
    
    # Проверяем авторизацию
    if auth_menu():
        # Инициализируем базу данных
        conn, cursor = init_db()
        if conn and cursor:
            cursor.close()
            conn.close()
            print("\nПодключение к базе данных установлено")
            main_menu()
        else:
            print("Не удалось подключиться к базе данных")
            return
    else:
        print("Авторизация не пройдена")

if __name__ == "__main__":
    main()