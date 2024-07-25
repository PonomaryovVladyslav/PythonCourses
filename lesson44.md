# Лекция 44. Сокеты. Django channels.

![](https://www.imaginarycloud.com/blog/content/images/2016/03/gifmachine-2.gif)

## Протокол

### Реализация чата

Допустим вы хотите реализовать на своём сайте чат. Вы знаете протокол HTTP, который подразумевает систему запрос-ответ.

Но что делать если вам необходимо обновить информацию у клиента, хотя он её не запрашивал (Вам пишут сообщение, но вы не
знаете когда именно оно будет написано)

Какие существуют варианты решения этой проблемы?

#### Множество запросов

Мы можем делать большое кол-во запросов в надежде, что уже кто-то прислал нам сообщение

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson44/lots_requests.png)

Чем плох такой подход?

Мы отправляем огромное кол-во запросов в "пустоту", расходуя ресурсы и выполняя не нужные запросы.

#### Длинное соединение (long polling)

Мы можем отдавать ответ только когда сообщение пришло.

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson44/long_polling.png)

Как это реализовать? Например, в коде можно использовать вечный цикл, и опрос какого либо хранилища, например `redis`.
Если данные появились, отдавать ответ.

Чем плох такой подход?

"Пустые" HTTP запросы заменяются на "пустые" запросы к хранилищу данных, что ничем особо не лучше, мы всё еще тратим
большое кол-во ресурсов. Большинство серверов и браузеров имеют ограничение на время запроса, что тоже является
проблемой для такого подхода.

#### Сокеты

Сокет это специальный вид соединения поверх HTTP, для создания постоянного соединения.

Как это работает?

![](https://www.pubnub.com/wp-content/uploads/2013/09/WebSockets2.png)

Клиент отправляет запрос на соединение с сокетом сервера.

Сервер принимает это соединение.

Клиент шлёт сообщение серверу.

Сервер рассылает это сообщение другим клиентам.

В любой момент обе стороны могут разорвать соединение если это необходимо.

Запросы для сокетов проходят по протоколу WebSocket и выполняются на адреса, которые начинаются с `ws://`, а
не `http://`

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson44/socket.png)

### Сфера применения

Где стоит применять веб сокеты? Основные сферы применения:

- Чаты

- Приложения реального времени (Например отображение курса валют, стоимости криптовалют итд.)

- IoT приложения (IoT - Internet of Things, интернет вещей, любые смарт предметы. Смарт-чайники, телевизоры, датчики
  дыма, кофе машины итд.)

- Онлайн игры

Но если необходимо, то можно применять где угодно.

## Django channels

Естественно для Python существует готовый пакет для поддержки этого протокола с поддержкой Django

[Дока](https://channels.readthedocs.io/en/stable/)

Устанавливается через `pip`

```pip install channels```

### Туториал

Давайте напишем простой чат при помощи Django

Создаём виртуальное окружение, устанавливаем django и channels, создаём джанго проект

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

Если вы используете версию django 2.2, то у вас не будет файла `asgi.py`, а он нам будет нужен. Не переживайте, мы его
создадим.

Файлы `wsgi.py` и `asgi.py` необходимы для запуска серверов, `wsgi` - синхронных, `asgi` - асинхронных. Веб сокет это
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

Для простоты, предлагаю удалить всё кроме `views.py` и `__init__.py`

Полученная структура:

```
chat/
    __init__.py
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

Создадим папку `templates`, добавим её в `settigns.py`

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

Если на инпуте нажимается энтер на клавиатуре, то имитируем нажатие на кнопку входа.

При нажатии на кнопку входа, берем значение из инпута и переходим на страницу `/chat/<значение импута>/` - этой страницы
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
from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('chat/', include('chat.urls')),
]
```

Теперь если мы запустим сервер, то увидим в консоли, что-то такое:

```
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
October 21, 2020 - 18:49:39
Django version 3.1.2, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

А если зайти на страницу http://127.0.0.1:8000/chat/ то будет вот так:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson44/chat_enter.png)

Попытка перейти на любую страницу ни к чему не приведёт, страницы комнаты пока просто нет :)

### Настройка Channels

Для настройки, необходимо изменить файл `asgi.py`, если его нет, то создать его.

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

Что мы сделали? Мы сказали нашему приложению, что мы планируем разные протоколы, обрабатывать по разному, в данный
момент, мы указали только протокол `http`, а значит что фактически, пока что, ничего не изменится

Добавляем приложение в `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'channels',
    'chat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

И добавляем настройку, что бы указать, что основной сервер был `asgi.py`

```python
# mysite/settings.py
# Channels
ASGI_APPLICATION = 'chatsite.asgi.application'
```

Теперь при запуске приложения вы должны увидеть немного другую надпись.

```
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
October 21, 2020 - 19:08:48
Django version 3.1.2, using settings 'mysite.settings'
Starting ASGI/Channels version 3.0.0 development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Обратите внимание, предпоследняя строка, теперь сервер запущен с поддержкой веб сокетов.

### Создаём страницу с конкретным чатом

Создадим html, `room.html`

```html
<!-- chat/templates/chat/room.html -->
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
            'ws://'
            + window.location.host
            + '/ws/chat/'
            + roomName
            + '/'
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

Фильтр json_script Добавит на страницу тег скрипт с данными из переменной, если открыть комнату с названием `test` то
отрендереная страница будет выглядеть так:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson44/room_script.png)

