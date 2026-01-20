# Лекция 11. Imports. Standard library. PEP8

### Оглавление курса

<details>
  <summary>Блок 1 — Python Basic (1–6)</summary>

  - [Лекция 1. Введение. Типизации. Переменные. Строки и числа. Булева алгебра. Ветвление](lesson01.md)
  - [Лекция 2. Обработка исключений. Списки, строки детальнее, срезы, циклы.](lesson02.md)
  - [Лекция 3: None. Range, list comprehension, sum, max, min, len, sorted, all, any. Работа с файлами](lesson03.md)
  - [Лекция 4. Хэш таблицы. Set, frozenset. Dict. Tuple. Немного об импортах. Namedtuple, OrderedDict](lesson04.md)
  - [Лекция 5. Функции, типизация, lambda. Map, zip, filter.](lesson05.md)
  - [Лекция 6. Алгоритмы и структуры данных](lesson06.md)
</details>

<details>
  <summary>Блок 2 — Git (7–8)</summary>

  - [Лекция 7. Git. История системы контроля версий. Локальный репозиторий. Базовые команды управления репозиторием.](lesson07.md)
  - [Лекция 8. Git. Удаленный репозиторий. Remote, push, pull. GitHub, Bitbucket, GitLab, etc. Pull request.](lesson08.md)
</details>

<details open>
  <summary>Блок 3 — Python Advanced (9–14)</summary>

  - [Лекция 9. Введение в ООП. Основные парадигмы ООП. Классы и объекты. Множественное наследование.](lesson09.md)
  - [Лекция 10. Magic methods. Итераторы и генераторы.](lesson10.md)
  - ▶ **Лекция 11. Imports. Standard library. PEP8**
  - [Лекция 12. Декораторы. Декораторы с параметрами. Декораторы классов (staticmethod, classmethod, property)](lesson12.md)
  - [Лекция 13. Тестирование](lesson13.md)
  - [Лекция 14. Проектирование. Паттерны. SOLID.](lesson14.md)
</details>

<details>
  <summary>Блок 4 — SQL (15–17)</summary>

  - [Лекция 15. СУБД. PostgreSQL. SQL. DDL. Пользователи. DCL. DML. Связи.](lesson15.md)
  - [Лекция 16. СУБД. DQL. SELECT. Индексы. Group by. Joins.](lesson16.md)
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
  - [Лекция 29. REST аутентификация. Авторизация. Permissions. Фильтрация.](lesson29.md)
  - [Лекция 30. Тестирование. Django, REST API.](lesson30.md)
</details>

<details>
  <summary>Блок 7 — Python async (31–33)</summary>

  - [Лекция 31. Celery. Multithreading. GIL. Multiprocessing](lesson31.md)
  - [Лекция 32. Asyncio. Aiohttp. Асинхронное программирование на практике.](lesson32.md)
  - [Лекция 33. Сокеты. Django channels.](lesson33.md)
</details>

<details>
  <summary>Блок 8 — Deployment (34–35)</summary>

  - [Лекция 34. Linux. Все что нужно знать для деплоймента.](lesson34.md)
  - [Лекция 35. Deployment](lesson35.md)
</details>

- [Лекция 36. Методологии разработки. CI/CD. Монолит и микросервисы. Docker](lesson36.md)


