# Лекция 16. СУБД. DQL. SELECT. Индексы. Group by. Joins.

### Оглавление курса

- Блок 1 — Python Basic (1–6):
  - [Лекция 1. Введение. Типизации. Переменные. Строки и числа. Булева алгебра. Ветвление](lesson01.md)
  - [Лекция 2. Обработка исключений. Списки, строки детальнее, срезы, циклы.](lesson02.md)
  - [Лекция 3: None. Range, list comprehension, sum, max, min, len, sorted, all, any. Работа с файлами](lesson03.md)
  - [Лекция 4. Хэш таблицы. Set, frozenset. Dict. Tuple. Немного об импортах. Namedtuple, OrderedDict](lesson04.md)
  - [Лекция 5. Функции, типизация, lambda. Map, zip, filter.](lesson05.md)
  - [Лекция 6. Рекурсия. Алгоритмы. Бинарный поиск, сортировки](lesson06.md)
- Блок 2 — Git (7–8):
  - [Лекция 7. Git. История системы контроля версий. Локальный репозиторий. Базовые команды управления репозиторием.](lesson07.md)
  - [Лекция 8. Git. Удаленный репозиторий. Remote, push, pull. GitHub, Bitbucket, GitLab, etc. Pull request.](lesson08.md)
- Блок 3 — Python Advanced (9–14):
  - [Лекция 9. Введение в ООП. Основные парадигмы ООП. Классы и объекты.](lesson09.md)
  - [Лекция 10. Множественное наследование. MRO. Magic methods.](lesson10.md)
  - [Лекция 11. Imports. Standard library. PEP8](lesson11.md)
  - [Лекция 12. Декораторы. Декораторы с параметрами. Декораторы классов (staticmethod, classmethod, property)](lesson12.md)
  - [Лекция 13. Тестирование](lesson13.md)
  - [Лекция 14. Проектирование. Паттерны. SOLID.](lesson14.md)
- Блок 4 — SQL (15–17):
  - [Лекция 15. СУБД. PostgreSQL. SQL. DDL. Пользователи. DCL. DML. Связи.](lesson15.md)
  - ▶ **Лекция 16. СУБД. DQL. SELECT. Индексы. Group by. Joins.**
  - [Лекция 17. СУБД. Нормализация. Аномалии. Транзакции. ACID. TCL. Backup](lesson17.md)
- Вне блоков:
  - [Лекция 18. Virtual env. Pip. Устанавливаемые модули. Pyenv.](lesson18.md)
- Блок 5 — Django (19–26):
  - [Лекция 19. Знакомство с Django](lesson19.md)
  - [Лекция 20. Templates. Static](lesson20.md)
  - [Лекция 21. Модели. Связи. Meta. Abstract, proxy.](lesson21.md)
  - [Лекция 22. Django ORM.](lesson22.md)
  - [Лекция 23. Forms, ModelForms. User, Authentication.](lesson23.md)
  - [Лекция 24. ClassBaseView](lesson24.md)
  - [Лекция 25. NoSQL. Куки, сессии, кеш](lesson25.md)
  - [Лекция 26. Логирование. Middleware. Signals. Messages. Manage commands](lesson26.md)
- Блок 6 — Django Rest Framework (27–30):
  - [Лекция 27. Что такое API. REST и RESTful. Django REST Framework.](lesson27.md)
  - [Лекция 28. @api_view, APIView, ViewSets, Pagination, Routers](lesson28.md)
  - [Лекция 29. REST аутентификация. Авторизация. Permissions. Фильтрация.](lesson29.md)
  - [Лекция 30. Тестирование. Django, REST API.](lesson30.md)
- Блок 7 — Python async (31–33):
  - [Лекция 31. Celery. Multithreading. GIL. Multiprocessing](lesson31.md)
  - [Лекция 32. Асинхронное программирование в Python. Корутины. Asyncio.](lesson32.md)
  - [Лекция 33. Сокеты. Django channels.](lesson33.md)
- Блок 8 — Deployment (34–35):
  - [Лекция 34. Linux. Все что нужно знать для деплоймента.](lesson34.md)
  - [Лекция 35. Deployment](lesson35.md)
- Вне блоков:
  - [Лекция 36. Методологии разработки. CI/CD. Монолит и микросервисы. Docker](lesson36.md)


![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSet_oHygtk-HIEN4JI7Y8Ma0_UF0Co3HaHwQ&s)

## DQL (Data query language) (Язык запроса данных)

`DQL` - Еще одна подгруппа языка `SQL` которая состоит из всего одного слова `SELECT`.
Но, не спешим радоваться, в нем деталей примерно как во всех прошлых командах вместе взятых.

## SELECT

Самый простой вариант запроса выглядит так:

```sql
SELECT *
FROM book;
```

Выбрать все столбцы и все колонки из таблицы `book`.
> В продакшене старайтесь избегать SELECT * — лучше явно перечислять нужные столбцы.


