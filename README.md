# Scrapy - Yelp
Для запуска проекта необходимо:
- Насторить файл `settings.py`, для отправки статистики парсегна на почту 
```sh
MAIL_HOST = ''
MAIL_PORT = ''
MAIL_FROM = ''
MAIL_USER = ''
MAIL_PASS = ''
MAIL_TO = ''
```
- Насторить файл `alembic.ini`, для создания БД
```sh
sqlalchemy.url = ''
```
- Устанавливаем все пакеты
```sh
$ python start.py
```
- Запускаем Scrapy
```sh
$ python start_parse.py
```