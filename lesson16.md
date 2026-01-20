# Лекция 16. СУБД. DQL. SELECT. Индексы. GROUP BY. Joins.

### Оглавление курса

<details>
  <summary>Блок 1 — Python Basic (1–6)</summary>

  - [Лекция 1. Введение. Типизации. Переменные. Строки и числа. Булева алгебра. Ветвление](lesson01.md)
  - [Лекция 2. Обработка исключений. Списки, строки детальнее, срезы, циклы.](lesson02.md)
  - [Лекция 3. None. Range, list comprehension, sum, max, min, len, sorted, all, any. Работа с файлами](lesson03.md)
  - [Лекция 4. Хэш-таблицы. Set, frozenset. Dict. Tuple. Немного об импортах. Namedtuple, OrderedDict](lesson04.md)
  - [Лекция 5. Функции, типизация, lambda. Map, zip, filter.](lesson05.md)
  - [Лекция 6. Алгоритмы и структуры данных](lesson06.md)
</details>

<details>
  <summary>Блок 2 — Git (7–8)</summary>

  - [Лекция 7. Git. История системы контроля версий. Локальный репозиторий. Базовые команды управления репозиторием.](lesson07.md)
  - [Лекция 8. Git. Удаленный репозиторий. Remote, push, pull. GitHub, Bitbucket, GitLab, etc. Pull request.](lesson08.md)
</details>

<details>
  <summary>Блок 3 — Python Advanced (9–14)</summary>

  - [Лекция 9. Введение в ООП. Основные парадигмы ООП. Классы и объекты. Множественное наследование.](lesson09.md)
  - [Лекция 10. Magic methods. Итераторы и генераторы.](lesson10.md)
  - [Лекция 11. Imports. Standard library. PEP 8](lesson11.md)
  - [Лекция 12. Декораторы. Декораторы с параметрами. Декораторы классов (staticmethod, classmethod, property)](lesson12.md)
  - [Лекция 13. Тестирование](lesson13.md)
  - [Лекция 14. Проектирование. Паттерны. SOLID.](lesson14.md)
</details>

<details open>
  <summary>Блок 4 — SQL (15–17)</summary>

  - [Лекция 15. СУБД. PostgreSQL. SQL. DDL. Пользователи. DCL. DML. Связи.](lesson15.md)
  - ▶ **Лекция 16. СУБД. DQL. SELECT. Индексы. GROUP BY. Joins.**
  - [Лекция 17. СУБД. Нормализация. Аномалии. Транзакции. ACID. TCL. Backup](lesson17.md)
</details>

- [Лекция 18. Virtual env. Pip. Устанавливаемые модули. Pyenv.](lesson18.md)

<details>
  <summary>Блок 5 — Django (19–26)</summary>

  - [Лекция 19. Знакомство с Django](lesson19.md)
  - [Лекция 20. Templates. Static](lesson20.md)
  - [Лекция 21. Модели. Связи. Meta. Abstract, proxy.](lesson21.md)
  - [Лекция 22. Django ORM.](lesson22.md)
  - [Лекция 23. Forms, ModelForms. User, Authentication.](lesson23.md)
  - [Лекция 24. ClassBaseView](lesson24.md)
  - [Лекция 25. NoSQL. Куки, сессии, кеш](lesson25.md)
  - [Лекция 26. Логирование. Middleware. Signals. Messages. Manage commands](lesson26.md)
</details>

<details>
  <summary>Блок 6 — Django Rest Framework (27–30)</summary>

  - [Лекция 27. Что такое API. REST и RESTful. Django REST Framework.](lesson27.md)
  - [Лекция 28. @api_view, APIView, ViewSets, Pagination, Routers](lesson28.md)
  - [Лекция 29. REST-аутентификация. Авторизация. Permissions. Фильтрация.](lesson29.md)
  - [Лекция 30. Тестирование. Django, REST API.](lesson30.md)
</details>

<details>
  <summary>Блок 7 — Python async (31–33)</summary>

  - [Лекция 31. Celery. Multithreading. GIL. Multiprocessing](lesson31.md)
  - [Лекция 32. Asyncio. Aiohttp. Асинхронное программирование на практике.](lesson32.md)
  - [Лекция 33. Сокеты. Django Channels.](lesson33.md)
</details>

<details>
  <summary>Блок 8 — Deployment (34–35)</summary>

  - [Лекция 34. Linux. Всё, что нужно знать для деплоймента.](lesson34.md)
  - [Лекция 35. Deployment](lesson35.md)
