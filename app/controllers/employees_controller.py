from db.database import cursor, conn
def add_employees(id, last_name, first_name, middle_name, tab_number, inn, snils, 
                  gender, birth_date, birth_place, address, education, profession, 
                  marital_status, hire_date, dismissal_date, is_active):
        
        cursor.execute("""INSERT INTO employees (id, last_name, first_name, middle_name, tab_number, inn, snils,gender, 
                                birth_date, birth_place, address, education, profession, 
                                marital_status, hire_date, dismissal_date, is_active) VALUES 
                                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
                                (id, last_name, first_name, middle_name, tab_number, inn, snils,gender, 
                                birth_date, birth_place, address, education, profession, 
                                marital_status, hire_date, dismissal_date, is_active))
        conn.commit()
        return True                                                                

def get_all_employees():
    cursor.execute("SELECT id, last_name, first_name FROM employees")
    return cursor.fetchall()

def change_dismissal_date(id, dismissal_date):
    cursor.execute("UPDATE employees SET dismissal_date = %s WHERE id = %s", (dismissal_date, id))
    conn.commit()
    return True

def delete_employee(id):
    cursor.execute("DELETE FROM employees WHERE id = %s", (id))
    conn.commit()
    return True



