#  программа для обращения к базе данных
import decimal
import pprint

import psycopg2

from config import NAME_DB, NAME_U, PASS, HOST


def answer_bd(text: str, *args) -> list:
    connect = psycopg2.connect(dbname=NAME_DB, user=NAME_U, password=PASS, host=HOST)
    cursor = connect.cursor()
    cursor.execute(text, args)
    answer = cursor.fetchall()
    cursor.close()  # закрываем курсор
    connect.close()
    return answer


def add_db(text: str, *args) -> None:
    connect = psycopg2.connect(dbname=NAME_DB, user=NAME_U, password=PASS, host=HOST)
    cursor = connect.cursor()
    cursor.execute(text, args)
    cursor.close()
    connect.commit()
    connect.close()


def get_my_user_id(tg_id: int) -> int:
    return answer_bd("SELECT * FROM users WHERE tg_id=%s", tg_id)[0][0]


# обращение базе данных и получение данных о всех магазинах
def get_all_my_shop(user_id) -> list:  # TODO
    tt = answer_bd("SELECT * FROM shops WHERE id_seller=%s", user_id)
    return ['apple', 'banana', 'cherry']


# обращение базе данных и получение данных о всех принадлежащщих человеку продуктов
def get_all_my_product(user_id) -> list:  # TODO
    nn = answer_bd("SELECT * FROM product")
    return [i[1] for i in nn]
    # tt = answer_bd("SELECT * FROM user_prod WHERE id_user=%s", user_id)
    # pp = answer_bd("SELECT * FROM products WHERE id_prod in (select id_prod from user_prod where id_user=%s)", user_id)
    return ['apple', 'banana', 'cherry', 'kiwi', 'pineapple']


# обращение базе данных и получение данных о всех продуктов принадлежащих магазину
def get_shop_product(user_id, shop_id) -> list:  # TODO
    tt = answer_bd("SELECT * FROM products WHERE id_prod in (select id_prod from prod_shop where id_shop=%s)", shop_id)
    return ['apple', 'banana', 'kiwi', 'pineapple']


#  добавление  имеющемуся продукту еще элементов
def add_some_product(index: int) -> None:  # TODO
    pass


#  уменьшение количества элементов продукта
def del_some_product(index: int, count=1) -> None:  # TODO
    pass


# вернуть количество элементов продукта
def count_product(index: int) -> int:  # TODO
    pass


#  вернуть количество типов продуктов, имеющихся у юзера
def my_product_count(id: int) -> int:  # TODO
    pass


def search_id_user(id_user: int) -> int:
    users = answer_bd("SELECT * FROM users WHERE id_tg=%s", id_user)
    if len(users) == 0:
        return 0
    return users[0][0]


def search_id_product(name: str, fr_ve: bool) -> int:
    users = answer_bd("SELECT * FROM product WHERE name_prod=%s AND fr_or_ve=%s", name, fr_ve)
    if len(users) == 0:
        return 0
    return users[0][0]


def search_name_product(id_prod: int) -> str:
    users = answer_bd("SELECT * FROM product WHERE id_prod=%s", id_prod)
    if len(users) == 0:
        return "we can't find any product"
    return users[0][1]


#  добавление юзера в бд
def add_user(id_user: int, username: str, first_name: str, second_name: str, money: int) -> None:
    sql_query = "insert into users values (%s, %s, %s, %s, %s, %s)"
    add_db(sql_query, free_user_id(), id_user, first_name, second_name, username, money)


#  добавление нового продукта в бд
def add_product(name: str, fr_ve: bool) -> None:
    add_db("insert into product values (%s, %s, %s)", free_product_id(), name, fr_ve)


def add_shop(name: str, seller: int) -> None:
    add_db('insert into shops values (%s, %s, %s)', free_shop_id(), seller, name)


def add_prod_user(id_prod: int, id_user: int, count: int) -> None:
    tt = answer_bd('SELECT * FROM user_prod WHERE id_prod=%s and id_user=%s', id_prod, id_user)
    if len(tt) == 0:
        add_db("insert into user_prod values (%s, %s, %s)", id_prod, id_user, count)
    else:
        add_db("UPDATE user_prod SET count=%s WHERE id_user=%s and id_prod=%s",
               tt[0][2] + count, id_user, id_prod)


def change_count_pr_user(id_prod: int, id_user: int, count: int) -> None:
    add_db("UPDATE user_prod SET count=%s WHERE id_user=%s and id_prod=%s",
           count, id_user, id_prod)


def add_shop_prod(id_prod: int, id_shop: int, count: int, price: decimal) -> None:
    tt = answer_bd('SELECT * FROM prod_shop WHERE id_prod=%s and id_shop=%s', id_prod, id_shop)
    if len(tt) == 0:
        add_db("insert into prod_shop values (%s, %s, %s, %s)", id_prod, id_shop, count, price)
    else:
        add_db("UPDATE prod_shop SET count=%s WHERE id_shop=%s and id_prod=%s",
               tt[0][2] + count, id_shop, id_prod)


def change_price_pr_shop(id_prod: int, id_shop: int, price: decimal) -> None:
    add_db("UPDATE prod_shop SET price=%s WHERE id_shop=%s and id_prod=%s",
           price, id_shop, id_prod)


def add_count_pr_shop(id_prod: int, id_shop: int, count: int) -> None:
    tt = answer_bd('SELECT * FROM prod_shop WHERE id_prod=%s and id_shop=%s', id_prod, id_shop)
    add_db("UPDATE prod_shop SET count=%s WHERE id_shop=%s and id_prod=%s",
           tt[0][2] + count, id_shop, id_prod)


#  поиск свободного индекса для пользователя
def free_user_id() -> int:
    all_users = answer_bd("SELECT * FROM users")
    if all_users:
        return max([i[0] for i in all_users]) + 1
    return 1


#  поиск свободного индекса для продукта
def free_product_id() -> int:
    all_prod = answer_bd("SELECT * FROM product")
    if all_prod:
        return max([i[0] for i in all_prod]) + 1
    return 1


def free_shop_id() -> int:
    all_shop = answer_bd("SELECT * FROM shop")
    if all_shop:
        return max([i[0] for i in all_shop]) + 1
    return 1


try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(dbname=NAME_DB, user=NAME_U, password=PASS, host=HOST)
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    all_fruit = cur.fetchall()
    cur.close()  # закрываем курсор
    conn.close()
    pprint.pprint(all_fruit)
except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Can`t establish connection to database')
