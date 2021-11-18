from mysql.connector import connect, Error

session = connect(host='localhost', user='root', password='password', database='blackmarket')


def add_user(first, last, type_):
    try:
        with session as connection:
            add_user_query = f"INSERT INTO user (first_name, last_name, type) VALUES ('{first}', " \
                             f"'{last}', '{type_}')"
            with connection.cursor() as cursor:
                cursor.execute(add_user_query)
                connection.commit()
    except Error as e:
        print(e)