Можно выбрать только часть столбцов:

```sql
SELECT title, page_count
FROM book;
```

Теперь мы выбираем только колонки `title` и `page_count`.

На самом деле SQL является еще и калькулятором, поэтому мы можем получить не только значение, но и вычисления:

```sql
SELECT title, page_count / 2
FROM book;
```

Тут мы разделили количество страниц в книге на 2.

> Вообще SQL можно использовать как калькулятор и без данных. Это довольно странно, но можно.

```sql
SELECT 40 + 2;
```

### Условия выбора (WHERE)

В реальности, доставать все данные из таблицы практически никогда не нужно. Обычно мы вытаскиваем только необходимую нам
информацию.

```sql
SELECT id, name, author
FROM book
WHERE author = 'King';

SELECT id, name
FROM book
WHERE genre IN ('Action', 'Comedy');


SELECT id, name
FROM book
WHERE page_count BETWEEN 100 AND 200;
```

В первом запросе мы вытаскиваем все книги у которых в поле автор записано `King`.
Во втором, все книги у которых жанр это `Action` или `Comedy`.
В третьем все книги у которых кол-во страниц от 100 до 200.

> Естественно все условия можно комбинировать через `OR` и `AND`

### Именование полученной таблицы

Для того чтобы назвать результаты ваших запросов, можно использовать ключевое слово `as`. Это нам ещё в дальнейшем
понадобится.

```sql
SELECT title, page_count / 2 as sheets
FROM book;
```

Тут `sheets` это метка

> Метки часто называют словом псевдоним

### DISTINCT

Ключевое слово `DISTINCT` используется, чтобы получить только уникальные значения для какого-либо поля.

```sql
SELECT DISTINCT publisher
FROM book;
```

Чтобы получить список уникальных издателей для всех книг.

### Сортировка (ORDER BY)

Часто нам необходимо данные отсортировать на этапе получения.

Для этого нам поможет `ORDER BY`:

```sql
SELECT title, publisher_id
FROM book
ORDER BY title;
```

Что можно делать с сортировкой:

- Указывать порядок (прямой или обратный)
- Указывать более одного поля для сортировки

Примеры:

Указываем порядок:

```sql
SELECT title, publisher_id
FROM book
ORDER BY title ASC;

SELECT title, publisher_id
FROM book
ORDER BY title DESC;
```

Указываем несколько полей для сортировки.

```sql
SELECT title, publisher_id
FROM book
ORDER BY title, publisher_id DESC;

SELECT title, publisher_id
FROM book
ORDER BY title DESC, publisher ASC;
```

### Ограничения (LIMIT)

Также мы можем ограничить количество получаемых результатов. Зачем это делать? А что если под наше условие подходит
миллиард записей? Сможем ли мы их все обработать? Думаю, что нет. Но мы всегда можем указать необходимую нам сортировку,
и только после этого указать лимит в каком-то небольшом количестве данных.

```sql
SELECT *
FROM publisher
LIMIT 10;
```

Вернет только первые 10 значений.

```sql
SELECT *
FROM publisher
LIMIT 10 OFFSET 10;
```

Вернет значения с 11-ого по 20-е. `OFFSET` - сдвиг по данным.

## Индексация

