import psycopg2

def init_db():

    try:
        conn = psycopg2.connect(
        dbname='automized_helperistus',
        user='postgres',
        password='admin',
        host='localhost',
        port=5432
        )
        cursor=conn.cursor()
        conn.commit()
        print('База данных инициализирована успешно!')
        return conn, cursor

    except psycopg2.IntegrityError as e:
        conn.rollback()
        print(f"Ошибка инициализации базы данных: {e}")
        return None, None

# Создание подключения и курсора
conn, cursor = init_db()
if conn and cursor:
    print("Можно продолжать работу")
else:
    print("Не удалось подключиться к базе данных")