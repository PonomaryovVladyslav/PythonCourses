# Лекция 32. Асинхронное программирование в Python. Корутины. Asyncio.

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

<details>
  <summary>Блок 3 — Python Advanced (9–14)</summary>

  - [Лекция 9. Введение в ООП. Основные парадигмы ООП. Классы и объекты.](lesson09.md)
  - [Лекция 10. Множественное наследование. MRO. Magic methods.](lesson10.md)
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
  - [Лекция 21. Модели. Связи. Meta. Abstract, proxy](lesson21.md)
  - [Лекция 22. Django ORM](lesson22.md)
  - [Лекция 23. Forms, ModelForms. User, Authentication](lesson23.md)
  - [Лекция 24. ClassBaseView](lesson24.md)
  - [Лекция 25. NoSQL. Куки, сессии, кеш](lesson25.md)
  - [Лекция 26. Логирование. Middleware. Signals. Messages. Manage commands](lesson26.md)
</details>

<details>
  <summary>Блок 6 — Django Rest Framework (27–30)</summary>

  - [Лекция 27. Что такое API. REST и RESTful. Django REST Framework](lesson27.md)
  - [Лекция 28. @api_view, APIView, ViewSets, Pagination, Routers](lesson28.md)
  - [Лекция 29. REST аутентификация. Авторизация. Permissions. Фильтрация](lesson29.md)
  - [Лекция 30. Тестирование. Django, REST API.](lesson30.md)
</details>

<details open>
  <summary>Блок 7 — Python async (31–33)</summary>

  - [Лекция 31. Celery. Multithreading. GIL. Multiprocessing](lesson31.md)
  - ▶ **Лекция 32. Асинхронное программирование в Python. Корутины. Asyncio**
  - [Лекция 33. Сокеты. Django channels.](lesson33.md)
</details>

<details>
  <summary>Блок 8 — Deployment (34–35)</summary>

  - [Лекция 34. Linux. Все что нужно знать для деплоймента.](lesson34.md)
  - [Лекция 35. Deployment](lesson35.md)
</details>

- [Лекция 36. Методологии разработки. CI/CD. Монолит и микросервисы. Docker](lesson36.md)

> **Напоминание:** Итераторы и генераторы мы изучали в [Лекции 10](lesson10.md). Здесь мы рассмотрим, как генераторы
> могут не только возвращать значения, но и принимать их — это основа для понимания async/await.

## Корутины

