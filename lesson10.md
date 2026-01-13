# Лекция 10. Множественное наследование. MRO. Magic methods.

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

  - [Лекция 9. Введение в ООП. Основные парадигмы ООП. Классы и объекты.](lesson09.md)
  - ▶ **Лекция 10. Множественное наследование. MRO. Magic methods.**
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
  - [Лекция 32. Асинхронное программирование в Python. Корутины. Asyncio.](lesson32.md)
  - [Лекция 33. Сокеты. Django channels.](lesson33.md)
</details>

<details>
  <summary>Блок 8 — Deployment (34–35)</summary>

  - [Лекция 34. Linux. Всё, что нужно знать для деплоймента.](lesson34.md)
  - [Лекция 35. Deployment](lesson35.md)
</details>

- [Лекция 36. Методологии разработки. CI/CD. Монолит и микросервисы. Docker](lesson36.md)


![](https://i.ytimg.com/vi/ektST9ppziE/maxresdefault.jpg)

## Множественное наследование

Множественное наследование — это возможность у класса-потомка наследовать функционал не от одного, а от нескольких
родителей. Благодаря этому мы можем создавать сложные структуры, сохраняя простой и легко поддерживаемый код.

Во многих языках программирования нет множественного наследования, так что давайте разбираться, как это вообще работает.

Например, у нас есть класс автомобиля:

```python
class Auto:
    def ride(self):
        print("Riding on ground")

```

Также у нас есть класс для лодки:

```python
class Boat:
    def swim(self):
        print("Sailing in the ocean")

```

Теперь, если нам нужно запрограммировать автомобиль-амфибию, который будет плавать в воде и ездить по земле, мы вместо
написания нового класса можем просто унаследовать от уже существующих, просто написав их через запятую:

```python
class Auto:
    def ride(self):
        print("Riding on ground")


class Boat:
    def swim(self):
        print("Sailing in the ocean")


class Amphibian(Auto, Boat):
    pass


a = Amphibian()
a.ride()
a.swim()
```

![](https://python-course.eu/images/oop/clock_calendar_500w.webp)

Теперь наш класс имеет атрибуты и методы обоих родителей (их может быть сколько угодно).

Обратите внимание, что объект класса Amphibian будет одновременно объектом класса Auto и Boat, то есть:

```python
a = Amphibian()
isinstance(a, Auto)
# True
isinstance(a, Boat)
# True
isinstance(a, Amphibian)
# True
```

### Миксины (Mixins)

Миксин, он же примесь, — это тип классов, которые нужны, чтобы добавлять к обычным классам какие-то методы или атрибуты,
но эти классы не используются для создания объектов, только как примесь. (Нас ничего не останавливает создать объект
этого класса, но задача в другом)

Представим, что мы программируем класс для автомобиля.
Мы хотим, чтобы у нас была возможность слушать музыку в машине.
Конечно, можно просто добавить метод `play_music()` в класс `Car`:

```python
class Car:
    def ride(self):
        print("Riding a car")

    def play_music(self, song):
        print(f"Now playing: {song}.")


c = Car()
c.ride()
# Riding a car
c.play_music("Queen - Bohemian Rhapsody")
# Now playing: Queen - Bohemian Rhapsody
```

Но что, если у нас есть ещё и телефон, радио или любой другой девайс, с которого мы будем слушать музыку?
В таком случае лучше вынести функционал проигрывания музыки в отдельный класс-миксин:

```python
class MusicPlayerMixin:
    def play_music(self, song):
        print(f"Now playing: {song}.")
```

Мы можем «домешивать» этот класс в любой, где нужна функция проигрывания музыки:

```python
class Smartphone(MusicPlayerMixin):
    pass


class Radio(MusicPlayerMixin):
    pass


class Amphibian(Auto, Boat, MusicPlayerMixin):
    pass
```

В рамках изучения Django мы будем довольно много использовать такие классы, рекомендую детально ознакомиться.
Небольшие рекомендации по миксинам:
- давайте им суффикс Mixin (например, MusicPlayerMixin);
- избегайте состояния и лишних __init__ в миксинах; держите их маленькими и специализированными;
- если миксин должен переопределять методы баз, ставьте его левее в списке базовых классов.


### Diamond problem. MRO

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190612120714/diamond-problem-solution.png)

Итак, классы-наследники могут использовать родительские атрибуты и методы.
Но что, если у нескольких родителей будут одинаковые атрибуты или методы?
Какой метод в таком случае будет использовать наследник?

Рассмотрим классический пример:

```python
class A:
    def hi(self):
        print("A")


class B(A):
    def hi(self):
        print("B")


class C(A):
    def hi(self):
        print("C")


class D(B, C):
    pass


d = D()
d.hi()
```

Эта ситуация, так называемое ромбовидное наследование (diamond problem), решается в Python путем установления порядка
разрешения методов.

В современном Python используется C3-линеаризация (MRO, Method Resolution Order). Порядок поиска атрибутов/методов формируется линейно на основе иерархии и указанного порядка базовых классов. Важно, в каком порядке написаны базовые в объявлении класса.

В Python 2 «old‑style» классы имели другой порядок, но «new‑style» (наследующиеся от object) также использовали C3. Сейчас Python 2 устарел.

В Python 3 можно посмотреть, в каком порядке будут проинспектированы родительские классы, при помощи метода класса `mro()`:

### MRO - Method resolution order

Чтобы посмотреть, в каком порядке Python будет искать атрибуты или методы у родителей, у любого класса можно вызывать
метод `mro()`:

```python
>>> D.mro()
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

Обратите внимание, в конце всегда будет `object`, если вы используете любой Python.
Потому что вообще всё отнаследовано от него, как я и говорил на прошлом занятии. (Всё это объект!)

Если по какой-то причине вас не устраивает существующий порядок, есть возможность вызвать метод ровно из того класса,
откуда вам надо, но это считается плохой практикой и лучше так не делать, а полностью поменять структуру.

Если вам необходимо использовать метод конкретного родителя, например, `hi()` класса С, нужно напрямую вызвать его по
имени класса, передав `self` в качестве аргумента:

```python
# НЕ НАДО ТАК ДЕЛАТЬ!!!
class D(B, C):
    def call_hi(self):
        C.hi(self)


d = D()
d.call_hi()
```

[Большая статья про МРО и вообще множественное наследование тут](https://habr.com/ru/post/62203/?_ga=2.205768979.1207595081.1598867257-330984554.1578271027)

## Magic methods (Они же иногда называются dunder-методы)

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
3. Перегрузка операторов: `__add__`, `__sub__`, `__mul__` и т.д.
4. Контейнеры и последовательности: `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`
5. Итерации: `__iter__`, `__next__`
6. Контекстные менеджеры: `__enter__`, `__exit__`
7. Другие методы: `__call__`, `__hash__`, `__eq__` и многие другие

### Инициализация и удаление объектов. `__init__` и `__del__`

#### `__init__`

Метод `__init__` вызывается, когда объект класса создается. Он инициализирует объект.

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

Используйте `__str__()` когда нужно строковое представление объекта для конечных пользователей, акцентируя внимание на
читаемости, а не на полноте. Используйте `__repr__()` для создания строки, которая будет интересна разработчикам, стремясь
к точности и однозначности представления.

### Перегрузка операторов

Что такое перегрузка? Это возможность переопределить действие, которое уже существует.

Магические методы позволяют перегружать операторы. Например, метод `__add__` перегружает оператор +.

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

### Итерации

Для создания итераторов в Python используются методы `__iter__` и `__next__`.

О том, как это работает, вас ждёт целая лекция ближе к концу курса!

```python
class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.max:
            raise StopIteration
        self.current += 1
        return self.current

c = Counter(3)
for number in c:
    print(number)  # 1 2 3

```

### Контекстные менеджеры

Методы `__enter__` и `__exit__` позволяют использовать объекты в контексте with.

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

Это далеко не полный список того, что можно делать с классами; магических методов гораздо больше. Всё, что вам надо знать, — это
что на любое действие уже существует заготовка. Нужно только найти, что именно переписывать.

[Хорошая статья по теме](https://habr.com/ru/post/186608/)

## Создание Собственных Исключений в Python

Программирование часто требует работы с различными типами ошибок и исключений. В Python существует множество встроенных исключений, таких как `ValueError`, `TypeError` и `IndexError`, которые помогают обрабатывать различные виды ошибок. Однако иногда возникает необходимость создать собственные исключения для более точной и специфичной обработки ошибок в вашей программе. В этой статье мы рассмотрим, как создавать и использовать собственные исключения в Python.

### Зачем нужны собственные исключения?

Собственные исключения позволяют:

1. **Улучшить читабельность кода**: Вы можете использовать описательные имена исключений, чтобы было ясно, какая ошибка произошла и почему.
2. **Обеспечить точность обработки ошибок**: Вы можете точно указать, какие ошибки должны быть перехвачены и обработаны.
3. **Создавать многоуровневую иерархию ошибок**: Позволяет создавать базовые и специализированные исключения для более гибкой обработки ошибок.

### Как создать собственное исключение?

Для создания собственного исключения в Python, необходимо создать новый класс, который наследует от базового класса исключений, обычно это `Exception`.

#### Пример простого исключения

```python
class MyCustomError(Exception):
    """Класс для пользовательского исключения."""
```

#### Пример исключения с дополнительной информацией

```python
class InvalidInputError(Exception):
    """Исключение вызывается, когда ввод недействителен."""

    def __init__(self, message, value):
        self.message = message
        self.value = value
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.value}'
```

### Использование собственных исключений

После создания собственного исключения, вы можете использовать его в своем коде, как и любое другое встроенное исключение.

#### Пример использования

```python
def divide(a, b):
    if b == 0:
        raise InvalidInputError("Деление на ноль", b)
    return a / b

