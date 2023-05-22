# PostgreSQL - Система управления базами данных (СУБД/DBMS)
# Это ряд программ и интмрументов позволяющих создовать БД, управлять ею и манипулировать данными внутри(CRUD)

# Postgres - База данных, она объективно реалиционная, то есть хранятся в виде таблиц, и таблицы имеют свяхи между собой

# SQL (Structed Query language) - Декларативный язык структурных запросов, он применяется для создания и полусения данных при помощи 
# запросов в БД

#-----------------
# Команда для входа в бд через юзера postgres:
# sudo -u postgres psql

# Команда для входа:
# exit

# Команда для входа в своего юзера 
# psql

# Команда для выхода:
# \q

# Создание суперюзера
# CREATE ROLE "username" SUPERUSER LOGIN PASSWORD "1";

# Изменения пароля
# ALTER USER "username" WITH PASSWORD "1";

# создание бд
# CREATE DATABASE "name";

# \l - Список всех бд

# \du - Все юзеры

# \d - подробная инфа про таблицы(заранее подключится к бд)

# \dt -Все таблицы 

# \c "name" - Команда дл подключения бд

# psql -U <username> -d <dbnmae> - подключается под выбранным username к dbname
#
#-----------------------------------------------
# Типы полей в Postgres:
# Numeric Types (числовые)
    
#     a. smallint(2 bytes) -> -32767 to 32767
#     b. integer(4 bytes) -> -2.147... to 2.147...
#     c. bigint (8 bytes) -> infinite
#     d. real (4 bytes) -> float - число с плавающей число(макс 6 чисел после запятой)
#     f. double precsion (8 bytes) -> real с двойной точностью(в двое больше чисел)
#     d. serial (4 bytes) -> integer, auto - increment

# Character types(Символьные типы(строки))
#     a. varchar(кол-во символов) -> если мы укажем 50 символов, а заполним только 10, то оставлные будут свободны. Макс 255
#     b. char (кол-во символов) -> если мы укажем 50 символов, а заполним только 10, то оставлные будут пробелами. Макс 255
#     c. text() -> неограниченное кол-во символов

# Bollen Type
#     a. boolean(1 bytes) -> True/False

# date -> Клаендарная дата (год.месяц.день)

# location -> Координатная точка (x, y) - (245, -12)

# enumerate Type:
#     ('a','b','c')
#     CREATE TYPE <any name> AS ENUM ("Happy","Sad","Mad")
#_-----------------------------------------------------
# Команда для создания таблицы 
# CREATE TABLE <tablename>(
#     <colum> <type>,
# )

# CREATE TABLE films (
# code char(5),
# title varchar (100),
# date date,
# genre varchar(50),
# budget integer,
# country varchar(50),
# id serial
# );

# Команда для добавления данных в таблицу
# INSERT INTO <tabelname> [(colums)] VALUES (data),(data);

# insert into films(code, title, date, genre, budget, country) values('het5', 'lord of rings', '2001-07-11', 'fantasy', '1130000', 'usa');

# Команда для получения данных 
# SELECT (colums)* FROM <table>


# Команда для обновления данных
# UPDATE <table> SET <colum> = <new_value> WHERE <colum> = <value>

# Команда для удаления данных
# DELETE FROM <table> WHERE <colum> = <value>

# ORDER BY: Позволят сортировать выходящие данные по убыванию или возрастанию. ASС(по взростанию) DESC(По убыванию)
# SELECT <ROW> FROM <TABLENANE> ORDER BY <ROW> [ASC/DESC]


# WHERE: Используется для фильтрации по полям. будут выводится только те данные которые соответствую условию оператора
# SELECT <ROW> FROM <TABLENAME> WHERE <ROW> = ' Чему либо';

# BETWEEN: Условие между
# SELECT * FROM products WHERE id BETWEEN 3 and 8

# LIKE: Выводит результат который соответствует введенному щаблону для строк
# Чувствителен к регистру
# ILIKE: Тоже самое только не зависит от регистра
# SELECT <ROW> FROM <TABLENAME> WHERE <row> LIKE/ILIKE 'Чему либо'

# AND оператор и, для множественных условий 
# IN: WHERE <row> in (1,2,3,4);

# Экспорт бд(ДАМП):
# pg_dump -U <username> -d "bdname" > 'file.sql'   

# Импорт:
# psql -U <username> -d <dbname> -f <filename>

# LIMIT: Ставит онраничение в кол-ве получаемых данных

# DROP TABLE



# DELETE FORM <table> WHERE <colum> = <value>

# json является типом данных для баз данных 

#--------------------------------------------------------
# Связи между таблицами(relatioms)
    # 1. Оидн к одному (One to one) - Члеовек и паспорт
        # В одну из таблиц добавляется поле fk и дается ограничение unique
    # 2. Один ко многим (One to many) - Человек и банковские карты
        # В таблицу много добавляется поле fk
    # 3. Много к многим (Many to many) - Студенты и преподы
        # Создается вспомогательная таблица со связями

# Ограничения: 
    # 1. NOT NULL - Обязательно к заполнению
    # 2. UNIQUE - то что будут хранится только уникальные данные
    # 3. CHEK -> CHEK age > -1 - Ограничение проверки на улсовие
    # 4. PRIMARY KEY(для установки идентификатора данных в таблице)
    # 5. FOREIGN KEY(для установки связей между таблицами)
    # 6. ON DELETE - Дя установки поведения при удалении данных которые были связаны