![](https://habrastorage.org/webt/zy/vb/px/zyvbpxrx43dnun4q8wcegtqwnn0.png)

А теперь о том, ради чего это, собственно, затевалось. Оказывается, генератор может не только возвращать значения, но и
принимать их на вход.

О стандарте можно почитать тут [PEP 342](https://www.python.org/dev/peps/pep-0342/).

Предлагаю сразу начать с примера. Напишем простую реализацию генератора, который может складывать два аргумента, хранить
историю результатов и выводить историю.

```python
def calc():
    history = []
    while True:
        x = yield
        if x == 'h':
            print(history)
            continue
        print(x)
        history.append(x)


c = calc()

next(c)  # Необходимая инициация. Можно написать c.send(None)
c.send(1)  # Выведет 1
c.send(100)  # Выведет 100
c.send(666)  # Выведет 666
c.send('h')  # Выведет [1, 100, 666]
c.close()  # Закрываем генератор, данные сотрутся, генератор необходимо будет создавать заново.
```

Пример с передачей более чем одного параметра

```python
def calc():
    history = []
    while True:
        x, y = (yield)
        if x == 'h':
            print(history)
            continue
        result = x + y
        print(result)
        history.append(result)


c = calc()

next(c)  # Необходимая инициация. Можно написать c.send(None)
c.send((1, 2))  # Выведет 3
c.send((100, 30))  # Выведет 130
c.send((666, 0))  # Выведет 666
c.send(('h', 0))  # Выведет [3, 130, 666]
c.close()  # Закрываем генератор, данные сотрутся, генератор необходимо будет создавать заново.
```

### send, throw, close

В Python 2.5 добавили в генераторы возможность отправлять данные и `exception`.

- `send` - передача данных в корутину. `send(None)` - равносильно `next`.

- `throw` - передача исключения в корутину. Например, `GeneratorExit` для выхода из корутины.

- `close` - для "закрытия" корутины и очистки локальной памяти корутины.

### Корутина как декоратор

Т.е. мы создали генератор, проинициализировали его и подаём ему входные данные. В свою очередь он эти данные
обрабатывает и сохраняет своё состояние между вызовами до тех пор, пока мы его не закрыли. После каждого вызова
генератор возвращает управление туда, откуда его вызвали. Это важнейшее свойство генераторов мы и будем использовать.

Теперь, когда мы разобрались с общим принципом работы, давайте теперь избавим себя от необходимости каждый раз руками
инициализировать генератор. Решим это типичным для Python образом, с помощью декоратора.

```python
def coroutine(f):
    def wrap(*args, **kwargs):
        gen = f(*args, **kwargs)
        gen.send(None)
        return gen

    return wrap


@coroutine
def calc():
    history = []
    while True:
        x, y = (yield)
        if x == 'h':
            print(history)
            continue
        result = x + y
        print(result)
        history.append(result)
```

## Asyncio

![](http://risovach.ru/upload/2020/10/mem/internet_253267592_orig_.jpg)
Документация: https://docs.python.org/3/library/asyncio.html


Начиная с Python 3.4, существует новый модуль `asyncio`, который вводит `API` для обобщенного асинхронного
программирования. Мы можем использовать корутины с этим модулем для простого и понятного выполнения асинхронного кода.

<details>
<summary>📜 Исторический пример (только для понимания эволюции asyncio, НЕ используйте в новом коде)</summary>

До Python 3.5 корутины создавались с помощью декоратора `@asyncio.coroutine` и ключевого слова `yield from`:

```python
import asyncio
import datetime
import random


@asyncio.coroutine
def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print(f"Loop: {num} Time: {datetime.datetime.now()}")
        if (loop.time() + 1.0) >= end_time:
            break
        yield from asyncio.sleep(random.randint(0, 5))


loop = asyncio.get_event_loop()

asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))

loop.run_forever()
```

Этот код показывает, как две корутины выполняются конкурентно: когда одна "спит" (`yield from asyncio.sleep`),
event loop переключается на другую.

**⚠️ Этот синтаксис устарел!** Декоратор `@asyncio.coroutine` был deprecated в Python 3.8 и **полностью удалён в Python 3.11**.

</details>

Современный способ (Python 3.7+) — использовать `async/await`:

Документация: PEP 492 — https://peps.python.org/pep-0492/

### Встроенные корутины

![](https://raw.githubusercontent.com/kblok/kblok.github.io/master/img/deeper-async/bob-loves-async.jpg)

Помните, мы все еще используем функции на основе генератора? В Python 3.5 мы получили новые встроенные корутины, которые
используют синтаксис `async / await`. Современный вариант (Python 3.7+):

```python
import asyncio
import datetime
import random


async def display_date(num, duration=10):
    start_time = asyncio.get_event_loop().time()
    end_time = start_time + duration
    while True:
        print(f"Loop: {num} Time: {datetime.datetime.now()}")
        if asyncio.get_event_loop().time() >= end_time:
            break
        await asyncio.sleep(random.randint(0, 5))


async def main():
    await asyncio.gather(
        display_date(1, 10),
        display_date(2, 10),
    )


asyncio.run(main())
```

Для определения встроенной корутины определение функции помечается ключевым словом `async`, а вместо `yield from` используется `await`.

> **Примечание:** В Python 3.10+ использование `asyncio.get_event_loop()` вне работающего event loop вызывает `DeprecationWarning`. Рекомендуется использовать `asyncio.run()` для запуска корутин.

### Корутины на генераторах и встроенные корутины

Функционально нет никакой разницы между корутинами на генераторах и встроенными корутинами кроме различия в синтаксисе.
Кроме того, не допускается смешивания их синтаксисов. То есть нельзя использовать `await` внутри корутин на генераторах
или `yield` / `yield from` внутри встроенных корутин.

<details>
<summary>📜 Исторический пример: смешивание генераторных и async корутин (Python 3.6-3.10)</summary>

В переходный период можно было использовать декоратор `@types.coroutine` для совместимости старых генераторов с новым синтаксисом `async/await`:

```python
import asyncio
import datetime
import random
import types


@types.coroutine
def my_sleep_func():
    yield from asyncio.sleep(random.randint(0, 5))


async def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print(f"Loop: {num} Time: {datetime.datetime.now()}")
        if (loop.time() + 1.0) >= end_time:
            break
        await my_sleep_func()


loop = asyncio.get_event_loop()

asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))

loop.run_forever()
```

**⚠️ Этот подход устарел!** В современном Python используйте только `async/await`. Декоратор `@types.coroutine` и `yield from` в asyncio контексте не рекомендуются.

</details>

## Asyncio. Loop, run, create_task, gather, etc.

### loop

`loop` - один набор событий, до версии Python 3.7 любые корутины запускались исключительно внутри `loop`

Давайте рассмотрим пример, где отдельная корутина вычисляет факториал последовательно (сначала 2, потом 3, потом 4 и т.
д.) и делает паузу на одну секунду перед следующим вычислением:

```python
import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")


loop = asyncio.get_event_loop()
loop.run_until_complete(factorial('A', 4))
```

Обратите внимание, этот код будет работать на Python 3.6+

### run

То же самое для Python 3.7+ будет выглядеть так:

```python
import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")


asyncio.run(factorial('A', 4))  # Добавлено в 3.7

# Output:
# Task A: Compute factorial(2)...
# Task A: Compute factorial(3)...
# Task A: Compute factorial(4)...
# Task A: factorial(4) = 24
```

### create_tasks

Рассмотрим код, в котором основная корутина запускает две других.

```python
import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"Started at {time.strftime('%X')}")

    await say_after(1, 'hello,')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())

# Output:
# Started at 16:28:52
# hello,
# world
# finished at 16:28:55
```

Обязаны ли мы задавать параметры там же, где и запускаем корутину? Нет, мы можем сделать это через `create_task`

```python
async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello,'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Подождите, пока обе задачи не будут выполнены (должно пройти около 2 секунд.)
    await task1
    await task2
```

Попытка запустить асинхронный метод синхронно не приведёт ни к чему, это просто не будет работать.

```python
import asyncio


async def nested():
    return 42


async def main():
    # Ничего не произойдет, если мы просто вызовем "nested()".
    # Объект корутины создан, но не await,
    # так что *не будет работать вообще*.
    nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".


asyncio.run(main())
```

### gather

Что если нам необходимо запустить асинхронно несколько одинаковых задач с разными параметрами? Нам поможет `gather`.

Вернёмся к коду с факториалами:

```python
import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")


async def main():
    # Запланировать дерево вызовов *конкурентно*:
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )


asyncio.run(main())

# Ожидаемый вывод:
#
#     Task A: Compute factorial(2)...
#     Task B: Compute factorial(2)...
#     Task C: Compute factorial(2)...
#     Task A: factorial(2) = 2
#     Task B: Compute factorial(3)...
#     Task C: Compute factorial(3)...
#     Task B: factorial(3) = 6
#     Task C: Compute factorial(4)...
#     Task C: factorial(4) = 24
```

Обратите внимание, если вам необходимо вернуть значения, вы свободно можете использовать `return`, где это необходимо.

```python
import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():
    # Запланировать дерево вызовов *конкурентно*:
    res = await asyncio.gather(
        factorial("A", 4),
        factorial("B", 3),
        factorial("C", 2),
    )
    print(res)


asyncio.run(main())

# Output:
# Task A: Compute factorial(2)...
# Task B: Compute factorial(2)...
# Task C: Compute factorial(2)...
# Task C: factorial(2) = 2
# Task A: Compute factorial(3)...
# Task B: Compute factorial(3)...
# Task B: factorial(3) = 6
# Task A: Compute factorial(4)...
# Task A: factorial(4) = 24
# [24, 6, 2]
```

Вы можете быть уверены в том, что в переменную `res` результаты придут именно в том порядке, в котором вы их запросили,
в примере результат всегда будет [24, 6, 2], никакой неожиданности.

### Ограничение параллелизма (concurrency limits)

Иногда важно ограничить одновременное число выполняющихся задач (например, чтобы не перегружать API/БД).

— Семафор
```python
import asyncio

sem = asyncio.Semaphore(10)

async def fetch(url):
    async with sem:          # одновременно не более 10
        return await do_io(url)

await asyncio.gather(*(fetch(u) for u in urls))
```

— BoundedSemaphore
```python
sem = asyncio.BoundedSemaphore(10)  # выбросит ошибку, если кто-то "вернёт" семафор лишний раз
```

— Пакетная обработка (батчи)
```python
BATCH = 20
for i in range(0, len(urls), BATCH):
    chunk = urls[i:i+BATCH]
    await asyncio.gather(*(fetch(u) for u in chunk))
```

— Worker pool через очередь
```python
import asyncio

async def worker(name, q):
    while True:
        url = await q.get()
        try:
            await fetch(url)
        finally:
            q.task_done()

q = asyncio.Queue()
for u in urls:
    q.put_nowait(u)

workers = [asyncio.create_task(worker(i, q)) for i in range(5)]
await q.join()
for w in workers:
    w.cancel()
```

### Таймауты, ошибки и отмена

— Таймауты (оборачиваем awaited-операцию)
```python
await asyncio.wait_for(fetch(url), timeout=5)
```

— Ошибки в gather
```python
results = await asyncio.gather(*tasks, return_exceptions=True)
```

— Отмена задач
```python
task = asyncio.create_task(fetch(url))
...
task.cancel()
try:
    await task
except asyncio.CancelledError:
    pass
```

### TaskGroup (Python 3.11+)

`TaskGroup` — структурированный способ управления группой задач. Если одна задача падает, остальные автоматически отменяются:

```python
import asyncio


async def fetch(url):
    await asyncio.sleep(1)
    return f"Result from {url}"


async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch("/a"))
        task2 = tg.create_task(fetch("/b"))

    # После выхода из контекста все задачи гарантированно завершены
    print(task1.result(), task2.result())


asyncio.run(main())
```

### asyncio.timeout() (Python 3.11+)

Новый контекстный менеджер для таймаутов, более удобный чем `wait_for`:

```python
import asyncio


async def long_operation():
    await asyncio.sleep(10)
    return "done"


async def main():
    try:
        async with asyncio.timeout(5):
            result = await long_operation()
    except TimeoutError:
        print("Операция превысила таймаут!")


asyncio.run(main())
```

Также есть `asyncio.timeout_at(when)` для указания абсолютного времени.

### asyncio.to_thread() (Python 3.9+)

Позволяет запускать синхронный (блокирующий) код в отдельном потоке, не блокируя event loop:

```python
import asyncio
import time


def blocking_io():
    """Синхронная функция, которая блокирует поток"""
    time.sleep(2)
    return "Результат блокирующей операции"


async def main():
    print("Запускаем блокирующую операцию в отдельном потоке...")

    # Запускаем синхронную функцию в отдельном потоке
    result = await asyncio.to_thread(blocking_io)

    print(f"Получили: {result}")


asyncio.run(main())
```

Это особенно полезно для:
- Работы с библиотеками, не поддерживающими async (например, `requests`, `PIL`)
- CPU-bound операций (хотя для них лучше использовать `ProcessPoolExecutor`)
- Файловых операций

### Асинхронные итераторы и контекстные менеджеры

#### async with

`async with` используется для асинхронных контекстных менеджеров — объектов с методами `__aenter__` и `__aexit__`:

```python
import asyncio


class AsyncResource:
    async def __aenter__(self):
        print("Открываем ресурс...")
        await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Закрываем ресурс...")
        await asyncio.sleep(0.5)

    async def do_something(self):
        return "Работа с ресурсом"


async def main():
    async with AsyncResource() as resource:
        result = await resource.do_something()
        print(result)


asyncio.run(main())
```

#### async for

`async for` используется для асинхронных итераторов — объектов с методами `__aiter__` и `__anext__`:

```python
import asyncio


class AsyncCounter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current >= self.stop:
            raise StopAsyncIteration
        await asyncio.sleep(0.5)  # Имитация асинхронной операции
        self.current += 1
        return self.current


async def main():
    async for number in AsyncCounter(5):
        print(number)


asyncio.run(main())

# Output:
# 1
# 2
# 3
# 4
# 5
```

#### Асинхронные генераторы

Можно создавать асинхронные генераторы с помощью `async def` и `yield`:

```python
import asyncio


async def async_range(start, stop):
    for i in range(start, stop):
        await asyncio.sleep(0.1)
        yield i


async def main():
    async for num in async_range(1, 6):
        print(num)


asyncio.run(main())
```

Это далеко не все методы и подробности корутин, за всеми деталями
в [документацию](https://docs.python.org/3/library/asyncio.html)

## Aiohttp.
Документация: https://docs.aiohttp.org/


Как мы помним, одно из основных преимуществ использования асинхронности - это возможность отправки параллельных HTTP
запросов, не дожидаясь результатов других. К сожалению, при использовании корутин вместе с классическим `requests`
запросы будут выполнены синхронно, т. к. сами запросы не являются `awaitable` объектами, и результат будет таким же, как
если бы вы использовали обычный `sleep`, а не асинхронными, соседние корутины будут ждать остальные. Чтобы такого не
было, существует специальный пакет `aiohttp`, его необходимо устанавливать через `pip`:

```pip install aiohttp```

После чего необходимо создать асинхронный клиент, и можно выполнять запросы.

```python
import aiohttp
import asyncio


async def main():
    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get("https://httpbin.org/get") as resp:
            print(resp.status)
            data = await resp.json()
            print(data.get("url"))


asyncio.run(main())

# Output:
# 200
# https://httpbin.org/get
```

#### Ограничение параллельных HTTP-запросов (aiohttp + Semaphore)

```python
import aiohttp
import asyncio

sem = asyncio.Semaphore(10)

async def fetch(session, url):
    async with sem:
        async with session.get(url, timeout=10) as r:
            return await r.text()

async def main():
    urls = ["https://httpbin.org/get"] * 50
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*(fetch(session, u) for u in urls))
        print(len(results))


asyncio.run(main())
```

**Замечания:**
- Переиспользуйте один `ClientSession` для всех запросов
- Всегда задавайте таймауты
- Избегайте блокирующих вызовов внутри async-функций

### Альтернатива: httpx

Документация: https://www.python-httpx.org/

`httpx` — современная альтернатива `aiohttp` и `requests`, которая поддерживает как синхронный, так и асинхронный API:

```bash
pip install httpx
```

```python
import httpx
import asyncio


async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org/get")
        print(response.status_code)
        print(response.json())


asyncio.run(main())
```

Преимущества `httpx`:
- Единый API для sync и async
- Поддержка HTTP/2
- Совместимость с API `requests`
- Встроенная поддержка таймаутов


