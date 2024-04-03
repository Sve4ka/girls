#  программа для обращения к базе данных


import pprint
import psycopg2
from config import NAME_DB, NAME_U, PASS, HOST


# обращение базе данных и получение данных о всех магазинах
def get_all_my_shop(user_id) -> list:  # TODO
    return ['apple', 'banana', 'cherry']


# обращение базе данных и получение данных о всех принадлежащщих человеку продуктов
def get_all_my_product(user_id) -> list:  # TODO
    return ['apple', 'banana', 'cherry', 'kiwi', 'pineapple']


# обращение базе данных и получение данных о всех продуктов принадлежащих магазину
def get_shop_product(user_id, shop_id) -> list:  # TODO
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


#  проверить наличие данного юзера в базе данных
def search_user(id: int) -> bool:  # TODO
    pass


#  добавление юзера в бд
def add_user(id: int, name: str) -> None:  # TODO
    pass


#  добавление нового продукта в бд
def add_product(id_seller: int, price: float, name: str, count: int) -> None:  # TODO
    pass


#  поиск свободного индекса для пользователя
def free_user_id() -> int:  # TODO
    pass


#  поиск свободного индекса для продукта
def free_product_id() -> int:  # TODO
    pass


try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(dbname=NAME_DB, user=NAME_U, password=PASS, host=HOST)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM fruit')
    all_fruit = cursor.fetchall()
    cursor.close()  # закрываем курсор
    conn.close()
    pprint.pprint(all_fruit)
except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Can`t establish connection to database')
