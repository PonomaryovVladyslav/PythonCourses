# Лекция 28. Middleware. Signals. Messages. Manage commands

## Middleware

![](https://memegenerator.net/img/instances/81631865.jpg)

Дока [Тут](https://docs.djangoproject.com/en/4.2/topics/http/middleware/)

Мы с вами рассмотрели основные этапы того, какие этапы должен пройти request на всём пути нашей request-response системы,
но на самом деле каждый request проходит кучу дополнительных обработок, таких как middleware, причём каждый request 
делает это дважды, при "входе" и при "выходе".

Если открыть файл `settings.py`, то там можно обнаружить переменную `MIDDLEWARE`, или `MIDDLEWARE_CLASSES` (для старых
версий Django), которая выглядит примерно так:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

Каждая из этих строк - это отдельная мидлварина, и абсолютно **каждый** request проходит через код, описанный в этих
файлах, например, `django.contrib.auth.middleware.AuthenticationMiddleware` отвечает за то, чтобы в нашем request
всегда был пользователь, если он залогинен, а `django.middleware.csrf.CsrfViewMiddleware` отвечает за проверку наличия и
правильности CSRF токена, которые мы рассматривали ранее.

Причём при "входе" request будет проходить сверху вниз (сначала секьюрити, потом сессии и т. д.), а при "выходе" снизу
вверх (начиная XFrame и заканчивая Security)

**Middleware - это декоратор над request**

### Как этим пользоваться?

Если мы хотим использовать самописные мидлвары, мы должны понимать, как они работают.

Можно описать мидлвар двумя способами: функциональным и основанным на классах. Рассмотрим оба:

Функционально:

```python
def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
```

Как вы можете заметить, синтаксис очень близок к декораторам.

`get_response()` - функция, которая отвечает за всё, что происходит вне мидлвары и отвечает за обработку запроса, по сути
это будет наша `view`, а мы можем дописать любой нужный нам код до или после, соответственно на "входе" реквеста или
на "выходе" респонса.

Так почти никто не пишет :) Рассмотрим, как этот же функционал работает для классов:

```python
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
```

При таком подходе функционал работает при помощи магических методов, функционально выполняет то же самое, но по моему
личному мнению гораздо элегантнее.

При инициализации мы получаем обработчик, а при выполнении вызываем его же, но с возможностью добавить нужный код до
или после.

Чтобы активировать мидлвар, необходимо дописать путь к нему в переменную `MIDDLEWARE` в `settings.py`.

Допустим, если мы создали файл `middleware.py` в приложении под названием `main`, и в этом файле создали
класс `CheckUserStatus`, который нужен, чтобы мы могли обработать какой-либо статус пользователя, нужно дописать в
переменную этот класс:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'main.middleware.CheckUserStatus',  # Новый мидлвар
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

Обратите внимание, я добавил мидлвар после `django.contrib.auth.middleware.AuthenticationMiddleware`, так как до этого
мидлвара в нашем реквесте нет переменной юзер.

## Миксин для мидлвар

На самом деле для написания мидлвар существует миксин, чтобы упростить наш код.

```python
django.utils.deprecation.MiddlewareMixin
```

В нём уже расписаны методы `__init__` и `__call__`.

`__init_()` принимает метод для обработки request, а в `__call__` расписаны методы для обработки request или response.

Метод `__call__` вызывает 4 действия:

1. Вызывает `self.process_request(request)` (если описан) для обработки request.
2. Вызывает `self.get_response(request)`, чтобы получить response для дальнейшего использования.
3. Вызывает `self.process_response(request, response)` (если описан) для обработки response.
4. Возвращает response.

Зачем это нужно?

Чтобы описывать только тот функционал, который мы будем использовать, и случайно не зацепить что-то рядом.

Например, так выглядит мидлвар для добавления юзера в реквест.

```python
from django.contrib import auth
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject


def get_user(request):
    if not hasattr(request, '_cached_user'):
        request._cached_user = auth.get_user(request)
    return request._cached_user


class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        assert hasattr(request, 'session'), (
            "The Django authentication middleware requires session middleware "
            "to be installed. Edit your MIDDLEWARE setting to insert "
            "'django.contrib.sessions.middleware.SessionMiddleware' before "
            "'django.contrib.auth.middleware.AuthenticationMiddleware'."
        )
        request.user = SimpleLazyObject(lambda: get_user(request))
```
Описание: при получении реквеста добавить в него пользователя, информация о котором хранится в сессии.

## Signals

Сигналы. Часто мы оказываемся в ситуации, когда нам нужно выполнять какие-либо действия до или после определённого
события. Конечно, мы можем прописать код там, где нам нужно, но вместо этого мы можем использовать сигналы.

Сигналы отлавливают, что определённое действие выполнено или будет следующим, и выполняют необходимый нам код.

Список экшенов [тут](https://docs.djangoproject.com/en/4.2/ref/signals/).
Описание [тут](https://docs.djangoproject.com/en/4.2/topics/signals/).

Примеры сигналов:

```
django.db.models.signals.pre_save & django.db.models.signals.post_save # Выполняется перед сохранением или сразу после сохранения объекта
django.db.models.signals.pre_delete & django.db.models.signals.post_delete # Выполняется перед удалением или сразу после удаления объекта
django.db.models.signals.m2m_changed # Выполняется при изменении любых ManyToMany связей (добавили студента в группу или убрали, например)
django.core.signals.request_started & django.core.signals.request_finished # Выполняется при начале запроса или при его завершении.
```

Это далеко не полный список действий, на которые могут реагировать сигналы.

Каждый сигнал имеет функции `connect()` и `disconnect()` для того, чтобы привязать/отвязать сигнал к действию.

```python
from django.core.signals import request_finished

request_finished.connect(my_callback)
```

где `my_callback` - это функция, которую нужно выполнять по получению сигнала.

Но гораздо чаще применяется синтаксис с использованием декоратора `receiver`

```python
from django.core.signals import request_finished
from django.dispatch import receiver


@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")
```

У сигнала есть параметр `receiver` и может быть параметр `sender`. Сендер - это объект, который отправляет сигнал
(например, модель, для которой описывается сигнал).

```python
from django.db.models.signals import pre_save
from django.dispatch import receiver
from myapp.models import MyModel


@receiver(pre_save, sender=MyModel)
def my_handler(sender, **kwargs):
    ...
```

Сигнал можно создать под любое действие, если это необходимо. Допустим, нужно отправить сигнал, что пицца готова.

Сначала создадим сигнал.

```python
import django.dispatch

pizza_done = django.dispatch.Signal()
```

И в нужном месте можно отправить:

```python
class PizzaStore:
    ...

    def send_pizza(self, toppings, size):
        pizza_done.send(sender=self.__class__, toppings=toppings, size=size)
        ...
```

## Messages

Дока [тут](https://docs.djangoproject.com/en/4.2/ref/contrib/messages/)

Довольно часто в веб-приложениях вам необходимо отображать одноразовое уведомление для пользователя после обработки
формы или некоторых других типов пользовательского ввода ("Вы успешно зарегистрировались", "Скидка активирована",
"Недостаточно бонусов").

Для этого Django обеспечивает полную поддержку обмена сообщениями на основе файлов cookie и сеансов как для анонимных,
так и для аутентифицированных пользователей.

Инфраструктура сообщений позволяет вам временно хранить сообщения в одном запросе и извлекать их для отображения в
следующем запросе (обычно в следующем).

Каждое сообщение имеет определенный уровень, который определяет его приоритет (например, информация, предупреждение или
ошибка).

### Подключение

По дефолту, если проект был создан через `django-admin`, то `messages` изначально подключены.

`django.contrib.messages` должны быть в `INSTALLED_APPS`.

В переменной `MIDDLEWARE` должны быть `django.contrib.sessions.middleware.SessionMiddleware`
and `django.contrib.messages.middleware.MessageMiddleware`.

По дефолту данные сообщений хранятся в сессии, это является причиной, почему мидлвар для сессий должен быть подключен.

В переменной `context_processors` в переменной `TEMPLATES` должны
содержаться `django.contrib.messages.context_processors.messages`.

#### context_processors

Ключ в переменной `OPTIONS` в переменной `TEMPLATES` отвечает за то, что по дефолту будет присутствовать как переменная
во всех наших темплейтах. Изначально выглядит вот так:

```python
'context_processors': [
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
]
```

`django.template.context_processors.debug`, если в `settings.py` переменная `DEBUG`==`True`, добавляет в темплейт
информацию о подробностях, если произошла ошибка.

`django.template.context_processors.request` добавляет в контекст данные из реквеста, переменная `request`.

`django.contrib.auth.context_processors.auth` добавляет переменную `user` с информацией о пользователе.

`django.contrib.messages.context_processors.messages` добавляет сообщения на страницу.

### Storage backends

Хранить сообщения можно в разных местах.

По дефолту существует три варианта хранения:

`class storage.session.SessionStorage` - хранение в сессии

`class storage.cookie.CookieStorage` - хранение в куке

`class storage.fallback.FallbackStorage` - пытаемся хранить в куке, если не помещается используем сессию. Будет
использовано по умолчанию.

Если нужно изменить, добавьте в `settings.py` переменную:

```python
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
```

Если нужно написать свой класс для хранения сообщений, то нужно наследоваться от `class storage.base.BaseStorage` и
описать 2 метода `_get()` и `_store()`.

### Как этим пользоваться?

Во view необходимо добавить сообщение.

Это можно сделать несколькими способами:

#### add_message()

```python
from django.contrib import messages

messages.add_message(request, messages.INFO, 'Hello world.')
```

Метод `add_message()` позволяет добавить сообщение к реквесту, принимает сам реквест, тип сообщения (успех, провал
информация и т. д.) и сам текст сообщения. На самом деле, второй параметр - это просто цифра, а текст добавлен для чтения.

Чаще всего используется в методах **form_valid()**, **form_invalid()**

#### Сокращенные методы

```python
messages.debug(request, '%s SQL statements were executed.' % count)
messages.info(request, 'Three credits remain in your account.')
messages.success(request, 'Profile details updated.')
messages.warning(request, 'Your account expires in three days.')
messages.error(request, 'Document deleted.')
```

Эти 5 типов сообщений являются стандартными, но, если необходимо, всегда можно добавить свои типы. Как это сделать
описано в доке.

### Как отобразить?

`context_processors`, который находится в настройках, уже добавляет нам в темплейт переменную `messages`, а дальше 
мы можем использовать классические темплейт теги.

Примеры:

```html
{% if messages %}
<ul class="messages">
    {% for message in messages %}
    <li
            {% if message.tags %} class="{{ message.tags }}" {% endif %}>{{ message }}
    </li>
    {% endfor %}
</ul>
{% endif %}
```

```html
{% if messages %}
<ul class="messages">
    {% for message in messages %}
    <li
            {% if message.tags %} class="{{ message.tags }}" {% endif %}>
        {% if message.level == DEFAULT_MESSAGE_LEVELS.ERROR %}Important: {% endif %}
        {{ message }}
    </li>
    {% endfor %}
</ul>
{% endif %}
```

Чаще всего такой код располагают в блоке в базовом шаблоне, чтобы не указывать его на каждой странице отдельно.

#### Использование во view

Если нам вдруг необходимо получить список текущих сообщение во view, мы можем это сделать при помощи
метода `get_messages()`.

```python
from django.contrib.messages import get_messages

storage = get_messages(request)
for message in storage:
    do_something_with_the_message(message)
```

### Messages и Class-Based Views

Можно добавлять сообщения при помощи миксинов, примеры:

```python
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from myapp.models import Author


class AuthorCreate(SuccessMessageMixin, CreateView):
    model = Author
    success_url = '/success/'
    success_message = "%(name)s was created successfully"
```

```python
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from myapp.models import ComplicatedModel


class ComplicatedCreate(SuccessMessageMixin, CreateView):
    model = ComplicatedModel
    success_url = '/success/'
    success_message = "%(calculated_field)s was created successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.calculated_field,
        )
```

## Manage-команды и настройки.

Manage-команды в рамках Django - это возможность запустить скрипт из консоли для выполнения абсолютно различных действий.

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

### Check

```
python manage.py check [app_label [app_label ...]]
```

Например:

```
django-admin check auth admin myapp
```

Команда для запуска проверки кода на качество (например, что неправильно указаны аргументы модели или некорректно
указано свойство для класса админки и т. д., список огромный)
Посмотреть базовый список проверок можно [Тут](https://docs.djangoproject.com/en/4.2/ref/checks/)

### makemessages

```
python manage.py makemessages
```

Командна для работы с переводами (локализацией) сайтов.

Команда проходит через весь код и ищет места, которые заготовлены для перевода (для Python кода - это везде, где вы
используете метод `gettext`, для шаблонов - везде, где используется темплейт тег `translate`,
подробнее [Тут](https://docs.djangoproject.com/en/4.2/topics/i18n/translation/)).

Создаёт\обновляет файлы, в которых хранятся\будут храниться переводы текста на друге языки. Принимает параметры `--all`
, `--extension`, `--locale`, `--exclude`, `--domain`, `--ignore` и т. д.

Подробности использования
параметров [тут](https://docs.djangoproject.com/en/4.2/ref/django-admin/#django-admin-makemessages)

Обсудим основные.

`--locale LOCALE, -l LOCALE` нужно для указания языка, на который планируется перевод (на самом деле повлияет только 
на то, как будет называться файл с переводами, и как этот перевод будет называться в системе), например, для 
французского можно назвать файл `fr`, для итальянского `it` и т. д.

```
django-admin makemessages --locale=pt_BR
django-admin makemessages --locale=pt_BR --locale=fr
django-admin makemessages -l pt_BR
django-admin makemessages -l pt_BR -l fr
```

`--ignore PATTERN` - игнорировать (не искать) переводы в определённых местах, например, `--ignore *.py' - игнорировать
все Python файлы.

Создаст файлы с расширением `.po` и списком всех мест, где нужно будет указать перевод.

```
#. Translators: This message appears on the home page only
# path/to/python/file.py:123
msgid "Welcome to my site."
msgstr ""
```

Комментарием указано, откуда конкретно взят текст для перевода, ниже сам текст, который нужно перевести, и место, где мы
можем указать перевод.

### compilemessages

Компилирует файлы для переводов.

Делает из `.po` файлов `.mo` файлы. Django принимает именно `.mo` в качестве файлов, откуда брать перевод.

Поддерживает указание локали и игнор, подробнее в доке.

### createcachedtable

Создаёт таблицу для кеша в базе данных, подробно рассматривали на занятии по сессиям и кешам.

### shell

Уже известная вам команда `shell` открывает интерактивную `python` консоль с уже импортированными библиотеками вашего
проекта, например, Django.

### dbshell

По аналогии со знакомой нам командой `shell` открывает консоль со всеми необходимыми импортированными данными, но для
базы данных.

Например, для PostgreSQL, откроется `psql` и т. д.

### diffsettings

Команда, которая покажет, чем отличается ваш файл `settings.py` от оригинала.

### dumpdata

Команда для работы с фикстурами.

Фикстуры - это файлы отображения базы данных в формат JSON.

Команда `dumpdata` вытащит все данные из базы данных и преобразует всё в формат JSON.

Может принимать имя только нескольких приложений или даже только некоторых моделей, или наоборот - исключить какие-то
приложения или модели.

### loaddata

Команда, обратная команде `dumpdata`, для загрузки JSON файла в базу данных.

Подробно будем рассматривать эти командны на практике во время занятия по тестированию Django.

### flush

Команда, необходимая для очистки базы данных, но не отмены миграций (сохраняем структуру, теряем все данные).

### sqlflush

Отпечатает, какой SQL код будет выполнен при применении команды `flush`.

### inspectdb

Команда, необходимая для проверки соответствия ваших моделей и вашей базы данных. Незаменимо при переносе проекта извне
на Django.

### makemigrations

Уже известная вам команда, которая создаёт файлы миграций, и может принимать имя приложения, чтобы создать только для
конкретного приложения.

Может принимать важный параметр `--empty`, при этом флаге создастся пустая миграция, никак не привязанная к моделям.
Выглядеть будет примерно вот так:

```python
# Generated by Django 3.0.7 on 2020-10-29 11:59

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
# Generated by Django 3.0.7 on 2020-10-29 11:59

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

Для обратной миграции чаще всего действия не требуются (хоть и далеко не всегда), поэтому чаще всего обратная миграция
записывается в виде лямбды `lambda x, y: None`

![](https://lh3.googleusercontent.com/proxy/a3WuV3A8umBdVGJA7UVrM50cqloRtS9MhMcq9GYmYwwExEAnYkqNVajL5BBHi_3gwnu4-3s8xDHzTQStrjgrMDZg5lQ)

Типовая Data Migration:

```python
# Generated by Django 3.0.7 on 2020-10-29 11:59

from django.db import migrations


def some_forward_action(apps, schema_editor):
    Team = apps.get_model('storages', 'Team') # Приложение и модель
    Team.objects.create(name='B2B')
    Team.objects.create(name='CX')
    Team.objects.create(name='SFA')


class Migration(migrations.Migration):
    dependencies = [
        ('storages', '0003_auto_20201029_1352'),
    ]

    operations = [
        migrations.RunPython(some_forward_action, lambda x, y: None)
    ]
```

### migrate

Уже известная вам команда для применения миграции

```
django-admin migrate [app_label] [migration_name]
```

Может быть указано приложение, к которому применяется, и имя миграции (на самом деле достаточно первых четырех цифр).
Указывание имени нужно для отката миграций. Допустим, у вас уже применена миграция номер 8, а вы поняли, что проблема
была в миграции номер 6, это значит, что можно откатить базу до миграции номер 5. Естественно с потерей данных, и 
провести новые миграции, для этого нужно сделать:

```
manage.py migrate my_app 0005
```

Важным флагом является ```--fake```, при применении этого флага изменения в базу внесены не будут, но Django будет
видеть, что миграция была применена. Нужно, чтобы использовать базы с уже заполненными данными, созданными вне Django
проекта.

> Вместо цифр можно указать значение `zero`, что позволяет откатить все миграции для этого приложения.

### sqlmigrate

Отпечатает, какой SQL код будет выполнен при применении команды `migrate`

### showmigrations

Также уже известная вам команда, которая отобразит список миграций и их состояние (применена или нет).

### runserver

Команда для запуска тестового сервера, можно указывать порт и многие другие настройки **Не применяется на продакшене,
только для разработки**. Как это делается на продакшене, рассмотрим в следующих лекциях.

### sendtestemail

Отправка тестового имейла (работает, только если отправка писем была настроена) принимает два параметра - от кого и кому.

Например:

```python manage.py sendtestemail myownemail@gmail.com myanotheremail@gmail.com```

### sqlsequencereset

Команда для сброса последовательностей базы данных, может принимать название приложения.

Если вы удалите все объекты из базы и начнёте создавать новые, id будут продолжаться вне зависимости от того, сколько
объектов было раньше, потому что `id` вычисляется из специальных объектов базы, которые называются `sequence`.

Если их сбросить, то `id` будет назначаться снова с `1`.

**Не применять на базах с данными!!**

### squashmigrations

Команда, которая применяется для того, чтобы `сжать` несколько миграций в одну.

Например, в приложении `myapp` миграции от 4-ой до 7-ой - это добавления новых полей в одну и ту же модель. Чтобы сжать 
эти миграции в одну, нужно выполнить:

```python manage.py squashmigrations myapp 0004 0007```

### startapp

Команда для создания нового приложения.

### startproject

Команда для создания нового проекта.

### test

Команда для запуска тестов. Рассмотрим её на следующих занятиях.

## Команды базовых приложений

### django.contrib.auth

### changepassword

Команда для смены пароля конкретному пользователю.

```manage.py changepassword ringo```

### createsuperuser

Команда для создания пользователя со всеми правами.

### django.contrib.sessions

### clearsession

Команда для очистки базы данных от информации о сессиях. При базовых настройках вся информация о сессиях автоматически
пишется в базу данных.

### django.contrib.staticfiles

Команды для статики, вообще работу статики и медиа рассмотрим на следующих занятиях.

## Написание своих скриптов

По факту, все вышеописанные команды написаны на Python, а это значит, что мы можем написать свои команды.

Допустим, у нас есть проект пиццерии, в рамках которого есть приложение `orders`, отвечающее за заказы, и мы хотим, 
чтобы все заказы, которые не были закрыты вручную, ровно в 18:00 были переведены в статус для ручной проверки, а владелец
заведения получил письмо о том, что такие заказы есть.

Самый простой путь - это создать `manage-команду`. В приложении создадим папку `management`, а в ней папку `commands`, 
названия созданных в этой папке файлов будет соответствовать кастомной manage-команде.

```
orders/
    __init__.py
    models.py
    management/
        commands/
            close_orders.py
    tests.py
    views.py
```

В файле нужно создать класс, наследованный от `BaseCommand`:

```python
from django.core.management.base import BaseCommand
from orders.models import Order
import send_email


class Command(BaseCommand):
    help = "Close orders which weren't closed manually"

    def handle(self, *args, **options):
        orders = Order.objects.filter(status="opened")
        if orders:
            orders.update(status="manual")
            send_email("Not closed orders", f"Hey, you have {orders.count()} orders with status 'opened'")
            self.stdout.write(self.style.SUCCESS('Successfully closed orders'))
```

Запустить такую команду можно из консоли:

```python manage.py close_orders```

Теперь можно при помощи любой утилиты для работы с консолью поставить задачу в расписание, например, для UNIX систем
можно использовать CRON.

```python
0 18 * * 1-5 /some/path/pizza/manage.py close_orders
```
