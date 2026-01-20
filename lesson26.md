# Лекция 26. Логирование. Middleware. Signals. Background Tasks. Messages. Manage commands

### Оглавление курса

<details>
  <summary>Блок 1 — Python Basic (1–6)</summary>

  - [Лекция 1. Введение. Типизации. Переменные. Строки и числа. Булева алгебра. Ветвление](lesson01.md)
  - [Лекция 2. Обработка исключений. Списки, строки детальнее, срезы, циклы.](lesson02.md)
  - [Лекция 3. None. Range, list comprehension, sum, max, min, len, sorted, all, any. Работа с файлами](lesson03.md)
  - [Лекция 4. Хеш-таблицы. Set, frozenset. Dict. Tuple. Немного об импортах. Namedtuple, OrderedDict](lesson04.md)
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

<details>
  <summary>Блок 4 — SQL (15–17)</summary>

  - [Лекция 15. СУБД. PostgreSQL. SQL. DDL. Пользователи. DCL. DML. Связи.](lesson15.md)
  - [Лекция 16. СУБД. DQL. SELECT. Индексы. Group by. Joins.](lesson16.md)
  - [Лекция 17. СУБД. Нормализация. Аномалии. Транзакции. ACID. TCL. Backup](lesson17.md)
</details>

- [Лекция 18. Virtual env. Pip. Устанавливаемые модули. Pyenv.](lesson18.md)

<details open>
  <summary>Блок 5 — Django (19–26)</summary>

  - [Лекция 19. Знакомство с Django](lesson19.md)
  - [Лекция 20. Templates. Static](lesson20.md)
  - [Лекция 21. Модели. Связи. Meta. Abstract, proxy](lesson21.md)
  - [Лекция 22. Django ORM](lesson22.md)
  - [Лекция 23. Forms, ModelForms. User, Authentication](lesson23.md)
  - [Лекция 24. ClassBaseView](lesson24.md)
  - [Лекция 25. NoSQL. Куки, сессии, кеш](lesson25.md)
  - ▶ **Лекция 26. Логирование. Middleware. Signals. Background Tasks. Messages. Manage commands**
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

## Введение

В Django помимо представлений важно уметь наблюдать и управлять жизненным циклом запроса. В этом уроке мы начнём с
**логирования** (наблюдаемость), затем перейдём к **middleware** (сквозные обработки request/response), **signals**
(разделение побочных эффектов), **background tasks** (фоновые задачи), **messages** (flash‑сообщения для UI) и кратко затронем **manage‑команды**.

Куда что применять кратко:
- Логирование — наблюдаемость, отладка, аудит. Используем logging + конфигурацию LOGGING.
- Middleware — быстрые и stateless сквозные операции; тяжёлую логику не размещаем.
- Signals — реакция на события модели/системы; тяжёлые задачи выносим в очереди, используем dispatch_uid.
- Background Tasks (Django 6.0+) — встроенный фреймворк для фоновых задач; сигнал ставит задачу, воркер выполняет.
- Messages — дружелюбная коммуникация с пользователем между перенаправлениями.
- Manage‑команды и data migrations — операции обслуживания и изменения данных (упомянем современный `RunPython.noop`).

---

## 📝 Логирование в Django

