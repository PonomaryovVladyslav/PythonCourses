# Лекция 33. Сокеты. Django channels.

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
  - [Лекция 32. Asyncio. Aiohttp. Асинхронное программирование на практике.](lesson32.md)
  - ▶ **Лекция 33. Сокеты. Django channels**
</details>

<details>
  <summary>Блок 8 — Deployment (34–35)</summary>

  - [Лекция 34. Linux. Все что нужно знать для деплоймента.](lesson34.md)
  - [Лекция 35. Deployment](lesson35.md)
</details>

- [Лекция 36. Методологии разработки. CI/CD. Монолит и микросервисы. Docker](lesson36.md)

![](https://media1.giphy.com/media/v1.Y2lkPTZjMDliOTUybzBodTR3NTVqbjBuZjk0Z3A5NTFsb200dWtvYm1qYmNocnN5NnFlbyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/9r75ILTJtiDACKOKoY/200w.gif)

## Протокол

### Реализация чата

Допустим вы хотите реализовать на своём сайте чат. Вы знаете протокол HTTP, который подразумевает систему запрос-ответ.

Но что делать, если вам необходимо обновить информацию у клиента, хотя он её не запрашивал (вам пишут сообщение, но вы не
знаете, когда именно оно будет написано)?

Какие существуют варианты решения этой проблемы?

#### Множество запросов

Мы можем делать большое количество запросов в надежде, что уже кто-то прислал нам сообщение

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson44/lots_requests.png)

Чем плох такой подход?

Мы отправляем огромное количество запросов в «пустоту», расходуя ресурсы и выполняя ненужные запросы.

#### Длинное соединение (long polling)

Мы можем отдавать ответ только когда сообщение пришло.

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson44/long_polling.png)

Как это реализовать? Например, в коде можно использовать вечный цикл и опрос какого-либо хранилища, например `redis`.
Если данные появились — отдавать ответ.

Чем плох такой подход?

«Пустые» HTTP-запросы заменяются на «пустые» запросы к хранилищу данных, что ничем особо не лучше — мы всё ещё тратим
большое количество ресурсов. Большинство серверов и браузеров имеют ограничение на время запроса, что тоже является
проблемой для такого подхода.

#### Сокеты

Сокет — это специальный вид соединения поверх HTTP для создания постоянного соединения.

Как это работает?

![](https://www.pubnub.com/wp-content/uploads/2013/09/WebSockets2.png)

Клиент отправляет запрос на соединение с сокетом сервера.

Сервер принимает это соединение.

Клиент шлёт сообщение серверу.

Сервер рассылает это сообщение другим клиентам.

В любой момент обе стороны могут разорвать соединение, если это необходимо.

Запросы для сокетов проходят по протоколу WebSocket и выполняются на адреса, которые начинаются с `ws://`, а
не `http://`

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson44/socket.png)

### Сфера применения

Где стоит применять веб-сокеты? Основные сферы применения:

- Чаты

- Приложения реального времени (например, отображение курса валют, стоимости криптовалют и т. д.)

- IoT-приложения (IoT — Internet of Things, интернет вещей, любые смарт-предметы: смарт-чайники, телевизоры, датчики
  дыма, кофемашины и т. д.)

- Онлайн игры

Но если необходимо, то можно применять где угодно.

## Django channels

Естественно, для Python существует готовый пакет для поддержки этого протокола с поддержкой Django

