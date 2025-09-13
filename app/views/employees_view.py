from db.database import cursor, conn
def add_employees():
    id = input("ID (оставьте пустым для автоинкремента): ")
    last_name = input("Фамилия: ")
    first_name = input("Имя: ")
    middle_name = input("Отчество: ")
    tab_number = input("Табельный номер: ")
    inn = input("ИНН: ")
    snils = input("СНИЛС: ")
    gender = input("Пол: ")
    birth_date = input("Дата рождения: ")
    birth_place = input("Место рождения: ")
    address = input("Адрес: ")
    education = input("Образование: ")
    profession = input("Профессия: ")
    marital_status = input("Семейное положение: ")
    hire_date = input("Дата приема на работу: ")
    dismissal_date = input("Дата увольнения: ")
    is_active = input("Активен (1/0): ")
    return id, last_name, first_name, middle_name, tab_number, inn, snils, gender, birth_date, birth_place, address, education, profession, marital_status, hire_date, dismissal_date, is_active

def show_all_employees(employees):
    print("Работники:")
    print(employees)
    for employee in employees:
        print(f"ID: {employee[0]}, last_name: {employee[1]}, first_name: {employee[2]}")
        return cursor.fetchall()
    
def change_dismissal_date():
    id = input("ID сотрудника для изменения даты увольнения: ")
    dismissal_date = input("Новая дата увольнения (YYYY-MM-DD): ")
    cursor.execute("UPDATE employees SET dismissal_date = %s WHERE id = %s", (dismissal_date, id))
    conn.commit()
    print("Дата увольнения обновлена.")
    return id, dismissal_date

def deleting_employee():
    id = input("ID сотрудника для удаления: ")
    cursor.execute("DELETE FROM employees WHERE id = %s", (id))
    conn.commit()
    print("Сотрудник удален.")
    return id