</details>

- [Лекция 36. Методологии разработки. CI/CD. Монолит и микросервисы. Docker](lesson36.md)


![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSet_oHygtk-HIEN4JI7Y8Ma0_UF0Co3HaHwQ&s)

## DQL (Data query language) (Язык запроса данных)

`DQL` — ещё одна подгруппа языка `SQL`, которая состоит из всего одного слова `SELECT`.
Но не спешим радоваться: в нём деталей примерно как во всех прошлых командах вместе взятых.

## SELECT

Самый простой вариант запроса выглядит так:

```sql
SELECT * FROM book;
```

Выбрать все столбцы и все колонки из таблицы `book`.
> В продакшене старайтесь избегать SELECT * — лучше явно перечислять нужные столбцы.

Можно выбрать только часть столбцов:

```sql
SELECT title, page_count
FROM book;
```

Теперь мы выбираем только колонки `title` и `page_count`.

На самом деле SQL является ещё и калькулятором, поэтому мы можем получить не только значение, но и вычисления:

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

В первом запросе мы вытаскиваем все книги, у которых в поле «автор» записано `King`.
Во втором — все книги, у которых жанр — это `Action` или `Comedy`.
В третьем — все книги, у которых количество страниц от 100 до 200.

> Естественно, все условия можно комбинировать через `OR` и `AND`.

### Именование полученной таблицы

Для того чтобы назвать результаты ваших запросов, можно использовать ключевое слово `AS`. Это нам ещё в дальнейшем
понадобится.

```sql
SELECT title, page_count / 2 as sheets
FROM book;
```

Тут `sheets` — это метка.

> Метки часто называют словом «псевдоним».

### DISTINCT

Ключевое слово `DISTINCT` используется для получения только уникальных значений какого-либо поля.

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

Также мы можем ограничить количество получаемых результатов. Зачем это делать? А что, если под наше условие подходит
миллиард записей? Сможем ли мы их все обработать? Думаю, что нет. Но мы всегда можем указать необходимую нам сортировку
и только после этого указать лимит в каком-то небольшом количестве данных.

```sql
SELECT *
FROM publisher
LIMIT 10;
```

Вернёт только первые 10 значений.

```sql
SELECT *
FROM publisher
LIMIT 10 OFFSET 10;
```

Вернёт значения с 11-го по 20-е. `OFFSET` — сдвиг по данным.

## Индексация