[Дока](https://channels.readthedocs.io/en/stable/)

Устанавливается через `pip`

```pip install "channels[daphne]"```

### Туториал

Давайте напишем простой чат при помощи Django

Создаём виртуальное окружение, устанавливаем Django и Channels, создаём Django-проект

```django-admin startproject chatsite```

Получим такую структуру:

```
chatsite/
    manage.py
    chatsite/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
```

В современных версиях Django `asgi.py` создаётся автоматически (Django 3.0+). Если у вас очень старая версия, файл можно
создать вручную.

Файлы `wsgi.py` и `asgi.py` необходимы для запуска серверов: `wsgi` — для синхронных, `asgi` — для асинхронных. WebSocket —
асинхронная технология.

Создадим приложение для чата

```python3 manage.py startapp chat```

Получим примерно такую структуру файлов:

```
chat/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

Для простоты предлагаю удалить всё, кроме `views.py` и `__init__.py`, и создать папку `templates`:

Полученная структура:

```
chat/
    __init__.py
    templates/
    views.py
```

Добавляем наше приложение в `INSTALLED_APPS` в `settings.py`

```
# chatsite/settings.py
INSTALLED_APPS = [
    'chat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Создадим папку `templates` и добавим её в `settings.py`

Создадим файл `index.html` в папке `templates`:

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>Chat Rooms</title>
</head>
<body>
What chat room would you like to enter?<br>
<input id="room-name-input" type="text" size="100"><br>
<input id="room-name-submit" type="button" value="Enter">

<script>
    document.querySelector('#room-name-input').focus();
    document.querySelector('#room-name-input').onkeyup = function (e) {
        if (e.keyCode === 13) {  // enter, return
            document.querySelector('#room-name-submit').click();
        }
    };

    document.querySelector('#room-name-submit').onclick = function (e) {
        var roomName = document.querySelector('#room-name-input').value;
        window.location.pathname = '/chat/' + roomName + '/';
    };
</script>
</body>
</html>
```

Что будет на этой странице?

Поле для ввода и кнопка войти. Это будет возможность зайти в конкретный чат, по его названию.

Что делает JS?

При заходе на страницу сразу выделяет поле для ввода имени чата.

Если на инпуте нажимается Enter на клавиатуре, то имитируем нажатие на кнопку входа.

При нажатии на кнопку входа берём значение из инпута и переходим на страницу `/chat/<значение инпута>/` — этой страницы
пока не существует.

Создадим view для этой страницы.

```python
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'index.html'
```

Создадим файл с урлами внутри приложения:

```
chat/
    __init__.py
    urls.py
    views.py
```

```python
# chat/urls.py
from django.urls import path

from chat.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]
```

А в основных урлах

```
# chatsite/urls.py
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('chat/', include('chat.urls')),
]
```

Теперь, если мы запустим сервер, то увидим в консоли что-то такое:

```
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
January 11, 2026 - 10:30:00
Django version 5.1, using settings 'chatsite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

А если зайти на страницу http://127.0.0.1:8000/chat/ то будет вот так:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson44/chat_enter.png)

Попытка перейти на любую страницу ни к чему не приведёт, страницы комнаты пока просто нет :)

### Настройка Channels

Для настройки необходимо изменить файл `asgi.py`; если его нет, то создать его.

```python
# chatsite/asgi.py
import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatsite.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)
})
```

Что мы сделали? Мы сказали нашему приложению, что планируем разные протоколы обрабатывать по-разному. В данный
момент мы указали только протокол `http`, а значит, фактически пока что ничего не изменится

Добавляем приложение в `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'daphne',
    'chat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

И добавляем настройку, чтобы указать, что основной сервер — `asgi.py`

```python
# mysite/settings.py
# Channels
ASGI_APPLICATION = 'chatsite.asgi.application'
```

Теперь при запуске приложения вы должны увидеть немного другую надпись.

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
January 11, 2026 - 10:35:00
Django version 5.1, using settings 'chatsite.settings'
Starting ASGI/Daphne version 4.1.0 development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Обратите внимание на предпоследнюю строку: теперь сервер запущен с поддержкой веб-сокетов.

### Создаём страницу с конкретным чатом

Создадим html файл `room.html` в папке `chat/templates/`:

```html
<!-- chat/templates/room.html -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>Chat Room</title>
</head>
<body>
<textarea id="chat-log" cols="100" rows="20"></textarea><br>
<input id="chat-message-input" type="text" size="100"><br>
<input id="chat-message-submit" type="button" value="Send">
{{ room_name|json_script:"room-name" }}
<script>
    const roomName = JSON.parse(document.getElementById('room-name').textContent);

    const chatSocket = new WebSocket(
            (window.location.protocol === 'https:' ? 'wss' : 'ws') + '://' +
            window.location.host +
            '/ws/chat/' + roomName + '/'
    );

    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        document.querySelector('#chat-log').value += (data.message + '\n');
    };

    chatSocket.onclose = function (e) {
        console.error('Chat socket closed unexpectedly');
    };

    document.querySelector('#chat-message-input').focus();
    document.querySelector('#chat-message-input').onkeyup = function (e) {
        if (e.keyCode === 13) {  // enter, return
            document.querySelector('#chat-message-submit').click();
        }
    };

    document.querySelector('#chat-message-submit').onclick = function (e) {
        const messageInputDom = document.querySelector('#chat-message-input');
        const message = messageInputDom.value;
        chatSocket.send(JSON.stringify({
            'message': message
        }));
        messageInputDom.value = '';
    };
