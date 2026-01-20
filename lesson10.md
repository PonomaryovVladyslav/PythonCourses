# Лекция 10. Magic methods. Итераторы и генераторы.

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
  - [Лекция 8. Git. Удалённый репозиторий. Remote, push, pull. GitHub, Bitbucket, GitLab, etc. Pull request.](lesson08.md)
</details>

<details open>
  <summary>Блок 3 — Python Advanced (9–14)</summary>

  - [Лекция 9. Введение в ООП. Основные парадигмы ООП. Классы и объекты. Множественное наследование.](lesson09.md)
  - ▶ **Лекция 10. Magic methods. Итераторы и генераторы.**
  - [Лекция 11. Imports. Standard library. PEP8](lesson11.md)
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

  - [Лекция 34. Linux. Всё, что нужно знать для деплоймента.](lesson34.md)
  - [Лекция 35. Deployment](lesson35.md)
</details>

- [Лекция 36. Методологии разработки. CI/CD. Монолит и микросервисы. Docker](lesson36.md)

## Magic methods (они же иногда называются dunder-методы)

![](https://files.realpython.com/media/Python-Magic-Methods_Watermarked.a69c3876000a.jpg)

Магические методы, также известные как dunder-методы (от double underscore — двойное подчёркивание), являются
специальными методами, которые
начинаются и заканчиваются двойным подчеркиванием, например, `__init__`. Эти методы позволяют нам настраивать поведение
объектов классов и переопределять встроенные функции и операторы.

### Что такое магические методы?

Магические методы — это специальные методы, которые позволяют вам переопределить или настроить поведение объектов в
Python. Они выполняют специфические задачи и автоматически вызываются при использовании различных операторов и функций.

### Классификация магических методов

Магические методы можно условно разделить на несколько категорий:

1. Инициализация и удаление объектов: `__init__`, `__del__`
2. Представление объектов: `__str__`, `__repr__`
3. Перегрузка операторов: `__add__`, `__sub__`, `__mul__` и т. д.
4. Контейнеры и последовательности: `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`
5. Итерации: `__iter__`, `__next__`
6. Контекстные менеджеры: `__enter__`, `__exit__`
7. Другие методы: `__call__`, `__hash__`, `__eq__` и многие другие

### Инициализация и удаление объектов. `__init__` и `__del__`

#### `__init__`

Метод `__init__` вызывается, когда объект класса создаётся. Он инициализирует объект.

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

alice = Person("Alice", 30)
bob = Person(name='Bob', age=35)
print(alice.name)  # Alice
print(alice.age)   # 30
print(bob.name)  # Bob
print(bob.age)   # 35
```

`__init__` есть практически у каждого класса — это очень часто используемый метод.

#### `__del__`

Метод `__del__` вызывается перед уничтожением объекта.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Deleting {self.name}")

alice = Person("Alice")
del alice  # Deleting Alice
```


### Представление объектов. `__str__` и `__repr__`

Методы `__str__` и `__repr__` позволяют вам определить, как объект будет представлен в виде строки.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

alice = Person("Alice", 30)
print(str(alice))  # Alice, 30 years old
print(repr(alice)) # Person(name=Alice, age=30)

```

Используйте `__str__()`, когда нужно строковое представление объекта для конечных пользователей, акцентируя внимание на
читаемости, а не на полноте. Используйте `__repr__()` для создания строки, которая будет интересна разработчикам, — стремясь
к точности и однозначности представления.

### Перегрузка операторов

Что такое перегрузка? Это возможность переопределить действие, которое уже существует.

Магические методы позволяют перегружать операторы. Например, метод `__add__` перегружает оператор `+`.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 1)
print(v1 + v2)  # Vector(3, 4)
```

#### Полный список магических методов перегрузки операторов
1. Арифметические операторы

    - `__add__(self, other)`: для оператора `+`
    - `__sub__(self, other)`: для оператора `-`
    - `__mul__(self, other)`: для оператора `*`
    - `__truediv__(self, other)`: для оператора `/`
    - `__floordiv__(self, other)`: для оператора `//`
    - `__mod__(self, other)`: для оператора `%`
    - `__pow__(self, other)`: для оператора `**`
    - `__radd__(self, other)`: для оператора `+` (правосторонний)
    - `__rsub__(self, other)`: для оператора `-` (правосторонний)
    - `__rmul__(self, other)`: для оператора `*` (правосторонний)
    - `__rtruediv__(self, other)`: для оператора `/` (правосторонний)
    - `__rfloordiv__(self, other)`: для оператора `//` (правосторонний)
    - `__rmod__(self, other)`: для оператора `%` (правосторонний)
    - `__rpow__(self, other)`: для оператора `**` (правосторонний)
    - `__iadd__(self, other)`: для оператора `+=`
    - `__isub__(self, other)`: для оператора `-=`
    - `__imul__(self, other)`: для оператора `*=`
    - `__itruediv__(self, other)`: для оператора `/=`
    - `__ifloordiv__(self, other)`: для оператора `//=`
    - `__imod__(self, other)`: для оператора `%=`
    - `__ipow__(self, other)`: для оператора `**=`

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __truediv__(self, other):
        return Number(self.value / other.value)

    def __floordiv__(self, other):
        return Number(self.value // other.value)

    def __mod__(self, other):
        return Number(self.value % other.value)

    def __pow__(self, other):
        return Number(self.value ** other.value)

    def __str__(self):
        return str(self.value)

n1 = Number(10)
n2 = Number(2)
print(n1 + n2)  # 12
print(n1 - n2)  # 8
print(n1 * n2)  # 20
print(n1 / n2)  # 5.0
print(n1 // n2) # 5
print(n1 % n2)  # 0
print(n1 ** n2) # 100
```

2. Операторы сравнения

    - `__eq__(self, other)`: для оператора `==`
    - `__ne__(self, other)`: для оператора `!=`
    - `__lt__(self, other)`: для оператора `<`
    - `__le__(self, other)`: для оператора `<=`
    - `__gt__(self, other)`: для оператора `>`
    - `__ge__(self, other)`: для оператора `>=`

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __str__(self):
        return f"{self.name}, {self.age}"

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)
print(p1 == p2)  # False
print(p1 > p2)   # True
```

3. Логические операторы

    - `__and__(self, other)`: для оператора `&`
    - `__or__(self, other)`: для оператора `|`
    - `__xor__(self, other)`: для оператора `^`
    - `__invert__(self)`: для оператора `~`
    - `__rand__(self, other)`: для оператора `&` (правосторонний)
    - `__ror__(self, other)`: для оператора `|` (правосторонний)
    - `__rxor__(self, other)`: для оператора `^` (правосторонний)
    - `__iand__(self, other)`: для оператора `&=`
    - `__ior__(self, other)`: для оператора `|=`
    - `__ixor__(self, other)`: для оператора `^=`

```python
class Bitwise:
    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        return Bitwise(self.value & other.value)

    def __or__(self, other):
        return Bitwise(self.value | other.value)

    def __xor__(self, other):
        return Bitwise(self.value ^ other.value)

    def __invert__(self):
        return Bitwise(~self.value)

    def __str__(self):
        return str(self.value)

b1 = Bitwise(6)  # 110 in binary
b2 = Bitwise(3)  # 011 in binary
print(b1 & b2)   # 2 (010 in binary)
print(b1 | b2)   # 7 (111 in binary)
print(b1 ^ b2)   # 5 (101 in binary)
print(~b1)       # -7 (two's complement)
```

4. Смешанные операторы

    - `__neg__(self)`: для оператора унарного минуса `-`
    - `__pos__(self)`: для оператора унарного плюса `+`
    - `__abs__(self)`: для функции `abs()`
    - `__invert__(self)`: для оператора `~`
    - `__complex__(self)`: для функции `complex()`
    - `__int__(self)`: для функции `int()`
    - `__float__(self)`: для функции `float()`
    - `__round__(self, n)`: для функции `round()`
    - `__index__(self)`: для функций `hex(), oct(), bin()`
    - `__trunc__(self)`: для функции `math.trunc()`
    - `__floor__(self)`: для функции `math.floor()`
    - `__ceil__(self)`: для функции `math.ceil()`

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __neg__(self):
        return Number(-self.value)

    def __pos__(self):
        return Number(+self.value)

    def __abs__(self):
        return Number(abs(self.value))

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __round__(self, n):
        return round(self.value, n)

    def __index__(self):
        return int(self.value)

    def __str__(self):
        return str(self.value)

n = Number(-5)
print(-n)          # 5
print(+n)          # -5
print(abs(n))      # 5
print(int(n))      # -5
print(float(n))    # -5.0
print(round(n, 1)) # -5.0
print(hex(n))      # -0x5
```

### Контейнеры и последовательности

Методы, такие как `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, и `__contains__`, позволяют реализовать поведение контейнеров.

```python
class CustomList:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

    def __contains__(self, item):
        return item in self.items

cl = CustomList()
cl.items.append(1)
cl.items.append(2)
print(len(cl))  # 2
print(cl[0])    # 1
cl[1] = 3
print(cl[1])    # 3
del cl[0]
print(len(cl))  # 1
print(3 in cl)  # True
```

### Контекстные менеджеры

Методы `__enter__` и `__exit__` позволяют использовать объекты в контексте `with`.

```python
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with ManagedFile('test.txt') as f:
    f.write('Hello, world!')

```

### Другие методы

Метод `__call__` позволяет сделать объект вызываемым, как функцию.

```python
class Greeter:
    def __init__(self, name):
        self.name = name

    def __call__(self, greeting):
        return f"{greeting}, {self.name}!"

g = Greeter("Alice")
print(g("Hello"))  # Hello, Alice!
```

Это свойство мы будем использовать на занятии по декораторам!

`__hash__`

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return (self.name, self.age) == (other.name, other.age)

    def __hash__(self):
        return hash((self.name, self.age))

p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
print(p1 == p2)               # True
print(hash(p1) == hash(p2))  # True
```

Это далеко не полный список того, что можно делать с классами; магических методов гораздо больше. Всё, что вам надо знать, —
это что на любое действие уже существует заготовка. Нужно только найти, что именно переписывать.

[Хорошая статья по теме](https://habr.com/ru/post/186608/)

### Магические атрибуты (Magic Attributes)

Помимо магических **методов**, в Python есть магические **атрибуты** — специальные свойства, которые Python автоматически создаёт для объектов, классов, функций и модулей. Они также начинаются и заканчиваются двойным подчёркиванием.

Что такое модуль, пакет и докстринг, мы детально рассмотрим на следующем занятии, а пока достаточно знать, что это такое.

Модуль — это файл с расширением `.py`, который содержит определения и инструкции Python.

Пакет — это директория, которая содержит файл `__init__.py` и другие модули.

Докстринг — это строка, которая является первым выражением в модуле, функции, классе или методе. Она используется для документирования кода.

#### Атрибуты функций

```python
def greet(name: str) -> str:
    """Приветствует пользователя по имени."""
    return f"Hello, {name}!"

print(greet.__name__)        # 'greet' — имя функции
print(greet.__doc__)         # 'Приветствует пользователя по имени.' — docstring
print(greet.__module__)      # '__main__' — модуль, где определена функция
print(greet.__annotations__) # {'name': <class 'str'>, 'return': <class 'str'>}
print(greet.__defaults__)    # None (или кортеж значений по умолчанию)
```

| Атрибут           | Описание                                              |
|-------------------|-------------------------------------------------------|
| `__name__`        | Имя функции (строка)                                  |
| `__doc__`         | Строка документации (docstring)                       |
| `__module__`      | Имя модуля, в котором определена функция              |
| `__annotations__` | Словарь аннотаций типов                               |
| `__defaults__`    | Кортеж значений аргументов по умолчанию               |
| `__kwdefaults__`  | Словарь значений keyword-only аргументов по умолчанию |
| `__code__`        | Объект скомпилированного кода функции                 |
| `__globals__`     | Ссылка на глобальное пространство имён модуля         |
| `__closure__`     | Кортеж ячеек замыкания (или None)                     |

#### Атрибуты классов и объектов

```python
class Animal:
    """Базовый класс животного."""
    species = "Unknown"

    def __init__(self, name: str):
        self.name = name

dog = Animal("Buddy")

# Атрибуты класса
print(Animal.__name__)      # 'Animal' — имя класса
print(Animal.__doc__)       # 'Базовый класс животного.'
print(Animal.__module__)    # '__main__'
print(Animal.__bases__)     # (<class 'object'>,) — родительские классы
print(Animal.__mro__)       # Method Resolution Order — порядок поиска методов

# Атрибуты экземпляра
print(dog.__class__)        # <class '__main__.Animal'> — класс объекта
print(dog.__dict__)         # {'name': 'Buddy'} — словарь атрибутов экземпляра
```

| Атрибут      | Описание                                                                                        |
|--------------|-------------------------------------------------------------------------------------------------|
| `__name__`   | Имя класса                                                                                      |
| `__doc__`    | Docstring класса                                                                                |
| `__module__` | Модуль, где определён класс                                                                     |
| `__bases__`  | Кортеж базовых (родительских) классов                                                           |
| `__mro__`    | Method Resolution Order — порядок разрешения методов                                            |
| `__dict__`   | Словарь атрибутов (для класса — методы и атрибуты класса, для экземпляра — атрибуты экземпляра) |
| `__class__`  | Ссылка на класс объекта                                                                         |

#### Атрибуты модулей

```python
import math

print(math.__name__)    # 'math' — имя модуля
print(math.__doc__)     # Документация модуля
print(math.__file__)    # Путь к файлу модуля
print(math.__package__) # Имя пакета (для модулей в пакетах)
```

#### Зачем это нужно?

1. **Интроспекция** — исследование объектов во время выполнения:
   ```python
   def describe(obj):
       print(f"Type: {type(obj).__name__}")
       print(f"Doc: {obj.__doc__}")
   ```

2. **Декораторы** — сохранение метаданных оригинальной функции (см. `functools.wraps` в лекции 12):
   ```python
   from functools import wraps

   def my_decorator(func):
       @wraps(func)  # Копирует __name__, __doc__ и др.
       def wrapper(*args, **kwargs):
           return func(*args, **kwargs)
       return wrapper
   ```

3. **Отладка и логирование**:
   ```python
   import logging

   def log_call(func):
       def wrapper(*args, **kwargs):
           logging.info(f"Calling {func.__name__}")
           return func(*args, **kwargs)
       return wrapper
   ```

4. **Сериализация и ORM** — Django и другие фреймворки используют `__dict__` для работы с атрибутами объектов.


## Итераторы

Документация: https://docs.python.org/3/tutorial/classes.html#iterators

Во многих современных языках программирования используют такие сущности, как итераторы. Основное их назначение — это
упрощение навигации по элементам объекта, который, как правило, представляет собой некоторую коллекцию (список, словарь
и т. п.). Язык Python в этом случае не исключение, и в нём тоже есть поддержка итераторов. Итератор представляет собой
объект-перечислитель, который для данного объекта выдаёт следующий элемент либо бросает исключение, если элементов
больше нет.

Основное место использования итераторов – это цикл `for`. Если вы перебираете элементы в некотором списке или символы в
строке с помощью цикла `for`, то фактически это означает, что при каждой итерации цикла происходит обращение к
итератору, содержащемуся в строке/списке с требованием выдать следующий элемент, если элементов в объекте больше нет,
то итератор генерирует исключение, обрабатываемое в рамках цикла `for` незаметно для пользователя.

Приведем несколько примеров, которые помогут лучше понять эту концепцию. Для начала выведем элементы произвольного
списка на экран.

```python
num_list = [1, 2, 3, 4, 5]
for i in num_list:
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5
```

Как уже было сказано, объекты, элементы которых можно перебирать в цикле `for`, содержат в себе объект-итератор. Для
того чтобы его получить, необходимо использовать функцию `iter()`, а для извлечения следующего элемента из итератора —
функцию `next()`.

```python
itr = iter(num_list)
print(next(itr))  # 1
print(next(itr))  # 2
print(next(itr))  # 3
print(next(itr))  # 4
print(next(itr))  # 5
print(next(itr))  # StopIteration
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
```

Как видно из приведенного выше примера, вызов функции `next(itr)` каждый раз возвращает следующий элемент из списка, а
когда эти элементы заканчиваются, генерируется исключение `StopIteration`.

### Последовательности и итерируемые объекты

По сути, вся разница между последовательностями и итерируемыми объектами (**не итераторами**) заключается в том, что в
последовательностях элементы упорядочены.

Таким образом, последовательностями являются списки, кортежи и даже строки.

```python
numbers = [1, 2, 3, 4, 5]
letters = ('a', 'b', 'c')
characters = 'habristhebestsiteever'

numbers[1]      # 2
letters[2]      # 'c'
characters[11]  # 's'
characters[0:4] # 'habr'
```

Итерируемые объекты же, напротив, не упорядочены, но тем не менее могут быть использованы там, где требуется итерация:
цикл `for`, выражения-генераторы, списковые включения (list comprehensions) — как примеры.

```python
# Множества не поддерживают индексацию
unordered_numbers = {1, 2, 3}
unordered_numbers[1]  # TypeError: 'set' object is not subscriptable

# Словари индексируются по ключам, не по позиции
users = {'males': 23, 'females': 32}
users[1]  # KeyError: 1

# Но их можно итерировать
[number ** 2 for number in unordered_numbers]  # [1, 4, 9]

for user in users:
    print(user)
# Output:
# males
# females
```

**Последовательность — всегда итерируемый объект, итерируемый объект — не всегда последовательность.**

### Как работает `for`

Цикл `for` вызывает метод `iter()` и к полученному объекту применяет метод `next()`, пока не встретит
исключение `StopIteration`.

Это называется *протокол итерации*. На самом деле он применяется не только в цикле `for`, но и в генераторном выражении,
и даже при распаковке и «звёздочке»:

```python
coordinates = [1, 2, 3]
x, y, z = coordinates

numbers = [1, 2, 3, 4, 5]
a, b, *rest = numbers

print(rest)
[3, 4, 5]
```

В случае, если мы передаём в `iter()` итератор, то получаем тот же самый итератор:

```python
numbers = [1, 2, 3, 4, 5]
iter1 = iter(numbers)
iter2 = iter(iter1)
next(iter1)
# 1
next(iter2)
# 2
iter1 is iter2
# True
```

Подытожим.

`Итерируемый объект` — это что-то, что можно итерировать.

`Итератор` — это сущность, порождаемая функцией `iter`, с помощью которой происходит итерирование итерируемого объекта.

`Итератор` не имеет индексов и может быть использован только один раз.

### Итераторы повсюду

Мы уже видели много итераторов в Python. Многие встроенные функции являются итераторами.

Так, например, `enumerate()`:

```python
numbers = [1, 2, 3]
enumerate_var = enumerate(numbers)
enumerate_var
# <enumerate object at 0x7ff975dfdd80>
next(enumerate_var)
# (0, 1)
```

А также `zip()`:

```python
letters = ['a', 'b', 'c']
z = zip(letters, numbers)
z
# <zip object at 0x7ff975e00588>
next(z)
# ('a', 1)
```

И даже `open()`:

```python
f = open('foo.txt')
next(f)
# 'bar\n'
next(f)
# 'baz\n'
```

В Python очень много итераторов, и, как уже упоминалось выше, они откладывают выполнение работы до того момента, как мы
запрашиваем следующий элемент с помощью `next()`. Так называемое «ленивое» выполнение.

### Создание своих итераторов: `__iter__` и `__next__`

Если нужно обойти элементы внутри объекта вашего собственного класса, необходимо построить свой итератор. Создадим
класс, объект которого будет итератором, выдающим определенное количество единиц, которое пользователь задает при
создании объекта. Такой класс будет содержать конструктор, принимающий на вход количество единиц и метод `__next__()`,
без него экземпляры данного класса не будут итераторами.

```python
class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        raise StopIteration


s_iter1 = SimpleIterator(3)
print(next(s_iter1))
print(next(s_iter1))
print(next(s_iter1))
print(next(s_iter1))  # StopIteration
```

В нашем примере при четвертом вызове функции `next()` будет выброшено исключение `StopIteration`. Если мы хотим, чтобы с
данным объектом можно было работать в цикле `for`, то в класс `SimpleIterator` нужно добавить метод `__iter__()`,
который возвращает итератор, в данном случае этот метод должен возвращать `self`.

```python
class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        raise StopIteration


s_iter2 = SimpleIterator(5)
for i in s_iter2:
    print(i)
```

### Генераторные выражения

Генераторное выражение (в круглых скобках) создаёт ленивую последовательность. Списковое включение (в квадратных скобках) создаёт список сразу в памяти.

```python
gen = (i for i in range(10))      # генераторное выражение (лениво)
lst = [i for i in range(10)]      # списковое включение (список)
```

## Генераторы

Генераторы — это тоже итераторы, но их проще создавать.

### Return VS Yield

Ключевое слово `return` — это финальная инструкция в функции. Она предоставляет способ для возвращения значения. При
возвращении весь локальный стек очищается. И новый вызов начнется с первой инструкции.

Ключевое слово `yield` же сохраняет состояние между вызовами. Выполнение продолжается с момента, где управление было
передано в вызывающую область, то есть, сразу после последней инструкции `yield`.

### Генератор vs. Функция

Дальше перечислены основные отличия между генератором и обычной функцией.

Генератор использует `yield` для отправления значения пользователю, а у функции для этого есть `return`.

- При использовании генератора может быть больше одного вызова `yield`.
- Вызов `yield` останавливает исполнение и возвращает итератор, а `return` всегда выполняется последним.
- Вызов метода `next()` приводит к выполнению функции генератора.
- Локальные переменные и состояния сохраняются между последовательными вызовами метода `next()`.
- Каждый дополнительный вызов `next()` вызывает исключение `StopIteration`, если нет следующих элементов для обработки.

Дальше пример функции генератора с несколькими `yield`.

```python
def test_generator():
    x = 2
    print(f'Первый yield, x = {x}')
    yield x

    x *= 2
    print(f'Второй yield, x = {x}')
    yield x

    x *= 2
    print(f'Последний yield, x = {x}')
    yield x


# Вызов генератора
gen = test_generator()

# Вызов первого yield
next(gen)

# Вызов второго yield
next(gen)

# Вызов последнего yield
next(gen)
```

Вывод:

```
Первый yield, x = 2
Второй yield, x = 4
Последний yield, x = 8
```

Генераторы тоже реализуют протокол итератора:

Если генератор встречает `return`, то в этот момент генерируется исключение `StopIteration`.

Если функция завершается без `return`, то после последней строки вызывается `return` без параметров, что и
вызовет `StopIteration` в следующем примере:

```python
>>> def custom_range(number):
...     index = 0
...     while index < number:
...         yield index
...         index += 1
...
>>> range_of_four = custom_range(4)
>>> next(range_of_four)
0
>>> next(range_of_four)
1
>>> next(range_of_four)
2
>>> next(range_of_four)
3
>>> next(range_of_four)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

### Когда использовать генератор?

Есть много ситуаций, когда генератор оказывается полезным:

- Генераторы помогают обрабатывать большие объемы данных. Они позволяют производить так называемые ленивые вычисления.

- Подобным образом происходит потоковая обработка. Генераторы можно выстраивать друг за другом и использовать их как
  Unix-каналы.

- Они часто используются для чтения крупных файлов. Это делает код чище и компактнее, разделяя процесс на более мелкие
  сущности.

- Генераторы особенно полезны для веб-скрапинга и увеличения эффективности поиска. Они позволяют получить одну страницу,
  выполнить какую-то операцию и двигаться к следующей.

### Генератор vs Итератор: сравнение

Генератор кажется сложной концепцией, но его легко использовать в программах. Это хорошая альтернатива итераторам.

Рассмотрим следующий пример реализации арифметической прогрессии с помощью класса итератора:

```python
class AP:
    def __init__(self, a1, d, size):
        self.ele = a1
        self.diff = d
        self.len = size
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.len:
            raise StopIteration
        elif self.count == 0:
            self.count += 1
            return self.ele
        else:
            self.count += 1
            self.ele += self.diff
            return self.ele


for ele in AP(1, 2, 10):
    print(ele)
```

Ту же логику куда проще написать с помощью генератора:

```python
def ap(a1, d, size):
    count = 1
    while count <= size:
        yield a1
        a1 += d
        count += 1


for ele in ap(1, 2, 10):
    print(ele)
```

### Экономия памяти

Если использовать обычную функцию для возвращения списка, то она сформирует целую последовательность в памяти перед
отправлением. Это приведет к использованию большого количества памяти, что неэффективно.

Генератор же использует намного меньше памяти за счет обработки одного элемента за раз.

### Обработка больших данных

Генераторы полезны при обработке особенно больших объемов данных, например, Big Data. Они работают как бесконечный поток
данных.

Такие объемы нельзя хранить в памяти. Но генератор, выдающий по одному элементу за раз, представляет собой этот
бесконечный поток.

Следующий код теоретически может выдать все простые числа:

```python
def find_prime():
    num = 1
    while True:
        if num > 1:
            for i in range(2, num):
                if not num % i:
                    break
            else:
                yield num
        num += 1


for ele in find_prime():
    print(ele)
```

### Последовательность генераторов (pipeline)

С помощью генераторов можно создать последовательность разных операций. Это более чистый способ разделения обязанностей
между всеми компонентами и последующей интеграции их для получения нужного результата.

```python
def generate_numbers(limit):
    """Генератор чисел от 1 до limit"""
    for num in range(1, limit + 1):
        yield num


def filter_even(seq):
    """Фильтрует только чётные числа"""
    for num in seq:
        if num % 2 == 0:
            yield num


def square(seq):
    """Возводит числа в квадрат"""
    for num in seq:
        yield num ** 2


# Создаём pipeline: числа -> только чётные -> квадраты
pipeline = square(filter_even(generate_numbers(10)))

for result in pipeline:
    print(result)

# Output:
# 4
# 16
# 36
# 64
# 100
```

В примере выше связаны три генератора: первый генерирует числа от 1 до 10, второй фильтрует только чётные, третий возводит в квадрат. Данные «протекают» через pipeline лениво — по одному элементу за раз.

### yield from

Документация: [PEP 380](https://peps.python.org/pep-0380/)

Есть специальная конструкция `yield from`, она позволяет делегировать генерацию другому итератору:

```python
# Обычный yield
def numbers_range(n):
    for i in range(n):
        yield i


# yield from — то же самое, но короче
def numbers_range(n):
    yield from range(n)
```

`yield from` принимает в качестве параметра итератор. Генератор — это тоже итератор, а значит `yield from` может принимать другой генератор:

```python
def subgenerator():
    yield 'World'


def generator():
    yield 'Hello,'
    yield from subgenerator()  # Запрашиваем значение из subgenerator()
    yield '!'


for i in generator():
    print(i, end=' ')
# Вывод: Hello, World !
```

### Особенности генераторов

В случае использования выражения-генератора мы не храним значения, а значит, можем использовать его только один раз:

```python
gen = (x for x in range(0, 100 * 10000))
100 in gen
True
100 in gen
False
```

> **Важно:** Генераторы могут не только возвращать значения, но и принимать их на вход через метод `send()`.
> Это продвинутая тема, которая понадобится для понимания асинхронного программирования — подробнее в [Лекции 32](lesson32.md).

---

## Знакомство с async/await

В Python существует ещё один важный механизм, тесно связанный с генераторами — **асинхронное программирование**.
Вы будете встречать ключевые слова `async` и `await` в различных библиотеках и фреймворках, поэтому важно понимать,
что они означают.

### Зачем нужна асинхронность?

Представьте, что вам нужно скачать 100 файлов из интернета. При обычном (синхронном) подходе вы скачиваете их
по одному: начали первый → ждём → закончили → начали второй → ждём → и так далее.

Но большую часть времени программа просто **ждёт ответа от сервера**, ничего не делая!

Асинхронность позволяет **не ждать**, а переключиться на другую задачу, пока первая ожидает ответа:

```
Синхронно:          [====ждём====][====ждём====][====ждём====]  → 30 секунд
Асинхронно:         [==ждём==]
                      [==ждём==]
                        [==ждём==]                              → 10 секунд
```

### Что такое async и await?

- `async def` — объявляет **асинхронную функцию** (корутину)
- `await` — **приостанавливает** выполнение корутины, пока не завершится другая асинхронная операция

```python
import asyncio


async def say_hello():
    print("Привет!")
    await asyncio.sleep(1)  # Асинхронная пауза — не блокирует другие задачи
    print("Пока!")


# Запуск асинхронной функции
asyncio.run(say_hello())
```

### Как это связано с генераторами?

Исторически асинхронность в Python была построена на генераторах. Ключевое слово `yield` позволяло
«приостановить» функцию и вернуться к ней позже — именно это и нужно для асинхронного программирования.

В Python 3.5 появились `async`/`await` как более понятный синтаксис, но под капотом механизм похож:
корутина «приостанавливается» на `await` и возобновляется, когда результат готов.

### Простой пример: параллельные задачи

```python
import asyncio


async def download(name, seconds):
    print(f"Начинаю загрузку {name}...")
    await asyncio.sleep(seconds)  # Имитация загрузки
    print(f"Загрузка {name} завершена!")
    return name


async def main():
    # Запускаем три загрузки "параллельно"
    results = await asyncio.gather(
        download("файл1", 2),
        download("файл2", 1),
        download("файл3", 3),
    )
    print(f"Все загрузки завершены: {results}")


asyncio.run(main())

# Вывод:
# Начинаю загрузку файл1...
# Начинаю загрузку файл2...
# Начинаю загрузку файл3...
# Загрузка файл2 завершена!
# Загрузка файл1 завершена!
# Загрузка файл3 завершена!
# Все загрузки завершены: ['файл1', 'файл2', 'файл3']
```

Обратите внимание: все три загрузки **начались одновременно**, и общее время выполнения — 3 секунды
(время самой долгой задачи), а не 6 секунд (сумма всех).

### Когда использовать async/await?

✅ **Подходит для:**
- Сетевые запросы (HTTP, базы данных, API)
- Работа с файлами (чтение/запись)
- Любые операции ввода-вывода (I/O)

❌ **Не подходит для:**
- Вычислительные задачи (математика, обработка данных)
- CPU-bound операции — для них используйте `multiprocessing`

> **Подробнее** об асинхронном программировании, библиотеке `asyncio` и практическом применении
> мы поговорим в [Лекции 32](lesson32.md).

---

## Практика на занятии

### Задание 1. Расширение класса Student (магические методы)

Возьмите класс `Student` из прошлого занятия и добавьте:

1. Инициализация через `__init__(self, name, age, grades=None)`
2. Метод `add_grade(grade)` — добавляет оценку
3. Метод `average_grade()` — возвращает средний балл
4. `__str__` — возвращает `"Student: Иван, avg: 4.5"`
5. `__repr__` — возвращает `"Student('Иван', 20, [4, 5, 5])"`
6. `__eq__` — два студента равны, если у них одинаковые имя и возраст
7. `__lt__` — сравнение по среднему баллу (для сортировки)

```python
# Пример использования:
s1 = Student("Иван", 20, [4, 5, 5])
s2 = Student("Мария", 19, [5, 5, 5])
s3 = Student("Пётр", 21, [3, 4, 4])

print(s1)  # Student: Иван, avg: 4.67
print(repr(s2))  # Student('Мария', 19, [5, 5, 5])

# Сортировка по среднему баллу
students = [s1, s2, s3]
print(max(students).name)  # Мария (лучший средний балл)
```

### Задание 2. Простой итератор Countdown

Создайте класс `Countdown`, который итерируется от заданного числа до 0:

```python
class Countdown:
    def __init__(self, start: int):
        self.start = start

    def __iter__(self):
        # Ваш код
        pass

    def __next__(self):
        # Ваш код
        pass

# Пример использования:
for num in Countdown(5):
    print(num, end=" ")
# 5 4 3 2 1 0
```

И такое же задание, но с помощью генератора!

---

## Домашняя работа

### Задание 1. Расширение класса Group (контейнерные методы)

Возьмите класс `Group` и добавьте магические методы, чтобы группа вела себя как контейнер:

1. `__len__` — количество студентов в группе
2. `__getitem__(index)` — получение студента по индексу
3. `__setitem__(index, student)` — замена студента по индексу
4. `__delitem__(index)` — удаление студента по индексу
5. `__iter__` — итерация по студентам
6. `__contains__(student)` — проверка, есть ли студент в группе

```python
# Пример использования:
group = Group("Python-101")
group.add_student(Student("Иван", 20, [4, 5]))
group.add_student(Student("Мария", 19, [5, 5]))
group.add_student(Student("Пётр", 21, [3, 4]))

print(len(group))  # 3
print(group[0].name)  # Иван
print(Student("Мария", 19, [5, 5]) in group)  # True

for student in group:
    print(student)

# Найти лучшего студента
best = max(group)
print(f"Лучший студент: {best.name}")
```

### Задание 2. Класс Vector (перегрузка операторов)

Создайте класс `Vector` для работы с математическими векторами:

```python
class Vector:
    def __init__(self, *components):
        self.components = components

    def __add__(self, other): ...      # v1 + v2
    def __sub__(self, other): ...      # v1 - v2
    def __mul__(self, scalar): ...     # v * 3 (умножение на скаляр)
    def __rmul__(self, scalar): ...    # 3 * v
    def __eq__(self, other): ...       # v1 == v2
    def __abs__(self): ...             # abs(v) — длина вектора
    def __len__(self): ...             # len(v) — размерность
    def __getitem__(self, index): ...  # v[0]
    def __repr__(self): ...            # Vector(1, 2, 3)
    def __str__(self): ...             # "(1, 2, 3)"
```

```python
# Пример использования:
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1 + v2)      # (5, 7, 9)
print(v1 - v2)      # (-3, -3, -3)
print(v1 * 2)       # (2, 4, 6)
print(3 * v1)       # (3, 6, 9)
print(abs(v1))      # 3.7416... (sqrt(1+4+9))
print(v1 == Vector(1, 2, 3))  # True
print(len(v1))      # 3
print(v1[0])        # 1
```

### Задание 3. Контекстный менеджер Timer

Создайте контекстный менеджер `Timer`, который измеряет время выполнения блока кода:

```python
import time

class Timer:
    def __init__(self, name: str = "Block"):
        self.name = name
        self.elapsed = None

    def __enter__(self):
        # Запомнить время начала
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Вычислить и вывести время
        pass

# Пример использования:
with Timer("Sorting"):
    data = [i for i in range(1000000)]
    sorted(data, reverse=True)
# Sorting: 0.1234 seconds

with Timer("Sleeping"):
    time.sleep(0.5)
# Sleeping: 0.5012 seconds
```

### Задание 4. Генераторы

**4.1. Генератор Fibonacci**

Напишите генератор `fibonacci(n)`, который выдаёт первые `n` чисел Фибоначчи:

```python
def fibonacci(n: int):
    # Ваш код с yield
    pass

print(list(fibonacci(10)))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

**4.2. Бесконечный генератор**

Напишите генератор `infinite_sequence(start=0)`, который бесконечно генерирует числа:

```python
def infinite_sequence(start: int = 0):
    # Ваш код
    pass

gen = infinite_sequence(10)
print(next(gen))  # 10
print(next(gen))  # 11
print(next(gen))  # 12
```

**4.3. Генератор для чтения файла по частям**

Напишите генератор `read_in_chunks(filename, chunk_size=1024)`, который читает файл порциями:

```python
def read_in_chunks(filename: str, chunk_size: int = 1024):
    # Ваш код
    pass

for chunk in read_in_chunks("large_file.txt", 100):
    print(len(chunk))  # Выведет размеры порций
```

### Задание 5. ⭐ Свой класс Range

Создайте класс `MyRange`, который работает как встроенный `range`, но реализован вами:

```python
class MyRange:
    def __init__(self, *args):
        # Поддержка MyRange(stop), MyRange(start, stop), MyRange(start, stop, step)
        pass

    def __iter__(self): ...
    def __len__(self): ...
    def __getitem__(self, index): ...  # Поддержка индексации и срезов
    def __contains__(self, value): ...
    def __repr__(self): ...
    def __eq__(self, other): ...
    def __reversed__(self): ...
```

```python
# Пример использования:
r = MyRange(1, 10, 2)

# Итерация
for i in r:
    print(i, end=" ")  # 1 3 5 7 9

# Длина
print(len(r))  # 5

# Индексация
print(r[0])   # 1
print(r[-1])  # 9
print(r[1:3]) # MyRange(3, 7, 2) или [3, 5]

# Проверка вхождения
print(5 in r)  # True
print(6 in r)  # False

# Сравнение
print(r == MyRange(1, 10, 2))  # True

# Обратный порядок
print(list(reversed(r)))  # [9, 7, 5, 3, 1]
```

**Подсказка:** изучите, как работает `range` — он не хранит все числа в памяти, а вычисляет их по формуле.

---

[← Лекция 9: Введение в ООП. Основные парадигмы ООП. Классы и объекты. Множественное наследование.](lesson09.md) | [Лекция 11: Imports. Standard library. PEP8 →](lesson11.md)