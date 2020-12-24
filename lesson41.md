# Урок 41. Celery

![](https://i.kym-cdn.com/entries/icons/original/000/022/857/Screen_Shot_2017-05-01_at_12.53.31_PM.png)

## Что это вообще такое?

Celery – это система для управления очередями задач. Принципиально умеет 2 вещи: брать задачи из очереди и выполнять задачи по расписанию.

#### Воркер

В нашем понимании воркер это отдельно запущенный скрипт (процесс) для выполнения определённых задач, селери запускается на одном или нескольких воркерах, что бы выполнять задачи паралельно на каждом воркере.

#### Брокер

Брокер сообщений (он же диспетчер очереди) — это штука, которая принимает и отдает сообщения между отдельными модулями/приложениями внутри некоторой сложной системы, где модули/приложения должны общаться между собой — то есть пересылать данные друг другу.

В нашем случае сообщением будет любая задача (кусок кода).

#### Очередь задач

Очереди задач используются как механизм для распределения работы по потокам или машинам (в нашем случае по воркерам).

В очередь задач, в любой момент мы можем добавить задачу. Воркеры постоянно отслеживают очередь задач и выполняют если появляются новые. 

Селери общается с помощью сообщений, обычно используя брокера для посредничества между клиентами и воркерами. Чтобы инициировать задачу, клиент добавляет сообщение в очередь, а затем брокер доставляет это сообщение воркеру.

Система Celery может состоять из нескольких воркеров и брокеров.

Celery написан на Python, но протокол может быть реализован на любом языке. В дополнение к Python есть node-celery и node-celery-ts для Node.js и клиент PHP.

Селери требуется "транспорт" (брокер) для отправки и получения сообщений. Чаще всего используются брокеры RabbitMQ и Redis, они являются полнофункциональными, но есть также поддержка множества других экспериментальных решений, включая использование SQLite для локальной разработки.

Celery может работать на одной машине, на нескольких машинах или даже в центрах обработки данных.

### RabbitMQ и Redis

#### RabbitMQ

RabbitMQ ‒ это брокер сообщений. Его основная цель ‒ принимать и отдавать сообщения. Его можно представлять себе, как почтовое отделение: когда Вы бросаете письмо в ящик, Вы можете быть уверены, что рано или поздно почтальон доставит его адресату. В этой аналогии RabbitMQ является одновременно и почтовым ящиком, и почтовым отделением, и почтальоном.

#### Redis

Redis – это высокопроизводительная БД с открытым исходным кодом (лицензия BSD), которая хранит данные в памяти, доступ к которым осуществляется по ключу доступа. Так же Редис это кэш и брокер сообщений.

Redis это `NoSQL` база данных! Для Celery крайне рекомендую использовать именно его.

## Celery вне Django

Для установки используем `pip`:

```
pip install celery
```

Создадим файл `tasks.py`

для использования, необходимо создать "приложение", в котором необходимо указать название (понадобится для указания брокеру) и брокера.

```python
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y
```

Мы описали задачу, и обозначили её через декоратор приложения селери.

Мы не вызывали задачу!!

Для того, что бы мы могли вызвать задачу, необходимо запустить селери как отдельное приложение:

```
celery -A tasks worker --loglevel=INFO
```

консольная команда будет доступна после установки celery

`-A app_name` - указать имя приложения, `worker` - запустить один воркер, лог левел, уровень подробностей.

### Запуск и обработка результата

Для запуска задач, есть много разных способов, тут рассмотрим базовый.

```
from tasks import add
add.delay(4, 4)
``` 

Для запуска задачи немедленно, используется метод `delay`.

Запуск задач возвращает не результат, а `AsyncResult`, для того что бы получать значения необходимо при создании приложения указать парамет `backend` который отвечает за место хранения результатов, таким параметром может быть Redis:

```python
app = Celery('tasks', backend='redis://localhost', broker='pyamqp://')
```

Результат будет иметь достаточно большое кол-во методов и атрибутов.

Основные два метода это `ready` и `get`

`ready` - булевое поле которое отвечает за то завершилась задача или еще в процессе.

`get` - ждет выполнения задачи и возвращает результат. Рекомендуется использовать после `ready`, что бы не ждать выполнения впустую.

```python
result = add.delay(4, 4)
result.ready()
result.get()
```

Иногда описание парметров задачи и ей вызов могут быть в совершенно разных местах, для этого существует механизм подписи:

```python
s1 = add.s(2, 2)
res = s1.delay()
res.get()
```

в этом примере `s1` это подпись задачи, тоесть здача заготовленная для выполнения, её можно сериализовать и отправить по сети, например, а выполнить в уже совершенно других местах.

Или если вы не знаете параметры целиком:

```python
# incomplete partial: add(?, 2)
s2 = add.s(2)
# resolves the partial: add(8, 2)
res = s2.delay(8)
res.get()
```

Задачи можно группировать:

```python
from celery import group
from proj.tasks import add

group(add.s(i, i) for i in range(10))().get()
```

### Виды запуска

Есть три варианта запуска тасков:
```
apply_async(args[, kwargs[, …]])
```
Отправка сообщения с указанием дополнительных параметров

```
delay(*args, **kwargs)
```
Отправка сообщения без каких либо параметров самого сообщения

```
calling (__call__)
```
Просто вызов, декоратор не мешает нам просто вызвать функцию без селери :) 