</script>
</body>
</html>
```

Что происходит на этой странице?

Текстовое поле для отображения записей в чате. Поле для ввода нового сообщения. Кнопка для отправки.

```{{ room_name|json_script:"room-name" }}```

Фильтр `json_script` добавит на страницу тег `<script>` с данными из переменной. Если открыть комнату с названием `test`, то
отрендеренная страница будет выглядеть так:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson44/room_script.png)

Нужно для того, чтобы считать переменную через JS.

Что происходит в JS?

В первой строке мы считываем из переменной имя комнаты.

И создаём соединение с веб-сокетом по адресу (`ws://127.0.0.1:8000/ws/chat/<имя чата>/`), мы создадим серверную часть
дальше. Обратите внимание: используется другой протокол, не `http`. При создании такого объекта запрос на соединение
отправляется автоматически.

Если по этому сокету приходит сообщение, мы добавляем его к нашему месту для текста

```js
chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    document.querySelector('#chat-log').value += (data.message + '\n');
};
```

Если соединение было разорвано — выводим в консоль ошибку

```js
chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
};
```

В случае отправки сообщения — отправляем его по сокету.

```js
document.querySelector('#chat-message-submit').onclick = function (e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
};
```

И создать view. Обратите внимание: нужно передать `room_name` в контекст шаблона:

```python
# chat/views.py
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'index.html'


class Room(TemplateView):
    template_name = 'room.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room_name'] = self.kwargs['room_name']
        return context
```

`urls.py`:

```python
# chat/urls.py
from django.urls import path

from chat.views import Index, Room

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<str:room_name>/', Room.as_view(), name='room'),
]
```

Запускаем сервер, заходим в любую комнату, пишем любое сообщение — и видим ошибку.

```WebSocket connection to 'ws://127.0.0.1:8000/ws/chat/lobby/' failed: Unexpected response code: 500```

Мы не создали бэкенд для сокета. Давайте сделаем это.

### Бэкенд сокета

Создадим новый файл `chat/consumers.py`

```
    __init__.py
    consumers.py
    urls.py
    views.py
```

```python
# chat/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
```

Что это такое? Это класс для работы с веб-сокетом.

Методы:

- `connect` — что делать при запросе на соединение.

- `disconnect` — что делать при разрыве соединения.

- `receive` — что делать при получении сообщения.

- `send` — отправить сообщение текущему клиентскому соединению. Для широковещательной отправки используйте `group_send` (через channel layer).

Создаём новый файл для урлов веб-сокета `routing.py`.

```
chat/
    __init__.py
    consumers.py
    routing.py
    urls.py
    views.py
```

```python
# chat/routing.py
from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r"^ws/chat/(?P<room_name>[\w-]+)/$", ChatConsumer.as_asgi()),
]
```

Обратите внимание: к классу был применён метод `as_asgi` — это аналог `as_view` для обычных классов.

Укажем эту переменную в нашем `asgi.py`:

```python
# chatsite/asgi.py
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatsite.settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

from chat.routing import websocket_urlpatterns

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ),
    }
)
```

Обратите внимание, мы добавили новый протокол для обработки.
**Примечание:** если используете `AllowedHostsOriginValidator`, убедитесь, что в `settings.py` добавлены `ALLOWED_HOSTS = ['127.0.0.1', 'localhost']` (для dev), иначе WebSocket-подключение может отклоняться.


Для того чтобы сокет работал, необходимы сессии, а для этого необходимо провести миграции.

```python manage.py migrate```

Проверяем — это уже будет работать.

**В данный момент работать будет только один чат, причем только сам с собой!!!**

Мы не добавили возможность создавать разные сокеты, для разных страниц. Для этого необходимо разделить данные по слоям.

### Подключаем channels

Для того чтобы использовать различные непересекающиеся чаты, мы будем использовать `group`. `group` — это
набор `channel`.

Для использования необходимо какое-либо внешнее хранилище. Мы будем использовать Redis.