Нужно для того, что бы считать переменную через JS.

Что происходит в JS?

В первой строке мы считываем из переменной имя комнаты.

И создаём соединение с веб сокетом по адресу (`ws://127.0.0.1:8000/ws/chat/<имя чата>/`), мы создадим серверную часть
дальше. Обратите внимание, используется другой протокол не `http`. При создании такого объекта, запрос на соединение
отправляется автоматически.

Если по этому сокету приходит сообщение, то мы добавляем его к нашему месту для текста

```js
chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    document.querySelector('#chat-log').value += (data.message + '\n');
};
```

Если соединение было разорвано, отписать в консоль ошибку

```js
chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
};
```

В случае отправки сообщения, отправить его по сокету.

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

И создать view.

```python
from django.views.generic import TemplateView


class Room(TemplateView):
    template_name = 'room.html'
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

Запускаем сервер, заходим в любую комнату, пишем любое сообщение и видим ошибку.

```WebSocket connection to 'ws://127.0.0.1:8000/ws/chat/lobby/' failed: Unexpected response code: 500```

Мы не создали бекэнд для сокета. Давайте сделаем это.

### Бекэнд сокета

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

Что это такое? Это класс для работы с веб сокетом.

Методы:

- connect - Что делать при запросе на соединение.

- disconnect - Что делать при разрыве соединения.

- receive - Что делать при приходе сообщения.

- send - Отправить сообщение всем кто подключён (включая отправителя, вообще всем).

Создаём новый файл для урлов веб сокета `routing.py`.

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
from django.urls import path
from .comsumer import ChatConsumer

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi(), name='room'),
]
```

Обратите внимание к классу был применён метод `as_asgi`, это аналогия `as_view` для обычных классов.

Укажем эту переменную в нашем `asgi.py`:

```python
# chatsite/asgi.py
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatsite.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
```

Обратите внимание, мы добавили новый протокол для обработки.

Для того, что бы сокет работал необходимы сессии, а для этого необходимо провести миграции.

```python manage.py migrate```

Проверяем, это уже будет работать.

**В данный момент работать будет только один чат!!!**

Мы не добавили возможность создавать разные сокеты, для разных страниц. Для этого необходимо разделить данные по слоям.

### Подключаем channels

Для того что бы использовать различные не пересекающиеся чаты, мы будем использовать `group`, `group` это
набор `channel`.

Для использования необходимо какое-либо внешнее хранилище. Мы будем использовать Redis.

Для этого необходимо установить еще один внешний модуль, для взаимодействия между нашими слоями и редисом.

```pip install channels_redis```

### Для пользователей Windows

На windows обычный редис не будет работать с последними версиями django-channels.

Необходимо установить [это](https://www.memurai.com/get-memurai) и запустить в консоли после:

```memurai```

Это аналог Redis, который будет работать

### Обновление settings

Необходимо обновить настройки и указать, что мы будем использовать redis:

```python
# chatsite/settings.py
# Channels
ASGI_APPLICATION = 'mysite.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
```

Для проверки работы редиса необходимо открыть `shell`:

```python manage.py shell```

```python
import channels.layers

channel_layer = channels.layers.get_channel_layer()
from asgiref.sync import async_to_sync

async_to_sync(channel_layer.send)('test_channel', {'type': 'hello'})
async_to_sync(channel_layer.receive)('test_channel')
{'type': 'hello'}
```

Напоминаю, изначально вебсокеты это асинхронная технология. Для использования её синхронно, мы будем использовать
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
        self.room_group_name = 'chat_%s' % self.room_name

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

`connect` - добавили создание группы, исходя из названия чата, и так же вызвали метод `accept`

`disconnect` - удаляем группу при разрыве соединения

`receive` - При получении сообщения мы выполняем для всей группы, метода `chat_message` могли назвать абсолютно как
угодно.

`chat_message` - отправка сообщения

Можем проверять. Открываем одинаковые названия чата в разных браузерах и пишем по сообщению с каждого

## Запускаем всё асинхронно

Допустим мы хотим отправить другу большой файл, но мы хотим писать сообщения пока файл загружается. В случае
использования синхронного подхода, это невозможно, при асинхронном, это будет работать.

Перепишем `consumers.py`

```python
# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

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
обычных на асинхронные, и вызов функций с обычного на асинхронные.

Всё, ваш чат полностью асинхронен.

### Тестирование

Для тестирования веб сокетов используются специфический ацептанс тесты. Разберите самостоятельно [тут](https://channels.readthedocs.io/en/stable/tutorial/part_4.html).


### Практика

1. Повторите туториал из этого занятия.

2. Давайте разбирать задания на диплом!