![](https://media.dev.to/cdn-cgi/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fa80rqyke0it7ud4j2nmg.png)

Индекс в базе данных — это специальная структура данных, которая улучшает скорость поиска данных в таблице. Индексы
создаются на основе одного или нескольких столбцов таблицы и позволяют быстро находить строки, удовлетворяющие
определенным условиям.

> Представьте индекс как оглавление книги: вместо того чтобы просматривать всю книгу, чтобы найти нужную информацию, вы
> можете просто заглянуть в оглавление и быстро перейти к нужной странице.

### Типы индексов в PostgreSQL

Индексы бывают разных типов, разные типы используются часто для разных типов данных. Вникать в детали нам пока нет
никакой необходимости, но я их перечислю.

#### B-Tree Индексы

Это самый распространенный тип индекса. B-Tree индексы используются по умолчанию при создании индекса и подходят для
большинства операций поиска и сортировки. (Работают на бинарном поиске)

#### Hash Индексы

Эти индексы полезны для операций равенства. Они не поддерживают диапазонные запросы и не так универсальны, как B-Tree
индексы.

#### GiST Индексы (Generalized Search Tree)

Используются для более сложных типов данных, таких как геометрические и полнотекстовые поиски.

#### GIN Индексы (Generalized Inverted Index)

Эти индексы эффективны для поиска в больших текстовых полях и массивных данных.

#### BRIN Индексы (Block Range INdexes)

Индексы, которые используются для очень больших таблиц, где данные имеют четкий порядок. Они занимают меньше места и
подходят для диапазонных запросов.

### Создание индексов

#### Создание B-Tree Индекса

```sql
CREATE INDEX index_name ON table_name (column_name);
```

Пример:

```sql
CREATE INDEX idx_users_last_name ON users (last_name);
```

Этот индекс ускорит запросы, которые фильтруют или сортируют данные по `last_name`.

### Создание уникального индекса

Уникальные индексы обеспечивают уникальность значений в столбце.

```sql
CREATE UNIQUE INDEX index_name ON table_name (column_name);
```

Пример:

```sql
CREATE UNIQUE INDEX idx_unique_email ON users (email);
```

### Создание многоколоночного индекса

Да, индекс не всегда привязан к одному полю

```sql
CREATE INDEX index_name ON table_name (column1, column2);
```

Пример:

```sql
CREATE INDEX idx_users_last_first_name ON users (last_name, first_name);
```

#### Функциональные и частичные индексы

- Индекс по выражению (expression index), напр. регистронезависимый поиск:

```sql
CREATE INDEX CONCURRENTLY idx_users_email_lower ON users (lower(email));
```

- Частичный индекс (partial):

```sql
CREATE INDEX idx_orders_open ON orders (created_at) WHERE status = 'open';
```

- Покрывающий индекс (INCLUDE):

```sql
CREATE INDEX idx_orders_user ON orders (user_id) INCLUDE (created_at);
```

Примечания:
- Порядок полей в многоколоночном индексе важен (левосторонний префикс).
- Для снижения блокировок используйте CREATE INDEX CONCURRENTLY / DROP INDEX CONCURRENTLY.
- Проверяйте планы запросов через EXPLAIN/EXPLAIN ANALYZE.

Этот индекс будет полезен для запросов, использующих оба столбца `last_name` и `first_name`.

### Использование индексов в запросах

Ничего дополнительного делать с индексом не нужно, если он есть, он уже будет влиять на работу системы.

#### Пример с использованием индекса

```sql
SELECT *
FROM users
WHERE last_name = 'Smith';
```

Если у нас есть индекс на столбце `last_name`, то этот запрос выполнится значительно быстрее.

#### Индексы и сортировка

```sql
SELECT *
FROM users
ORDER BY last_name;
```

Индекс на `last_name` также ускорит выполнение этого запроса.

### Управление индексами

#### Просмотр существующих индексов

Чтобы увидеть все индексы в таблице, можно использовать следующую команду:

```sql
\d table_name
```

#### Удаление индекса

Если индекс больше не нужен, его можно удалить:

```sql
DROP INDEX index_name;
```

Пример:

```sql
DROP INDEX idx_users_last_name;
```

### Проблемы связанные с индексами

А если все так хорошо и быстро, почему бы нам не создать индексы вообще на все поля и все будет работать быстрее?

И да и нет.

Если бы у нас были только операции чтения, то это было бы идеальное решение. Но у нас есть и другие операции.

Представьте книгу у которой есть оглавление (по сути та же индексация). Пока мы можем только читать книгу, проблем нет,
добавили несколько страниц в начале, чем упростили жизнь.

Но теперь представьте, что вы в эту книгу начинаете дописывать/удалять/изменять страницы или целые главы.

Для каждой такой операции, оглавление придется переписывать заново.

> Если в таблицу часто производится запись/изменение/удаление, то индекс только замедлил работу базы! А он еще и место
> занимает! Поэтому всегда нужно очень аккуратно относиться к индексам, это очень хороший инструмент, который легко
> может
> все сломать

## Встроенные функции

В `SQL` встроено довольно-таки большое количество функций которыми мы можем пользоваться и часть из них будет
использована в дальнейшем для агрегации данных, давайте с некоторыми из них познакомимся.

### Логические операторы и операторы сравнения

Таблица истинности для SQL, учитывающая `NULL`, отличается от обычной таблицы истинности, так как `NULL` в SQL
представляет неопределенное значение. В операциях сравнения и логических операциях `NULL` ведет себя особым образом.

Вот таблица истинности для SQL с учетом `NULL`:

### Логические операторы (AND, OR, NOT)

| A     | B     | A AND B | A OR B | NOT A |
|-------|-------|---------|--------|-------|
| TRUE  | TRUE  | TRUE    | TRUE   | FALSE |
| TRUE  | FALSE | FALSE   | TRUE   | FALSE |
| TRUE  | NULL  | NULL    | TRUE   | FALSE |
| FALSE | TRUE  | FALSE   | TRUE   | TRUE  |
| FALSE | FALSE | FALSE   | FALSE  | TRUE  |
| FALSE | NULL  | FALSE   | NULL   | TRUE  |
| NULL  | TRUE  | NULL    | TRUE   | NULL  |
| NULL  | FALSE | FALSE   | NULL   | NULL  |
| NULL  | NULL  | NULL    | NULL   | NULL  |

### Операторы сравнения (=, <>, <, >, <=, >=)

| A     | B     | A = B | A <> B | A < B | A > B | A <= B | A >= B |
|-------|-------|-------|--------|-------|-------|--------|--------|
| TRUE  | TRUE  | TRUE  | FALSE  | FALSE | FALSE | TRUE   | TRUE   |
| TRUE  | FALSE | FALSE | TRUE   | FALSE | TRUE  | FALSE  | TRUE   |
| TRUE  | NULL  | NULL  | NULL   | NULL  | NULL  | NULL   | NULL   |
| FALSE | TRUE  | FALSE | TRUE   | TRUE  | FALSE | TRUE   | FALSE  |
| FALSE | FALSE | TRUE  | FALSE  | FALSE | FALSE | TRUE   | TRUE   |
| FALSE | NULL  | NULL  | NULL   | NULL  | NULL  | NULL   | NULL   |
| NULL  | TRUE  | NULL  | NULL   | NULL  | NULL  | NULL   | NULL   |
| NULL  | FALSE | NULL  | NULL   | NULL  | NULL  | NULL   | NULL   |
| NULL  | NULL  | NULL  | NULL   | NULL  | NULL  | NULL   | NULL   |

### Примечания:

1. **Логические операторы:**
    - `A AND B` вернет `TRUE`, только если оба значения `TRUE`.
    - `A OR B` вернет `TRUE`, если хотя бы одно значение `TRUE`.
    - `NOT A` вернет противоположное значение, если `A` не `NULL`.

2. **Операторы сравнения:**
    - Любое сравнение с `NULL` всегда возвращает `NULL` (неопределенное).

Эти правила делают работу с `NULL` в SQL специфической, и при работе с данными нужно учитывать, что `NULL` не
эквивалентен ни `TRUE`, ни `FALSE`, а представляет собой третье состояние, которое требует особого внимания при
логических и сравнительных операциях.

### Математические действия и операторы

Прежде чем мы перейдем к математическим функциям, давайте рассмотрим основные математические операции в SQL:

- **Сложение (+)**: складывает два числа.
  ```sql
  SELECT 5 + 3 AS sum_result; -- Результат: 8
  ```
- **Вычитание (-)**: вычитает одно число из другого.
  ```sql
  SELECT 5 - 3 AS subtract_result; -- Результат: 2
  ```
- **Умножение (*)**: умножает два числа.
  ```sql
  SELECT 5 * 3 AS multiply_result; -- Результат: 15
  ```
- **Деление (/)**: делит одно число на другое.
  ```sql
  SELECT 6 / 3 AS divide_result; -- Результат: 2
  ```
- **Остаток от деления (%)**: возвращает остаток от деления одного числа на другое.
  ```sql
  SELECT 5 % 3 AS mod_result; -- Результат: 2
  ```

> Естественно их больше, если нужно что-то специфическое, обратитесь к документации.

### Математические функции и операторы

Математические функции позволяют выполнять различные математические операции с данными.

**Примеры:**

- `ABS(x)` — возвращает абсолютное значение числа `x`.
- `ROUND(x, d)` — округляет число `x` до `d` знаков после запятой.
- `CEIL(x)` — округляет число `x` до ближайшего большего целого.
- `FLOOR(x)` — округляет число `x` до ближайшего меньшего целого.
- `POWER(x, y)` — возвращает результат возведения `x` в степень `y`.

**Пример запроса:**

```sql
SELECT ABS(-15)           AS abs_value,
       ROUND(123.4567, 2) AS rounded_value,
       CEIL(4.3)          AS ceil_value,
       FLOOR(4.7)         AS floor_value,
       POWER(2, 3)        AS power_value;
```

### Функции для работы со строками

Функции для работы со строками помогают манипулировать строковыми данными.

**Примеры:**

- `LENGTH(str)` — возвращает длину строки `str`.
- `UPPER(str)` — преобразует строку `str` в верхний регистр.
- `LOWER(str)` — преобразует строку `str` в нижний регистр.
- `SUBSTRING(str, start, length)` — возвращает подстроку из строки `str`, начиная с позиции `start` и длиной `length`.
- `TRIM(str)` — удаляет пробелы с начала и конца строки `str`.

**Пример запроса:**

```sql
SELECT LENGTH('Hello, World!')          AS length_value,
       UPPER('hello')                   AS upper_value,
       LOWER('WORLD')                   AS lower_value,
       SUBSTRING('Hello, World!', 8, 5) AS substring_value,
       TRIM('  Hello  ')                AS trimmed_value;
```

### Функции для работы с датами и временем

Эти функции позволяют выполнять операции с датами и временем.

**Примеры:**

- `CURRENT_DATE` — возвращает текущую дату.
- `CURRENT_TIME` — возвращает текущее время.
- `now() + interval 'N unit'` — добавить/вычесть интервал ко времени/дате (например: + interval '5 days').
- `age(date2, date1)` — возвращает разницу между двумя датами (interval).
- `to_char(date, 'YYYY-MM-DD')` — форматирование даты/времени в строку.
- `EXTRACT(what FROM what)` - извлечь часть даты.

**Пример запроса:**

```sql
SELECT CURRENT_DATE                              AS current_date,
       CURRENT_TIME                              AS current_time,
       now() + interval '5 days'                 AS new_date,
       age(date '2023-08-10', date '2023-08-01') AS date_difference,
       to_char(CURRENT_DATE, 'YYYY-MM-DD')       AS formatted_date,
       EXTRACT(YEAR FROM date '2023-08-01');
```

### Оператор `LIKE`

Оператор `LIKE` используется для поиска по шаблону в строках.

**Примеры:**

- `%` — заменяет ноль или более символов.
- `_` — заменяет ровно один символ.

- ILIKE — регистронезависимый вариант LIKE в PostgreSQL.

**Пример запроса:**

```sql
SELECT *
FROM employees
WHERE name LIKE 'J%'; -- имена, начинающиеся с 'J'

SELECT *
FROM employees
WHERE name LIKE '_a%'; -- имена, где второй символ 'a'
```

### Функции форматирования

Функции форматирования позволяют изменить представление данных, например, чисел или дат.

**Примеры:**

- `to_char(number, 'FM999,999,990.00')` — форматирует число в соответствии с заданным форматом.
- `CAST(expression AS datatype)` — преобразует одно значение в другой тип данных.

**Пример запроса:**

```sql
SELECT to_char(123456.789, 'FM999,999,990.00') AS formatted_number,
       CAST('2024-08-01' AS TIMESTAMP)         AS casted_date;
```

### Агрегатные функции

Агрегатные функции выполняют вычисления над набором значений и возвращают одно значение.

**Примеры:**

- `COUNT(column)` — возвращает количество строк.
- `SUM(column)` — возвращает сумму значений в колонке.
- `AVG(column)` — возвращает среднее значение.
- `MAX(column)` — возвращает максимальное значение.
- `MIN(column)` — возвращает минимальное значение.

**Пример запроса:**

```sql
SELECT COUNT(*)    AS total_count,
       SUM(salary) AS total_salary,
       AVG(salary) AS average_salary,
       MAX(salary) AS max_salary,
       MIN(salary) AS min_salary
FROM employees;
```

## `GROUP BY` и `HAVING` в SQL

Обсудим `GROUP BY` и `HAVING` в SQL. Эти операторы позволяют группировать данные и фильтровать их на основе агрегатных
функций. Мы рассмотрим, как использовать эти операторы, приведем примеры запросов и разберем возможные применения.

### Введение в оператор `GROUP BY`

Оператор `GROUP BY` используется для группировки строк, имеющих одинаковые значения в определенных столбцах. После
группировки можно применять агрегатные функции, такие как `COUNT`, `SUM`, `AVG`, `MAX`, `MIN`, к каждой группе.

**Пример структуры запроса:**

```sql
SELECT column1, column2, AGGREGATE_FUNCTION(column3)
FROM table_name
GROUP BY column1, column2;
```

Важно: в SELECT при GROUP BY допустимы только агрегатные функции и/или столбцы, указанные в GROUP BY.

**Пример запроса:**

```sql
SELECT department, COUNT(employee_id) AS employee_count
FROM employees
GROUP BY department;
```

В этом примере все сотрудники группируются по отделам, и для каждого отдела подсчитывается количество сотрудников.

### Агрегатные функции с `GROUP BY`

Агрегатные функции играют важную роль при использовании `GROUP BY`. Вот несколько примеров:

- `COUNT(column)` — подсчитывает количество строк в каждой группе.
- `SUM(column)` — суммирует значения столбца в каждой группе.
- `AVG(column)` — вычисляет среднее значение столбца в каждой группе.
- `MAX(column)` — находит максимальное значение в каждой группе.
- `MIN(column)` — находит минимальное значение в каждой группе.

**Пример запроса:**

```sql
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department;
```

Этот запрос группирует сотрудников по отделам и вычисляет среднюю зарплату в каждом отделе.

### Введение в оператор `HAVING`

Оператор `HAVING` используется для фильтрации групп, образованных с помощью `GROUP BY`, на основе условий, которые
применяются к агрегатным функциям. Он аналогичен оператору `WHERE`, но применяется после группировки.

Где применять фильтры: WHERE - до группировки (фильтрует строки), HAVING - после группировки (фильтрует группы).

**Пример структуры запроса:**

```sql
SELECT column1, AGGREGATE_FUNCTION(column2)
FROM table_name
GROUP BY column1
HAVING AGGREGATE_FUNCTION(column2) condition;
```

**Пример запроса:**

```sql
SELECT department, COUNT(employee_id) AS employee_count
FROM employees
GROUP BY department
HAVING COUNT(employee_id) > 10;
```

Этот запрос группирует сотрудников по отделам и отображает только те отделы, в которых количество сотрудников больше 10.

### Совместное использование `GROUP BY` и `HAVING`

Часто `GROUP BY` и `HAVING` используются вместе для выполнения сложных запросов.

**Пример запроса:**

```sql
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

Этот запрос группирует сотрудников по отделам, вычисляет среднюю зарплату в каждом отделе и отображает только те отделы,
где средняя зарплата превышает 50000.

### Примеры использования `GROUP BY` и `HAVING` в реальных задачах

**Пример 1: Количество продаж по каждому продавцу**

```sql
SELECT salesperson_id, COUNT(sale_id) AS total_sales
FROM sales
GROUP BY salesperson_id;
```

Этот запрос отображает количество продаж, совершенных каждым продавцом.

**Пример 2: Средняя оценка студентов по каждому курсу**

```sql
SELECT course_id, AVG(grade) AS average_grade
FROM grades
GROUP BY course_id;
```

Этот запрос группирует оценки студентов по курсам и вычисляет среднюю оценку для каждого курса.

**Пример 3: Курсы с количеством студентов больше 30**

```sql
SELECT course_id, COUNT(student_id) AS student_count
FROM enrollments
GROUP BY course_id
HAVING COUNT(student_id) > 30;
```

Этот запрос отображает только те курсы, на которых зарегистрировано больше 30 студентов.

## Вложенность

На самом деле в любом месте запроса, можно разместить другой запрос (внутри `WHERE`, внутри `FROM` итд)

```sql
SELECT *
FROM tbl
WHERE c1 > 5;

SELECT *
FROM tbl
WHERE c1 IN (1, 2, 3);

SELECT *
FROM tbl
WHERE c1 IN (SELECT c1 FROM t2);

SELECT *
FROM tbl
WHERE c1 IN (SELECT c3 FROM t2 WHERE c2 = tbl.c1 + 10);

SELECT *
FROM tbl
WHERE c1 BETWEEN (SELECT c3 FROM t2 WHERE c2 = tbl.c1 + 10) AND 100;

SELECT *
FROM tbl
WHERE EXISTS (SELECT c1 FROM t2 WHERE c2 > tbl.c1);
```

### Оператор WITH

Для упрощения понимания некоторых запросов, мы можем применить оператор `WITH`, который является именованным подзапросом (CTE). Это позволяет вынести сложный подзапрос и затем переиспользовать его по имени.

```sql
-- select top revenue months
WITH monthly_revenue AS (SELECT EXTRACT(YEAR FROM date)  AS year,
                                EXTRACT(MONTH FROM date) AS month,
                                SUM(amount)              AS total_amount
                         FROM revenue
                         GROUP BY year, month
                         )
SELECT *
FROM monthly_revenue
WHERE total_amount > (SELECT SUM(total_amount) / 100 FROM monthly_revenue)
ORDER BY total_amount DESC;
```

> Получение самых прибыльных месяцев

### Использование операторов `UNION`, `INTERSECT` и `EXCEPT` в SQL

Обсудим три мощных оператора в SQL: `UNION`, `INTERSECT` и `EXCEPT`. Эти операторы используются для комбинирования
результатов двух или более запросов, позволяя выполнять сложные операции с множествами данных. Давайте рассмотрим каждый
из них подробнее, включая синтаксис, примеры и случаи применения.

#### Оператор `UNION`

Оператор `UNION` объединяет результаты двух или более запросов в одну результирующую таблицу. Он исключает дублирующиеся
строки, возвращая только уникальные записи. Если необходимо сохранить дублирующиеся строки, используется
оператор `UNION ALL`.

**Синтаксис:**

```sql
SELECT column1, column2
FROM table1
UNION
SELECT column1, column2
FROM table2;
```

**Пример:**

```sql
SELECT name, email
FROM customers
UNION
SELECT name, email
FROM prospects;
```

Этот запрос объединяет списки имен и email-адресов из таблиц `customers` и `prospects`, исключая дубликаты.

**Пример с `UNION ALL`:**

```sql
SELECT name, email
FROM customers
UNION ALL
SELECT name, email
FROM prospects;
```

Этот запрос объединяет списки имен и email-адресов, включая все дублирующиеся записи.

#### Оператор `INTERSECT`

Оператор `INTERSECT` возвращает только те строки, которые присутствуют в обоих запросах. Он используется для нахождения
пересечения множеств данных.

**Синтаксис:**

```sql
SELECT column1, column2
FROM table1
INTERSECT
SELECT column1, column2
FROM table2;
```

**Пример:**

```sql
SELECT name, email
FROM customers
INTERSECT
SELECT name, email
FROM newsletter_subscribers;
```

Этот запрос возвращает список имен и email-адресов, которые есть как в таблице `customers`, так и в
таблице `newsletter_subscribers`.

#### Оператор `EXCEPT`

Оператор `EXCEPT` возвращает строки из первого запроса, которых нет во втором запросе. Он используется для нахождения
разности множеств данных.

**Синтаксис:**

```sql
SELECT column1, column2
FROM table1
EXCEPT
SELECT column1, column2
FROM table2;
```

**Пример:**

```sql
SELECT name, email
FROM customers
EXCEPT
SELECT name, email
FROM unsubscribed_users;
```

Этот запрос возвращает список имен и email-адресов, которые есть в таблице `customers`, но отсутствуют в
таблице `unsubscribed_users`.

#### Важные замечания

1. **Количество и типы столбцов:** Все запросы, объединяемые с помощью `UNION`, `INTERSECT` и `EXCEPT`, должны
   возвращать одинаковое количество столбцов, и типы данных этих столбцов должны быть совместимы.
2. **Порядок сортировки:** Для упорядочивания результатов объединенных запросов используется оператор `ORDER BY` после
   всех объединенных запросов.

**Пример с `ORDER BY`:**

```sql
SELECT name, email
FROM customers
UNION
SELECT name, email
FROM prospects
ORDER BY name;
```

Этот запрос объединяет списки имен и email-адресов, исключает дубликаты и сортирует результат по имени.

#### Примеры использования в реальных задачах

1. **Объединение данных из нескольких таблиц:**

```sql
SELECT product_id, product_name
FROM warehouse_1
UNION
SELECT product_id, product_name
FROM warehouse_2;
```

Этот запрос объединяет списки продуктов из двух складов.

2. **Поиск общих записей:**

```sql
SELECT student_id, course_id
FROM course_enrollments_spring
INTERSECT
SELECT student_id, course_id
FROM course_enrollments_fall;
```

Этот запрос находит студентов, которые зарегистрировались на один и тот же курс как весной, так и осенью.

3. **Исключение данных:**

```sql
SELECT employee_id, name
FROM employees
EXCEPT
SELECT employee_id, name
FROM retired_employees;
```

Этот запрос возвращает список действующих сотрудников, исключая тех, кто вышел на пенсию.

## Использование оператора `JOIN` в SQL

Использование оператора `JOIN` в SQL для объединения таблиц. Вы же еще помните, что таблицы в базе могут и даже должны
быть связаны? Так вот чаще всего нам нужно будет извлекать данных именно из связанных таблиц, а для этого нам
понадобится оператор `JOIN`

### Временное именование таблиц

В SQL часто возникает необходимость упростить запись запросов, особенно когда таблицы имеют длинные названия. Для этого
можно использовать временные имена (алиасы). Алиасы создаются с помощью ключевого слова `AS`. Я уже использовал их чуть
выше в примерах, давайте разберемся

**Пример:**

```sql
SELECT e.name, d.name
FROM employees AS e
         JOIN departments AS d ON e.department_id = d.id;
```

В этом примере `employees` временно именуется как `e`, а `departments` — как `d`. Это делает запрос более читабельным и
менее громоздким.

### про `JOIN`

![](https://external-preview.redd.it/6J5DBM3M4E4MLs5ci7DfWu0XL7vvG5fUG8NPXVcthRo.jpg?auto=webp&s=28f061e74b66aebb9d89e21a81e5162a4201a5e5)

Операторы `JOIN` используются для объединения строк из двух или более таблиц на основе связующего условия. Существует
несколько типов `JOIN`:

1. **INNER JOIN**
2. **LEFT JOIN (или LEFT OUTER JOIN)**
3. **RIGHT JOIN (или RIGHT OUTER JOIN)**
4. **FULL JOIN (или FULL OUTER JOIN)**
5. **CROSS JOIN**
6. **SELF JOIN**

Рассмотрим данные для примеров:

**Таблица `employees`:**

| employee_id | name  | department_id | manager_id |
|-------------|-------|---------------|------------|
| 1           | Alice | 1             | NULL       |
| 2           | Bob   | 2             | 1          |
| 3           | Carol | 1             | 1          |
| 4           | Dave  | NULL          | 2          |
| 5           | Eve   | 3             | 2          |

**Таблица `departments`:**

| department_id | name        |
|---------------|-------------|
| 1             | Sales       |
| 2             | Engineering |
| 3             | HR          |
| 4             | Marketing   |

### INNER JOIN

`INNER JOIN` возвращает строки, у которых есть совпадающие значения в обеих таблицах.

**Пример:**

```sql
SELECT e.name AS employee_name, d.name AS department_name
FROM employees AS e
         INNER JOIN departments AS d ON e.department_id = d.department_id;
```

**Результат:**

| employee_name | department_name |
|---------------|-----------------|
| Alice         | Sales           |
| Bob           | Engineering     |
| Carol         | Sales           |
| Eve           | HR              |

### LEFT JOIN
#### USING

Короткая форма соединения, если имя ключевого столбца совпадает в обеих таблицах:

```sql
SELECT e.name, d.name
FROM employees e
JOIN departments d USING (department_id);
```


`LEFT JOIN` возвращает все строки из левой таблицы и совпадающие строки из правой таблицы. Если совпадений нет, то
возвращаются `NULL` для столбцов правой таблицы.

**Пример:**

```sql
SELECT e.name AS employee_name, d.name AS department_name
FROM employees AS e
         LEFT JOIN departments AS d ON e.department_id = d.department_id;
```

**Результат:**

| employee_name | department_name |
|---------------|-----------------|
| Alice         | Sales           |
| Bob           | Engineering     |
| Carol         | Sales           |
| Dave          | NULL            |
| Eve           | HR              |

### RIGHT JOIN

> Примечание: на практике RIGHT JOIN используется редко; чаще такой запрос переписывают через LEFT JOIN.

`RIGHT JOIN` возвращает все строки из правой таблицы и совпадающие строки из левой таблицы. Если совпадений нет, то
возвращаются `NULL` для столбцов левой таблицы.

**Пример:**

```sql
SELECT e.name AS employee_name, d.name AS department_name
FROM employees AS e
         RIGHT JOIN departments AS d ON e.department_id = d.department_id;
```

**Результат:**

| employee_name | department_name |
|---------------|-----------------|
| Alice         | Sales           |
| Bob           | Engineering     |
| Carol         | Sales           |
| Eve           | HR              |
| NULL          | Marketing       |

### FULL JOIN

`FULL JOIN` возвращает все строки, когда есть совпадения в левой или правой таблицах. Если совпадений нет, то
возвращаются `NULL` для отсутствующих совпадений с обеих сторон.

**Пример:**

```sql
SELECT e.name AS employee_name, d.name AS department_name
FROM employees AS e
         FULL JOIN departments AS d ON e.department_id = d.department_id;
```

**Результат:**

| employee_name | department_name |
|---------------|-----------------|
| Alice         | Sales           |
| Bob           | Engineering     |
| Carol         | Sales           |
| Dave          | NULL            |
| Eve           | HR              |
| NULL          | Marketing       |

### CROSS JOIN

`CROSS JOIN` возвращает декартово произведение двух таблиц, то есть каждая строка из первой таблицы соединяется с каждой
строкой из второй таблицы.

> Осторожно: результат — декартово произведение; размер результата растёт как N×M.

**Пример:**

```sql
SELECT e.name AS employee_name, d.name AS department_name
FROM employees AS e
         CROSS JOIN departments AS d;
```

**Результат:**

| employee_name | department_name |
|---------------|-----------------|
| Alice         | Sales           |
| Alice         | Engineering     |
| Alice         | HR              |
| Alice         | Marketing       |
| Bob           | Sales           |
| Bob           | Engineering     |
| Bob           | HR              |
| Bob           | Marketing       |
| Carol         | Sales           |
| Carol         | Engineering     |
| Carol         | HR              |
| Carol         | Marketing       |
| Dave          | Sales           |
| Dave          | Engineering     |
| Dave          | HR              |
| Dave          | Marketing       |
| Eve           | Sales           |
| Eve           | Engineering     |
| Eve           | HR              |
| Eve           | Marketing       |

### SELF JOIN

`SELF JOIN` — это соединение таблицы с самой собой. Используется, когда нужно сравнить строки внутри одной таблицы.

**Пример:**

```sql
SELECT e1.name AS employee, e2.name AS manager
FROM employees AS e1
         JOIN employees AS e2 ON e1.manager_id = e2.employee_id;
```

**Результат:**

| employee | manager |
|----------|---------|
| Bob      | Alice   |
| Carol    | Alice   |
| Dave     | Bob     |
| Eve      | Bob     |

### Пример рекурсивного запроса

Рекурсивные запросы в SQL используются для работы с иерархическими данными, такими как структуры директорий или
организационные структуры. В SQL для этого используется конструкция `WITH RECURSIVE`.

**Пример:**

```sql
WITH RECURSIVE EmployeeHierarchy AS (SELECT employee_id, name, manager_id, 1 AS level
                                     FROM employees
                                     WHERE manager_id IS NULL
                                     UNION ALL
                                     SELECT e.employee_id, e.name, e.manager_id, eh.level + 1
                                     FROM employees AS e
                                              JOIN EmployeeHierarchy AS eh ON e.manager_id = eh.employee_id)
SELECT employee_id, name, manager_id, level
FROM EmployeeHierarchy;
```

**Результат:**

| employee_id | name  | manager_id | level |
|-------------|-------|------------|-------|
| 1           | Alice | NULL       | 1     |
| 2           | Bob   | 1          | 2     |
| 3           | Carol | 1          | 2     |
| 4           | Dave  | 2          | 3     |
| 5           | Eve   | 2          | 3     |

Этот запрос строит иерархию сотрудников, начиная с тех, у кого нет менеджера, и далее рекурсивно добавляя подчиненных.
