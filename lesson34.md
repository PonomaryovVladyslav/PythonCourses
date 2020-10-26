# Урок 34. Middlewares. Signals

## Middlewares

![](https://memegenerator.net/img/instances/81631865.jpg)

Дока [Тут](https://docs.djangoproject.com/en/3.1/topics/http/middleware/)

Мы с вами рассмотрели основные этапы того какие этапы должен пройти реквест на всём пути нашей реквест-респонс системы, но на самом деле каждый реквест проходит кучу дополнительных обработок таких как мидлвары, причём каждый реквест делает это дважды, при "входе" и при "выходе".

Если открыть файл `settings.py` то там можно обнаружить переменную `MIDDLEWARES`, или `MIDDLEWARE_CLASSES` (Для старых версий Django)

Которая выглядит примерно вот так:

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

Каждая из этих строк, это отдельная мидлварина, и абсолютно **каждый** реквест проходит через код описанный в этих файлах, например `django.contrib.auth.middleware.AuthenticationMiddleware` отвечает за то, что бы в рашем реквесте всегда был пользователь если он залогинен, а `django.middleware.csrf.CsrfViewMiddleware` отвечает за CSRF токены, которые мы рассматривали ранее.

Причём при "входе" реквест будет проходить сверху вниз (Сначала секьюрити, потом сессии итд), а при "выходе" снизу вверх (начиная с Икс фрейма, заканчивая секьюрити)
 
**Мидлвар это по своей сути это декоратор над реквестом**
 
### Как этим пользоваться?

Если мы хотим использовать самописные мидлвары, мы должны понимать как они работают.

Можно описать мидлвар двумя способами функциональным и основанным на классах, рассмотрим оба:

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

Как вы можете заметить синтаксис очень близок к декораторам.

`get_response` - функция которая отвечает за всё что происходит мне мидлвары и овечает за обработку запроса, по сути это будет наша `view`, а мы можемдописать любой нужный нам код, до или после, соответсвенно на "входе" реквеста или на "выходе" респонса. 

Так почти никто не пишет :) расммотрим как этот же функционал работает для классов:

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

При таком подходе функционал работает при помощи меджик методов, функционально выполняет тоже самое, но по моему личному мнению гораздо элегантнее.

При инициализации, мы получаем обработчик, а при выполнении вызываем его же, но с возможностью добавить нужный код до или после.

Что бы активировать мидлвар нам необходимо дописать путь к нему, в переменную `MIDDLEWARES` в `settings.py`.

Допустим, если мы создали файл `middlewares.py` в приложении под названием `main` и в этом файле создали класс `CheckUserStatus` который нужен что бы мы могли обработать какой либо статус пользователя, нужно дописать в переменную этот класс:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'main.middlewares.CheckUserStatus', # Новый мидлвар
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```
 
Обратите внимание я добавил мидлвар после `django.contrib.auth.middleware.AuthenticationMiddleware` так как до этого мидлвара в нашем реквесте нет переменной юзер.

## Миксин для мидлвар

На самом деле для написания мидлвар существует миксин, что бы упростить наш код.

```python
django.utils.deprecation.MiddlewareMixin
```

В нём уже расписан методы `__init__` и `__call__`

Инит принимает метод для обработки реквеста, а в вызове расписанны методы для обработки ревеста или респонса.

Метод колл вызывает 4 действия:

1. Вызывает `self.process_request(request)` (Если описан) для обработки ревекста.
2. Вызывает `self.get_response(request)` что бы получить респонс для дальнейшего использования.
3. Вызывает `self.process_response(request, response)` (Если описан) для обработки респонса.
4. Возвращает респонс

Зачем это нужно?

Что бы описывать только тот функционал который мы будем использовать, и случайно не зацепить, что-то рядом.

Например так выглядит миддлвар для добавления юзера в реквест.

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

Всё что тут описанно, это что делать при реквесте, добавить реквесту юзера, то при помощи какой магии это работает, мы рассмотрим на следующей лекции.


## Signals

Сигналы. Часто мы оказывамеся к ситуации когда нам нужно выполнять какие-либо действия до\после какого-то определённого события, мы конечно можем прописать код там где нам нужно, но вместо этого ммы можем использоваться сигналы.

Сигналы отлавливают что опрёделённое действие выполненно или будет следующим, и выполняет необходимый нам код.

Список экшенов [тут](https://docs.djangoproject.com/en/3.1/ref/signals/). Описание [тут](https://docs.djangoproject.com/en/3.1/topics/signals/).

Примеры сигналов:

```
django.db.models.signals.pre_save & django.db.models.signals.post_save # Выполняется перед сохраннием или сразу после сохранения объекта
django.db.models.signals.pre_delete & django.db.models.signals.post_delete # Выполняется перед удалением или сразу после удаления объекта
django.db.models.signals.m2m_changed # Выполняется при изменении любых мэни ту мени связей (добавили студента в группу или убрали, например)
django.core.signals.request_started & django.core.signals.request_finished # Выполняется при начале запроса, или при тего завершении.
```

Это далеко не полный список действий на которые могут реагировать сигналы.

Каждый сигнал имеет функции `connect` и `disconnect` для того что бы привязать\отвязать к действию сигнал

```python
from django.core.signals import request_finished

request_finished.connect(my_callback)
```

где `my_callback` это функция, которую нужно выполнять по получению сигнала.

Но гораздо чаще применяется синтаксис с использованием декоратора `receiver`

```python
from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")
```

У сигнала есть параметр `receiver` и может быть параметр `sender`, сендер, это объект который отправляет сигнал, например модель, для которой описывается сигнал.

```python
from django.db.models.signals import pre_save
from django.dispatch import receiver
from myapp.models import MyModel


@receiver(pre_save, sender=MyModel)
def my_handler(sender, **kwargs):
    ...
```

Сигнал можно создать под любое действие если это необходимо. Допустим нужно отправить сигнал, что пицца готова.

Сначала создадим сигнал.

```python
import django.dispatch

pizza_done = django.dispatch.Signal()
```

И в нужном месте можно отправить

```python
class PizzaStore:
    ...

    def send_pizza(self, toppings, size):
        pizza_done.send(sender=self.__class__, toppings=toppings, size=size)
        ...
```