### Основные параметры apply_async()

1. сountdown - отправить через

```python
add.apply_async((2,2), countdown=10)
# отправить через 10 секунд
```

2. eta - отправить в конкретное время

```python
add.apply_async((2,2), eta=now() + timedelta(seconds=10))
# отправить через 10 секунд
```

3. expires - время после которого перестать выполнять задачу, можно указать как цифру так и время

```python
add.apply_async((4,5), countdown=60, expires=120)
add.apply_async((4,5), expires=now() + timedelta(days=2))
```

4. link - выполнить другую задачу по звершению текущей, основываясь на результатах текущей

```python
add.apply_async((2, 2), link=add.s(16))
# ( 2 + 2 ) + 16
```

### Переодические задачи

Селери может выполнять какие-либо задачи просто по графику

Для этого нужно настроить приложение:

```python
app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}
app.conf.timezone = 'UTC'

```

Ключ словаря, это только название, можно указать что угодно.

Таск это выполняемый таск :)

`args` его аргументы

`schedule`: частота выполнения в секундах

### выполнение по крону

```python
from celery.schedules import crontab

app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-monday-morning': {
        'task': 'tasks.add',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (16, 16),
    },
}
```

Cron - система задания расписания, можно сделать практически какое угодно.

### по действиям солнца

```
from celery.schedules import solar

app.conf.beat_schedule = {
    # Executes at sunset in Melbourne
    'add-at-melbourne-sunset': {
        'task': 'tasks.add',
        'schedule': solar('sunset', -37.81753, 144.96715),
        'args': (16, 16),
    },
```

В данном случае выполнять во время восхода, по указанным координатам, параметром много включая закат с учётом зданий ;)

Для расписания нужно запускать отдельный воркер для расписания (смотреть в доке) 

### Celery и Django

Для использования селери в django рекомендуется создать еще один файл `celery.py` на одном уровне с `settings.py`

```python
import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
```

Параметр `namespace` при указании конфига будет отвечать за то с какого слова будут начинатся настройки в `settings.py`

Например:

```python
# Celery Configuration Options
CELERY_TIMEZONE = "Australia/Tasmania"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
```


`app.autodiscover_tasks()` - эта строчка будет отвечать за автоматический поиск таков во всех приложениях.

На тоже же уровне где и `settings.py` создать\использовать файл `__init__.py` в зависимости от версии python

```python
# __init__.py
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ('celery_app',)
```

Все задачи необходимо покрывать не стандартным декоратором `task`, а декоратором `shared_task` тогда django сможет автоматически найти все таски в приложении.

```python
# tasks.py

from celery import shared_task
from demoapp.models import Widget


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_widgets():
    return Widget.objects.count()


@shared_task
def rename_widget(widget_id, name):
    w = Widget.objects.get(id=widget_id)
    w.name = name
    w.save()
```

Так же для Django существует много различных расширений, например: 

`django-celery-results` - что бы хранить резльутаты в бд или кеше джанго, за подробностями в доку.

`django-celery-beat` - настройка для переодических задач, сразу вшитая в админку джаго, за подробностями опять же в доку.