![](https://media.dev.to/cdn-cgi/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fa80rqyke0it7ud4j2nmg.png)

Индекс в базе данных — это специальная структура данных, которая улучшает скорость поиска данных в таблице. Индексы
создаются на основе одного или нескольких столбцов таблицы и позволяют быстро находить строки, удовлетворяющие
определённым условиям.

> Представьте индекс как оглавление книги: вместо того чтобы просматривать всю книгу, чтобы найти нужную информацию, вы
> можете просто заглянуть в оглавление и быстро перейти к нужной странице.

### Типы индексов в PostgreSQL

Индексы бывают разных типов; разные типы часто используются для разных типов данных. Вникать в детали нам пока нет
никакой необходимости, но я их перечислю.

#### B-Tree Индексы

Это самый распространённый тип индекса. B-Tree индексы используются по умолчанию при создании индекса и подходят для
большинства операций поиска и сортировки (работают на бинарном поиске).

#### Hash Индексы

Эти индексы полезны для операций равенства. Они не поддерживают диапазонные запросы и не так универсальны, как B-Tree
индексы.

#### GiST Индексы (Generalized Search Tree)

Используются для более сложных типов данных, таких как геометрические и полнотекстовые поиски.

#### GIN Индексы (Generalized Inverted Index)

Эти индексы эффективны для поиска в больших текстовых полях и массивных данных.

#### BRIN Индексы (Block Range INdexes)

Индексы, которые используются для очень больших таблиц, где данные имеют чёткий порядок. Они занимают меньше места и
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

Да, индекс не всегда привязан к одному полю.

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
- Для снижения блокировок используйте `CREATE INDEX CONCURRENTLY` / `DROP INDEX CONCURRENTLY`.
- Проверяйте планы запросов через `EXPLAIN` / `EXPLAIN ANALYZE`.

Этот индекс будет полезен для запросов, использующих оба столбца `last_name` и `first_name`.

### Использование индексов в запросах

Ничего дополнительного делать с индексом не нужно: если он есть, он уже будет влиять на работу системы.

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

### Проблемы, связанные с индексами

А если всё так хорошо и быстро, почему бы нам не создать индексы вообще на все поля, и всё будет работать быстрее?

И да и нет.

Если бы у нас были только операции чтения, то это было бы идеальное решение. Но у нас есть и другие операции.

Представьте книгу, у которой есть оглавление (по сути, та же индексация). Пока мы можем только читать книгу, проблем нет —
добавили несколько страниц в начале, чем упростили жизнь.

Но теперь представьте, что вы в эту книгу начинаете дописывать/удалять/изменять страницы или целые главы.

Для каждой такой операции оглавление придётся переписывать заново.

> Если в таблицу часто производится запись/изменение/удаление, то индекс только замедлит работу базы! А он ещё и место
> занимает! Поэтому всегда нужно очень аккуратно относиться к индексам — это очень хороший инструмент, который легко
> может всё сломать.

### EXPLAIN и EXPLAIN ANALYZE

Чтобы понять, как PostgreSQL выполняет запрос и использует ли индексы, используется команда `EXPLAIN`.

#### EXPLAIN — план выполнения

```sql
EXPLAIN SELECT * FROM users WHERE email = 'test@example.com';
```

Результат:
```
                        QUERY PLAN
-----------------------------------------------------------
 Seq Scan on users  (cost=0.00..25.00 rows=1 width=100)
   Filter: (email = 'test@example.com'::text)
```

- **Seq Scan** — последовательное сканирование (читает всю таблицу)
- **cost** — оценка стоимости (startup..total)
- **rows** — ожидаемое количество строк
- **width** — средний размер строки в байтах

#### EXPLAIN ANALYZE — реальное выполнение

`EXPLAIN ANALYZE` не только показывает план, но и выполняет запрос, показывая реальное время:

```sql
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'test@example.com';
```

Результат:
```
                        QUERY PLAN
-----------------------------------------------------------
 Seq Scan on users  (cost=0.00..25.00 rows=1 width=100)
                    (actual time=0.015..0.234 rows=1 loops=1)
   Filter: (email = 'test@example.com'::text)
   Rows Removed by Filter: 999
 Planning Time: 0.085 ms
 Execution Time: 0.267 ms
```

- **actual time** — реальное время (startup..total) в миллисекундах
- **rows** — реальное количество возвращённых строк
- **loops** — сколько раз выполнялся этот узел
- **Rows Removed by Filter** — сколько строк отфильтровано

#### Сравнение с индексом и без

```sql
-- Без индекса
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'test@example.com';
-- Seq Scan on users ... (actual time=0.015..0.234 rows=1 loops=1)

-- Создаём индекс
CREATE INDEX idx_users_email ON users(email);

-- С индексом
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'test@example.com';
-- Index Scan using idx_users_email on users ... (actual time=0.012..0.013 rows=1 loops=1)
```

#### Типы сканирования

| Тип сканирования    | Описание                                      |
|---------------------|-----------------------------------------------|
| Seq Scan            | Последовательное чтение всей таблицы          |
| Index Scan          | Поиск по индексу + чтение данных из таблицы   |
| Index Only Scan     | Все данные берутся из индекса (самый быстрый) |
| Bitmap Index Scan   | Индекс создаёт битовую карту, потом читает    |

#### Полезные опции EXPLAIN

```sql
-- Подробный вывод с буферами
EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM users WHERE id = 1;

-- Вывод в формате JSON (удобно для парсинга)
EXPLAIN (FORMAT JSON) SELECT * FROM users WHERE id = 1;

-- Показать настройки планировщика
EXPLAIN (VERBOSE) SELECT * FROM users WHERE id = 1;
```

> Используйте `EXPLAIN ANALYZE` для оптимизации медленных запросов. Если видите `Seq Scan` на большой таблице с
> условием WHERE — скорее всего, нужен индекс.

## Встроенные функции

В SQL встроено довольно-таки большое количество функций, которыми мы можем пользоваться, и часть из них будет
использована в дальнейшем для агрегации данных. Давайте с некоторыми из них познакомимся.

### Логические операторы и операторы сравнения

Таблица истинности для SQL, учитывающая `NULL`, отличается от обычной таблицы истинности, так как `NULL` в SQL
представляет неопределённое значение. В операциях сравнения и логических операциях `NULL` ведёт себя особым образом.

Вот таблица истинности для SQL с учётом `NULL`:

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
    - `A AND B` вернёт `TRUE`, только если оба значения `TRUE`.
    - `A OR B` вернёт `TRUE`, если хотя бы одно значение `TRUE`.
    - `NOT A` вернёт противоположное значение, если `A` не `NULL`.

2. **Операторы сравнения:**
    - Любое сравнение с `NULL` всегда возвращает `NULL` (неопределённое).

Эти правила делают работу с `NULL` в SQL специфической, и при работе с данными нужно учитывать, что `NULL` не
эквивалентен ни `TRUE`, ни `FALSE`, а представляет собой третье состояние, которое требует особого внимания при
логических и сравнительных операциях.

### Математические действия и операторы

Прежде чем мы перейдём к математическим функциям, давайте рассмотрим основные математические операции в SQL:

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

> Естественно, их больше; если нужно что-то специфическое, обратитесь к документации.

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
- `EXTRACT(what FROM what)` — извлечь часть даты.

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

- `ILIKE` — регистронезависимый вариант `LIKE` в PostgreSQL.

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
функций. Мы рассмотрим, как использовать эти операторы, приведём примеры запросов и разберём возможные применения.

### Введение в оператор `GROUP BY`

Оператор `GROUP BY` используется для группировки строк, имеющих одинаковые значения в определённых столбцах. После
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

Где применять фильтры: `WHERE` — до группировки (фильтрует строки), `HAVING` — после группировки (фильтрует группы).

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

## Оконные функции (Window Functions)

Оконные функции выполняют вычисления над набором строк, связанных с текущей строкой, но в отличие от агрегатных функций
не схлопывают строки в одну. Каждая строка сохраняется в результате.

### Синтаксис

```sql
function_name() OVER (
    [PARTITION BY column1, column2, ...]
    [ORDER BY column3, column4, ...]
    [ROWS/RANGE frame_specification]
)
```

- **PARTITION BY** — разбивает данные на группы (как GROUP BY, но без схлопывания)
- **ORDER BY** — определяет порядок строк внутри окна
- **ROWS/RANGE** — определяет границы окна

### ROW_NUMBER, RANK, DENSE_RANK

```sql
SELECT
    name,
    department,
    salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num,
    RANK() OVER (ORDER BY salary DESC) AS rank,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank
FROM employees;
```

| name  | department | salary | row_num | rank | dense_rank |
|-------|------------|--------|---------|------|------------|
| Alice | IT         | 100000 | 1       | 1    | 1          |
| Bob   | Sales      | 100000 | 2       | 1    | 1          |
| Carol | IT         | 90000  | 3       | 3    | 2          |
| Dave  | HR         | 80000  | 4       | 4    | 3          |

- **ROW_NUMBER** — уникальный номер для каждой строки
- **RANK** — одинаковые значения получают одинаковый ранг, следующий ранг пропускается
- **DENSE_RANK** — как RANK, но без пропусков

### PARTITION BY — группировка без схлопывания

```sql
-- Ранг сотрудника внутри своего отдела
SELECT
    name,
    department,
    salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

| name  | department | salary | dept_rank |
|-------|------------|--------|-----------|
| Alice | IT         | 100000 | 1         |
| Carol | IT         | 90000  | 2         |
| Bob   | Sales      | 100000 | 1         |
| Dave  | HR         | 80000  | 1         |

### LAG и LEAD — доступ к соседним строкам

```sql
SELECT
    date,
    revenue,
    LAG(revenue, 1) OVER (ORDER BY date) AS prev_day_revenue,
    LEAD(revenue, 1) OVER (ORDER BY date) AS next_day_revenue,
    revenue - LAG(revenue, 1) OVER (ORDER BY date) AS daily_change
FROM daily_sales;
```

| date       | revenue | prev_day_revenue | next_day_revenue | daily_change |
|------------|---------|------------------|------------------|--------------|
| 2024-01-01 | 1000    | NULL             | 1200             | NULL         |
| 2024-01-02 | 1200    | 1000             | 1100             | 200          |
| 2024-01-03 | 1100    | 1200             | 1500             | -100         |

- **LAG(column, n)** — значение из строки на n позиций назад
- **LEAD(column, n)** — значение из строки на n позиций вперёд

### FIRST_VALUE, LAST_VALUE, NTH_VALUE

```sql
SELECT
    name,
    department,
    salary,
    FIRST_VALUE(name) OVER (PARTITION BY department ORDER BY salary DESC) AS top_earner,
    LAST_VALUE(name) OVER (
        PARTITION BY department ORDER BY salary DESC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS lowest_earner
FROM employees;
```

### Агрегатные функции как оконные

```sql
SELECT
    date,
    revenue,
    SUM(revenue) OVER (ORDER BY date) AS running_total,
    AVG(revenue) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS week_avg
FROM daily_sales;
```

- **running_total** — накопительная сумма
- **week_avg** — скользящее среднее за 7 дней

### Практические примеры

```sql
-- Топ-3 сотрудника по зарплате в каждом отделе
SELECT * FROM (
    SELECT
        name,
        department,
        salary,
        ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rn
    FROM employees
) ranked
WHERE rn <= 3;

-- Процент от общей суммы
SELECT
    department,
    salary,
    ROUND(salary * 100.0 / SUM(salary) OVER (), 2) AS percent_of_total,
    ROUND(salary * 100.0 / SUM(salary) OVER (PARTITION BY department), 2) AS percent_of_dept
FROM employees;
```

> Оконные функции — мощный инструмент для аналитических запросов. Они позволяют делать вычисления, которые раньше
> требовали сложных подзапросов или самосоединений.

## Вложенность

На самом деле в любом месте запроса можно разместить другой запрос (внутри `WHERE`, внутри `FROM` и т. д.).

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

Этот запрос объединяет списки имён и email-адресов из таблиц `customers` и `prospects`, исключая дубликаты.

**Пример с `UNION ALL`:**

```sql
SELECT name, email
FROM customers
UNION ALL
SELECT name, email
FROM prospects;
```

Этот запрос объединяет списки имён и email-адресов, включая все дублирующиеся записи.

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

Этот запрос возвращает список имён и email-адресов, которые есть как в таблице `customers`, так и в
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

Этот запрос возвращает список имён и email-адресов, которые есть в таблице `customers`, но отсутствуют в
таблице `unsubscribed_users`.

#### Важные замечания

1. **Количество и типы столбцов:** Все запросы, объединяемые с помощью `UNION`, `INTERSECT` и `EXCEPT`, должны
   возвращать одинаковое количество столбцов, и типы данных этих столбцов должны быть совместимы.
2. **Порядок сортировки:** Для упорядочивания результатов объединённых запросов используется оператор `ORDER BY` после
   всех объединённых запросов.

**Пример с `ORDER BY`:**

```sql
SELECT name, email
FROM customers
UNION
SELECT name, email
FROM prospects
ORDER BY name;
```

Этот запрос объединяет списки имён и email-адресов, исключает дубликаты и сортирует результат по имени.

### Порядок выполнения SQL-запроса

Теперь, когда вы знакомы со всеми основными ключевыми словами, важно понять, что порядок написания SQL-запроса
отличается от порядка его выполнения. Это объясняет многие «странности» SQL.

**Порядок написания:**
```sql
SELECT columns
FROM table
WHERE condition
GROUP BY columns
HAVING condition
ORDER BY columns
LIMIT n;
```

**Порядок выполнения:**

```
1. FROM      — определяется источник данных (таблицы, JOIN)
2. WHERE     — фильтруются строки
3. GROUP BY  — группируются строки
4. HAVING    — фильтруются группы
5. SELECT    — выбираются и вычисляются столбцы
6. DISTINCT  — удаляются дубликаты
7. ORDER BY  — сортируются результаты
8. LIMIT     — ограничивается количество строк
```

**Почему это важно:**

```sql
-- Ошибка: нельзя использовать алиас из SELECT в WHERE
SELECT price * quantity AS total
FROM orders
WHERE total > 100;  -- Ошибка! total ещё не существует

-- Правильно: повторить выражение
SELECT price * quantity AS total
FROM orders
WHERE price * quantity > 100;

-- Или использовать подзапрос
SELECT * FROM (
    SELECT price * quantity AS total
    FROM orders
) AS subquery
WHERE total > 100;
```

```sql
-- Алиас можно использовать в ORDER BY (выполняется после SELECT)
SELECT price * quantity AS total
FROM orders
ORDER BY total;  -- Работает!
```


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

Использование оператора `JOIN` в SQL для объединения таблиц. Вы же ещё помните, что таблицы в базе могут и даже должны
быть связаны? Так вот, чаще всего нам нужно будет извлекать данные именно из связанных таблиц, а для этого нам
понадобится оператор `JOIN`.

### Временное именование таблиц

В SQL часто возникает необходимость упростить запись запросов, особенно когда таблицы имеют длинные названия. Для этого
можно использовать временные имена (алиасы). Алиасы создаются с помощью ключевого слова `AS`. Я уже использовал их чуть
выше в примерах — давайте разберёмся.

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

`FULL JOIN` возвращает все строки, когда есть совпадения в левой или правой таблице. Если совпадений нет, то
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

Этот запрос строит иерархию сотрудников, начиная с тех, у кого нет менеджера, и далее рекурсивно добавляет подчинённых.

### LATERAL JOIN

`LATERAL` позволяет подзапросу в `FROM` ссылаться на столбцы из предыдущих таблиц в том же `FROM`. Это похоже на
коррелированный подзапрос, но в контексте `JOIN`.

**Пример: получить 3 последних заказа для каждого пользователя**

Без LATERAL пришлось бы использовать оконные функции:

```sql
SELECT * FROM (
    SELECT
        u.id AS user_id,
        u.name,
        o.id AS order_id,
        o.created_at,
        ROW_NUMBER() OVER (PARTITION BY u.id ORDER BY o.created_at DESC) AS rn
    FROM users u
    JOIN orders o ON u.id = o.user_id
) ranked
WHERE rn <= 3;
```

С LATERAL — более читаемо:

```sql
SELECT u.id, u.name, recent_orders.*
FROM users u
CROSS JOIN LATERAL (
    SELECT o.id AS order_id, o.created_at, o.total_amount
    FROM orders o
    WHERE o.user_id = u.id
    ORDER BY o.created_at DESC
    LIMIT 3
) AS recent_orders;
```

**Как это работает:**
1. Для каждой строки из `users` выполняется подзапрос
2. Подзапрос может использовать `u.id` из внешней таблицы
3. Результаты соединяются

**Пример: статистика по каждому отделу**

```sql
SELECT d.name AS department, stats.*
FROM departments d
CROSS JOIN LATERAL (
    SELECT
        COUNT(*) AS employee_count,
        AVG(salary) AS avg_salary,
        MAX(salary) AS max_salary
    FROM employees e
    WHERE e.department_id = d.id
) AS stats;
```

**LEFT JOIN LATERAL**

Если подзапрос может вернуть 0 строк, используйте `LEFT JOIN LATERAL`:

```sql
SELECT u.id, u.name, last_order.order_id, last_order.created_at
FROM users u
LEFT JOIN LATERAL (
    SELECT o.id AS order_id, o.created_at
    FROM orders o
    WHERE o.user_id = u.id
    ORDER BY o.created_at DESC
    LIMIT 1
) AS last_order ON true;
```

> `LATERAL` полезен, когда нужно выполнить подзапрос для каждой строки основной таблицы с использованием значений из
> этой строки. Часто это более читаемая альтернатива оконным функциям или коррелированным подзапросам.

## Представления (Views)

Представление (View) — это виртуальная таблица, основанная на результате SQL-запроса. Представление не хранит данные
физически, а выполняет запрос каждый раз при обращении к нему.

### Создание представления

```sql
-- Простое представление
CREATE VIEW active_users AS
SELECT id, name, email
FROM users
WHERE is_active = true;

-- Использование представления как обычной таблицы
SELECT * FROM active_users;
SELECT name FROM active_users WHERE id > 100;
```

### Представления с вычислениями

```sql
CREATE VIEW order_summary AS
SELECT
    o.id AS order_id,
    u.name AS customer_name,
    o.created_at,
    SUM(oi.quantity * oi.price) AS total_amount
FROM orders o
JOIN users u ON o.user_id = u.id
JOIN order_items oi ON o.id = oi.order_id
GROUP BY o.id, u.name, o.created_at;
```

### Обновляемые представления

Простые представления (без JOIN, GROUP BY, DISTINCT и т. д.) могут быть обновляемыми:

```sql
CREATE VIEW russian_users AS
SELECT id, name, email, country
FROM users
WHERE country = 'Russia';

-- Можно вставлять данные через представление
INSERT INTO russian_users (name, email, country)
VALUES ('Иван', 'ivan@example.com', 'Russia');

-- WITH CHECK OPTION запрещает вставку данных, не соответствующих условию представления
CREATE VIEW russian_users AS
SELECT id, name, email, country
FROM users
WHERE country = 'Russia'
WITH CHECK OPTION;
```

### Управление представлениями

```sql
-- Изменить представление
CREATE OR REPLACE VIEW active_users AS
SELECT id, name, email, created_at
FROM users
WHERE is_active = true AND email_verified = true;

-- Удалить представление
DROP VIEW active_users;

-- Удалить каскадно (если есть зависимые представления)
DROP VIEW active_users CASCADE;
```

> Представления полезны для: упрощения сложных запросов, ограничения доступа к данным (показывать только определённые
> столбцы), создания абстракций над структурой БД.

## Материализованные представления (Materialized Views)

В отличие от обычных представлений, материализованные представления физически хранят результат запроса. Это ускоряет
чтение, но данные могут устаревать.

### Создание материализованного представления

```sql
CREATE MATERIALIZED VIEW monthly_sales AS
SELECT
    DATE_TRUNC('month', created_at) AS month,
    COUNT(*) AS orders_count,
    SUM(total_amount) AS total_sales
FROM orders
GROUP BY DATE_TRUNC('month', created_at);
```

### Обновление данных

```sql
-- Полное обновление (блокирует чтение)
REFRESH MATERIALIZED VIEW monthly_sales;

-- Обновление без блокировки (требует UNIQUE INDEX)
CREATE UNIQUE INDEX ON monthly_sales (month);
REFRESH MATERIALIZED VIEW CONCURRENTLY monthly_sales;
```

### Когда использовать

| Обычное представление                   | Материализованное представление             |
|-----------------------------------------|---------------------------------------------|
| Данные всегда актуальны                 | Данные могут устаревать                     |
| Запрос выполняется при каждом обращении | Запрос выполняется при REFRESH              |
| Подходит для простых запросов           | Подходит для сложных аналитических запросов |
| Не занимает дополнительное место        | Занимает место на диске                     |

```sql
-- Удаление
DROP MATERIALIZED VIEW monthly_sales;
```

## Хранимые функции (Stored Functions)

Хранимые функции позволяют инкапсулировать логику на стороне базы данных. PostgreSQL поддерживает несколько языков,
наиболее распространённый — PL/pgSQL.

### Простая функция

```sql
CREATE OR REPLACE FUNCTION get_full_name(first_name TEXT, last_name TEXT)
RETURNS TEXT AS $$
BEGIN
    RETURN first_name || ' ' || last_name;
END;
$$ LANGUAGE plpgsql;

-- Использование
SELECT get_full_name('John', 'Doe');  -- 'John Doe'
```

### Функция с запросом

```sql
CREATE OR REPLACE FUNCTION get_user_orders_count(user_id_param INTEGER)
RETURNS INTEGER AS $$
DECLARE
    orders_count INTEGER;
BEGIN
    SELECT COUNT(*) INTO orders_count
    FROM orders
    WHERE user_id = user_id_param;

    RETURN orders_count;
END;
$$ LANGUAGE plpgsql;

-- Использование
SELECT name, get_user_orders_count(id) AS orders
FROM users;
```

### Функция, возвращающая таблицу

```sql
CREATE OR REPLACE FUNCTION get_active_users_by_country(country_param TEXT)
RETURNS TABLE (
    user_id INTEGER,
    user_name TEXT,
    user_email TEXT
) AS $$
BEGIN
    RETURN QUERY
    SELECT id, name, email
    FROM users
    WHERE country = country_param AND is_active = true;
END;
$$ LANGUAGE plpgsql;

-- Использование
SELECT * FROM get_active_users_by_country('Russia');
```

### Функция с условной логикой

```sql
CREATE OR REPLACE FUNCTION calculate_discount(total NUMERIC, customer_type TEXT)
RETURNS NUMERIC AS $$
BEGIN
    IF customer_type = 'vip' THEN
        RETURN total * 0.20;
    ELSIF customer_type = 'regular' THEN
        RETURN total * 0.10;
    ELSE
        RETURN 0;
    END IF;
END;
$$ LANGUAGE plpgsql;
```

### Управление функциями

```sql
-- Удалить функцию
DROP FUNCTION get_full_name(TEXT, TEXT);

-- Посмотреть определение функции
\df+ get_full_name
```

> Хранимые функции полезны для: инкапсуляции бизнес-логики, повторного использования кода, повышения производительности
> (меньше сетевых запросов), обеспечения безопасности (доступ через функции, а не напрямую к таблицам).

## Триггеры (Triggers)

Триггер — это автоматическое действие, которое выполняется при изменении данных в таблице. Представьте его как
"наблюдателя", который реагирует на INSERT, UPDATE или DELETE.

### Зачем нужны триггеры

- **Автоматическое обновление полей** — например, `updated_at` при каждом изменении
- **Валидация данных** — проверка бизнес-правил перед сохранением
- **Ведение истории изменений** — логирование кто, когда и что изменил
- **Синхронизация данных** — обновление связанных таблиц

### Как работает триггер

Триггер состоит из двух частей:
1. **Триггерная функция** — что делать
2. **Сам триггер** — когда это делать

### Пример 1: Автоматическое обновление даты изменения

Самый частый случай — автоматически обновлять поле `updated_at`:

```sql
-- Шаг 1: Создаём функцию
CREATE OR REPLACE FUNCTION update_modified_at()
RETURNS TRIGGER AS $$
BEGIN
    -- NEW — это новая версия строки, которую мы изменяем
    NEW.updated_at = NOW();
    RETURN NEW;  -- Возвращаем изменённую строку
END;
$$ LANGUAGE plpgsql;

-- Шаг 2: Создаём триггер
CREATE TRIGGER set_updated_at
    BEFORE UPDATE ON users           -- Перед обновлением таблицы users
    FOR EACH ROW                     -- Для каждой изменяемой строки
    EXECUTE FUNCTION update_modified_at();
```

Теперь при любом UPDATE в таблице users поле `updated_at` обновится автоматически:

```sql
UPDATE users SET name = 'Новое имя' WHERE id = 1;
-- updated_at обновится автоматически!
```

### Пример 2: Валидация email перед вставкой

```sql
CREATE OR REPLACE FUNCTION validate_email()
RETURNS TRIGGER AS $$
BEGIN
    -- Проверяем, что email содержит @
    IF NEW.email NOT LIKE '%@%' THEN
        RAISE EXCEPTION 'Некорректный email: %', NEW.email;
    END IF;

    -- Приводим email к нижнему регистру
    NEW.email = LOWER(NEW.email);

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_email
    BEFORE INSERT OR UPDATE ON users
    FOR EACH ROW
    EXECUTE FUNCTION validate_email();
```

### Пример 3: Логирование удалений

```sql
-- Таблица для хранения удалённых записей
CREATE TABLE deleted_users (
    id BIGINT,
    name TEXT,
    email TEXT,
    deleted_at TIMESTAMPTZ DEFAULT NOW()
);

-- Функция, которая сохраняет удалённую запись
CREATE OR REPLACE FUNCTION log_deleted_user()
RETURNS TRIGGER AS $$
BEGIN
    -- OLD — это удаляемая строка
    INSERT INTO deleted_users (id, name, email)
    VALUES (OLD.id, OLD.name, OLD.email);

    RETURN OLD;  -- Для DELETE возвращаем OLD
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER save_deleted_user
    AFTER DELETE ON users            -- После удаления
    FOR EACH ROW
    EXECUTE FUNCTION log_deleted_user();
```

### BEFORE vs AFTER

| BEFORE                                    | AFTER                                  |
|-------------------------------------------|----------------------------------------|
| Выполняется **до** операции               | Выполняется **после** операции         |
| Можно изменить данные (NEW)               | Данные уже сохранены                   |
| Можно отменить операцию (RETURN NULL)     | Операция уже выполнена                 |
| Для валидации и модификации               | Для логирования и уведомлений          |

### Специальные переменные в триггерах

| Переменная      | Описание                                   |
|-----------------|--------------------------------------------|
| `NEW`           | Новая версия строки (для INSERT/UPDATE)    |
| `OLD`           | Старая версия строки (для UPDATE/DELETE)   |
| `TG_OP`         | Тип операции: 'INSERT', 'UPDATE', 'DELETE' |
| `TG_TABLE_NAME` | Имя таблицы, на которой сработал триггер   |

### Управление триггерами

```sql
-- Временно отключить триггер (например, для массовой загрузки данных)
ALTER TABLE users DISABLE TRIGGER set_updated_at;

-- Включить обратно
ALTER TABLE users ENABLE TRIGGER set_updated_at;

-- Отключить ВСЕ триггеры на таблице
ALTER TABLE users DISABLE TRIGGER ALL;

-- Удалить триггер
DROP TRIGGER set_updated_at ON users;
```

> **Важно:** Триггеры выполняются внутри той же транзакции, что и основная операция. Если триггер вызовет ошибку,
> вся операция будет отменена.

---

[← Лекция 15: СУБД. PostgreSQL. SQL. DDL. Пользователи. DCL. DML. Связи.](lesson15.md) | [Лекция 17: СУБД. Нормализация. Аномалии. Транзакции. ACID. TCL. Backup →](lesson17.md)
