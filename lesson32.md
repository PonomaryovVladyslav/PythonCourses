# Лекция 32. Asyncio. Aiohttp. Асинхронное программирование на практике.

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

  - [Лекция 9. Введение в ООП. Основные парадигмы ООП. Классы и объекты. Множественное наследование.](lesson09.md)
  - [Лекция 10. Magic methods. Итераторы и генераторы.](lesson10.md)
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
  - ▶ **Лекция 32. Asyncio. Aiohttp. Асинхронное программирование на практике.**
  - [Лекция 33. Сокеты. Django channels.](lesson33.md)
</details>

<details>
  <summary>Блок 8 — Deployment (34–35)</summary>

  - [Лекция 34. Linux. Все что нужно знать для деплоймента.](lesson34.md)
  - [Лекция 35. Deployment](lesson35.md)
</details>

- [Лекция 36. Методологии разработки. CI/CD. Монолит и микросервисы. Docker](lesson36.md)

> **Напоминание:** Базовые концепции `async`/`await` мы рассмотрели в [Лекции 10](lesson10.md).
> Здесь мы углубимся в практическое использование библиотеки `asyncio`.

## Asyncio

![](http://risovach.ru/upload/2020/10/mem/internet_253267592_orig_.jpg)

**Документация:** https://docs.python.org/3/library/asyncio.html

`asyncio` — это стандартная библиотека Python для написания асинхронного кода с использованием синтаксиса `async`/`await`.

Ключевые концепции:
- **Корутина (coroutine)** — функция, объявленная через `async def`
- **Event loop** — цикл событий, который управляет выполнением корутин
- **Task** — обёртка над корутиной для параллельного выполнения
- **await** — приостанавливает корутину до завершения асинхронной операции

```python
import asyncio


async def say_hello(name, delay):
    await asyncio.sleep(delay)
    print(f"Привет, {name}!")


async def main():
    # Запускаем две корутины параллельно
    await asyncio.gather(
        say_hello("Мир", 2),
        say_hello("Python", 1),
    )


asyncio.run(main())

# Вывод (через 1 сек):
# Привет, Python!
# (через 2 сек):
# Привет, Мир!
```

## Asyncio. Loop, run, create_task, gather, etc.

### loop

`loop` — один набор событий, до версии Python 3.7 любые корутины запускались исключительно внутри `loop`

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

**Семафор**
```python
import asyncio

sem = asyncio.Semaphore(10)

async def fetch(url):
    async with sem:          # одновременно не более 10
        return await do_io(url)

await asyncio.gather(*(fetch(u) for u in urls))
```

**BoundedSemaphore**
```python
sem = asyncio.BoundedSemaphore(10)  # выбросит ошибку, если кто-то «вернёт» семафор лишний раз
```

**Пакетная обработка (батчи)**
```python
BATCH = 20
for i in range(0, len(urls), BATCH):
    chunk = urls[i:i+BATCH]
    await asyncio.gather(*(fetch(u) for u in chunk))
```

**Worker pool через очередь**
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

**Таймауты** (оборачиваем awaited-операцию)
```python
await asyncio.wait_for(fetch(url), timeout=5)
```

**Ошибки в gather**
```python
results = await asyncio.gather(*tasks, return_exceptions=True)
```

**Отмена задач**
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

`TaskGroup` — структурированный способ управления группой задач. Если одна задача падает с ошибкой, остальные автоматически отменяются:

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

Новый контекстный менеджер для таймаутов, более удобный, чем `wait_for`:

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


Как мы помним, одно из основных преимуществ использования асинхронности — это возможность отправки параллельных HTTP-запросов, не дожидаясь результатов других. К сожалению, при использовании корутин вместе с классическим `requests`
запросы будут выполнены синхронно, т. к. сами запросы не являются `awaitable`-объектами, и результат будет таким же, как
если бы вы использовали обычный `sleep`, а не асинхронный — соседние корутины будут ждать остальные. Чтобы такого не
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

### POST-запросы и отправка JSON

```python
import aiohttp
import asyncio


async def create_user(session, user_data):
    async with session.post(
        "https://httpbin.org/post",
        json=user_data,
        headers={"Content-Type": "application/json"}
    ) as resp:
        return await resp.json()


async def main():
    async with aiohttp.ClientSession() as session:
        result = await create_user(session, {"name": "John", "age": 30})
        print(result)


asyncio.run(main())
```

### Обработка ошибок и retry-логика

При работе с сетью ошибки неизбежны. Вот паттерн для обработки ошибок с повторными попытками:

```python
import aiohttp
import asyncio
from aiohttp import ClientError, ClientResponseError


async def fetch_with_retry(session, url, max_retries=3, delay=1):
    """Запрос с повторными попытками при ошибках."""
    for attempt in range(max_retries):
        try:
            async with session.get(url) as resp:
                resp.raise_for_status()  # Вызовет исключение для 4xx/5xx
                return await resp.json()
        except ClientResponseError as e:
            if e.status >= 500 and attempt < max_retries - 1:
                # Серверная ошибка — пробуем ещё раз
                await asyncio.sleep(delay * (attempt + 1))
                continue
            raise
        except ClientError as e:
            if attempt < max_retries - 1:
                await asyncio.sleep(delay * (attempt + 1))
                continue
            raise

    raise Exception(f"Не удалось получить {url} после {max_retries} попыток")


async def main():
    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        try:
            data = await fetch_with_retry(session, "https://httpbin.org/get")
            print(data)
        except Exception as e:
            print(f"Ошибка: {e}")


asyncio.run(main())
```

## Сравнение sync vs async: бенчмарк

Давайте на практике сравним синхронный и асинхронный подходы. Выполним 20 HTTP-запросов:

### Синхронный вариант (requests)

```python
import requests
import time


def fetch_sync(url):
    response = requests.get(url, timeout=10)
    return response.status_code


def main_sync():
    urls = ["https://httpbin.org/delay/1"] * 20  # Каждый запрос занимает ~1 сек

    start = time.time()
    results = [fetch_sync(url) for url in urls]
    elapsed = time.time() - start

    print(f"Синхронно: {len(results)} запросов за {elapsed:.2f} сек")


main_sync()
# Синхронно: 20 запросов за ~20 сек
```

### Асинхронный вариант (aiohttp)

```python
import aiohttp
import asyncio
import time


async def fetch_async(session, url):
    async with session.get(url) as resp:
        return resp.status


async def main_async():
    urls = ["https://httpbin.org/delay/1"] * 20

    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_async(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    elapsed = time.time() - start

    print(f"Асинхронно: {len(results)} запросов за {elapsed:.2f} сек")


asyncio.run(main_async())
# Асинхронно: 20 запросов за ~1-2 сек
```

### Результаты

| Подход      | 20 запросов (delay=1s) | Ускорение  |
|-------------|------------------------|------------|
| Синхронный  | ~20 сек                | 1x         |
| Асинхронный | ~1-2 сек               | **10-20x** |

### Когда async даёт выигрыш?

✅ **Async эффективен для I/O-bound задач:**
- HTTP-запросы к внешним API
- Запросы к базам данных
- Чтение/запись файлов
- WebSocket-соединения

❌ **Async НЕ поможет для CPU-bound задач:**
- Математические вычисления
- Обработка изображений
- Шифрование
- Парсинг больших данных

Для CPU-bound задач используйте `multiprocessing` или `asyncio.to_thread()`.

## Async в Django

Начиная с Django 3.1, появилась поддержка асинхронных view. В Django 4.1+ эта поддержка стала более зрелой.

### Async Views

```python
# views.py
import asyncio
import aiohttp
from django.http import JsonResponse


async def fetch_external_api(request):
    """Асинхронный view для запроса к внешнему API."""
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.example.com/data") as resp:
            data = await resp.json()
    return JsonResponse(data)


# Можно использовать asyncio.gather для параллельных запросов
async def fetch_multiple_apis(request):
    """Параллельные запросы к нескольким API."""
    async with aiohttp.ClientSession() as session:
        tasks = [
            session.get("https://api.example.com/users"),
            session.get("https://api.example.com/products"),
            session.get("https://api.example.com/orders"),
        ]
        responses = await asyncio.gather(*tasks)
        data = {
            "users": await responses[0].json(),
            "products": await responses[1].json(),
            "orders": await responses[2].json(),
        }
    return JsonResponse(data)
```

### Ограничения: Django ORM

**⚠️ Важно:** Django ORM пока **синхронный**! Нельзя напрямую использовать ORM в async view:

```python
# ❌ НЕПРАВИЛЬНО — заблокирует event loop!
async def bad_view(request):
    users = User.objects.all()  # Синхронный вызов в async контексте
    return JsonResponse({"count": len(users)})
```

### sync_to_async

Для использования синхронного кода (включая ORM) в async-контексте используйте `sync_to_async`:

```python
from asgiref.sync import sync_to_async
from django.http import JsonResponse
from .models import User


@sync_to_async
def get_users_count():
    return User.objects.count()


@sync_to_async
def get_user_by_id(user_id):
    return User.objects.get(id=user_id)


async def users_count_view(request):
    count = await get_users_count()
    return JsonResponse({"count": count})


# Или inline с декоратором
async def user_detail_view(request, user_id):
    get_user = sync_to_async(User.objects.get, thread_sensitive=True)
    try:
        user = await get_user(id=user_id)
        return JsonResponse({"name": user.name, "email": user.email})
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)
```

### async_to_sync

Обратная ситуация — вызов async-кода из синхронного контекста:

```python
from asgiref.sync import async_to_sync
import aiohttp


async def fetch_data_async(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


# В синхронном коде (например, в management command)
def sync_function():
    data = async_to_sync(fetch_data_async)("https://api.example.com/data")
    print(data)
```

### Когда использовать async views в Django?

✅ **Используйте async views когда:**
- Делаете запросы к внешним API
- Работаете с WebSocket (Django Channels)
- Выполняете много I/O операций параллельно

❌ **Не используйте async views когда:**
- Основная работа — с Django ORM (пока он синхронный)
- Простые CRUD-операции
- Нет явной выгоды от параллелизма

> **Примечание:** Django 5.0+ активно развивает async ORM. Следите за обновлениями!

## Паттерны и best practices

### Producer-Consumer

Классический паттерн для обработки потока данных:

```python
import asyncio
import random


async def producer(queue, name):
    """Производитель — добавляет задачи в очередь."""
    for i in range(5):
        await asyncio.sleep(random.uniform(0.1, 0.5))
        item = f"{name}-item-{i}"
        await queue.put(item)
        print(f"[{name}] Произведено: {item}")
    await queue.put(None)  # Сигнал завершения


async def consumer(queue, name):
    """Потребитель — обрабатывает задачи из очереди."""
    while True:
        item = await queue.get()
        if item is None:
            queue.task_done()
            break
        await asyncio.sleep(random.uniform(0.2, 0.6))  # Имитация обработки
        print(f"[{name}] Обработано: {item}")
        queue.task_done()


async def main():
    queue = asyncio.Queue(maxsize=10)

    # Запускаем производителей и потребителей
    producers = [
        asyncio.create_task(producer(queue, f"P{i}"))
        for i in range(2)
    ]
    consumers = [
        asyncio.create_task(consumer(queue, f"C{i}"))
        for i in range(3)
    ]

    await asyncio.gather(*producers)

    # Отправляем сигналы завершения для всех потребителей
    for _ in consumers:
        await queue.put(None)

    await asyncio.gather(*consumers)


asyncio.run(main())
```

### Graceful Shutdown

Корректное завершение при получении сигнала (Ctrl+C):

```python
import asyncio
import signal


async def long_running_task(name):
    try:
        while True:
            print(f"[{name}] Работаю...")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print(f"[{name}] Получен сигнал отмены, завершаюсь...")
        # Здесь можно выполнить cleanup
        raise


async def main():
    tasks = [
        asyncio.create_task(long_running_task(f"Task-{i}"))
        for i in range(3)
    ]

    # Обработчик сигнала
    def shutdown():
        print("Получен сигнал завершения!")
        for task in tasks:
            task.cancel()

    loop = asyncio.get_running_loop()
    for sig in (signal.SIGTERM, signal.SIGINT):
        loop.add_signal_handler(sig, shutdown)

    try:
        await asyncio.gather(*tasks)
    except asyncio.CancelledError:
        print("Все задачи отменены")


# На Windows сигналы работают иначе, используйте try/except KeyboardInterrupt
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Завершено по Ctrl+C")
```

### Типичные ошибки

#### 1. Забытый await

```python
# ❌ НЕПРАВИЛЬНО
async def bad():
    asyncio.sleep(1)  # Забыли await — ничего не произойдёт!
    print("Готово")

# ✅ ПРАВИЛЬНО
async def good():
    await asyncio.sleep(1)
    print("Готово")
```

#### 2. Блокирующий код в async-функции

```python
import time

# ❌ НЕПРАВИЛЬНО — блокирует весь event loop!
async def bad():
    time.sleep(5)  # Синхронный sleep
    return "done"

# ✅ ПРАВИЛЬНО
async def good():
    await asyncio.sleep(5)  # Асинхронный sleep
    return "done"

# ✅ Или используйте to_thread для блокирующего кода
async def also_good():
    await asyncio.to_thread(time.sleep, 5)
    return "done"
```

#### 3. Создание задач без ожидания

```python
# ❌ НЕПРАВИЛЬНО — задача может не выполниться
async def bad():
    asyncio.create_task(some_coroutine())  # Задача "потеряется"
    return "done"

# ✅ ПРАВИЛЬНО — сохраняем ссылку и ждём
async def good():
    task = asyncio.create_task(some_coroutine())
    # ... другой код ...
    await task  # Ждём завершения
    return "done"
```

#### 4. Неправильная обработка исключений в gather

```python
# ❌ Одно исключение отменит все задачи
async def bad():
    await asyncio.gather(task1(), task2(), task3())

# ✅ return_exceptions=True — все задачи выполнятся
async def good():
    results = await asyncio.gather(
        task1(), task2(), task3(),
        return_exceptions=True
    )
    for result in results:
        if isinstance(result, Exception):
            print(f"Ошибка: {result}")
```

### Отладка async-кода

Включите debug-режим asyncio для поиска проблем:

```python
import asyncio

# Способ 1: через переменную окружения
# PYTHONASYNCIODEBUG=1 python script.py

# Способ 2: программно
asyncio.run(main(), debug=True)
```

В debug-режиме asyncio:
- Предупреждает о корутинах, которые не были awaited
- Показывает, где были созданы задачи
- Логирует медленные callback'и (>100ms)

---

## Практика на занятии

### Задание 1. Параллельные запросы

Напишите асинхронную функцию, которая:
1. Принимает список URL-адресов
2. Делает GET-запросы ко всем URL параллельно
3. Возвращает словарь `{url: status_code}`
4. Обрабатывает ошибки (таймаут, недоступный сервер)

```python
import aiohttp
import asyncio


async def fetch_all(urls: list[str], timeout: int = 10) -> dict[str, int | str]:
    """
    Возвращает словарь {url: status_code} или {url: "error: описание"}
    """
    # Ваш код здесь
    pass


# Пример использования:
urls = [
    "https://httpbin.org/get",
    "https://httpbin.org/status/404",
    "https://httpbin.org/delay/2",
    "https://invalid-url-that-does-not-exist.com",
]

results = asyncio.run(fetch_all(urls))
print(results)
# {'https://httpbin.org/get': 200, 'https://httpbin.org/status/404': 404, ...}
```

### Задание 2. Rate Limiter

Реализуйте асинхронный rate limiter, который ограничивает количество запросов в секунду:

```python
import asyncio
import time


class AsyncRateLimiter:
    def __init__(self, max_requests: int, period: float = 1.0):
        """
        max_requests: максимальное количество запросов
        period: период в секундах
        """
        # Ваш код здесь
        pass

    async def acquire(self):
        """Ожидает, пока можно сделать запрос."""
        # Ваш код здесь
        pass


# Пример использования:
async def main():
    limiter = AsyncRateLimiter(max_requests=5, period=1.0)

    async def make_request(i):
        await limiter.acquire()
        print(f"[{time.strftime('%H:%M:%S')}] Запрос {i}")

    tasks = [make_request(i) for i in range(15)]
    await asyncio.gather(*tasks)


asyncio.run(main())
# Должно выводить по 5 запросов в секунду
```

---

## Домашняя работа

### Задание 1. Асинхронный веб-скрапер

Напишите асинхронный скрапер, который:
1. Получает список URL страниц
2. Скачивает HTML каждой страницы параллельно (с ограничением в 5 одновременных запросов)
3. Извлекает заголовок страницы (`<title>`)
4. Возвращает словарь `{url: title}`

Используйте `asyncio.Semaphore` для ограничения параллелизма.

```python
async def scrape_titles(urls: list[str], max_concurrent: int = 5) -> dict[str, str]:
    """Возвращает {url: title} для каждой страницы."""
    # Ваш код здесь
    pass


# Пример:
urls = [
    "https://python.org",
    "https://docs.python.org",
    "https://pypi.org",
]
titles = asyncio.run(scrape_titles(urls))
print(titles)
```

### Задание 2. Producer-Consumer с обработкой ошибок

Реализуйте систему producer-consumer, где:
1. Producer генерирует случайные числа и кладёт их в очередь
2. Consumer берёт числа из очереди и проверяет, простые ли они
3. Если число простое — сохраняет в результат
4. Обработайте graceful shutdown по Ctrl+C

```python
async def is_prime(n: int) -> bool:
    """Проверяет, является ли число простым."""
    # Ваш код здесь
    pass


async def producer(queue: asyncio.Queue, count: int):
    """Генерирует count случайных чисел."""
    # Ваш код здесь
    pass


async def consumer(queue: asyncio.Queue, results: list):
    """Проверяет числа на простоту."""
    # Ваш код здесь
    pass


async def main():
    # Ваш код здесь
    pass
```

### Задание 3. ⭐ Async Context Manager для API-клиента

Создайте асинхронный контекстный менеджер для работы с API:

```python
class AsyncAPIClient:
    def __init__(self, base_url: str, rate_limit: int = 10):
        """
        base_url: базовый URL API
        rate_limit: максимум запросов в секунду
        """
        pass

    async def __aenter__(self):
        # Инициализация сессии
        pass

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # Закрытие сессии
        pass

    async def get(self, endpoint: str) -> dict:
        # GET-запрос с rate limiting
        pass

    async def post(self, endpoint: str, data: dict) -> dict:
        # POST-запрос с rate limiting
        pass


# Пример использования:
async def main():
    async with AsyncAPIClient("https://httpbin.org", rate_limit=5) as client:
        # Параллельные запросы с автоматическим rate limiting
        tasks = [client.get("/get") for _ in range(20)]
        results = await asyncio.gather(*tasks)
        print(f"Получено {len(results)} ответов")


asyncio.run(main())
```

---

[← Лекция 31: Celery. Multithreading. GIL. Multiprocessing](lesson31.md) | [Лекция 33: Сокеты. Django Channels. →](lesson33.md)
