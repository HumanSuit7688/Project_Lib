import sqlite3

connect = sqlite3.connect('project_db.db')
cur = connect.cursor()

"""ТАБЛИЦА 'ПОЛЬЗОВАТЕЛИ' """
# cur.execute('CREATE TABLE IF NOT EXISTS users ('
#             'id INTEGER PRIMARY KEY,'
#             'fio TEXT NOT NULL,'
#             'grade TEXT NOT NULL,'
#             'email TEXT NOT NULL,'
#             'phone_numb TEXT NOT NULL,'
#             'password TEXT NOT NULL)')

"""ТАБЛИЦА 'АДМИНЫ' """
# cur.execute('CREATE TABLE IF NOT EXISTS admins ('
#             'id INTEGER PRIMARY KEY,'
#             'fio INTEGER NOT NULL,'
#             'email TEXT NOT NULL,'
#             'password TEST NOT NULL)')

"""ТАБЛИЦА 'КНИГИ' """
# cur.execute('CREATE TABLE IF NOT EXISTS books ('
#             'id INTEGER PRIMARY KEY,'
#             'name TEXT NOT NULL,'
#             'author TEXT NOT NULL,'
#             'amount INTEGER NOT NULL)')

"""ТАБЛИЦА 'КНИГА-ПОЛЬЗОВАТЕЛЬ' """
# cur.execute('CREATE TABLE IF NOT EXIST CONNECTION ('
#             'id INTEGER PRIMARY KEY,'
#             'user_id INTEGER,'
#             'book_id INTEGER,'
#             'date_start '
#             ''
#             ')')


connect.commit()
connect.close()