📚 [Документация](https://docs.djangoproject.com/en/stable/topics/logging/)

### Что это?

**Логирование** — это процесс записи информации о работе приложения. В Django используется встроенный модуль Python `logging`, который настраивается через словарь `LOGGING` в settings.py.

### Зачем нужно?

- Отладка проблем в продакшене
- Мониторинг производительности
- Аудит действий пользователей
- Анализ ошибок и исключений

### Базовая настройка

Минимальная конфигурация в `settings.py`:

```python
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "django.log",
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False,
        },
        "myapp": {  # замените на имя вашего приложения
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
```

### Использование в коде

```python
import logging

logger = logging.getLogger(__name__)

def my_view(request):
    logger.debug("Начало обработки запроса")
    logger.info("Пользователь %s выполнил действие", request.user.username)

    try:
        # ваш код
        result = some_operation()
        logger.info("Операция выполнена успешно")
        return result
    except Exception as e:
        logger.error("Ошибка при выполнении операции: %s", e, exc_info=True)
        raise
```

### Уровни логирования

| Уровень    | Числовое значение | Когда использовать                          |
|------------|-------------------|---------------------------------------------|
| `DEBUG`    | 10                | Детальная информация для отладки            |
| `INFO`     | 20                | Общая информация о работе                   |
| `WARNING`  | 30                | Предупреждения о потенциальных проблемах    |
| `ERROR`    | 40                | Ошибки, которые не останавливают работу     |
| `CRITICAL` | 50                | Критические ошибки, приложение может упасть |

---

### Логирование SQL-запросов

Полезно для отладки N+1 проблем и оптимизации:

```python
# settings.py (только для разработки!)
LOGGING = {
    # ... остальные настройки ...
    "loggers": {
        "django.db.backends": {
            "handlers": ["console"],
            "level": "DEBUG",  # Покажет все SQL-запросы
            "propagate": False,
        },
    },
}
```

---

### Структурированное логирование (JSON)

Для production рекомендуется JSON-формат — его легко парсить системами мониторинга:

```python
# settings.py
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(levelname)s %(name)s %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "json",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}
```

Установка: `pip install python-json-logger`

Вывод будет таким:
```json
{"asctime": "2025-01-15 10:30:00", "levelname": "INFO", "name": "myapp.views", "message": "User logged in", "user_id": 123}
```

---

### Логирование в Production

#### Интеграция с Sentry

[Sentry](https://sentry.io/) — популярный сервис для отслеживания ошибок:

```python
# settings.py
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://your-dsn@sentry.io/project",
    integrations=[DjangoIntegration()],
    traces_sample_rate=0.1,  # 10% запросов для performance monitoring
    send_default_pii=True,
)
```

#### Централизованное логирование (ELK Stack)

Для больших проектов логи отправляют в Elasticsearch:

```
Приложение → Filebeat → Logstash → Elasticsearch → Kibana
     ↓
  JSON-логи в файл или stdout
```

> 💡 **Совет:** В Docker/Kubernetes логируйте в stdout — оркестратор сам соберёт логи.

---

### Контекстное логирование

Добавляйте контекст к логам для удобства отладки:

```python
import logging

logger = logging.getLogger(__name__)

def process_order(request, order_id):
    # Создаём адаптер с дополнительным контекстом
    extra = {
        "user_id": request.user.id,
        "order_id": order_id,
        "ip": request.META.get("REMOTE_ADDR"),
    }

    logger.info("Processing order", extra=extra)

    try:
        order = Order.objects.get(pk=order_id)
        # ... обработка
        logger.info("Order processed successfully", extra=extra)
    except Order.DoesNotExist:
        logger.warning("Order not found", extra=extra)
    except Exception as e:
        logger.exception("Failed to process order", extra=extra)
        raise
```

---

## 🧩 Middleware

![](https://memegenerator.net/img/instances/81631865.jpg)

📚 [Официальная документация](https://docs.djangoproject.com/en/stable/topics/http/middleware/)

### Что это?

Мы с вами рассмотрели основные этапы того, какие этапы должен пройти request на всём пути нашей request-response
системы,
но на самом деле каждый request проходит кучу дополнительных обработок, таких как middleware, причём каждый request
делает это дважды, при «входе» и при «выходе».

**Middleware** — это фреймворк обработки запросов и ответов. Каждый HTTP-запрос проходит через цепочку middleware
«вперёд» к view и «обратно» — к пользователю. Это похоже на слоёный пирог: каждый слой может что-то сделать с запросом
или ответом.

```plaintext
Request ↓
 ┌─────────────────────────────────────────────────────────┐
 │ SecurityMiddleware                                      │
 │ SessionMiddleware                                       │
 │ CommonMiddleware                                        │
 │ CsrfViewMiddleware                                      │
 │ AuthenticationMiddleware                                │
 │ YOUR CUSTOM MIDDLEWARE                                  │
 │ MessageMiddleware                                       │
 │ Clickjacking Protection (XFrameOptionsMiddleware)       │
 └─────────────────────────────────────────────────────────┘
                    View →
         ← Response (тот же путь обратно)
```

---

### Пример структуры в `settings.py`

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'main.middleware.CheckUserStatus',  # ваш кастомный
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

---

### Как написать свой middleware?

#### ✅ Вариант 1: Функциональный

```python
import logging
logger = logging.getLogger(__name__)

def simple_middleware(get_response):
    def middleware(request):
        logger.debug("Before view")
        response = get_response(request)
        logger.debug("After view")
        return response

    return middleware
```

#### ✅ Вариант 2: Классовый (рекомендуется)

```python
import logging
from django.http import HttpResponse
logger = logging.getLogger(__name__)

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.debug("Before view")
        # Пример короткого замыкания запроса:
        # if some_condition(request):
        #     return HttpResponse("Blocked", status=403)
        response = self.get_response(request)
        logger.debug("After view")
        return response
```

Добавьте middleware в `settings.py`.

---

### 🔧 Практические примеры middleware

#### 1. Request Timing (измерение времени запроса)

```python
import time
import logging

logger = logging.getLogger(__name__)


class RequestTimingMiddleware:
    """Логирует время выполнения каждого запроса."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.perf_counter()

        response = self.get_response(request)

        duration = time.perf_counter() - start_time
        logger.info(
            "Request %s %s completed in %.3fs",
            request.method,
            request.path,
            duration,
        )

        # Можно добавить заголовок в ответ
        response["X-Request-Duration"] = f"{duration:.3f}s"
        return response
```

#### 2. Request ID (для трассировки запросов)

```python
import uuid


class RequestIDMiddleware:
    """Добавляет уникальный ID к каждому запросу для трассировки."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Берём ID из заголовка или генерируем новый
        request_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())
        request.request_id = request_id

        response = self.get_response(request)

        response["X-Request-ID"] = request_id
        return response
```

#### 3. IP Blocking (блокировка по IP)

```python
from django.http import HttpResponseForbidden
from django.conf import settings


class IPBlockMiddleware:
    """Блокирует запросы с определённых IP-адресов."""

    def __init__(self, get_response):
        self.get_response = get_response
        self.blocked_ips = getattr(settings, "BLOCKED_IPS", [])

    def __call__(self, request):
        ip = self.get_client_ip(request)

        if ip in self.blocked_ips:
            return HttpResponseForbidden("Access denied")

        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0].strip()
        return request.META.get("REMOTE_ADDR")
```

---

### 🪝 Дополнительные хуки middleware

Помимо `__call__`, middleware может определять специальные методы:

```python
class AdvancedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Вызывается ПЕРЕД вызовом view, но ПОСЛЕ URL routing.
        Можно проверить, какой view будет вызван.

        Return None — продолжить выполнение
        Return HttpResponse — прервать и вернуть ответ
        """
        # Пример: логирование вызываемого view
        logger.debug(f"Calling view: {view_func.__name__}")
        return None

    def process_exception(self, request, exception):
        """
        Вызывается, если view выбросил исключение.

        Return None — исключение обрабатывается стандартно
        Return HttpResponse — вернуть этот ответ вместо ошибки
        """
        logger.exception(f"Exception in view: {exception}")
        # Можно вернуть кастомную страницу ошибки
        return None

    def process_template_response(self, request, response):
        """
        Вызывается, если response имеет метод render() (TemplateResponse).
        Позволяет модифицировать контекст шаблона.
        """
        if hasattr(response, "context_data"):
            response.context_data["middleware_data"] = "injected"
        return response
```

#### Порядок вызова хуков

```plaintext
Request ↓
  1. Middleware1.__call__ (before get_response)
  2. Middleware2.__call__ (before get_response)
  3. process_view (все middleware, сверху вниз)
  4. View выполняется
  5. process_exception (если была ошибка, снизу вверх)
  6. process_template_response (если TemplateResponse, снизу вверх)
  7. Middleware2.__call__ (after get_response)
  8. Middleware1.__call__ (after get_response)
Response ↑
```

---

### 💡 Совет

Порядок **имеет значение**! Если вы добавили middleware, работающий с `request.user`, он должен быть **после**
`AuthenticationMiddleware`.

---

### 🔧 MiddlewareMixin

Для совместимости с устаревшими API:

```python
from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ...

    def process_response(self, request, response):
        ...
```

> ⚠️ `MiddlewareMixin` — это legacy-подход. Для новых проектов используйте классовый middleware с `__call__`.

---

## 📡 Signals (Сигналы)

📚 [Signals](https://docs.djangoproject.com/en/stable/topics/signals/)

### Что это?

Сигналы — способ уведомить части вашего приложения о том, что «что-то произошло», — например, сохранение объекта. Это
помогает **разделить ответственность** и **не писать логику в моделях или view напрямую**.

---

### Часто используемые сигналы:

| Сигнал                                 | Когда вызывается            |
|----------------------------------------|-----------------------------|
| `pre_save` / `post_save`               | До/после сохранения объекта |
| `pre_delete` / `post_delete`           | До/после удаления объекта   |
| `m2m_changed`                          | Изменения в ManyToMany      |
| `request_started` / `request_finished` | Начало/конец запроса        |
| `pre_migrate` / `post_migrate`         | До/после миграций           |
| `user_logged_in` / `user_logged_out`   | Вход/выход пользователя     |

---

### 🤔 Сигналы vs переопределение save()

Когда что использовать?

| Критерий                           | Сигналы                      | Переопределение `save()`      |
|------------------------------------|------------------------------|-------------------------------|
| Логика связана с моделью напрямую  | ❌                            | ✅ Лучший выбор                |
| Логика в другом приложении         | ✅ Разделение ответственности | ❌ Создаёт зависимость         |
| Нужно реагировать на bulk-операции | ❌ Сигналы не вызываются      | ❌ `save()` тоже не вызывается |
| Отладка и читаемость               | ❌ Скрытая логика             | ✅ Явная логика                |
| Сторонние приложения               | ✅ Единственный способ        | ❌ Нельзя изменить             |
| Аудит/логирование                  | ✅ Хороший выбор              | ⚠️ Можно, но засоряет модель  |

**Правило:** Если логика — часть бизнес-логики модели, используйте `save()`. Если это побочный эффект (уведомления, аудит, кеш) — сигналы.

---

### Использование с декоратором

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import Order


@receiver(post_save, sender=Order)
def after_order_save(sender, instance, created, **kwargs):
    if created:
        send_email_to_manager(instance)
```

> Чтобы избежать двойной регистрации обработчика при повторных импортах/автоперезапусках, используйте `dispatch_uid`.

```python
@receiver(post_save, sender=Order, dispatch_uid="order_post_save_once")
def after_order_save(sender, instance, created, **kwargs):
    ...
```

- Тяжёлые операции в сигнале (отправка email, внешние API) лучше выносить в очередь задач (Celery/RQ) — сигнал только ставит задачу.
- В современных версиях Django для кастомных сигналов не требуется `providing_args` — параметр удалён.

---

### Пример: m2m_changed

Сигнал `m2m_changed` вызывается при изменении ManyToMany связей:

```python
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from myapp.models import Article


@receiver(m2m_changed, sender=Article.tags.through)
def tags_changed(sender, instance, action, pk_set, **kwargs):
    """
    Вызывается при изменении тегов статьи.

    action может быть:
    - "pre_add" / "post_add" — перед/после добавления
    - "pre_remove" / "post_remove" — перед/после удаления
    - "pre_clear" / "post_clear" — перед/после очистки всех связей
    """
    if action == "post_add":
        # pk_set — множество ID добавленных тегов
        print(f"Added tags {pk_set} to article {instance.title}")

        # Пример: инвалидация кеша
        cache.delete(f"article_{instance.id}_tags")

    elif action == "post_remove":
        print(f"Removed tags {pk_set} from article {instance.title}")

    elif action == "post_clear":
        print(f"Cleared all tags from article {instance.title}")
```

> ⚠️ **Важно:** `sender` — это промежуточная таблица (`Article.tags.through`), а не сама модель!

---

### Ручной сигнал

```python
from django.dispatch import Signal

pizza_done = Signal()

# Отправка сигнала
pizza_done.send(sender=None, toppings=["pepperoni"], size="large")

# Подписка на сигнал
@receiver(pizza_done)
def on_pizza_done(sender, toppings, size, **kwargs):
    print(f"Pizza {size} with {toppings} is ready!")
```

---

### ⚠️ Потенциальные проблемы

- **Скрытая логика**: сигналы вызываются «в фоне», усложняя отладку.
- **Неявные зависимости**: сложно понять, кто слушает сигнал.
- **Ошибки в сигналах → падает всё** (если не обработать исключение).
- **Не работают с bulk-операциями**: `QuerySet.update()`, `bulk_create()` не вызывают сигналы.

```python
# ❌ Сигнал post_save НЕ вызовется!
Order.objects.filter(status="pending").update(status="completed")

# ✅ Сигнал вызовется для каждого объекта
for order in Order.objects.filter(status="pending"):
    order.status = "completed"
    order.save()
```

Используйте **осознанно и выборочно**, особенно в больших проектах.

---

### 📁 Где регистрировать сигналы?

Обычно сигналы регистрируются в отдельном модуле `signals.py` внутри вашего приложения, а затем подключаются в
`apps.py`.

#### Пример структуры:

```
myapp/
├── apps.py
├── models.py
├── signals.py
```

#### signals.py:

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order


@receiver(post_save, sender=Order)
def notify_manager(sender, instance, created, **kwargs):
    if created:
        print(f"New order created: {instance.id}")
```

#### apps.py:

```python
from django.apps import AppConfig


class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        import myapp.signals
```

📌 Метод `ready()` вызывается при старте Django, и именно там следует **импортировать** модуль с сигналами, чтобы они
были зарегистрированы. Не подключайте сигналы в `models.py` или `__init__.py` — это может привести к проблемам с
импортами.

---

### ℹ️ Что такое `apps.py`?

Файл `apps.py` содержит класс-настройку вашего приложения и используется Django для конфигурации.

#### Пример базовой конфигурации:

```python
from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
```

### Что можно делать в `apps.py`?

- Регистрировать сигналы
- Выполнять инициализацию сторонних библиотек
- Проверять зависимости
- Настраивать логгеры
- Создавать фоновые задачи или cron-хуки (например, через Celery beat)

📌 Только не загружайте `ready()` тяжёлыми действиями — он вызывается при **каждом запуске** процесса Django.

---

## 🚀 Background Tasks (Django 6.0+)

📚 [Документация](https://docs.djangoproject.com/en/6.0/topics/tasks/)

### Что это?

**Background Tasks** — это встроенный фреймворк Django для выполнения кода **вне цикла request-response**. Появился в Django 6.0 (декабрь 2025).

Раньше для фоновых задач требовались сторонние решения (Celery, RQ, Dramatiq). Теперь Django предоставляет **единый API** для определения и постановки задач в очередь, а выполнение остаётся за внешними воркерами.

### Когда использовать?

- Отправка email (не блокируем пользователя)
- Обработка загруженных файлов (ресайз изображений, конвертация)
- Вызовы внешних API (платёжные системы, уведомления)
- Генерация отчётов
- Любые «тяжёлые» операции из сигналов

### Определение задачи

Задачи определяются декоратором `@task`:

```python
# myapp/tasks.py
from django.core.mail import send_mail
from django.tasks import task


@task
def send_welcome_email(user_email, username):
    """Отправка приветственного письма новому пользователю."""
    return send_mail(
        subject="Добро пожаловать!",
        message=f"Привет, {username}! Рады видеть вас.",
        from_email=None,  # использует DEFAULT_FROM_EMAIL
        recipient_list=[user_email],
    )


@task(priority=10, queue_name="reports")
def generate_monthly_report(user_id, month, year):
    """Генерация отчёта с высоким приоритетом."""
    # ... тяжёлая логика
    return {"status": "completed", "rows": 1500}
```

### Постановка задачи в очередь

```python
from myapp.tasks import send_welcome_email

# В view или сигнале
def register_user(request):
    user = User.objects.create(...)

    # Ставим задачу в очередь — не блокируем ответ
    result = send_welcome_email.enqueue(
        user_email=user.email,
        username=user.username,
    )

    # result — это TaskResult с уникальным id
    print(f"Task ID: {result.id}")

    return redirect("profile")
```

### Настройка backends

Backends настраиваются в `settings.py` через `TASKS`:

```python
# Для разработки — выполняет задачи сразу (синхронно)
TASKS = {
    "default": {
        "BACKEND": "django.tasks.backends.immediate.ImmediateBackend",
    }
}

# Для тестов — сохраняет задачи без выполнения
TASKS = {
    "default": {
        "BACKEND": "django.tasks.backends.dummy.DummyBackend",
    }
}
```

#### Встроенные backends:

| Backend            | Описание                          | Использование |
|--------------------|-----------------------------------|---------------|
| `ImmediateBackend` | Выполняет задачи сразу, синхронно | Разработка    |
| `DummyBackend`     | Сохраняет задачи без выполнения   | Тестирование  |

> ⚠️ **Важно:** Для production нужен сторонний backend с реальным воркером (см. [Community Ecosystem](https://docs.djangoproject.com/en/6.0/topics/tasks/)).

### Интеграция с сигналами

Типичный паттерн — сигнал ставит задачу в очередь:

```python
# myapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from .tasks import notify_manager, process_order


@receiver(post_save, sender=Order, dispatch_uid="order_created")
def on_order_created(sender, instance, created, **kwargs):
    if created:
        # Лёгкая задача — можно в сигнале
        notify_manager.enqueue(order_id=instance.id)

        # Тяжёлая задача — обязательно в очередь
        process_order.enqueue(order_id=instance.id)
```

### Работа с транзакциями

При использовании транзакций важно ставить задачу **после коммита**, иначе воркер может не найти объект в БД:

```python
from functools import partial
from django.db import transaction


def create_order(request):
    with transaction.atomic():
        order = Order.objects.create(...)

        # ❌ Неправильно — задача может выполниться до коммита
        # process_order.enqueue(order_id=order.id)

        # ✅ Правильно — задача ставится после коммита
        transaction.on_commit(
            partial(process_order.enqueue, order_id=order.id)
        )

    return redirect("orders")
```

### Получение результата

```python
from django.tasks import default_task_backend

# При постановке задачи
result = send_welcome_email.enqueue(user_email="user@example.com", username="John")
task_id = result.id  # Сохраняем для последующего использования

# Позже — получаем результат
result = send_welcome_email.get_result(task_id)
# или через backend
result = default_task_backend.get_result(task_id)

# Проверяем статус
print(result.status)  # RUNNING, SUCCESSFUL, FAILED

# Обновляем статус
result.refresh()

# Получаем значение (если SUCCESSFUL)
if result.status == "SUCCESSFUL":
    print(result.return_value)

# Получаем ошибки (если FAILED)
if result.status == "FAILED":
    for error in result.errors:
        print(error.exception_class)
        print(error.traceback)
```

### Task Context

Задача может получить информацию о себе через контекст:

```python
import logging
from django.tasks import task

logger = logging.getLogger(__name__)


@task(takes_context=True)
def retry_aware_task(context, data):
    """Задача, которая знает о попытках выполнения."""
    logger.info(
        f"Попытка {context.attempt}, Task ID: {context.task_result.id}"
    )
    # ... логика
```

### ⚠️ Ограничения

1. **JSON-сериализация**: Аргументы и возвращаемые значения должны быть JSON-сериализуемыми
   ```python
   # ❌ Не работает
   my_task.enqueue(datetime.now())  # datetime не сериализуется
   my_task.enqueue(user)  # Model instance не сериализуется

   # ✅ Работает
   my_task.enqueue(user_id=user.id)  # Передаём ID
   my_task.enqueue(timestamp=datetime.now().isoformat())  # Строка
   ```

2. **Django не запускает воркеры**: Фреймворк только определяет и ставит задачи. Выполнение — ответственность внешней инфраструктуры.

3. **Round-trip типов**: После JSON-сериализации типы могут измениться
   ```python
   # tuple → list после сериализации
   my_task.enqueue(data=(1, 2, 3))  # В задаче будет [1, 2, 3]
   ```

> 📌 Django Tasks — это **стандартизированный API**. Для production используйте совместимые backends из экосистемы, или Celery для сложных сценариев (см. лекцию 31).

---

## ✉️ Messages (Flash-сообщения)

📚 [Документация](https://docs.djangoproject.com/en/stable/ref/contrib/messages/)

Сообщения позволяют показать одноразовое уведомление пользователю после запроса. Пример — «Вы успешно
зарегистрировались».

---

### Включение

Убедитесь, что:

- `'django.contrib.messages'` в `INSTALLED_APPS`
- `'django.contrib.messages.middleware.MessageMiddleware'` в `MIDDLEWARE`
- `django.contrib.messages.context_processors.messages` в `TEMPLATES -> OPTIONS -> context_processors`

---

### Как использовать

```python
from django.contrib import messages


def my_view(request):
    messages.success(request, "Профиль обновлён!")
    return redirect("profile")
```

---

### Уровни сообщений

```python
messages.debug(request, "Отладка")
messages.info(request, "Информация")
messages.success(request, "Успех!")
messages.warning(request, "Предупреждение")
messages.error(request, "Ошибка")
```

---

### Отображение в шаблоне

```html
{% if messages %}
<ul class="messages">
    {% for message in messages %}
    <li class="{{ message.tags }}">{{ message }}</li>
    {% endfor %}
</ul>
{% endif %}
```

---

### Использование с CBV (Class-Based Views)

```python
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

class MyView(SuccessMessageMixin, CreateView):
    form_class = MyForm
    success_message = "Объект успешно создан!"
    success_url = reverse_lazy("my-list")  # или переопределите get_success_url()
```

> По умолчанию используется `FallbackStorage` (`MESSAGE_STORAGE`). При необходимости можно сменить backend в настройке `MESSAGE_STORAGE`.


---

### 💡 Практические кейсы

| Сценарий                    | Пример сообщения   |
|-----------------------------|--------------------|
| Успешная регистрация        | `messages.success` |
| Ошибка заполнения формы     | `messages.error`   |
| Предупреждение о балансе    | `messages.warning` |
| Отображение отладочной info | `messages.debug`   |

---

## 🧪 Повторим и закрепим

✅ Middleware — это **обработчик запроса и ответа**, может быть функцией или классом
✅ Signals позволяют **реагировать на действия** модели без изменения её кода
✅ Background Tasks (Django 6.0+) — встроенный способ **выносить тяжёлые операции** из сигналов и view
✅ Messages — это **одноразовые уведомления**, удобно использовать после redirect'ов
✅ Не забывайте включать нужные middleware и context_processors
✅ Middleware работают в **двух направлениях**: запрос и ответ
✅ Для production Background Tasks требуют **внешний backend** с воркерами

---

## Manage-команды и настройки.

> Документация по командам: https://docs.djangoproject.com/en/stable/ref/django-admin/


Manage-команды в рамках Django - это возможность запустить скрипт из консоли для выполнения абсолютно различных
действий.

Существует три способа запуска manage-команды:

```
django-admin <command> [options]
python manage.py <command> [options]
python -m django <command> [options]
```

В случае запуска через `django-admin` вы можете указать, какой файл настроек использовать при помощи опции `--settings`.

Если вы запускаете команду через `manage.py` (самый распространенный способ), файл настроек будет выбран в соответствии
с самим файлом `manage.py` (Напоминаю структуру, информация о файле настроек для Django проекта находится именно в
файле `manage.py`).

Мы использовали некоторые команды, но давайте посмотрим подробнее.

## Доступные команды.

![](https://www.meme-arsenal.com/memes/d4d5ed953c6b783bc97f142cb8e89d4d.jpg)

| Категория                            | Команда            | Описание                                             | Пример использования                                |
|--------------------------------------|--------------------|------------------------------------------------------|-----------------------------------------------------|
| 🏗 **Создание проекта и приложений** | `startproject`     | Создает новый Django-проект                          | `django-admin startproject mysite`                  |
|                                      | `startapp`         | Создает новое Django-приложение                      | `python manage.py startapp blog`                    |
| 🔄 **Миграции и работа с БД**        | `makemigrations`   | Генерирует файлы миграций на основе моделей          | `python manage.py makemigrations users`             |
|                                      | `migrate`          | Применяет миграции к базе данных                     | `python manage.py migrate`                          |
|                                      | `showmigrations`   | Показывает все миграции и их статус                  | `python manage.py showmigrations`                   |
|                                      | `sqlmigrate`       | Показывает SQL-код конкретной миграции               | `python manage.py sqlmigrate users 0001`            |
|                                      | `squashmigrations` | Объединяет несколько миграций в одну                 | `python manage.py squashmigrations users 0001 0005` |
|                                      | `flush`            | Удаляет все данные из базы (сохраняя структуру)      | `python manage.py flush`                            |
|                                      | `sqlflush`         | Показывает SQL-код, который будет выполнен при flush | `python manage.py sqlflush`                         |
|                                      | `sqlsequencereset` | Сброс последовательностей (id)                       | `python manage.py sqlsequencereset users`           |
|                                      | `inspectdb`        | Генерирует модели на основе существующей БД          | `python manage.py inspectdb > models.py`            |
| 🧪 **Тестирование**                  | `test`             | Запускает unit-тесты                                 | `python manage.py test`                             |
| 🧠 **Управление пользователями**     | `createsuperuser`  | Создание суперпользователя                           | `python manage.py createsuperuser`                  |
|                                      | `changepassword`   | Изменение пароля пользователя                        | `python manage.py changepassword admin`             |
| 🌐 **Сервер и консоль**              | `runserver`        | Запускает локальный сервер разработки                | `python manage.py runserver 8080`                   |
|                                      | `shell`            | Открывает Django shell                               | `python manage.py shell`                            |
|                                      | `dbshell`          | Открывает shell для БД (например, `psql`)            | `python manage.py dbshell`                          |
| 🗃 **Работа с данными (фикстуры)**   | `dumpdata`         | Экспорт данных в JSON (фикстуры)                     | `python manage.py dumpdata > data.json`             |
|                                      | `loaddata`         | Импорт данных из JSON-файла                          | `python manage.py loaddata data.json`               |
| 📖 **Работа с переводами**           | `makemessages`     | Поиск строк для перевода (создает `.po`)             | `python manage.py makemessages -l ru`               |
|                                      | `compilemessages`  | Компиляция `.po` в `.mo` для использования           | `python manage.py compilemessages`                  |
| 📦 **Кэш и сессии**                  | `createcachetable` | Создает таблицу в БД для хранения кэша               | `python manage.py createcachetable`                 |
|                                      | `clearsessions`    | Удаляет устаревшие сессии из БД                      | `python manage.py clearsessions`                    |
| 🔧 **Отладка и администрирование**   | `check`            | Проверка проекта на ошибки конфигурации              | `python manage.py check`                            |
|                                      | `diffsettings`     | Сравнение текущих и дефолтных настроек               | `python manage.py diffsettings`                     |
|                                      | `sendtestemail`    | Отправка тестового письма (если email настроен)      | `python manage.py sendtestemail user@example.com`   |
| 📜 **Пользовательские команды**      | (имя команды)      | Кастомная команда в `management/commands/`           | `python manage.py close_orders`                     |

Как создавать проект и приложения вы в целом научились, давайте посмотрим на новые команды, или как можно не стандартно
использовать старые.

## 🔄 **Миграции и работа с БД**

### makemigrations

Уже известная вам команда, которая создаёт файлы миграций, и может принимать имя приложения, чтобы создать только для
конкретного приложения.

Может принимать важный параметр `--empty`, при этом флаге создастся пустая миграция, никак не привязанная к моделям.
Выглядеть будет примерно вот так:

```python


from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('storages', '0003_auto_20201029_1352'),
    ]

    operations = [
    ]
```

Тут указано приложение, для которого миграция будет применена, и прошлая миграция, с которой текущая миграция будет
связана.

Зачем это вообще надо?

Мы можем в операции добавить любые интересующие нас действия, например, выполнения кода на Python.

Для этого нужно добавить класс `RunPython` из пакета `migrations`, который будет принимать два метода, первый будет
выполнен в случае выполнения миграции, второй - в случае отката миграции.

```python


from django.db import migrations


def some_forward_action(apps, schema_editor):
    Team = apps.get_model('storages', 'Team')
    Team.objects.create(name='B2B')
    Team.objects.create(name='CX')
    Team.objects.create(name='SFA')


def some_backward_action(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('storages', '0003_auto_20201029_1352'),
    ]

    operations = [
        migrations.RunPython(some_forward_action, some_backward_action)
    ]
```

Такие миграции называются **Data Migrations**.

Чаще всего для того, чтобы занести какие-либо данные в базу данных на этапе миграции, например, создать заведомо
известные объекты, как в моём примере, или для установки вычисляемого значения по умолчанию.

Для обратной миграции чаще всего действия не требуются (хоть и далеко не всегда).

#### Полный пример Data Migration:

```python
from django.db import migrations


def create_initial_teams(apps, schema_editor):
    """Создаёт начальные команды при миграции."""
    Team = apps.get_model('storages', 'Team')
    Team.objects.create(name='B2B')
    Team.objects.create(name='CX')
    Team.objects.create(name='SFA')


class Migration(migrations.Migration):
    dependencies = [
        ('storages', '0003_auto_20201029_1352'),
    ]

    operations = [
        # Современный способ — используем RunPython.noop для обратной миграции
        migrations.RunPython(create_initial_teams, migrations.RunPython.noop)
    ]
```

> 💡 **Совет:** Используйте `migrations.RunPython.noop` вместо `lambda x, y: None` — это более читаемый и современный подход.

#### Когда нужна обратная миграция:

```python
def create_default_category(apps, schema_editor):
    Category = apps.get_model('shop', 'Category')
    Category.objects.create(name='Uncategorized', slug='uncategorized')


def delete_default_category(apps, schema_editor):
    Category = apps.get_model('shop', 'Category')
    Category.objects.filter(slug='uncategorized').delete()


class Migration(migrations.Migration):
    operations = [
        migrations.RunPython(create_default_category, delete_default_category)
    ]
```

### migrate

Уже известная вам команда для применения миграции

Команда migrate применяется для выполнения миграций и синхронизации состояния базы данных с текущими моделями проекта.

```
python manage.py migrate [app_label] [migration_name]
```

- app_label — имя приложения, миграции которого необходимо применить.

- migration_name — имя конкретной миграции (обычно достаточно первых четырёх цифр из имени миграции).

Если не указать параметры, команда применит **все миграции для всех приложений**.

#### Пример: откат миграции

Допустим, вы уже применили миграции до `0008`, но обнаружили ошибку в `0006`. Вы можете откатить состояние базы данных
до миграции `0005`:

```bash
python manage.py migrate my_app 0005
```

> ⚠️ Это приведёт к откату всех миграций после 0005 и, скорее всего, приведёт к потере данных, связанных с удаляемыми
> моделями и полями.

#### Флаг `--fake`

Флаг `--fake` позволяет пометить миграцию как выполненную, **не внося реальные изменения** в базу данных:

```bash
python manage.py migrate my_app 0005 --fake
```

Этот приём используется в ситуациях, когда база данных уже была подготовлена вручную или через внешнюю систему (например
переносите проект с другого фреймворка на джанго), и вы хотите синхронизировать Django с её текущим состоянием.

#### Откат до нуля

Если вместо номера миграции указать `zero`, можно откатить **все миграции** для указанного приложения:

```bash
python manage.py migrate my_app zero
```

> 🔥 **Важно:** Откат миграций удалит таблицы и данные. Сделайте резервную копию!


### showmigrations

Также уже известная вам команда, которая отобразит список миграций и их состояние (применена или нет).


### `sqlmigrate`

Команда `sqlmigrate` позволяет **посмотреть SQL-код**, который будет сгенерирован и выполнен при применении определённой миграции. Это особенно полезно, если вы хотите:

- понять, какие **структурные изменения** будут внесены в базу;
- провести **аудит миграций** перед деплоем;
- получить SQL-запросы для ручного применения или изучения.

```bash
python manage.py sqlmigrate <app_label> <migration_name>
```

- `app_label` — имя приложения, например `users`;
- `migration_name` — имя миграции **без префикса `0XXX_`**, достаточно просто `0001` или `initial`.

#### Пример:

```bash
python manage.py sqlmigrate users 0001
```

Вывод будет содержать SQL-запросы, необходимые для создания таблиц и индексов, например:

```sql
CREATE TABLE "users_user" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "username" varchar(150) NOT NULL UNIQUE,
    "email" varchar(254) NOT NULL
);
```

> 🔍 **Совет:** Используйте `sqlmigrate`, чтобы убедиться, что миграции не создают неожиданных изменений, особенно если вы вносите правки вручную или используете `RunSQL`.

### squashmigrations

Команда `squashmigrations` используется для объединения нескольких последовательных миграций в одну, чтобы упростить структуру миграций и улучшить читаемость проекта.

Это особенно полезно после активной разработки, когда в приложении накопилось множество миграций, добавляющих поля, изменяющих типы или удаляющих элементы в одной и той же модели.

#### Синтаксис

```bash
python manage.py squashmigrations <app_label> <start_migration> <end_migration>
```

#### Пример

Допустим, в приложении `myapp` имеются миграции `0004`, `0005`, `0006` и `0007`, каждая из которых добавляет или изменяет поля в одной модели. Чтобы объединить их в одну миграцию, выполните:

```bash
python manage.py squashmigrations myapp 0004 0007
```

Это создаст новую миграцию, содержащую совокупность всех изменений между `0004` и `0007`, и заменит старые миграции.

> Совет: squash-команды следует выполнять **только после того**, как все предыдущие миграции были применены на всех окружениях, иначе возможны проблемы с синхронизацией структуры базы данных.

#### Когда применять squashmigrations

- После нескольких итераций разработки модели, когда накопилось много миграций.
- Перед выпуском в продакшн, чтобы упростить аудит миграций.
- Для улучшения производительности применения миграций при CI/CD.

#### Примечание

Squash не удаляет старые миграции автоматически — вы можете проверить и при необходимости удалить их вручную после тестирования новой объединённой миграции.


### flush

Команда `flush` очищает базу данных от всех данных пользователя, сбрасывая содержимое всех таблиц, **но не отменяя миграций и не удаляя структуру базы**.

Это значит, что после выполнения команды:

- Все таблицы останутся на месте.
- Все миграции будут считаться применёнными.
- Будут удалены все данные, включая созданных пользователей, записи моделей и данные сессий.
- Значения автоинкрементных полей (`id`) будут сброшены (если это поддерживает СУБД).

```bash
python manage.py flush
```

После выполнения вы получите предупреждение с подтверждением:

```bash
You have requested a flush of the database.
This will IRREVERSIBLY DESTROY all data in the database.
Are you sure you want to do this?
```

#### Применение:

- Для быстрого сброса данных при локальной разработке.
- При подготовке к демонстрации, когда нужна «чистая» база.
- Для очистки базы перед загрузкой фикстур:

```bash
python manage.py flush
python manage.py loaddata initial_data.json
```

> ⚠️ **Важно**: не используйте `flush` в продакшене — она удалит все данные и их восстановление будет невозможно без резервной копии.

### sqlflush

Команда `sqlflush` выводит SQL-инструкции, которые будут выполнены при вызове команды [`flush`](#flush).

Это полезно, если вы хотите:

- Предварительно увидеть, какие SQL-команды будут применены;
- Понять, какие таблицы будут очищены;
- Использовать SQL напрямую (например, для предварительного анализа или отладки).

#### Синтаксис

```
python manage.py sqlflush
```

#### Пример использования

```bash
$ python manage.py sqlflush
BEGIN;
DELETE FROM "myapp_modelname";
DELETE FROM "auth_user";
DELETE FROM "django_session";
...
COMMIT;
```

#### Примечания

- Команда **не выполняет очистку базы данных**, она **только печатает SQL**, который бы использовался.
- Учитывает текущую конфигурацию базы данных и зарегистрированные модели.


### sqlsequencereset

Команда `sqlsequencereset` используется для сброса последовательностей автогенерации идентификаторов (например, `id`) в базе данных. Это важно, когда вы вручную очищаете таблицы и хотите, чтобы следующая вставка начиналась с `id = 1`.

```bash
python manage.py sqlsequencereset <app_label>
```

- `<app_label>` — имя приложения Django, для которого нужно сбросить последовательности.

Например:

```bash
python manage.py sqlsequencereset blog
```

Эта команда не вносит изменений в базу напрямую, а просто **печатает SQL-код**, который необходимо выполнить для сброса последовательностей. Это особенно полезно при ручной очистке таблиц с помощью `flush` или `truncate`.

#### Почему это нужно?

Когда вы удаляете все записи из таблицы вручную (например, через `DELETE FROM`), следующий `id` по умолчанию не будет начинаться с 1, так как значение хранится в последовательности (sequence). `sqlsequencereset` позволяет сбросить эти sequence-объекты, чтобы обеспечить консистентность ID.

⚠️ **Важно:**
Не применяйте сброс последовательностей на продуктивной базе с пользовательскими данными. Это может привести к конфликтам ключей.

#### Пример вывода:

```sql
SELECT setval(pg_get_serial_sequence('"myapp_mymodel"', 'id'), COALESCE(MAX("id"), 1), max("id") IS NOT null) FROM "myapp_mymodel";
```

Этот SQL-запрос устанавливает значение последовательности `id` в зависимости от текущих данных в таблице.

### inspectdb

Команда `inspectdb` используется для генерации моделей Django на основе уже существующей базы данных.

Это особенно полезно, если вы начинаете работать над проектом с существующей схемой базы данных, которая ранее не использовалась с Django. Вместо того чтобы вручную описывать модели, вы можете сгенерировать их автоматически.

```bash
python manage.py inspectdb
```

Вывод будет содержать Python-код с определениями моделей, которые можно скопировать в файл `models.py` соответствующего приложения.

#### Пример использования

Предположим, у вас есть существующая база данных с таблицами `users` и `orders`. Выполнив команду:

```bash
python manage.py inspectdb > myapp/models.py
```

Вы получите файл `models.py` с автосгенерированными моделями:

```python
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    email = models.EmailField()

    class Meta:
        managed = False
        db_table = 'users'
```

#### Параметры

- `--database`: имя подключения к базе данных, если используется не дефолтное (`default`).
- `--include-partial`: добавляет частично поддерживаемые поля.
- `--table`: позволяет указать конкретные таблицы для генерации моделей.

Пример для одной таблицы:

```bash
python manage.py inspectdb --table users
```

#### Обратите внимание

- Генерируемые модели будут иметь `managed = False`, что означает, что Django не будет пытаться мигрировать эти таблицы.
- После генерации моделей их часто нужно вручную отредактировать: переименовать поля, добавить связи, ограничения и т. д.
- Это хороший старт, но не замена полноценного проектирования моделей вручную.

#### Когда использовать?

- При переносе существующего проекта (например, с PHP или Java) на Django.
- При необходимости подключиться к сторонней базе и использовать Django ORM без миграций.
- Для быстрого создания моделей для репорта или анализа на основе чужой БД.

## 🧠 **Управление пользователями**

### changepassword

Команда для смены пароля конкретному пользователю.

```manage.py changepassword ringo```

### createsuperuser

Команда для создания пользователя со всеми правами.


## 🌐 **Сервер и консоль**

### shell

Команда `shell` запускает интерактивную Python-консоль с уже настроенной Django-средой. Это означает, что вам не нужно вручную импортировать модели, настройки и другие компоненты проекта — всё уже доступно.

Примеры использования:
```bash
python manage.py shell
```

Полезно для:
- Ручного тестирования функций и моделей
- Временного взаимодействия с ORM
- Быстрого импорта и анализа данных

---

### dbshell

Команда `dbshell` открывает интерактивную консоль для работы с базой данных, указанной в настройках `DATABASES`.

Например, если вы используете PostgreSQL, будет открыт `psql`, если SQLite — обычная SQLite-консоль и т.д.

Примеры:
```bash
python manage.py dbshell
```

Полезно для:
- Прямого выполнения SQL-запросов
- Быстрого анализа или модификации данных на низком уровне
- Отладки проблем с миграциями и схемой

> Убедитесь, что нужный клиент базы данных установлен в системе (например, `psql` для PostgreSQL, `mysql` для MySQL).

---

### runserver

Команда `runserver` запускает встроенный отладочный сервер Django.

Пример:
```bash
python manage.py runserver
```

Можно указать IP и порт:
```bash
python manage.py runserver 0.0.0.0:8000
```

По умолчанию используется порт `8000` и адрес `127.0.0.1`.

Полезно для:
- Разработки и локального тестирования приложения
- Быстрой демонстрации функциональности

> ⚠️ **Важно:** `runserver` не предназначен для продакшена. На боевых серверах используйте WSGI-серверы, такие как Gunicorn, uWSGI, Daphne и т. п.

## 🗃 **Работа с данными (фикстуры)**

### dumpdata

Команда `dumpdata` используется для создания резервной копии данных из базы данных в виде JSON-файла (или в другом формате, если указать).

Это особенно полезно для:

- создания фикстур (fixtures), которые можно использовать для загрузки данных в тестовую или начальную среду;
- резервного копирования состояния отдельных приложений или моделей;
- миграции данных между проектами.

#### Синтаксис

```bash
python manage.py dumpdata [app_label.ModelName] [--indent N] [--output filename.json]
```

#### Примеры использования

- Сохранить все данные из базы:
  ```bash
  python manage.py dumpdata > all_data.json
  ```

- Сохранить данные только из приложения `blog`:
  ```bash
  python manage.py dumpdata blog > blog_data.json
  ```

- Сохранить данные из конкретной модели `Author`:
  ```bash
  python manage.py dumpdata blog.Author > authors.json
  ```

- Сохранять с отступами (удобнее для чтения):
  ```bash
  python manage.py dumpdata blog.Author --indent 2 > authors.json
  ```

- С указанием имени файла напрямую:
  ```bash
  python manage.py dumpdata blog --output blog_data.json
  ```

#### Подсказка

Вы можете комбинировать команды с `--exclude`:
```bash
python manage.py dumpdata --exclude auth.permission --exclude contenttypes > data.json
```

---

### loaddata

Команда `loaddata` загружает данные из JSON-файла (или другого формата фикстур) обратно в базу данных.

Это особенно полезно для:

- восстановления состояния базы из резервной копии;
- начального наполнения базы данных (например, при запуске нового окружения);
- использования в тестах.

#### Синтаксис

```bash
python manage.py loaddata filename.json
```

#### Примеры использования

- Загрузка полного дампа:
  ```bash
  python manage.py loaddata all_data.json
  ```

- Загрузка дампа только моделей `Author`:
  ```bash
  python manage.py loaddata authors.json
  ```

- Загрузка нескольких файлов:
  ```bash
  python manage.py loaddata file1.json file2.json
  ```

#### Подсказка

Фикстуры можно хранить в директориях `fixtures/` в каждом приложении — Django их найдёт автоматически.

---

> **Важно:** При загрузке данных из JSON-файла все `id`, указанные в файле, будут использоваться как есть. Убедитесь, что данные не конфликтуют с уже существующими.

## 📖 **Работа с переводами**

# Команды `makemessages` и `compilemessages` в Django

В Django команды `makemessages` и `compilemessages` используются для организации и управления локализацией (переводом интерфейса на разные языки).

## Команда `makemessages`

Команда `makemessages` используется для создания или обновления файлов перевода (`.po`), которые содержат строки, подлежащие переводу.

### Синтаксис

```bash
python manage.py makemessages -l <locale> [опции]
```

### Основные параметры

- `-l, --locale` — язык перевода (например, `fr`, `pt_BR`, `uk`).
- `--ignore` — шаблон файлов, которые нужно игнорировать.
- `--extension` — расширения файлов, где следует искать переводы (по умолчанию `.html`, `.txt`, `.py`).
- `--domain` — можно указать `djangojs` для перевода JS-файлов.

### Пример

```bash
python manage.py makemessages -l uk
```

Этот вызов создаст (или обновит) файл перевода `uk/LC_MESSAGES/django.po`.

### Где использовать `makemessages`

- В проектах с мультиязычным интерфейсом.
- При локализации текстов, сообщений и шаблонов.
- В любых Django-приложениях, где используется `gettext`, `ugettext`, либо шаблонные теги `{% trans "..." %}`.

### Пример строки перевода

В `views.py`:

```python
from django.utils.translation import gettext as _

def my_view(request):
    output = _("Welcome to my site.")
    return HttpResponse(output)
```

В `.po` файле:

```po
msgid "Welcome to my site."
msgstr "Ласкаво просимо на мій сайт."
```

---

## Команда `compilemessages`

После редактирования `.po` файлов необходимо скомпилировать их в `.mo` файлы, которые используются Django во время выполнения.

### Синтаксис

```bash
python manage.py compilemessages [опции]
```

### Пример

```bash
python manage.py compilemessages
```

Эта команда пройдёт по всем подкаталогам и скомпилирует `.po` файлы в `.mo` файлы.

### Когда использовать `compilemessages`

- После каждого изменения или добавления новых переводов.
- Перед сборкой и деплоем проекта, если используется мультиязычность.

---

## Итоговый сценарий работы с переводами

```bash
# Обнаружение строк для перевода
python manage.py makemessages -l fr

# Перевод строк вручную в файле locale/fr/LC_MESSAGES/django.po

# Компиляция перевода
python manage.py compilemessages
```

> **Важно:** Убедитесь, что в `settings.py` указана настройка `LOCALE_PATHS`, чтобы Django знал, где искать переводы:
>
> ```python
> LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]
> ```
## Написание собственных manage-команд в Django

В Django вы можете создавать собственные команды для `manage.py`, как и встроенные команды (`migrate`, `runserver`, `makemigrations` и т.д.). Это полезно для автоматизации задач: отчёты, массовые изменения в базе, уведомления и др.

### Пример: автоматическое закрытие заказов в пиццерии

Предположим, у нас есть проект пиццерии, и мы хотим, чтобы каждый день в 18:00 система проверяла заказы, которые остались в статусе «открыт», переводила их в статус «manual» и отправляла уведомление владельцу заведения.

### Шаг 1: структура проекта

Создаём команду `close_orders` внутри приложения `orders`:

```
orders/
├── __init__.py
├── models.py
├── management/
│   └── commands/
│       └── close_orders.py
├── tests.py
└── views.py
```

> Папки `management` и `commands` должны быть именно с такими названиями.

### Шаг 2: Реализация команды

```python
from django.core.management.base import BaseCommand
from orders.models import Order
from orders.utils import send_email  # примерная утилита отправки писем

class Command(BaseCommand):
    help = "Close orders which weren't closed manually"

    def handle(self, *args, **options):
        orders = Order.objects.filter(status="opened")
        if orders.exists():
            orders.update(status="manual")
            send_email(
                subject="Unclosed orders",
                message=f"You have {orders.count()} unclosed orders marked as 'manual'.",
                to="owner@example.com"
            )
            self.stdout.write(self.style.SUCCESS("Successfully closed open orders."))
        else:
            self.stdout.write("No open orders to close.")
```

### Шаг 3: Запуск команды

Запустить команду можно вручную:

```bash
python manage.py close_orders
```

### Шаг 4: Автоматизация через CRON (Linux)

Добавьте в расписание `cron` выполнение этой команды каждый день в 18:00:

```cron
0 18 * * 1-5 /usr/bin/python3 /path/to/project/manage.py close_orders
```

> Убедитесь, что активировано правильное виртуальное окружение, или используйте путь до интерпретатора прямо из него.

---

Создание кастомных `manage.py` команд — мощный способ автоматизировать задачи и расширить функциональность вашего проекта.

---

## 📋 Итоги лекции

В этой лекции мы изучили инструменты Django для наблюдаемости, обработки запросов и автоматизации:

| Инструмент           | Назначение                                   | Когда использовать                          |
|----------------------|----------------------------------------------|---------------------------------------------|
| **Logging**          | Запись информации о работе приложения        | Отладка, мониторинг, аудит                  |
| **Middleware**       | Сквозная обработка request/response          | Аутентификация, timing, CORS, rate limiting |
| **Signals**          | Реакция на события без изменения кода модели | Уведомления, аудит, инвалидация кеша        |
| **Background Tasks** | Выполнение кода вне цикла запроса            | Email, обработка файлов, внешние API        |
| **Messages**         | Одноразовые уведомления пользователю         | Flash-сообщения после redirect              |
| **Manage-команды**   | Скрипты для автоматизации                    | Cron-задачи, импорт данных, обслуживание    |

### Ключевые правила:

1. **Логирование** — используйте JSON-формат в production, интегрируйте с Sentry/ELK
2. **Middleware** — порядок важен! Не размещайте тяжёлую логику
3. **Signals** — используйте `dispatch_uid`, выносите тяжёлые операции в очереди
4. **Background Tasks** — передавайте ID объектов, не сами объекты; используйте `transaction.on_commit`
5. **Messages** — не забывайте про `MessageMiddleware` и context processor
6. **Data Migrations** — используйте `RunPython.noop` для обратных миграций

---

## 📝 Домашнее задание

### Уровень 1: Базовый

1. **Настройте логирование** в вашем проекте:
   - Создайте отдельный логгер для вашего приложения
   - Настройте вывод в файл с форматом `verbose`
   - Добавьте логирование в одну из view (начало обработки, результат, ошибки)

2. **Создайте middleware** для логирования времени выполнения запросов:
   - Логируйте метод, путь и время в миллисекундах
   - Добавьте заголовок `X-Request-Duration` в ответ

3. **Добавьте flash-сообщения** в форму регистрации или создания объекта:
   - `messages.success` при успешном создании
   - `messages.error` при ошибке валидации

### Уровень 2: Продвинутый

4. **Создайте сигнал** для аудита изменений модели:
   - При сохранении объекта логируйте, кто и что изменил
   - Используйте `dispatch_uid`
   - Зарегистрируйте сигнал в `apps.py`

5. **Напишите manage-команду** для вашего проекта:
   - Команда должна принимать аргументы (например, `--days=7`)
   - Выводите результат с использованием `self.style.SUCCESS/ERROR`
   - Пример: очистка старых записей, генерация отчёта, отправка напоминаний

6. **Создайте Data Migration**:
   - Добавьте начальные данные для справочника (категории, статусы, роли)
   - Используйте `RunPython.noop` для обратной миграции

### Уровень 3: Экспертный

7. **Реализуйте Request ID middleware**:
   - Генерируйте UUID для каждого запроса
   - Добавляйте его в логи через `logging.Filter`
   - Возвращайте в заголовке ответа

8. **Интегрируйте сигналы с Background Tasks** (Django 6.0+):
   - При создании заказа ставьте задачу отправки email в очередь
   - Используйте `transaction.on_commit`

---

## ❓ Вопросы для самопроверки

1. В каком порядке вызываются middleware при обработке запроса и ответа?

2. Почему сигналы не вызываются при использовании `QuerySet.update()`?

3. Чем `RunPython.noop` лучше `lambda x, y: None`?

4. Когда лучше использовать переопределение `save()` вместо сигнала `post_save`?

5. Почему важно использовать `transaction.on_commit` при постановке задач в очередь?

6. Какой backend для Background Tasks использовать в production?

7. Где правильно регистрировать сигналы и почему?

8. Как добавить контекст (user_id, request_id) ко всем логам в рамках одного запроса?

---

[← Лекция 25: NoSQL. Куки, сессии, кеш](lesson25.md) | [Лекция 27: Что такое API. REST и RESTful. Django REST Framework. →](lesson27.md)