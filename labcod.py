import sqlite3
from sqlite3 import Error


# Функція для створення з'єднання до БД 
def create_connection(eff1c):
    conn = None
    try:
        conn = sqlite3.connect(eff1c)
    except Error as e:
        print(e)
    return conn


# Вибір всіх значень в таблиці addresses
def select_all_addresses(conn):
    sql = 'SELECT * FROM addresses'
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)


# Створення нової адреси
def create_address(conn, full_name):
    sql = ''' INSERT INTO addresses(full_name, address)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, full_name)


# Зміна адреси
def update_address(conn, address):
    sql = ''' UPDATE addresses
              SET address = ?
              WHERE full_name = ?'''
    cur = conn.cursor()
    cur.execute(sql, address)
    conn.commit()


# Видалення адреси
def remove_address(conn, removed_address):
    sql = ''' DELETE FROM addresses WHERE full_name = ? '''
    cur = conn.cursor()
    cur.execute(sql, removed_address)
    conn.commit()



def main():

    database = r"eff1c.db" 
 
    # Встановлення з'єднання
    conn = create_connection(database)

    with conn:
        print("\nВсі адреси (ПІБ, адреса)")
        select_all_addresses(conn)
        print("\nВставка нового рядка...")
        create_address(conn, ('Мартинюк Андрій Андрійович','м. Луцьк вул. Лесі Українки 21'))
        print("\nВсі адреси (ПІБ, адреса)")
        select_all_addresses(conn)
        print("\nЗміна рядка...")
        update_address(conn, ('Мартинюк Андрій Андрійович','м. Луцьк вул. Рахманінова 2'))
        print("\nВсі адреси (ПІБ, адреса)")
        select_all_addresses(conn)
        print("\nВидалення рядка")
        remove_address(conn, ('Мартинюк Андрій Андрійович',))
        print("\nВсі адреси (ПІБ, адреса)")
        select_all_addresses(conn)
        
 
if __name__ == '__main__':
    main()