![](https://qph.cf2.quoracdn.net/main-qimg-d6a560c198bada465b104a5ad25bbc77-pjlq)

## Импорты

## Лекция: Импортирование в Python

Сегодня мы поговорим о важной теме в Python — импортировании модулей. Это ключевая часть работы с кодом, которая
позволяет нам организовывать и переиспользовать код в наших проектах.

В этой части лекции мы затронем:

1. Ключевые слова `from`, `import` и `as`.
2. Абсолютные и относительные импорты.
3. Роль файлов `__init__.py`.
4. Специфичное значение конструкции `if __name__ == '__main__':`.

### Модули и пакеты

#### Модули

Модуль в Python — это файл, содержащий определения и инструкции Python. Модули позволяют организовывать код в логически
связные части, упрощая его поддержку и переиспользование. Каждый модуль имеет своё собственное пространство имён,
что позволяет избегать конфликтов имён.

#### Основные концепции:

1. **Модуль как файл:**
    - Любой файл с расширением `.py` является модулем.
    - Имя модуля соответствует имени файла.

   Например, файл `math_operations.py` является модулем `math_operations`.

2. **Определения в модуле:**
    - Модуль может содержать функции, классы, переменные, а также исполняемый код.

    ```python
    # math_operations.py

    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    pi = 3.14159
    ```

3. **Импортирование модулей:**
    - Вы можете импортировать модуль, используя ключевое слово `import`.

    ```python
    import math_operations

    print(math_operations.add(5, 3))  # Вывод: 8
    print(math_operations.pi)         # Вывод: 3.14159
    ```

4. **Использование ключевых слов `from` и `import`:**
    - Вы можете импортировать конкретные функции или переменные из модуля.

    ```python
    from math_operations import add, pi

    print(add(5, 3))  # Вывод: 8
    print(pi)         # Вывод: 3.14159
    ```

5. **Псевдонимы с использованием ключевого слова `as`:**
    - Вы можете использовать псевдонимы для импортированных модулей или их частей.

    ```python
    import math_operations as mo

    print(mo.add(5, 3))  # Вывод: 8
    ```

#### Пакеты в Python

Пакет в Python — это коллекция модулей, организованных в директорию. Традиционно пакеты содержат файл `__init__.py`,
но начиная с Python 3.3 (PEP 420) существуют и namespace‑пакеты, которые могут обходиться без него. Пакеты позволяют
создавать иерархию модулей, упрощая организацию больших проектов.

**Пример структуры пакета:**

```
project/
    ├── package/
    │   ├── __init__.py
    │   ├── module1.py
    │   └── module2.py
    └── main.py
```

В файле `__init__.py` можно инициализировать пакет и упростить импорт модулей (хотя это совершенно не обязательно):

```python
# package/__init__.py
from .module1 import function1
from .module2 import function2
```

Теперь вы можете импортировать функции напрямую из пакета:

```python
# main.py
from package import function1, function2

function1()
function2()
```

#### Важные моменты

1. **Повторное использование кода:**
    - Модули позволяют переиспользовать код в разных частях проекта или в других проектах.

2. **Организация кода:**
    - Модули и пакеты помогают структурировать проект, делая его более понятным и лёгким в поддержке.

3. **Разделение пространства имён:**
    - Каждый модуль имеет своё собственное пространство имён, что позволяет избегать конфликтов имён.

4. **Публичные и приватные части:**
    - В модуле можно указать, какие части должны быть доступны извне, а какие — нет. Для этого используется соглашение
      об именовании: имена, начинающиеся с одного подчеркивания `_`, считаются приватными.

    ```python
    # example.py
    def public_function():
        pass

    def _private_function():
        pass
    ```

## Чуток детальнее

### Ключевые слова `from`, `import` и `as`

Python предоставляет несколько ключевых слов для импортирования модулей и их частей. Давайте рассмотрим их подробнее.

#### Ключевое слово `import`

Ключевое слово `import` используется для импортирования всего модуля. Когда вы импортируете модуль таким образом, вы
можете обращаться к его содержимому, используя точечную нотацию.

> Кроме вашего написанного кода, внутри Python существуют сотни, если не тысячи дополнительных модулей, которые можно
> импортировать.

> Какие-то из них используются постоянно, какие-то вы не увидите никогда.

> Кроме того, можно установить ещё тысячи, если не десятки тысяч готовых модулей, но об этом будет отдельная лекция.

**Пример:**

```python
import math

print(math.sqrt(16))  # Вывод: 4.0
```

#### Ключевое слово `from`

Ключевое слово `from` используется для импортирования конкретных частей модуля. Это позволяет вам импортировать только
те функции, классы или переменные, которые вам нужны.

**Пример:**

```python
from math import sqrt

print(sqrt(16))  # Вывод: 4.0
```

#### Ключевое слово `as`

Ключевое слово `as` позволяет вам дать импортированному модулю или его части псевдоним. Это может быть полезно для
сокращения длинных имён или разрешения конфликтов имён (например, когда в разных модулях есть функции с одинаковыми
названиями).

**Пример:**

```python
import math as m

print(m.sqrt(16))  # Вывод: 4.0
```

Или в сочетании с `from`:

```python
from math import sqrt as square_root

print(square_root(16))  # Вывод: 4.0
```

### Абсолютные и относительные импорты

#### Абсолютные импорты

Абсолютные импорты — это способ импортирования модулей, используя полный путь к модулю от корневого пакета. Они делают
ваш код более читаемым и ясным.

**Пример:**

Предположим, у нас есть следующая структура каталогов:

```
project/
    ├── main.py
    ├── package_a/
    │   └── __init__.py
    │   └── foo.py
    └── package_b/
        └── __init__.py
        └── bar.py
```

В файле `foo.py` мы можем импортировать функцию из `bar.py` таким образом:

```python
# package_a/foo.py
from package_b.bar import some_function
```

В этом примере мы используем абсолютный импорт, указывая полный путь от корня проекта (`package_b.bar`).

#### Относительные импорты

Относительные импорты используются для импортирования модулей относительно текущего модуля или пакета. Это удобный
способ, когда нужно импортировать модули, находящиеся в том же пакете или соседних пакетах.

**Пример:**

В файле `foo.py`, чтобы импортировать модуль `bar` из того же пакета `package_a`, мы можем использовать относительный
импорт:

```python
# package_a/foo.py
from .bar import some_function
```

Здесь `.` означает текущий пакет. Для импорта модуля из родительского пакета используем `..`:

```python
# package_a/foo.py
from ..package_b.bar import some_function
```

> Важно: относительные импорты корректно работают, когда модуль запускается как часть пакета. Запускайте из корня проекта с ключом `-m`:
>
> ```bash
> cd project
> python -m package_a.foo
> ```
> Так Python настроит `sys.path` и контекст пакета правильно; прямой запуск файла может привести к ошибкам импорта.

### 3. Роль файлов `__init__.py`

Файлы `__init__.py` используются для обозначения директорий как пакетов Python. Эти файлы могут быть пустыми, но их
присутствие сигнализирует интерпретатору Python, что директория должна рассматриваться как пакет.

**Примеры использования `__init__.py`:**

- **Пустой `__init__.py`**: простой способ указать, что директория является пакетом.
- **С кодом**: вы можете включить код в `__init__.py`, чтобы инициализировать пакет, настроить логирование или
  импортировать часто используемые подмодули:

```python
# package_a/__init__.py
from .foo import FooClass
from .bar import BarClass
```

Теперь при импорте `module_a` можно напрямую обращаться к `FooClass` и `BarClass`:

```python
from package_a import FooClass, BarClass
```

### 4. Специфичное значение конструкции `if __name__ == '__main__':`

В Python специальная переменная `__name__` содержит имя текущего модуля. Когда скрипт запускается как основная
программа, `__name__` имеет значение `'__main__'`. Это позволяет писать код, который будет выполняться только в случае,
если скрипт запущен напрямую, а не импортирован как модуль.

**Пример:**

Создадим файл `example.py`:

```python
# example.py
def main():
    print("Это главный скрипт.")


if __name__ == '__main__':
    main()
```

Если вы запустите `example.py`, вы увидите вывод «Это главный скрипт.». Но если вы импортируете этот файл как модуль в
другом скрипте:

```python
# another_script.py
import example
```

Никакой вывод не произойдёт, так как `main()` не будет вызван.

> Используем для того, чтобы отделить между собой основной файл и второстепенные модули.

## Стандартная библиотека и про некоторые модули

![](https://pvsmt99345.i.lithium.com/t5/image/serverpage/image-id/41242i1D8397BD21B07DA8/image-size/large?v=1.0&px=999)

Python — это мощный язык программирования с богатой стандартной библиотекой, включающей множество встроенных модулей.
Эти модули предоставляют функции и классы для выполнения широкого круга задач,
от работы с системой и файловой системой до математических операций и генерации случайных чисел.

«Стандартной библиотекой» называются те пакеты, которые не требуют дополнительной установки и поставляются сразу вместе
с языком программирования.

> Сегодня мы рассмотрим некоторые из наиболее часто используемых встроенных модулей в
> Python: `sys`, `os`, `math`, `random`, `collections`, `datetime` и `itertools`.

### `sys`

Модуль `sys` предоставляет доступ к некоторым переменным, используемым или поддерживаемым интерпретатором Python, а
также к функциям, которые взаимодействуют с ним.

**Примеры:**

```python
import sys

# Получить аргументы командной строки
print("Аргументы командной строки:", sys.argv)

# Выход из программы

> Замечание: в продакшн‑коде не рекомендуется вручную модифицировать `sys.path`. Лучше оформляйте проект как пакет и запускайте модули через `python -m ...`, чтобы окружение и пути настраивались корректно.

# Примечание: sys.exit(0) завершит выполнение программы, поэтому его обычно не используют в примерах.
# sys.exit(0)

# Версия Python
print("Версия Python:", sys.version)

# Путь поиска модулей
print("Путь поиска модулей:", sys.path)
```

### `os`

Модуль `os` предоставляет множество функций для взаимодействия с операционной системой.

**Примеры:**

```python
import os

# Получить текущую рабочую директорию
current_dir = os.getcwd()
print("Текущая рабочая директория:", current_dir)

# Изменить текущую рабочую директорию
new_dir = os.path.expanduser('~')  # к домашнему каталогу пользователя
os.chdir(new_dir)
print("Рабочая директория изменена на:", os.getcwd())

# Список файлов и директорий в текущей директории
files = os.listdir('.')
print("Файлы и директории в текущей директории:", files)

# Создание новой директории
new_dir_name = 'new_dir'
if not os.path.exists(new_dir_name):
    os.mkdir(new_dir_name)
    print("Создана директория:", new_dir_name)

# Удаление файла
file_name = 'test.txt'
if os.path.exists(file_name):
    os.remove(file_name)
    print("Файл удалён:", file_name)
else:
    print("Файл не существует:", file_name)
```

### `math`

Модуль `math` предоставляет доступ к математическим функциям, определённым в стандарте C.

**Примеры:**

```python
import math

# Вычислить квадратный корень
sqrt_value = math.sqrt(16)
print("Квадратный корень из 16:", sqrt_value)

# Вычислить синус угла в радианах
sin_value = math.sin(math.pi / 2)
print("Синус угла pi/2 радиан:", sin_value)

# Вычислить логарифм
log_value = math.log(10)
print("Натуральный логарифм 10:", log_value)

# Константы π и e
print("Константа π:", math.pi)
print("Константа e:", math.e)

# Округление вниз и вверх
floor_value = math.floor(3.7)
ceil_value = math.ceil(3.3)
print("Округление 3.7 вниз:", floor_value)
print("Округление 3.3 вверх:", ceil_value)
```

### `random`

Модуль `random` реализует генераторы псевдослучайных чисел для различных распределений.

**Примеры:**

```python
import random

# Случайное число от 0 до 1
random_value = random.random()
print("Случайное число от 0 до 1:", random_value)

# Случайное целое число в диапазоне
random_int = random.randint(1, 10)
print("Случайное целое число от 1 до 10:", random_int)

# Случайный выбор из списка
choices = ['apple', 'banana', 'cherry']
random_choice = random.choice(choices)
print("Случайный выбор из списка:", random_choice)

# Перемешивание списка
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("Перемешанный список:", my_list)

# Случайное вещественное число в диапазоне
random_float = random.uniform(1.0, 10.0)
print("Случайное вещественное число от 1.0 до 10.0:", random_float)
```

### `collections`

Модуль `collections` реализует специализированные контейнерные типы данных.

**Примеры:**

```python
from collections import Counter, defaultdict, deque, namedtuple

# Counter
text = "abracadabra"
counter = Counter(text)
print("Подсчёт символов в строке 'abracadabra':", counter)

# defaultdict
def_dict = defaultdict(int)
def_dict['apple'] += 1
print("defaultdict с начальным значением int:", def_dict)

# deque
queue = deque([1, 2, 3])
queue.appendleft(0)
queue.append(4)
print("Очередь deque после добавления элементов:", queue)

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print("Координаты точки:", p.x, p.y)
```

### `datetime`

Модуль `datetime` предоставляет классы для работы с датой и временем.

**Примеры:**

```python
from datetime import date, datetime, timedelta

# Текущая дата
today = date.today()
print("Текущая дата:", today)

# Текущее время
now = datetime.now()
print("Текущее время:", now)

# Вычисление разницы во времени
delta = timedelta(days=7)
next_week = today + delta
print("Дата через неделю:", next_week)

# Форматирование даты
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Форматированная дата и время:", formatted_date)

# Парсинг даты из строки
date_str = "2024-07-23"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
print("Парсинг даты из строки:", parsed_date)
```

### `itertools`

Модуль `itertools` предоставляет функции для создания итераторов для эффективных циклов.

**Примеры:**

```python
import itertools

# Бесконечный счётчик
print("Бесконечный счётчик с началом с 10 и шагом 2:")
for i in itertools.count(10, 2):
    if i > 20:
        break
    print(i, end=' ')
print()

# Повторение элемента
cycler = itertools.cycle(['A', 'B', 'C'])
print("Повторение элементов 'A', 'B', 'C':")
for _ in range(10):
    print(next(cycler), end=' ')
print()

# Комбинации
combinations = list(itertools.combinations('ABCD', 2))
print("Комбинации из 2 элементов строки 'ABCD':", combinations)

# Переключение значений
toggle = itertools.cycle([True, False])
print("Переключение значений True и False:")
for _ in range(6):
    print(next(toggle), end=' ')
print()
```

## Отладка (Debugging)

Отладка — это процесс поиска и исправления ошибок в коде. Умение эффективно отлаживать код — один из ключевых навыков
программиста.

### Print-debugging

Самый простой и часто используемый способ — добавление `print()` для вывода значений переменных:

```python
def calculate_total(items):
    total = 0
    for item in items:
        print(f"DEBUG: item = {item}, total before = {total}")  # Отладочный вывод
        total += item['price'] * item['quantity']
        print(f"DEBUG: total after = {total}")  # Отладочный вывод
    return total
```

**Советы:**
- Используйте префикс `DEBUG:` или `>>>` для отладочных сообщений — их легче найти и удалить.
- Выводите не только значения, но и имена переменных: `print(f"{x=}")` (Python 3.8+).

```python
x = 42
name = "Alice"
print(f"{x=}, {name=}")  # x=42, name='Alice'
```

### Встроенный отладчик pdb

Python имеет встроенный отладчик `pdb`. Начиная с Python 3.7, можно использовать функцию `breakpoint()`:

```python
def process_data(data):
    result = []
    for item in data:
        breakpoint()  # Программа остановится здесь
        processed = item * 2
        result.append(processed)
    return result

process_data([1, 2, 3])
```

Когда программа дойдёт до `breakpoint()`, откроется интерактивная консоль отладчика:

#### Основные команды pdb

| Команда    | Сокращение | Описание                                   |
|------------|------------|--------------------------------------------|
| `help`     | `h`        | Показать справку                           |
| `next`     | `n`        | Выполнить следующую строку                 |
| `step`     | `s`        | Войти внутрь функции                       |
| `continue` | `c`        | Продолжить выполнение до следующей точки   |
| `print`    | `p`        | Вывести значение переменной (`p variable`) |
| `list`     | `l`        | Показать код вокруг текущей строки         |
| `quit`     | `q`        | Выйти из отладчика                         |
| `where`    | `w`        | Показать стек вызовов                      |

```python
# Пример сессии отладки
# > /path/to/file.py(5)process_data()
# -> processed = item * 2
# (Pdb) p item
# 1
# (Pdb) p result
# []
# (Pdb) n
# (Pdb) p processed
# 2
# (Pdb) c
```

### Отладка в IDE

Современные IDE (PyCharm, VS Code) предоставляют визуальный отладчик с удобным интерфейсом.

#### VS Code

1. Установите расширение Python
2. Поставьте точку останова (breakpoint), кликнув слева от номера строки
3. Нажмите F5 или Run → Start Debugging
4. Используйте панель отладки для пошагового выполнения

#### PyCharm

1. Поставьте точку останова кликом слева от номера строки
2. Правый клик → Debug (или Shift+F9)
3. Используйте панель Debug для навигации

**Преимущества визуального отладчика:**
- Просмотр всех переменных в текущей области видимости.
- Просмотр стека вызовов.
- Условные точки останова (остановка только при выполнении условия).
- Watches — отслеживание конкретных выражений.

### Модуль logging вместо print

Для более серьёзных проектов вместо `print()` лучше использовать модуль `logging`:

```python
import logging

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def calculate_total(items):
    total = 0
    for item in items:
        logger.debug(f"Processing item: {item}")
        total += item['price'] * item['quantity']
        logger.debug(f"Running total: {total}")
    logger.info(f"Final total: {total}")
    return total
```

**Преимущества logging:**
- Разные уровни важности (DEBUG, INFO, WARNING, ERROR, CRITICAL).
- Легко включать/выключать без удаления кода.
- Можно направлять в файл, консоль или другие места.
- Автоматически добавляет время, имя модуля и т. д.

> **Совет:** Начинайте с `print()` для быстрой отладки, но в реальных проектах переходите на `logging`.

## Про docstring и комментарии

Комментарии и строковые литералы документации (docstrings) являются важными инструментами для написания чистого и
понятного кода. Комментарии помогают другим разработчикам (и вам самим в будущем) понять, что делает конкретный фрагмент
кода, а docstrings служат для создания документации, объясняющей, как пользоваться функциями, классами и модулями.

### Комментарии в Python

Комментарии в Python начинаются с символа `#` и продолжаются до конца строки. Python интерпретирует эти строки как
комментарии и игнорирует их при выполнении кода.

**Пример использования комментариев:**

```python
# Это однострочный комментарий
x = 5  # Это комментарий после кода


# Следующий код вычисляет факториал числа
def factorial(n):
    # Инициализируем результат
    result = 1
    # Перебираем все числа от 1 до n
    for i in range(1, n + 1):
        result *= i
    return result
```

Комментарии помогают объяснить сложную логику, описать алгоритмы или просто напомнить о важных вещах.

### Многострочные комментарии

В Python нет синтаксической поддержки многострочных комментариев, как в некоторых других языках программирования.
Однако для этого часто используют несколько однострочных комментариев:

**Пример многострочных комментариев:**

```python
# Это многострочный комментарий.
# Он используется для объяснения большого блока кода
# или сложного алгоритма.

x = 10
y = 20
z = x + y
```

### Строковые литералы документации (docstrings)

Docstrings — это строки, используемые для документирования модулей, классов, методов и функций. В отличие от обычных
комментариев, docstrings можно получить программно через атрибут `__doc__`.

**Пример использования docstring:**

```python
def add(a: int, b: int) -> int:
    """
    Возвращает сумму двух чисел.

    Аргументы:
    a -- первое число
    b -- второе число

    Возвращает:
    Сумма аргументов a и b.
    """
    return a + b


# Получение docstring
print(add.__doc__)
```

Этот docstring объясняет, что делает функция `add`, какие параметры она принимает и что возвращает.

### Docstrings для классов и модулей

Docstrings также используются для документирования классов и модулей.

**Пример docstring для класса:**

```python
class Dog:
    """
    Класс для представления собаки.

    Атрибуты:
    name (str) -- имя собаки
    age (int) -- возраст собаки

    Методы:
    bark() -- заставляет собаку лаять
    """

    def __init__(self, name: str, age: int):
        """
        Инициализирует объект Dog с именем и возрастом.

        Аргументы:
        name (str) -- имя собаки
        age (int) -- возраст собаки
        """
        self.name = name
        self.age = age

    def bark(self) -> str:
        """Заставляет собаку лаять."""
        return "Woof!"
```

**Пример docstring для модуля:**

```python
"""
Этот модуль предоставляет функции для работы с геометрическими фигурами.

Функции:
area_of_circle(radius) -- возвращает площадь круга с заданным радиусом
perimeter_of_square(side) -- возвращает периметр квадрата с заданной стороной
"""


def area_of_circle(radius: float) -> float:
    """Возвращает площадь круга с заданным радиусом."""
    from math import pi
    return pi * radius ** 2


def perimeter_of_square(side: float) -> float:
    """Возвращает периметр квадрата с заданной стороной."""
    return 4 * side
```

### Форматирование docstring

Существуют различные соглашения по форматированию docstring, включая стандарты Google, NumPy/SciPy и reStructuredText
(reST). Важно выбрать один стандарт и придерживаться его во всём проекте.
См. также PEP 257 (Docstring Conventions).


**Пример docstring в стиле Google:**

```python
def multiply(a: int | float, b: int | float) -> int | float:
    """
    Умножает два числа.

    Args:
        a (int, float): Первое число.
        b (int, float): Второе число.

    Returns:
        int, float: Произведение аргументов a и b.
    """
    return a * b
```

> См. также PEP 257 (Docstring Conventions) и PEP 484 (Type Hints).
> Docstring, как и типизации, в современном мире считаются обязательным стандартом написания кода, и я ожидаю от вас
> использования их во всех домашках и модулях!

![](https://ymatuhin.ru/assets/img/styleguide/styleguide.jpg)

## [PEP 8](https://peps.python.org/pep-0008/)

PEP 8 (Python Enhancement Proposal 8) — это руководство по стилю написания кода на Python. Соблюдение этого стандарта
помогает разработчикам создавать код, который легко читать и поддерживать. В этой лекции мы рассмотрим основные аспекты
PEP8, включая правила именования переменных, использование пробелов, составные инструкции, тернарный оператор и отступы
между функциями и классами.

### Импорты: порядок и группировка

- Сначала импорты стандартной библиотеки.
- Затем импорты сторонних пакетов (third‑party).
- Затем локальные импорты текущего проекта.
- Между группами — пустая строка.
- Предпочитайте абсолютные импорты; относительные используйте осмотрительно внутри пакета.
- Избегайте `from module import *`.
- Автоматизируйте: isort (порядок импортов), black (форматирование), ruff/flake8 (линтинг).


### Именование переменных

#### Правильное именование

1. **Переменные и функции**:
    - Используйте стиль `snake_case` (слова разделяются нижним подчеркиванием).
    - Примеры:
      ```python
      user_name = "John"
      calculate_total()
      ```

2. **Классы**:
    - Используйте стиль `CamelCase` (каждое слово начинается с заглавной буквы).
    - Примеры:
      ```python
      class UserProfile:
          pass
      ```

#### Неправильное именование

- Избегайте использования стиля `camelCase` для функций и переменных.
- Избегайте слишком коротких или слишком длинных имён.
- Избегайте имён, состоящих из одного символа (например, `x`, `y`), если только это не циклические переменные или
  индексы.

### Использование пробелов

#### Пробелы вокруг операторов

- Добавляйте пробелы вокруг операторов присваивания (`=`), арифметических операторов (`+`, `-`, `*`, `/` и т. д.), а
  также вокруг операторов сравнения (`==`, `!=`, `<`, `>` и т. д.).
  ```python
  a = b + c
  if a == b:
      pass
  ```

#### Пробелы внутри скобок

- Не добавляйте пробелы внутри круглых, квадратных или фигурных скобок.
  ```python
  my_list = [1, 2, 3]
  function_call(a, b)
  ```

#### Пробелы перед запятыми и после запятых

- Не добавляйте пробелы перед запятыми.
- Добавляйте пробелы после запятых.
  ```python
  my_tuple = (1, 2, 3)
  ```

### Составные инструкции

### Длина строки

- Классическая рекомендация: до 79 символов для кода и до 72 для docstring/комментариев.
- На практике команды часто выбирают 88 (совместимо с black) или 100/120.
- В проекте зафиксируйте одно значение и придерживайтесь его единообразно.


Избегайте составных инструкций, когда несколько операторов записаны в одной строке.

#### Неправильно

```python
import os;import sys
```

#### Правильно

```python
import os
import sys
```

### Тернарный оператор

Тернарный оператор в Python используется для написания кратких условий. Он позволяет сократить код, записывая условие и
результат в одной строке.

#### Пример использования

```python
result = x if condition else y
```

#### Пример

```python
is_even = True if number % 2 == 0 else False
```

### Отступы между функциями и классами

Отступы между функциями и классами способствуют лучшей читаемости кода и разделению логических блоков.

#### Правила

1. **Отступы между методами внутри класса**:
    - Используйте одну пустую строку.
    - Пример:
      ```python
      class MyClass:
          def method_one(self):
              pass

          def method_two(self):
              pass
      ```

2. **Отступы между классами и функциями на верхнем уровне**:
    - Используйте две пустые строки.
    - Пример:
      ```python
      class FirstClass:
          pass


      class SecondClass:
          pass


      def my_function():
          pass
      ```


---

## Практика на занятии

### Задание 1. Работа с datetime

Напишите функции для работы с датами:

```python
from datetime import datetime, timedelta

def parse_date(date_string: str, format: str = "%d.%m.%Y") -> datetime:
    """Парсит строку в объект datetime."""
    pass

def days_between(date1: datetime, date2: datetime) -> int:
    """Возвращает количество дней между двумя датами."""
    pass

def add_business_days(start_date: datetime, days: int) -> datetime:
    """Добавляет рабочие дни (пропуская субботу и воскресенье)."""
    pass
```

```python
# Пример использования:
d1 = parse_date("15.01.2024")
d2 = parse_date("20.01.2024")
print(days_between(d1, d2))  # 5

# Добавить 5 рабочих дней к пятнице 19.01.2024
friday = parse_date("19.01.2024")
result = add_business_days(friday, 5)
print(result.strftime("%d.%m.%Y"))  # 26.01.2024 (пропустили выходные)
```

### Задание 2. Работа с collections

Используйте модуль `collections` для решения задач:

**2.1. Counter — подсчёт слов**

```python
from collections import Counter

def word_frequency(text: str) -> dict:
    """Возвращает словарь {слово: количество}, топ-10 самых частых."""
    pass

text = "the quick brown fox jumps over the lazy dog the fox"
print(word_frequency(text))
# {'the': 3, 'fox': 2, 'quick': 1, ...}
```

**2.2. defaultdict — группировка**

```python
from collections import defaultdict

def group_by_length(words: list) -> dict:
    """Группирует слова по длине."""
    pass

words = ["cat", "dog", "elephant", "rat", "lion", "tiger"]
print(group_by_length(words))
# {3: ['cat', 'dog', 'rat'], 8: ['elephant'], 4: ['lion'], 5: ['tiger']}
```

---

## Домашняя работа

### Задание 1. Файловый менеджер (модуль os)

Напишите утилиты для работы с файловой системой:

```python
import os

def find_files(directory: str, extension: str) -> list:
    """
    Рекурсивно находит все файлы с указанным расширением.

    Args:
        directory: путь к директории
        extension: расширение файла (например, ".py")

    Returns:
        Список полных путей к найденным файлам
    """
    pass

def get_directory_size(directory: str) -> int:
    """Возвращает общий размер директории в байтах."""
    pass

def find_duplicates(directory: str) -> dict:
    """
    Находит файлы с одинаковыми именами в разных поддиректориях.

    Returns:
        Словарь {имя_файла: [список путей]}
    """
    pass
```

```python
# Пример использования:
py_files = find_files("/path/to/project", ".py")
print(f"Найдено {len(py_files)} Python-файлов")

size = get_directory_size("/path/to/project")
print(f"Размер: {size / 1024 / 1024:.2f} MB")
```

### Задание 2. Генератор паролей (модуль random)

Создайте гибкий генератор паролей:

```python
import random
import string

def generate_password(
    length: int = 12,
    use_uppercase: bool = True,
    use_lowercase: bool = True,
    use_digits: bool = True,
    use_special: bool = True,
    exclude_chars: str = "",
    must_include: str = ""
) -> str:
    """
    Генерирует случайный пароль.

    Args:
        length: длина пароля
        use_uppercase: использовать заглавные буквы
        use_lowercase: использовать строчные буквы
        use_digits: использовать цифры
        use_special: использовать спецсимволы
        exclude_chars: символы, которые нужно исключить
        must_include: символы, которые обязательно должны быть в пароле
    """
    pass

def check_password_strength(password: str) -> str:
    """
    Оценивает силу пароля.

    Returns:
        "weak", "medium", "strong" или "very strong"
    """
    pass
```

```python
# Пример использования:
pwd = generate_password(16, use_special=True)
print(pwd)  # "Kj#9xLm$2pQw&nRt"

print(check_password_strength("123456"))      # weak
print(check_password_strength("Password1"))   # medium
print(check_password_strength("Kj#9xLm$2p"))  # very strong
```

### Задание 3. Комбинаторика (модуль itertools)

Решите задачи с использованием `itertools`:

```python
import itertools

def all_combinations(items: list, min_size: int = 1, max_size: int = None) -> list:
    """Возвращает все комбинации элементов от min_size до max_size."""
    pass

def unique_permutations(items: list) -> list:
    """Возвращает уникальные перестановки (для списков с повторами)."""
    pass

def cartesian_product(*iterables) -> list:
    """Возвращает декартово произведение."""
    pass
```

```python
# Пример использования:
print(all_combinations([1, 2, 3], 2, 2))
# [(1, 2), (1, 3), (2, 3)]

print(unique_permutations([1, 1, 2]))
# [(1, 1, 2), (1, 2, 1), (2, 1, 1)]

print(cartesian_product([1, 2], ['a', 'b']))
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```

**Практическое применение:** Напишите функцию, которая генерирует все возможные комбинации пиццы из списка топпингов (от 1 до 4 топпингов):

```python
toppings = ["pepperoni", "mushrooms", "olives", "onions", "peppers"]
pizzas = all_pizza_combinations(toppings, max_toppings=4)
print(f"Всего вариантов пиццы: {len(pizzas)}")
```

### Задание 4. Рефакторинг по PEP8

Исправьте следующий код, чтобы он соответствовал PEP8:

```python
# bad_code.py — исправьте этот код

import sys,os
from collections import Counter,defaultdict
import random

def Calculate_Average(numbers_list):
    """this function calculates average"""
    if len(numbers_list)==0:return 0
    total=0
    for n in numbers_list:total+=n
    return total/len(numbers_list)

class user_account:
    def __init__(self,Name,email,Age):
        self.name=Name;self.email=email;self.age=Age
    def GetInfo(self):
        return f"User: {self.name}, Email: {self.email}"
    def is_adult(self):
        if self.age>=18:
            return True
        else:
            return False

def   process_data(  data,   flag=True):
    result=[]
    for item in data:
        if flag==True:
            result.append(item*2)
        else:
            result.append(item)
    return result

x=10
y=20
z=x+y
list1=[1,2,3,4,5]
dict1={"a":1,"b":2}
```

**Что нужно исправить:**
- Импорты (порядок, группировка).
- Именование (функции, классы, переменные).
- Пробелы (вокруг операторов, после запятых).
- Составные инструкции.
- Упрощение условий.
- Добавить docstrings.

### Задание 5. ⭐ Создание пакета

Создайте свой Python-пакет `myutils` со следующей структурой:

```
myutils/
├── __init__.py
├── strings/
│   ├── __init__.py
│   ├── validators.py    # is_email, is_phone, is_url
│   └── formatters.py    # to_snake_case, to_camel_case, truncate
├── numbers/
│   ├── __init__.py
│   ├── statistics.py    # mean, median, mode, std_dev
│   └── converters.py    # to_roman, from_roman, to_binary
└── files/
    ├── __init__.py
    └── utils.py         # read_json, write_json, read_csv, write_csv
```

**Требования:**

1. Каждый модуль должен иметь docstring.
2. Используйте относительные импорты внутри пакета.
3. В `__init__.py` экспортируйте основные функции для удобного импорта.
4. Добавьте `if __name__ == "__main__"` для тестирования модулей.

```python
# Пример использования после создания пакета:
from myutils.strings import is_email, to_snake_case
from myutils.numbers import mean, to_roman
from myutils import read_json  # Если экспортировано в __init__.py

print(is_email("test@example.com"))  # True
print(to_snake_case("HelloWorld"))   # hello_world
print(mean([1, 2, 3, 4, 5]))         # 3.0
print(to_roman(42))                  # XLII
```

### Задание 6. Рефакторинг модуля

Возьмите ваш модуль из первого блока курса и разбейте его на логические части:

```
my_project/
├── main.py      # Точка входа, основная логика
├── files.py     # Работа с файлами
├── utils.py     # Вспомогательные функции
├── models.py    # Классы данных (если есть)
└── config.py    # Константы и настройки
```

**Требования:**
- Используйте абсолютные импорты.
- Добавьте docstrings ко всем функциям и классам.
- Проверьте код на соответствие PEP8 (можно использовать `flake8` или `pylint`).
- Добавьте `if __name__ == "__main__"` в `main.py`.

---

[← Лекция 10: Magic methods. Итераторы и генераторы.](lesson10.md) | [Лекция 12: Декораторы. Декораторы с параметрами. Декораторы классов (staticmethod, classmethod, property) →](lesson12.md)
