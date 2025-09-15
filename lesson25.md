# Лекция 25. NoSQL. Куки, сессии, кеш

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
  - [Лекция 16. СУБД. DQL. SELECT. Индексы. Group by. Joins.](lesson16.md)
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
  - ▶ **Лекция 25. NoSQL. Куки, сессии, кеш**
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


![](https://imgb.ifunny.co/images/25d44f01a8e316a90fe39d4d7239a560e7f0c2fe1ae987596cd6788bd8eb1435_1.jpg)
## 📚 Введение в NoSQL

`NoSQL` (от англ. **Not Only SQL** — «не только SQL») — это термин, обозначающий типы баз данных, отличные от традиционных реляционных СУБД. NoSQL БД предлагают более гибкие модели хранения данных и лучше подходят для масштабируемых распределённых систем.

Подробнее:
- [Что такое NoSQL (Azure)](https://azure.microsoft.com/ru-ru/resources/cloud-computing-dictionary/what-is-nosql-database)
- [Обзор на Habr](https://habr.com/ru/articles/152477/)

---

### 🧨 Почему NoSQL?

NoSQL БД появились как ответ на ограничения реляционных СУБД в условиях:
- горизонтального масштабирования,
- работы с большими объёмами неструктурированных или слабо структурированных данных,
- необходимости высокой доступности и отказоустойчивости.

---

### ⚖️ Подробно о CAP-теореме

**CAP-теорема** (также называемая **теоремой Брюера**) гласит, что **в распределённой системе невозможно одновременно обеспечить**:

| Свойство       | Описание                                                                 |
|----------------|--------------------------------------------------------------------------|
| **Consistency** (Согласованность) | Все узлы видят одинаковые данные в один и тот же момент. |
| **Availability** (Доступность)    | Система всегда отвечает на запрос (даже если это не последняя версия). |
| **Partition Tolerance** (Устойчивость к разделению) | Система продолжает работать, даже если между узлами есть сетевые проблемы. |

🧠 **Зачем нужна CAP-теорема?**
При проектировании распределённых систем (особенно в NoSQL) часто приходится **жертвовать чем-то** ради надёжности и масштабируемости. Например:

- В случае сетевого разделения можно **либо отказать в доступе (жертвуем A)**,
- Либо **отдать устаревшие данные (жертвуем C)**.

**Вывод:** система может выбрать максимум **два из трёх свойств одновременно**.

**Примеры:**
- 🔸 **Cassandra** — AP: предпочитает доступность и устойчивость, согласованность достигается позже (eventual consistency).
- 🔸 **MongoDB (до 4.0)** — CP: жертвует доступностью при проблемах с сетью.
- 🔸 **Redis (в кластере)** — чаще AP.

---

### 🔢 Основные типы NoSQL баз данных

![](https://files.codingninjas.in/article_images/types-of-nosql-databases-0-1644120083.webp)

---

#### 1. 🗝️ Key-Value (Ключ-значение)

Простейшая модель, напоминающая словарь: `ключ → значение`.

**Пример хранения:**

```json
{
  "user:123": "Alice",
  "user:124": "Bob",
  "cart:456": {
    "item": "Book",
    "qty": 2
  }
}
```

**Где используется:**
- **Redis в GitHub** — как брокер сообщений и кэш состояний пайплайнов.
- **DynamoDB в Amazon** — хранение корзин и профилей пользователей.

---

#### 2. 📄 Document-oriented (Документные БД)

Хранят данные в виде документов (JSON, BSON и т.д.).

**Пример хранения:**

```json
{
  "_id": "user_001",
  "name": "Alice",
  "email": "alice@example.com",
  "orders": [
    {"item": "Book", "qty": 2},
    {"item": "Pen", "qty": 5}
  ]
}
```

**Где используется:**
- **MongoDB в eBay** — данные пользователей и товаров.
- **CouchDB в BBC** — автономный режим с синхронизацией.

---

#### 3. 📊 Column-family (Колонночные БД)

Колонночные базы данных **на первый взгляд похожи на реляционные**, но различие — **в физической организации хранения данных**.

##### 🆚 В чём отличие от реляционных БД?

|                      | Реляционные БД (PostgreSQL, MySQL) | Колонночные БД (Cassandra, Bigtable)     |
|----------------------|------------------------------------|-------------------------------------------|
| Единица хранения     | строка (row)                       | столбец (column) или «семейство столбцов» |
| Физическое хранение  | строки лежат вместе                | значения одного столбца лежат вместе      |
| Сценарий оптимизации | запись/чтение строк                | аналитика, агрегации по столбцам          |
| Гибкость схемы       | строго задана                      | допускаются разные наборы столбцов        |

**Пример хранения (упрощённо):**

```
RowKey: user1
  Name: Alice
  Age: 30
  City: Prague

RowKey: user2
  Name: Bob
  Age: 25
```

**Где используется:**
- **Cassandra в Netflix** — логирование, телеметрия.
- **Bigtable в YouTube** — просмотры, комментарии, рекомендации.

---

#### 4. 🔗 Graph (Графовые БД)

Графовые базы данных хранят данные как **узлы (nodes)** и **связи (edges)** между ними.

**Пример хранения:**

```
(Alice)-[:FRIEND]->(Bob)
(Alice)-[:LISTENS_TO]->(Song)
(Alice)-[:VISITED]->(Place)
```

##### 🧠 Почему графы так важны?

Механизм поиска связей между сущностями используется **повсеместно**:

- **Facebook**: "Возможно, вы знаете этого человека" — через общих друзей.
- **Spotify**: "Похожие исполнители" — через пользователей с похожими интересами.
- **Google Maps**: построение маршрута — как поиск кратчайшего пути в графе дорог.

Все эти задачи решаются **одними и теми же графовыми алгоритмами** (DFS, BFS, Dijkstra и т.д.) на одних и тех же структурах — графах.

**Где используется:**
- **Neo4j в eBay** — рекомендации и antifraud.
- **Amazon Neptune** — персонализация и графы предпочтений.
- **LinkedIn** — поиск и визуализация сетей профессиональных связей.

---

### 💡 Применение и сравнение

| Сценарий                      | Тип NoSQL         | Примеры                                      |
|------------------------------|-------------------|----------------------------------------------|
| Кэш, сессии, временные данные | Key-Value         | Redis, Memcached                             |
| Пользователи, CMS             | Document-oriented | MongoDB, CouchDB                             |
| Аналитика, временные ряды     | Column-family     | Cassandra, Bigtable                          |
| Связи, рекомендации, маршруты | Graph             | Neo4j, Neptune, OrientDB                     |

---

### 🧾 Когда использовать NoSQL?

✅ Используй, если:
- структура данных часто меняется или неформализована;
- требуется масштабирование и отказоустойчивость;
- важны скорость доступа и запись в real-time.

❌ Не подходит, если:
- необходима строгая согласованность и транзакции;
- бизнес-логика требует сложных JOIN-операций;
- используется строго табличная модель с контролем схемы.

---

> 💬 **Комментарий преподавателя:**
> Redis — универсальный инструмент. Он почти всегда есть в стеке. Даже если не используется на старте, его часто добавляют позже для кэширования, очередей и хранения сессий. Мы с ним ещё поработаем дальше по курсу.
# 🍪 Куки, 🧾 Сессии и ⚡ Кеширование в Django

> HTTP-протокол не сохраняет состояния. Чтобы "помнить" пользователя, его действия и не делать одни и те же вычисления
> много раз — используются куки, сессии и кеш.

---

## 🧭 Что нужно понимать

- **HTTP stateless** — каждый запрос сам по себе, без истории.
- **Cookie** — способ сохранять небольшие данные на стороне клиента (браузера).
- **Session** — способ сохранять пользовательские данные на сервере, привязанные к уникальному `sessionid`,
  передаваемому в Cookie.
- **Cache** — быстрая память для хранения часто используемых данных (не обязательно связанных с пользователем).

---

## 🍪 Cookie (печеньки)

Куки — это пары `ключ:значение`, которые браузер хранит локально и отправляет на сервер с каждым HTTP-запросом к
соответствующему домену.

**Примеры применения:**

- Сохранение корзины товаров
- Запоминание темы оформления
- Предзаполнение форм
- Авторизация через `sessionid`

![](https://www.web-labs.kz/wp-content/uploads/2020/05/cookie.png)

**Куки существуют только на уровне HTTP запроса!** Их может запоминать браузер, но прямого отношения к серверу они не
имеют!


**Пример установки/удаления cookie c флагами безопасности:**

```python
from django.http import HttpResponse

resp = HttpResponse("ok")
resp.set_cookie(
    "theme", "dark", max_age=7*24*3600,
    secure=True, httponly=True, samesite="Lax"
)
# ...
resp.delete_cookie("theme")
```

## 🧾 Сессии
>
> Документация: https://docs.djangoproject.com/en/stable/topics/http/sessions/ — основы сессий; настройки: https://docs.djangoproject.com/en/stable/ref/settings/#sessions
>

Сессия — это механизм сохранения информации между запросами одного и того же пользователя. Чаще всего для реализации
сессий используется привязка к куки.

**Как это работает в Django:**

```plaintext
Браузер → POST /login → Сервер:
    - создаёт Session в БД
    - возвращает Set-Cookie: sessionid=<uuid>

Браузер → GET /profile → Cookie: sessionid → Сервер:
    - достаёт данные из request.session
```

![](http://techbriefers.com/wp-content/uploads/2019/10/cookie-and-session-management-process-in-codeigniter.jpg)

**Где хранятся данные:**

- По умолчанию — в таблице базы данных `django_session`
- Также возможны:
    - Redis
    - Файлы
    - Signed cookies


**Предпосылки настройки (обычно включены в типичном проекте):**
- 'django.contrib.sessions' в INSTALLED_APPS
- 'django.contrib.sessions.middleware.SessionMiddleware' в MIDDLEWARE
- (Рекомендуется) 'django.contrib.auth.middleware.AuthenticationMiddleware'

---

### 🛠 Использование

```python
# Работа с сессией в Django
request.session['visited'] = True

# Проверка
if request.session.get('visited'):
    ...

# Удаление
del request.session['visited']
```

### 💡 Пример — ограничение комментариев

```python
def post_comment(request, comment):
    if request.session.get('has_commented', False):
        return HttpResponse("You've already commented.")
    request.session['has_commented'] = True
    return HttpResponse("Thanks!")
```

### 🧪 Пример — хранение временной метки

```python
request.session['last_action'] = timezone.now()
```


#### ⏳ Срок жизни сессии

```python
# Установить время жизни текущей сессии (секунды)
request.session.set_expiry(3600)  # 1 час
```

---

### 🧩 Вне запроса (SessionStore)

```python
from django.contrib.sessions.backends.db import SessionStore

s = SessionStore()
s['foo'] = 'bar'
s.create()
s.session_key  # сохранённый ключ
```

---

### 🛑 Важные нюансы

- Данные сессии сериализуются (по умолчанию JSON), поэтому объекты должны быть сериализуемыми. Подробно разберём сериализацию далее по курсу.
- Данные сохраняются **только при изменении** `request.session` как объекта

```python
request.session['foo'] = 'bar'  # сохранится
request.session['foo']['x'] = 1  # ❌ не сохранится
```


При вложенной мутации пометьте сессию изменённой:

```python
request.session.setdefault("cart", {})["id123"] = 2
request.session.modified = True  # зафиксировать изменения для сохранения
```


✅ Можно настроить:

```python
SESSION_SAVE_EVERY_REQUEST = True
```

---

### 🧹 Очистка старых сессий

```bash
python manage.py clearsessions
```

> Команду рекомендуется запускать периодически (cron/periodic job) — подробнее о планировании задач разберём позже по курсу.


Или вручную:

```python
from django.contrib.sessions.models import Session

Session.objects.filter(...).delete()
```

---

## ⚡ Кеширование
>
> Документация: https://docs.djangoproject.com/en/stable/topics/cache/ — основы кеширования; настройки: https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-CACHES; per-view cache: https://docs.djangoproject.com/en/stable/topics/cache/#the-per-view-cache
>

Кеш — это **временное хранилище** для ускорения доступа к часто используемым данным.

![](https://cdn.acunetix.com/wp_content/uploads/2018/12/image1-1.png)

### 💡 Пример

```python
# Вместо:
Article.objects.filter(published=True).order_by('-date')[:5]

# Лучше:
articles = cache.get('homepage_articles')
if not articles:
    articles = Article.objects.filter(...).all()
    cache.set('homepage_articles', articles, timeout=3600)
```

Альтернатива короче:

```python
articles = cache.get_or_set(
    "homepage:articles:v1",
    lambda: Article.objects.filter(published=True).order_by("-date")[:5],
    timeout=3600,
)
```

Счётчики (зависят от backend, поддерживаются Redis/Memcached):

```python
cache.incr("counter:visits", ignore_key_check=True)
# cache.decr("counter:visits")
```


---

## 📦 Варианты backends

| Хранилище  | Плюсы                                     | Минусы                       |
|------------|-------------------------------------------|------------------------------|
| Redis      | Быстро, работает в памяти, масштабируется | Требует установки и сервера  |
| Memcached  | Очень быстрый, простой                    | Только строковые ключи       |
| FileBased  | Не требует серверов                       | Медленный на больших объёмах |
| Database   | Ничего не нужно настраивать               | Нагрузка на БД               |
| DummyCache | Ничего не делает (для dev)                | Нет кеша :)                  |

---

## ⚙️ Настройки кеша (пример Redis)

Установка backend'а:

```bash
python -m pip install django-redis
```


```python
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
        "TIMEOUT": 3600,
        "KEY_PREFIX": "myapp",
    }
}
```

---

## 🎯 Использование

```python
from django.core.cache import cache

cache.set("key", "value", timeout=60)
cache.get("key")  # "value"
cache.delete("key")
```

Массовые операции:

```python
cache.set_many({"a": 1, "b": 2})
cache.get_many(["a", "b"])
```

---

## 🧱 Кеширование view

```python
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def my_view(request):
    ...
```

Или в `urls.py`:

```python
path("foo/", cache_page(900)(views.foo_view))
```

---

## 🧰 Кеширование шаблонов

```django
{% load cache %}
{% cache 300 sidebar %}
    ...HTML sidebar...
{% endcache %}
```

---

## 🧩 Пер-сайт кэш через middleware

```python
MIDDLEWARE = [
    "django.middleware.cache.UpdateCacheMiddleware",
    # ...
    "django.middleware.cache.FetchFromCacheMiddleware",
]
CACHE_MIDDLEWARE_SECONDS = 300
```

## 🧼 Очистка кеша

```python
cache.clear()
```

---

## ⛔ Отключение кеша для отдельной view

```python
from django.views.decorators.cache import never_cache


@never_cache
def dynamic_view(request):
    ...
```

---

## 📌 Итоги

- Куки — данные на клиенте (браузере).
- Сессии — данные на сервере, привязанные к пользователю.
- Кеш — быстрая память для **ускорения работы**, не связана напрямую с пользователем.
- Всё это критично для **безопасной**, **быстрой** и **удобной** работы сайта.

---

## 🧠 Вопросы для закрепления

1. Чем отличаются куки от сессий?
2. Почему сессии нельзя использовать для анонимных пользователей везде?
3. Где по умолчанию Django хранит сессии?
4. Что произойдёт, если модифицировать `request.session['key']['value']`?
5. Как бы вы реализовали кеширование главной страницы?
6. Как очистить все сессии, старше 30 дней?

---
