#!/usr/bin/python3
from sqlalchemy.engine.url import URL

postgres_db = {'drivername': 'postgres',
               'username': 'postgres',
               'password': 'postgres',
               'host': '192.168.99.100',
               'port': 5432}
print(URL.create(**postgres_db))

sqlite_db = {'drivername': 'sqlite', 'database': 'db.sqlite'}
print(URL.create(**sqlite_db))

connection_config = {
    'drivername': 'mysql',
    'username': 'root',
    'password': 'root',
    'host': 'localhost',
    'port': 3306,
    'database': 'my_db',
}

charset = 'utf8'
url = URL.create(**connection_config)
url = str(url) + f'?charset={charset}'
print(url)