Для этого необходимо установить ещё один внешний модуль для взаимодействия между нашими слоями и Redis.

```pip install channels_redis```

### Для пользователей Windows

На Windows обычный Redis не будет работать с последними версиями django-channels.

Необходимо установить [это](https://www.memurai.com/get-memurai) и запустить в консоли после:

```memurai```

Это аналог Redis, который будет работать.

### Обновление settings

Необходимо обновить настройки и указать, что мы будем использовать Redis:

```python
# chatsite/settings.py
# Channels
ASGI_APPLICATION = 'chatsite.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
```

Для проверки работы Redis необходимо открыть `shell`:

```bash
python manage.py shell
```

```python
import channels.layers
from asgiref.sync import async_to_sync

channel_layer = channels.layers.get_channel_layer()

# Отправляем сообщение в канал
async_to_sync(channel_layer.send)('test_channel', {'type': 'hello'})

# Получаем сообщение из канала
async_to_sync(channel_layer.receive)('test_channel')
# Output: {'type': 'hello'}
```

Напоминаю: изначально WebSocket — это асинхронная технология. Для использования её синхронно мы используем
встроенный метод `async_to_sync`.

В тесте мы отправили сообщение и получили его.

Теперь можно обновить `consumers.py`:

```python
# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
```

Методы:

`connect` — добавили создание группы исходя из названия чата, а также вызвали метод `accept`

`disconnect` — удаляем группу при разрыве соединения

`receive` — при получении сообщения мы выполняем для всей группы метод `chat_message` (могли назвать абсолютно как
угодно)

`chat_message` — отправка сообщения

Можем проверять. Открываем одинаковые названия чата в разных браузерах и пишем по сообщению с каждого

## Запускаем всё асинхронно

Допустим, мы хотим отправить другу большой файл, но хотим писать сообщения, пока файл загружается. В случае
использования синхронного подхода это невозможно; при асинхронном — это будет работать.

Перепишем `consumers.py`

```python
# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
```

Что мы изменили? Мы наследовались не от `WebsocketConsumer`, а от `AsyncWebsocketConsumer`, заменили все функции с
обычных на асинхронные и вызовы функций — с обычных на асинхронные.

Всё — ваш чат полностью асинхронен.

### Тестирование

Для тестирования веб-сокетов используются специфические acceptance (приёмочные) тесты.

> Для этих тестов необходимо предварительно установить Google Chrome, chromedriver и Selenium. Только Selenium
> устанавливается через `pip`

```
pip install selenium
```

Создадим файл `chat/tests.py`

Текущая структура файлов:

```
chat/
    __init__.py
    consumers.py
    routing.py
    templates/
        index.html
        room.html
    tests.py
    urls.py
    views.py
```

Содержимое файла:

```python
# chat/tests.py
from channels.testing import ChannelsLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class ChatTests(ChannelsLiveServerTestCase):
    serve_static = True  # emulate StaticLiveServerTestCase

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        try:
            # NOTE: Requires "chromedriver" binary to be installed in $PATH
            cls.driver = webdriver.Chrome()
        except:
            super().tearDownClass()
            raise

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_when_chat_message_posted_then_seen_by_everyone_in_same_room(self):
        try:
            self._enter_chat_room("room_1")

            self._open_new_window()
            self._enter_chat_room("room_1")

            self._switch_to_window(0)
            self._post_message("hello")
            WebDriverWait(self.driver, 2).until(
                lambda _: "hello" in self._chat_log_value,
                "Message was not received by window 1 from window 1",
            )
            self._switch_to_window(1)
            WebDriverWait(self.driver, 2).until(
                lambda _: "hello" in self._chat_log_value,
                "Message was not received by window 2 from window 1",
            )
        finally:
            self._close_all_new_windows()

    def test_when_chat_message_posted_then_not_seen_by_anyone_in_different_room(self):
        try:
            self._enter_chat_room("room_1")

            self._open_new_window()
            self._enter_chat_room("room_2")

            self._switch_to_window(0)
            self._post_message("hello")
            WebDriverWait(self.driver, 2).until(
                lambda _: "hello" in self._chat_log_value,
                "Message was not received by window 1 from window 1",
            )

            self._switch_to_window(1)
            self._post_message("world")
            WebDriverWait(self.driver, 2).until(
                lambda _: "world" in self._chat_log_value,
                "Message was not received by window 2 from window 2",
            )
            self.assertTrue(
                "hello" not in self._chat_log_value,
                "Message was improperly received by window 2 from window 1",
            )
        finally:
            self._close_all_new_windows()

    # === Utility ===

    def _enter_chat_room(self, room_name):
        self.driver.get(self.live_server_url + "/chat/")
        ActionChains(self.driver).send_keys(room_name, Keys.ENTER).perform()
        WebDriverWait(self.driver, 2).until(
            lambda _: room_name in self.driver.current_url
        )

    def _open_new_window(self):
        self.driver.execute_script('window.open("about:blank", "_blank");')
        self._switch_to_window(-1)

    def _close_all_new_windows(self):
        while len(self.driver.window_handles) > 1:
            self._switch_to_window(-1)
            self.driver.execute_script("window.close();")
        if len(self.driver.window_handles) == 1:
            self._switch_to_window(0)

    def _switch_to_window(self, window_index):
        self.driver.switch_to.window(self.driver.window_handles[window_index])

    def _post_message(self, message):
        ActionChains(self.driver).send_keys(message, Keys.ENTER).perform()

    @property
    def _chat_log_value(self):
        return self.driver.find_element(
            by=By.CSS_SELECTOR, value="#chat-log"
        ).get_property("value")
```

> Для тестов должна быть указана дополнительная настройка для базы данных!

```python
# mysite/settings.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "TEST": {
            "NAME": BASE_DIR / "db.sqlite3",
        },
    }
}
```

Запускаем и наслаждаемся

```
python3 manage.py test chat.tests
```

### pytest-django: live_server (пример e2e)

Для pytest можно написать аналогичный end-to-end тест, используя фикстуру live_server из pytest-django.

```bash
pip install pytest pytest-django selenium
```

Пример фикстуры браузера (Chrome в headless-режиме) в conftest.py:

```python
# conftest.py
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(scope="session")
def chrome_driver():
    opts = ChromeOptions()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    driver = Chrome(options=opts)
    try:
        yield driver
    finally:
        driver.quit()
```

Тест с использованием live_server:

```python
# tests/test_chat_live.py
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


def test_chat_room_e2e(live_server, chrome_driver):
    driver = chrome_driver

    # Открываем форму выбора комнаты
    driver.get(f"{live_server.url}/chat/")

    # Вводим имя комнаты и заходим
    ActionChains(driver).send_keys("room_pytest", Keys.ENTER).perform()
    WebDriverWait(driver, 3).until(lambda d: "room_pytest" in d.current_url)

    # Отправляем сообщение Enter'ом
    ActionChains(driver).send_keys("hello from pytest", Keys.ENTER).perform()

    # Проверяем, что сообщение появилось в логах
    def _has_message(d):
        val = d.find_element(By.CSS_SELECTOR, "#chat-log").get_property("value")
        return "hello from pytest" in val

    WebDriverWait(driver, 3).until(_has_message)
```

Запуск:

```bash
pytest -q -k chat_live
```

> **Примечание:** Для pytest-django необходимо создать файл `pytest.ini` или добавить секцию в `pyproject.toml`:
> ```ini
> # pytest.ini
> [pytest]
> DJANGO_SETTINGS_MODULE = chatsite.settings
> ```

## Дополнительные темы

### Аутентификация в WebSocket

В `scope` доступен объект `user`, если используется `AuthMiddlewareStack`:

```python
# chat/consumers.py
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]

        if self.user.is_anonymous:
            # Отклоняем неаутентифицированных пользователей
            await self.close()
            return

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
```

### Альтернативы Django Channels

- **Socket.IO** (с python-socketio) — популярная библиотека с автоматическим fallback на long-polling
- **Starlette WebSockets** — если используете FastAPI/Starlette
- **websockets** — низкоуровневая asyncio библиотека для WebSocket

### Полезные ссылки

- [Django Channels Documentation](https://channels.readthedocs.io/en/stable/)
- [channels_redis Documentation](https://github.com/django/channels_redis)
- [Daphne Documentation](https://github.com/django/daphne)

---

[← Лекция 32: Asyncio. Aiohttp. Асинхронное программирование на практике.](lesson32.md) | [Лекция 34: Linux. Все что нужно знать для деплоймента. →](lesson34.md)