try:
    result = divide(10, 0)
except InvalidInputError as e:
    print(e)
```

### Иерархия пользовательских исключений

Создание иерархии исключений может быть полезным, если ваш код может генерировать различные виды ошибок, которые имеют общие черты.

#### Пример иерархии

```python
class ApplicationError(Exception):
    """Базовый класс для всех исключений приложения."""
    pass

class DatabaseError(ApplicationError):
    """Исключения, связанные с базой данных."""
    pass

class FileNotFoundError(ApplicationError):
    """Исключения, связанные с отсутствием файла."""
    pass
```

### Пример использования иерархии

```python
def connect_to_database():
    raise DatabaseError("Не удалось подключиться к базе данных")

try:
    connect_to_database()
except ApplicationError as e:
    print(f"Произошла ошибка приложения: {e}")
except DatabaseError as e:
    print(f"Ошибка базы данных: {e}")
```

Практика:

1. К созданному на прошлом занятии классу студент задаём ему имя, возраст и оценки через `__init__`
2. Добавляем метод для добавления оценки
3. Добавляем метод(ы) вычисления среднего балла
4. Прописываем магический метод (или методы), которые позволяют найти студента с наилучшим средним баллом из списка
5. Берём класс группы из прошлого занятия
6. Добавляем возможность добавить студента к группе
7. Добавляем возможность удалить студента из группы
8. Добавляем возможность найти группу, в которой учится студент с самым высоким средним баллом