# Лекция 12. Декораторы. Декораторы с параметрами. Декораторы классов (staticmethod, classmethod, property)

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
  - [Лекция 11. Imports. Standard library. PEP8](lesson11.md)
  - ▶ **Лекция 12. Декораторы. Декораторы с параметрами. Декораторы классов (staticmethod, classmethod, property)**
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


![](https://tirinox.ru/wp-content/uploads/2019/10/risovach.ru_.jpg)

## Что такое декоратор

Итак, что же такое «декоратор»?

Декораторы — это мощный инструмент, который позволяет изменять поведение функций или методов без изменения их исходного
кода. Мы рассмотрим, что такое декораторы, как их создавать и использовать, а также обсудим примеры их практического
применения.

> Декораторы — это функции, которые принимают другую функцию в качестве аргумента и возвращают новую функцию с
> изменённым или расширенным поведением.
> Они позволяют добавлять функциональность к существующим функциям и методам простым и выразительным способом.

На самом деле про функции, это немного обман, потому что декоратором может быть любой вызываемый объект, и можно сделать
декоратор через классы, но об этом позже.

### Пример декоратора

```python
def simple_decorator(func):
    def wrapper():
        print("Что-то делается до вызова функции")
        func()
        print("Что-то делается после вызова функции")

    return wrapper


@simple_decorator
def say_hello():
    print("Hello!")


say_hello()
```

### Давайте разбираться, как это работает и что это за магия

В Python всё является объектами.

Функции в Python тоже являются объектами.

Давайте посмотрим, что из этого следует:

```python
def shout(word="Yes"):
    return word.capitalize() + "!"


print(shout())
# выведет: 'Yes!'

# Так как функция — это объект, вы можете связать её с переменной,
# как и любой другой объект
scream = shout

# Заметьте, что мы не используем скобок: мы НЕ вызываем функцию "shout",
# мы связываем её с переменной "scream". Это означает, что теперь мы
# можем вызывать "shout" через "scream":

print(scream())
# выведет: 'Yes!'

# Более того, это значит, что мы можем удалить "shout", и функция всё ещё
# будет доступна через переменную "scream"

del shout
try:
    print(shout())
except NameError:
    print("Нет такой функции")

print(scream())
# выведет: 'Yes!'
```

Запомним этот факт, скоро мы к нему вернёмся, но кроме того стоит понимать, что функция в Python может быть
определена… внутри другой функции!

```python
def talk():
    # Внутри определения функции "talk" мы можем определить другую...
    def whisper(word="yes"):
        return word.lower() + "..."

    # ... и сразу же её использовать!
    print(whisper())


# Теперь, КАЖДЫЙ РАЗ при вызове "talk" внутри неё определяется, а затем
# и вызывается функция "whisper".
talk()
# выведет: "yes..."

# Но вне функции "talk" НЕ существует никакой функции "whisper":
try:
    print(whisper())
except NameError:
    print("Нет такой функции, она видна только внутри функции talk")
```

### Ссылки на функции

Теперь мы знаем, что функции являются полноправными объектами, а значит:

- могут быть связаны с переменной;
- могут быть определены одна внутри другой.

> Что ж, а это значит, что одна функция может вернуть другую функцию! (Да, функция может быть возвращаемым значением.)

Давайте посмотрим:

```python
def get_talk(type="shout"):
    # Мы определяем функции прямо здесь
    def shout(word="Yes"):
        return word.capitalize() + "!"

    def whisper(word="yes"):
        return word.lower() + "..."

    # Затем возвращаем необходимую
    if type == "shout":
        # Заметьте, что мы НЕ используем "()", нам нужно не вызвать функцию,
        # а вернуть объект функции
        return shout
    else:
        return whisper


# Как использовать это непонятное нечто?
# Возьмём функцию и свяжем её с переменной
talk = get_talk()

# Как мы можем видеть, теперь "talk" — объект "function":
print(talk)
# выведет: <function shout at 0xb7ea817c>

# Который можно вызывать, как и функцию, определённую "обычным образом":
print(talk())

# Если нам захочется, можно вызвать её напрямую из возвращаемого значения:
print(get_talk("whisper")())
# выведет: yes...

```

> Подождите, раз мы можем возвращать функцию, значит, мы можем и передавать её другой функции как параметр:

```python
def do_something_before(func):
    print("Я делаю что-то ещё перед тем, как вызвать функцию, которую ты мне передал")
    print(func())


do_something_before(scream)

# выведет:
# Я делаю что-то ещё перед тем, как вызвать функцию, которую ты мне передал
# Yes!
```

Ну что, теперь у нас есть все необходимые знания для того, чтобы понять, как работают декораторы.

Как можно догадаться, декораторы — это просто своеобразные «обёртки», которые дают нам возможность делать
что-либо до и после того, как декорируемая функция что-то сделает, не изменяя её.

Создадим свой декоратор «вручную»:

```python

# Декоратор — это функция, ожидающая ДРУГУЮ функцию в качестве параметра
def my_shiny_new_decorator(a_function_to_decorate):
    # Внутри себя декоратор определяет функцию-"обёртку".
    # Она будет (что бы вы думали?..) обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.

    def the_wrapper_around_the_original_function():
        # Поместим здесь код, который мы хотим запускать ДО вызова
        # оригинальной функции
        print("Я — код, который отработает до вызова функции")

        # ВЫЗОВЕМ саму декорируемую функцию
        a_function_to_decorate()

        # А здесь поместим код, который мы хотим запускать ПОСЛЕ вызова
        # оригинальной функции
        print("А я — код, срабатывающий после")

    # На данный момент функция "a_function_to_decorate" НЕ ВЫЗЫВАЛАСЬ НИ РАЗУ

    # Теперь, вернём функцию-обёртку, которая содержит в себе
    # декорируемую функцию, и код, который необходимо выполнить до и после.
    # Всё просто!
    return the_wrapper_around_the_original_function


# Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.
def a_stand_alone_function():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?..")


a_stand_alone_function()
# выведет: Я простая одинокая функция, ты ведь не посмеешь меня изменять?..

# Однако, чтобы изменить её поведение, мы можем декорировать её, то есть
# просто передать декоратору, который обернет исходную функцию в любой код,
# который нам потребуется, и вернёт новую, готовую к использованию функцию:

a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function_decorated()
# выведет:
# Я — код, который отработает до вызова функции
# Я простая одинокая функция, ты ведь не посмеешь меня изменять?..
# А я — код, срабатывающий после

# Наверное, теперь мы бы хотели, чтобы каждый раз, во время вызова a_stand_alone_function, вместо неё
# вызывалась a_stand_alone_function_decorated. Нет ничего проще, просто перезапишем a_stand_alone_function
# функцией, которую нам вернул my_shiny_new_decorator:
a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function()
# выведет:
# Я — код, который отработает до вызова функции
# Я простая одинокая функция, ты ведь не посмеешь меня изменять?..
# А я — код, срабатывающий после

```

Этот же синтаксис можно реализовать через @декораторы.

Разрушаем ореол таинственности вокруг декораторов.

Вот так можно было записать предыдущий пример, используя синтаксис декораторов:

```python
@my_shiny_new_decorator
def another_stand_alone_function():
    print("Оставь меня в покое")


another_stand_alone_function()
# выведет:
# Я — код, который отработает до вызова функции
# Оставь меня в покое
# А я — код, срабатывающий после
```

Да, всё действительно так просто! Декоратор — просто синтаксический сахар для конструкций вида:

```python
another_stand_alone_function = my_shiny_new_decorator(another_stand_alone_function)
```

Конечно, можно вкладывать декораторы друг в друга, например так:

```python
def bread(func):
    def wrapper():
        print("</------\>")
        func()
        print("<\______/>")

    return wrapper


def ingredients(func):
    def wrapper():
        print("#tomatoes#")
        func()
        print("~lettuce~")

    return wrapper


def sandwich(food="--ham--"):
    print(food)


sandwich()
# выведет: --ham--
sandwich = bread(ingredients(sandwich))
sandwich()
# выведет:
# </------\>
# #tomatoes#
# --ham--
# ~lettuce~
# <\______/>
```

И используя синтаксис декораторов:

```python
@bread
@ingredients
def sandwich(food="--ham--"):
    print(food)


sandwich()
# выведет:
# </------\>
# #tomatoes#
# --ham--
# ~lettuce~
# <\______/>
```

Следует помнить о том, что порядок декорирования ВАЖЕН:

```python
@ingredients
@bread
def sandwich(food="--ham--"):
    print(food)


sandwich()
# выведет:
# #tomatoes#
# </------\>
# --ham--
# <\______/>
# ~lettuce~
```
> Примечание: декораторы применяются сверху вниз, а при вызове функции выполняются «изнутри наружу» (ближайший к функции — самый внутренний).


### Передача параметров в декоратор

Однако все декораторы, которые мы до этого рассматривали, не имели одного очень важного функционала — передачи
аргументов декорируемой функции.

Что ж, исправим это недоразумение!

Передача («проброс») аргументов в декорируемую функцию.

Никакой чёрной магии, всё, что нам необходимо — собственно, передать аргументы дальше!

```python
def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):  # аргументы прибывают отсюда
        print("Look what I've got:", arg1, arg2)
        function_to_decorate(arg1, arg2)

    return a_wrapper_accepting_arguments


# Теперь, когда мы вызываем функцию, которую возвращает декоратор,
# мы вызываем её "обёртку", передаём ей аргументы и уже в свою очередь
# она передаёт их декорируемой функции

@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print("My name is", first_name, last_name)


print_full_name("Peter", "Wenkman")
# выведет:
# Look what I've got: Peter Wenkman
# My name is Peter Wenkman
```

### Основные сферы применения декораторов

Декораторы могут быть использованы для различных задач, включая:

- Логирование.
- Измерение метрик (за сколько времени выполняется функция или сколько раз; по сути любые метрики).
- Управление доступом и аутентификация.
- Кэширование.

#### Пример логирования

```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами {args} и {kwargs}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} завершена")
        return result

    return wrapper


@log_decorator
def multiply(x, y):
    return x * y


multiply(2, 3)
```

#### Пример замера времени

```python
import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Время выполнения {func.__name__}: {end_time - start_time:.4f} секунд")
        return result

    return wrapper


@timer_decorator
def slow_function():
    time.sleep(2)
    return "Завершено"


slow_function()
```

> Кеширование и аутентификацию будем изучать, когда доберёмся до веба, но да, декораторы часто там применяются.

### Сохранение метаданных: functools.wraps

При декорировании функции мы заменяем её на wrapper. Это приводит к потере метаданных оригинальной функции:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """Приветствует пользователя"""
    print("Hello!")

print(greet.__name__)  # wrapper — не greet!
print(greet.__doc__)   # None — документация потеряна!
```

Это ломает интроспекцию, отладку и генерацию документации. Решение — `functools.wraps`:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # копирует __name__, __doc__, __annotations__ и др.
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """Приветствует пользователя"""
    print("Hello!")

print(greet.__name__)  # greet — правильно!
print(greet.__doc__)   # Приветствует пользователя — сохранено!
```

> **Правило:** всегда используйте `@wraps(func)` в своих декораторах. Это стандартная практика.

### Декорирование методов

Один из важных фактов, которые следует понимать, заключается в том, что функции и методы в Python — это практически
одно и то же за исключением того, что методы всегда ожидают первым параметром ссылку на сам объект (self). Это значит,
что мы можем создавать декораторы для методов так же, как и для функций, просто не забывая про `self`.

```python
def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3  # действительно, дружелюбно — снизим возраст ещё сильней :-)
        return method_to_decorate(self, lie)

    return wrapper


class Lucy(object):

    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def say_your_age(self, lie):
        print(f"I'm {self.age + lie}. Do I look like it?")


l = Lucy()
l.say_your_age(-3)
# выведет: I'm 26. Do I look like it?
```

Конечно, если мы создаём максимально общий декоратор и хотим, чтобы его можно было применить к любой функции или методу,
то стоит воспользоваться тем, что `*args` распаковывает список `args`, а `**kwargs` распаковывает словарь `kwargs`:

```python
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # Данная "обёртка" принимает любые аргументы
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("Did they pass me anything?")
        print(args)
        print(kwargs)
        # Теперь мы распакуем *args и **kwargs
        # Если вы не слишком хорошо знакомы с распаковкой, см. официальную документацию:
        # https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
        function_to_decorate(*args, **kwargs)

    return a_wrapper_accepting_arbitrary_arguments


@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("Python is cool, no argument here.")


function_with_no_argument()


# выведет:
# Did they pass me anything?
# ()
# {}
# Python is cool, no argument here.

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)


function_with_arguments(1, 2, 3)


# выведет:
# Did they pass me anything?
# (1, 2, 3)
# {}
# 1 2 3

@a_decorator_passing_arbitrary_arguments
def function_with_named_arguments(a, b, c, platypus="Why not?"):
    print(f"Do {a}, {b} and {c} like platypuses? {platypus}")


function_with_named_arguments("Bill", "Linus", "Steve", platypus="Definitely!")


# выведет:
# Did they pass me anything?
# ('Bill', 'Linus', 'Steve')
# {'platypus': 'Definitely!'}
# Do Bill, Linus and Steve like platypuses? Definitely!


class Mary(object):
    def __init__(self):
        self.age = 31

    @a_decorator_passing_arbitrary_arguments
    def say_your_age(self, lie=-3):  # Теперь мы можем указать значение по умолчанию
        print(f"I'm {self.age + lie}. Do I look like it?")


m = Mary()
m.say_your_age()
# выведет:
# Did they pass me anything?
# (<__main__ .Mary object at 0xb7d303ac>,)
# {}
# I'm 28. Do I look like it?

```

### Вызов декоратора с различными аргументами

Отлично, с этим разобрались. Что вы теперь скажете о том, чтобы попробовать вызывать декораторы с различными
аргументами?

Это не так просто, как кажется, поскольку декоратор должен принимать функцию в качестве аргумента, и мы не можем просто
так передать ему что-либо ещё.

## Декораторы с аргументами

> Давайте сделаем нечто страшное!

```python
def decorator_maker():
    print("I make decorators!\n"
          "I will be called only once when you ask me to create a decorator for you.")

    def my_decorator(func):
        print("I'm a decorator!\n"
              "I will be called only once: at the moment of decorating the function.")

        def wrapped():
            print("I'm the wrapper around the function being decorated.\n"
                  "I will be called every time you call the decorated function.\n"
                  "I return the result of the decorated function.")
            return func()

        print("I return the decorated function.")

        return wrapped

    print("I return the decorator.")
    return my_decorator


# Давайте теперь создадим декоратор. Это всего лишь ещё один вызов функции
new_decorator = decorator_maker()


# выведет:
# I make decorators!
# I will be called only once when you ask me to create a decorator for you.
# I return the decorator.

# Теперь декорируем функцию
def decorated_function():
    print("I'm the decorated function.")


decorated_function = new_decorator(decorated_function)
# выведет:
# I'm a decorator!
# I will be called only once: at the moment of decorating the function.
# I return the decorated function.


# Теперь наконец вызовем функцию:
decorated_function()
# выведет:
# I'm the wrapper around the function being decorated.
# I will be called every time you call the decorated function.
# I'm the decorated function.

```

Длинно? Длинно. Перепишем данный код без использования промежуточных переменных:

```python
def decorated_function():
    print("I'm the decorated function")


decorated_function = decorator_maker()(decorated_function)
# выведет:
# I make decorators!
# I will be called only once when you ask me to create a decorator for you.
# I return the decorator.
# I'm a decorator!
# I will be called only once: at the moment of decorating the function.
# I return the decorated function.

# Наконец:
decorated_function()
# выведет:
# I'm the wrapper around the function being decorated.
# I will be called every time you call the decorated function.
# I return the result of the decorated function.
# I'm the decorated function.
```

А теперь ещё раз, ещё короче:

```python
@decorator_maker()
def decorated_function():
    print("I am the decorated function.")


# выведет:
# I make decorators!
# I will be called only once when you ask me to create a decorator for you.
# I return the decorator.
# I'm a decorator!
# I will be called only once: at the moment of decorating the function.
# I return the decorated function.

# И снова:
decorated_function()
# выведет:
# I'm the wrapper around the function being decorated.
# I will be called every time you call the decorated function.
# I return the result of the decorated function.
# I'm the decorated function.
```

Вы заметили, что мы вызвали функцию, после знака `@`?

Вернёмся, наконец, к аргументам декораторов, ведь если мы используем функцию, чтобы создавать декораторы «на лету», мы
можем передавать ей любые аргументы, верно?

```python
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
    print("Я создаю декораторы! И я получил следующие аргументы:", decorator_arg1, decorator_arg2)

    def my_decorator(func):
        print("Я — декоратор. И ты всё же смог передать мне эти аргументы:", decorator_arg1, decorator_arg2)

        # Не перепутайте аргументы декораторов с аргументами функций!
        def wrapped(function_arg1, function_arg2):
            print("Я — обёртка вокруг декорируемой функции.\n"
                  "И я имею доступ ко всем аргументам: \n"
                  "\t- и декоратора: {} {}\n"
                  "\t- и функции: {} {}\n"
                  "Теперь я могу передать нужные аргументы дальше"
                  .format(decorator_arg1, decorator_arg2,
                          function_arg1, function_arg2))
            return func(function_arg1, function_arg2)

        return wrapped

    return my_decorator


@decorator_maker_with_arguments("Леонард", "Шелдон")
def decorated_function_with_arguments(function_arg1, function_arg2):
    print("Я — декорируемая функция и я знаю только о своих аргументах: {0}"
          " {1}".format(function_arg1, function_arg2))


decorated_function_with_arguments("Раджеш", "Говард")
# выведет:
# Я создаю декораторы! И я получил следующие аргументы: Леонард Шелдон
# Я — декоратор. И ты всё же смог передать мне эти аргументы: Леонард Шелдон
# Я — обёртка вокруг декорируемой функции.
# И я имею доступ ко всем аргументам:
#   — и декоратора: Леонард Шелдон
#   — и функции: Раджеш Говард
# Теперь я могу передать нужные аргументы дальше
# Я — декорируемая функция и я знаю только о своих аргументах: Раджеш Говард
```

Вот он, искомый декоратор, которому можно передавать произвольные аргументы.

Безусловно, аргументами могут быть любые переменные:

```python
c1 = "Пенни"
c2 = "Лесли"


@decorator_maker_with_arguments("Леонард", c1)
def decorated_function_with_arguments(function_arg1, function_arg2):
    print("Я — декорируемая функция и я знаю только о своих аргументах: {0}"
          " {1}".format(function_arg1, function_arg2))


decorated_function_with_arguments(c2, "Говард")
# выведет:
# Я создаю декораторы! И я получил следующие аргументы: Леонард Пенни
# Я — декоратор. И ты всё же смог передать мне эти аргументы: Леонард Пенни
# Я — обёртка вокруг декорируемой функции.
# И я имею доступ ко всем аргументам:
#   — и декоратора: Леонард Пенни
#   — и функции: Лесли Говард
# Теперь я могу передать нужные аргументы дальше
# Я — декорируемая функция и я знаю только о своих аргументах: Лесли Говард
```

Таким образом, мы можем передавать декоратору любые аргументы, как обычной функции. Мы можем использовать и распаковку
через `*args` и `**kwargs` в случае необходимости.

Но необходимо всегда держать в голове, что декоратор вызывается ровно один раз. Ровно в момент, когда Python
импортирует ваш скрипт. После этого мы уже не можем никак изменить аргументы, с которыми он был вызван.

Когда мы пишем `import x`, все функции из `x` декорируются сразу же, и мы уже не сможем ничего изменить.

> Немного практики: напишем декоратор, декорирующий декоратор.

Вот вам бонус. Это небольшая хитрость позволит вам превратить любой обычный декоратор в декоратор, принимающий
аргументы.

Изначально, чтобы получить декоратор, принимающий аргументы, мы создали его с помощью другой функции.

Мы обернули наш декоратор.

Есть ли у нас что-нибудь, чем можно обернуть функцию?

Точно, декораторы!

Давайте же немного развлечёмся и напишем декоратор для декораторов:

```python
def decorator_with_args(decorator_to_enhance):
    """
    Эта функция задумывается КАК декоратор и ДЛЯ декораторов.
    Она должна декорировать другую функцию, которая должна быть декоратором.
    Лучше выпейте чашку кофе.
    Она даёт возможность любому декоратору принимать произвольные аргументы,
    избавляя вас от головной боли о том, как же это делается, каждый раз, когда этот функционал необходим.
    """

    # Мы используем тот же трюк, который мы использовали для передачи аргументов:
    def decorator_maker(*args, **kwargs):
        # создадим на лету декоратор, который принимает как аргумент только
        # функцию, но сохраняет все аргументы, переданные своему "создателю"
        def decorator_wrapper(func):
            # Мы возвращаем то, что вернёт нам изначальный декоратор, который, в свою очередь
            # ПРОСТО ФУНКЦИЯ (возвращающая функцию).
            # Единственная ловушка в том, что этот декоратор должен быть именно такого
            # decorator(func, *args, **kwargs)
            # вида, иначе ничего не сработает
            return decorator_to_enhance(func, *args, **kwargs)

        return decorator_wrapper

    return decorator_maker
```

Это может быть использовано так:

```python
# Мы создаём функцию, которую будем использовать как декоратор и декорируем её :-)
# Не стоит забывать, что она должна иметь вид "decorator(func, *args, **kwargs)"

@decorator_with_args
def decorated_decorator(func, *args, **kwargs):
    def wrapper(function_arg1, function_arg2):
        print("Мне тут передали...:", args, kwargs)
        return func(function_arg1, function_arg2)

    return wrapper


# Теперь декорируем любую нужную функцию нашим новеньким, ещё блестящим декоратором:

@decorated_decorator(42, 404, 1024)
def decorated_function(function_arg1, function_arg2):
    print("Привет,", function_arg1, function_arg2)


decorated_function("Вселенная и", "всё прочее")
# выведет:
# Мне тут передали...: (42, 404, 1024) {}
# Привет, Вселенная и всё прочее

# Уфффффф!
```

### Рекомендации для работы с декораторами

Декораторы несколько замедляют вызов функции, не забывайте об этом.

Вы не можете «раздекорировать» функцию. Безусловно, существуют трюки, позволяющие создать декоратор, который можно
отсоединить от функции, но это плохая практика. Правильнее будет запомнить, что если функция декорирована — это не
отменить.

### Декоратор с опциональными аргументами

Часто возникает потребность в декораторе, который можно использовать двумя способами:

```python
@decorator        # без аргументов
def func(): ...

@decorator(arg=5) # с аргументами
def func(): ...
```

Вот универсальный шаблон для такого декоратора:

```python
from functools import wraps

def repeat(_func=None, *, times=2):
    """Декоратор, повторяющий вызов функции несколько раз.

    Можно использовать как @repeat, так и @repeat(times=5)
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper

    # Если декоратор вызван без аргументов (@repeat)
    if _func is not None:
        return decorator(_func)
    # Если декоратор вызван с аргументами (@repeat(times=5))
    return decorator


# Использование без аргументов — times=2 по умолчанию
@repeat
def say_hello():
    print("Hello!")

say_hello()
# Hello!
# Hello!


# Использование с аргументами
@repeat(times=3)
def say_bye():
    print("Bye!")

say_bye()
# Bye!
# Bye!
# Bye!
```

Ключевые моменты:
- `_func=None` — позволяет определить, вызван ли декоратор с аргументами.
- `*` после `_func` — все остальные аргументы только именованные (keyword-only).
- Если `_func` не None — декоратор вызван без скобок, сразу декорируем.
- Если `_func` is None — декоратор вызван со скобками, возвращаем внутренний decorator.

## Классы как декораторы

Как я и говорил, вполне допустимым является написание декораторов через классы.

> Можно использовать классы как декораторы, реализовав метод __call__.

```python
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Класс-декоратор до вызова функции")
        result = self.func(*args, **kwargs)
        print("Класс-декоратор после вызова функции")
        return result


@MyDecorator
def say_goodbye():
    print("Goodbye!")


say_goodbye()
```

## Декораторы методов класса

Если открыть документацию Python, то вы увидите, что язык предлагает три вида методов: статические, класса и экземпляра
класса.

Все методы, которые мы писали до этого момента, были методами экземпляра класса.

Давайте посмотрим, какие ещё бывают методы:

```python
class ToyClass:
    def instancemethod(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'
```

### Методы экземпляра класса

Не будем рассматривать подробно, так как это любой уже знакомый нам обычный метод класса.

Это наиболее часто используемый вид методов. Методы экземпляра класса принимают объект класса как первый аргумент,
который принято называть `self` и который указывает на сам экземпляр. Количество параметров метода не ограничено.

Встроенный пример метода экземпляра — `str.upper()`.

### Методы класса

Методы класса принимают класс в качестве параметра, который принято обозначать как `cls`. Он указывает на класс
ToyClass, а не на объект этого класса. При декларации методов этого вида используется декоратор `classmethod`.

Методы класса привязаны к самому классу, а не его экземпляру. Они могут менять состояние класса, что отразится на всех
объектах этого класса, но не могут менять конкретный объект.

Встроенный пример метода класса — `dict.fromkeys()` — возвращает новый словарь с переданными элементами в качестве
ключей.

```python
dict.fromkeys('AEIOU')  # <- вызывается при помощи класса dict
{'A': None, 'E': None, 'I': None, 'O': None, 'U': None}
```

Такие методы используются почти всегда для создания альтернативных конструкторов. Например, класс `Human`, у которого
есть параметр возраст. И мы можем как задать возраст напрямую, так и передать дату рождения для вычисления возраста.

```python
import datetime

class Human:
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @classmethod
    def from_birthday(cls, name: str, birthdate: str, date_format: str):
        today = datetime.datetime.now()
        day_of_birth = datetime.datetime.strptime(birthdate, date_format)
        age = int((today - day_of_birth).days // 365.2425)
        return cls(name, age)


h1 = Human("Anton", 35)
h2 = Human.from_birthday("Vlad", "01-06-1994", "%d-%m-%Y")
```

### Статические методы

Статические методы декларируются при помощи декоратора `staticmethod`. Им не нужен определённый первый аргумент (ни
`self`, ни `cls`).

Их можно воспринимать как методы, которые “не знают, к какому классу относятся”.
По сути ничем не отличаются от обычных функций.

Таким образом, статические методы прикреплены к классу лишь для удобства и не могут менять состояние ни класса, ни его
экземпляра.

#### Когда использовать каждый из методов?

Выбор того, какой из методов использовать, может показаться достаточно сложным. Тем не менее, с опытом этот выбор
делать гораздо проще.

Чаще всего метод класса используется тогда, когда нужен генерирующий метод, возвращающий объект класса. Как видим,
метод класса `from_birthday` используется для создания объекта класса `Human` по дате рождения, а не возрасту.

Статические методы в основном используются как вспомогательные функции и работают с данными, которые им передаются.

## @property (Свойство)

Конвертация метода класса в атрибуты только для чтения.

Один из самых простых способов использования `property` — это использовать его в качестве декоратора метода. Это
позволит вам превратить метод класса в атрибут класса.

Давайте взглянем на простой пример:

```python
class Person(object):
    """"""

    def __init__(self, first_name, last_name):
        """Конструктор"""
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        """
        Возвращаем полное имя
        """
        return f"{self.first_name} {self.last_name}"
```

В данном коде мы создали два класса атрибута, или свойств: `self.first_name` и `self.last_name`.

Далее мы создали метод `full_name`, который содержит декоратор `@property`. Это позволяет нам использовать следующий
код в сессии интерпретатора:

```python
person = Person("Mike", "Driscoll")

print(person.full_name)  # Mike Driscoll
print(person.first_name)  # Mike

person.full_name = "Jackalope"  # Ошибка, нельзя поменять значение, полученное через property
```

Как вы видите, в результате превращения метода в свойство мы можем получить к нему доступ при помощи обычной точечной
нотации. Однако если мы попытаемся настроить свойство на что-то другое, мы получим ошибку `AttributeError`.
Единственный способ изменить свойство `full_name` — сделать это косвенно:

```python
person.first_name = "Dan"
print(person.full_name)  # Dan Driscoll
```

## Абстракция и модуль abc

Абстракция позволяет задать «контракт» для подклассов: какие методы/свойства они обязаны реализовать.
В Python это делается через абстрактные базовые классы (ABC) из модуля `abc`.

### Базовое использование: ABC и @abstractmethod

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...  # обязан быть реализован в подклассе

class Rectangle(Shape):
    def __init__(self, w: float, h: float):
        self.w, self.h = w, h
    def area(self) -> float:
        return self.w * self.h
```

- Нельзя инстанцировать `Shape()`: будет `TypeError` (есть нереализованные абстрактные методы).
- Можно инстанцировать `Rectangle()`, поскольку `area` реализован.

### Абстрактные свойства (@property + @abstractmethod)

```python
from abc import ABC, abstractmethod

class DataSource(ABC):
    @property
    @abstractmethod
    def url(self) -> str:  # только «интерфейс»
        ...

    @property
    def host(self) -> str:  # обычное свойство, использует url
        return self.url.split('/')[2]

class Api(DataSource):
    def __init__(self, url: str):
        self._url = url
    @property
    def url(self) -> str:  # реализация абстрактного свойства
        return self._url
```

**Замечания:**
- Порядок декораторов важен: сначала `@property`, затем `@abstractmethod`.
- В подклассе можно расширять поведение, сохраняя контракт базового класса.

### Абстрактные classmethod и staticmethod

```python
from abc import ABC, abstractmethod

class Serializer(ABC):
    @classmethod
    @abstractmethod
    def from_dict(cls, d: dict) -> 'Serializer':
        ...

    @staticmethod
    @abstractmethod
    def name() -> str:
        ...

class UserSerializer(Serializer):
    @classmethod
    def from_dict(cls, d: dict) -> 'UserSerializer':
        return cls()
    @staticmethod
    def name() -> str:
        return 'user'
```
> Примечание: для абстрактных методов класса/статических методов обычно пишут сначала @classmethod/@staticmethod, затем @abstractmethod — как в примере выше.


### Виртуальная регистрация подклассов (register)

Иногда нужно объявить класс «подклассом» ABC без фактического наследования:

```python
from abc import ABC

class JsonSerializable(ABC):
    pass

class DictLike:
    def to_json(self) -> str:
        return '{}'

JsonSerializable.register(DictLike)
assert isinstance(DictLike(), JsonSerializable)  # True
```

**Предупреждение:** `register` не проверяет наличие «контракта» на уровне рантайма — это лишь маркировка для `isinstance`/`issubclass`.
Для статической проверки интерфейсов в больших кодовых базах часто удобнее `typing.Protocol`.

### Практические советы

- ABC — хороший способ зафиксировать обязательные методы и свойства и явно сообщить о намерениях дизайна.
- Если класс остался абстрактным (есть нереализованные методы/свойства), инстанцировать его нельзя.
- ABC удобно комбинировать с миксинами; держите миксины мелкими и ортогональными.
- Абстрактные `@property`, `@classmethod`, `@staticmethod` помогают описывать интерфейсы на уровне API, а не только реализации.

---

## Практика на занятии

### Задание 1. Декоратор логирования

Напишите декоратор `@log_calls`, который логирует вызовы функции:

```python
from functools import wraps

def log_calls(func):
    """Логирует вызов функции с аргументами и результатом."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Ваш код
        pass
    return wrapper

@log_calls
def add(a, b):
    return a + b

@log_calls
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

add(2, 3)
# Calling add(2, 3)
# add returned: 5

greet("Alice", greeting="Hi")
# Calling greet('Alice', greeting='Hi')
# greet returned: Hi, Alice!
```

### Задание 2. Декоратор замера времени

Напишите декоратор `@timer`, который измеряет время выполнения функции:

```python
import time
from functools import wraps

def timer(func):
    """Измеряет и выводит время выполнения функции."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Ваш код
        pass
    return wrapper

@timer
def slow_function():
    time.sleep(0.5)
    return "Done"

slow_function()
# slow_function executed in 0.5012 seconds
```

---

## Домашняя работа

### Задание 1. Декоратор retry

Напишите декоратор `@retry`, который повторяет вызов функции при возникновении исключения:

```python
import time
from functools import wraps

def retry(max_attempts: int = 3, delay: float = 1.0, exceptions: tuple = (Exception,)):
    """
    Повторяет вызов функции при исключении.

    Args:
        max_attempts: максимальное количество попыток
        delay: задержка между попытками (секунды)
        exceptions: кортеж исключений, при которых повторять
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Ваш код
            pass
        return wrapper
    return decorator

# Пример использования:
@retry(max_attempts=3, delay=0.5, exceptions=(ConnectionError, TimeoutError))
def fetch_data(url):
    # Имитация нестабильного соединения
    import random
    if random.random() < 0.7:
        raise ConnectionError("Connection failed")
    return {"data": "success"}

result = fetch_data("http://example.com")
# Attempt 1 failed: Connection failed. Retrying in 0.5s...
# Attempt 2 failed: Connection failed. Retrying in 0.5s...
# Attempt 3 succeeded!
```

### Задание 2. Декоратор cache (memoization)

Напишите декоратор `@cache`, который кеширует результаты вызовов функции:

```python
from functools import wraps

def cache(func):
    """Кеширует результаты вызовов функции."""
    # Ваш код
    pass

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Без кеша: fibonacci(35) занимает несколько секунд
# С кешем: мгновенно
print(fibonacci(35))  # 9227465

# Бонус: добавьте атрибут для просмотра статистики кеша
print(fibonacci.cache_info())  # {'hits': 33, 'misses': 36, 'size': 36}
```

**Бонус:** Реализуйте `@cache` с ограничением размера (LRU — Least Recently Used):

```python
@cache(maxsize=100)
def expensive_function(x):
    return x ** 2
```

### Задание 3. Декоратор validate_types

Напишите декоратор `@validate_types`, который проверяет типы аргументов по аннотациям:

```python
from functools import wraps

def validate_types(func):
    """Проверяет типы аргументов по аннотациям функции."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Используйте func.__annotations__ для получения аннотаций
        # Ваш код
        pass
    return wrapper

@validate_types
def add(a: int, b: int) -> int:
    return a + b

@validate_types
def greet(name: str, times: int = 1) -> str:
    return (name + "! ") * times

print(add(2, 3))        # 5
print(greet("Hello", 3)) # Hello! Hello! Hello!

add("2", "3")  # TypeError: Argument 'a' must be int, got str
greet(123, 1)  # TypeError: Argument 'name' must be str, got int
```

### Задание 4. Класс Temperature с @property

Создайте класс `Temperature` с использованием `@property` для автоматической конвертации:

```python
class Temperature:
    def __init__(self, celsius: float = 0):
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        """Температура в Цельсиях."""
        pass

    @celsius.setter
    def celsius(self, value: float):
        pass

    @property
    def fahrenheit(self) -> float:
        """Температура в Фаренгейтах."""
        pass

    @fahrenheit.setter
    def fahrenheit(self, value: float):
        pass

    @property
    def kelvin(self) -> float:
        """Температура в Кельвинах."""
        pass

    @kelvin.setter
    def kelvin(self, value: float):
        # Нельзя установить температуру ниже абсолютного нуля
        pass

# Пример использования:
temp = Temperature(25)
print(temp.celsius)     # 25
print(temp.fahrenheit)  # 77.0
print(temp.kelvin)      # 298.15

temp.fahrenheit = 32
print(temp.celsius)     # 0.0

temp.kelvin = 0
print(temp.celsius)     # -273.15

temp.kelvin = -10  # ValueError: Temperature cannot be below absolute zero
```

### Задание 5. Декоратор для методов класса

Напишите декоратор `@count_calls`, который считает количество вызовов метода:

```python
def count_calls(method):
    """Считает количество вызовов метода."""
    pass

class API:
    @count_calls
    def get_users(self):
        return ["Alice", "Bob"]

    @count_calls
    def get_posts(self):
        return ["Post 1", "Post 2"]

api = API()
api.get_users()
api.get_users()
api.get_posts()

print(api.get_users.call_count)  # 2
print(api.get_posts.call_count)  # 1
```

### Задание 6. ⭐ Декоратор rate_limit

Напишите декоратор `@rate_limit`, который ограничивает частоту вызовов функции:

```python
import time
from functools import wraps

def rate_limit(calls: int = 5, period: float = 60.0):
    """
    Ограничивает количество вызовов функции.

    Args:
        calls: максимальное количество вызовов
        period: период времени в секундах

    Raises:
        RateLimitExceeded: если лимит превышен
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Ваш код
            pass
        return wrapper
    return decorator

class RateLimitExceeded(Exception):
    pass

@rate_limit(calls=3, period=10.0)
def send_message(msg):
    print(f"Sending: {msg}")

# Пример использования:
send_message("Hello")      # OK
send_message("World")      # OK
send_message("!")          # OK
send_message("Too many!")  # RateLimitExceeded: Rate limit exceeded. Try again in 8.5 seconds.

# Через 10 секунд лимит сбрасывается
time.sleep(10)
send_message("I'm back!")  # OK
```

**Бонус:** Сделайте декоратор, который можно использовать с опциональными аргументами:

```python
@rate_limit  # Использует значения по умолчанию
def func1(): pass

@rate_limit(calls=10, period=30)  # С аргументами
def func2(): pass
```

### Задание 7. ⭐ Класс-декоратор Singleton

Создайте декоратор класса `@singleton`, который гарантирует единственный экземпляр:

```python
def singleton(cls):
    """Декоратор, превращающий класс в Singleton."""
    pass

@singleton
class Database:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        print(f"Connecting to {connection_string}")

# Пример использования:
db1 = Database("postgresql://localhost/db1")
# Connecting to postgresql://localhost/db1

db2 = Database("postgresql://localhost/db2")
# Ничего не выводится — возвращается существующий экземпляр

print(db1 is db2)  # True
print(db1.connection_string)  # postgresql://localhost/db1
```

---

[← Лекция 11: Imports. Standard library. PEP8](lesson11.md) | [Лекция 13: Тестирование →](lesson13.md)