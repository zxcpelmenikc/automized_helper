def add_employees():
    """Получает данные о новом работнике от пользователя"""
    print("\n--- Добавление нового работника ---")
    id = input("ID (оставьте пустым для автоинкремента): ")
    last_name = input("Фамилия: ")
    first_name = input("Имя: ")
    middle_name = input("Отчество: ")
    tab_number = input("Табельный номер: ")
    inn = input("ИНН: ")
    snils = input("СНИЛС: ")
    gender = input("Пол (М/Ж): ")
    birth_date = input("Дата рождения (YYYY-MM-DD): ")
    birth_place = input("Место рождения: ")
    address = input("Адрес: ")
    education = input("Образование: ")
    profession = input("Профессия: ")
    marital_status = input("Семейное положение: ")
    hire_date = input("Дата приема на работу (YYYY-MM-DD): ")
    dismissal_date = input("Дата увольнения (YYYY-MM-DD или пусто): ")
    is_active = input("Активен (1/0): ")
    
    # Валидация обязательных полей
    if not last_name or not first_name:
        print("❌ Фамилия и имя обязательны для заполнения!")
        return None
    
    return id, last_name, first_name, middle_name, tab_number, inn, snils, gender, birth_date, birth_place, address, education, profession, marital_status, hire_date, dismissal_date, is_active

def show_all_employees(employees):
    """Отображает список всех работников"""
    print("\n--- Список работников ---")
    if not employees:
        print("📝 Работники не найдены")
        return
    
    print(f"📊 Найдено работников: {len(employees)}")
    print("-" * 60)
    
    for employee in employees:
        print(f"ID: {employee[0]} | Фамилия: {employee[1]} | Имя: {employee[2]}")
    
    print("-" * 60)

def change_dismissal_date():
    """Получает данные для изменения даты увольнения"""
    print("\n--- Изменение даты увольнения ---")
    id = input("ID сотрудника для изменения даты увольнения: ")
    
    if not id:
        print("❌ ID не может быть пустым!")
        return None
    
    dismissal_date = input("Новая дата увольнения (YYYY-MM-DD или пусто для снятия увольнения): ")
    
    return id, dismissal_date

def deleting_employee():
    """Получает ID работника для удаления"""
    print("\n--- Удаление работника ---")
    id = input("ID сотрудника для удаления: ")
    
    if not id:
        print("❌ ID не может быть пустым!")
        return None
    
    # Подтверждение удаления
    confirm = input(f"Вы уверены, что хотите удалить работника с ID {id}? (да/нет): ").lower()
    if confirm not in ['да', 'yes', 'y', 'д']:
        print("❌ Удаление отменено")
        return None
    
    return id