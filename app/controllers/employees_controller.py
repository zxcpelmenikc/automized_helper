from db.database import init_db

def add_employees(id, last_name, first_name, middle_name, tab_number, inn, snils, 
                  gender, birth_date, birth_place, address, education, profession, 
                  marital_status, hire_date, dismissal_date, is_active):
    
    # Получаем соединение с базой данных
    conn, cursor = init_db()
    if not conn or not cursor:
        print("❌ Не удалось подключиться к базе данных")
        return False
    
    try:
        cursor.execute("""INSERT INTO employees (id, last_name, first_name, middle_name, tab_number, inn, snils,gender, 
                                birth_date, birth_place, address, education, profession, 
                                marital_status, hire_date, dismissal_date, is_active) VALUES 
                                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
                                (id, last_name, first_name, middle_name, tab_number, inn, snils,gender, 
                                birth_date, birth_place, address, education, profession, 
                                marital_status, hire_date, dismissal_date, is_active))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"❌ Ошибка при добавлении работника: {e}")
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        return False                                                                

def get_all_employees():
    # Получаем соединение с базой данных
    conn, cursor = init_db()
    if not conn or not cursor:
        print("❌ Не удалось подключиться к базе данных")
        return []
    
    try:
        cursor.execute("SELECT id, last_name, first_name FROM employees")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    except Exception as e:
        print(f"❌ Ошибка при получении списка работников: {e}")
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        return []

def change_dismissal_date(id, dismissal_date):
    # Получаем соединение с базой данных
    conn, cursor = init_db()
    if not conn or not cursor:
        print("❌ Не удалось подключиться к базе данных")
        return False
    
    try:
        cursor.execute("UPDATE employees SET dismissal_date = %s WHERE id = %s", (dismissal_date, id))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"❌ Ошибка при изменении даты увольнения: {e}")
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        return False

def delete_employee(id):
    # Получаем соединение с базой данных
    conn, cursor = init_db()
    if not conn or not cursor:
        print("❌ Не удалось подключиться к базе данных")
        return False
    
    try:
        cursor.execute("DELETE FROM employees WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"❌ Ошибка при удалении работника: {e}")
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        return False



