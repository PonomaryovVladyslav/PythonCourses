# Урок 39. REST Аутентификация, Авторизация, Permissions.

![](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQ_cLOesie903fmPPbl2YbqawKsycva_owf6Q&usqp=CAU)

## Аутентификация и её виды

Мы с вами разобрали аутентификацию для работы классического веб-приложения, на самом деле это был лишь один из видов
существующих аутентификаций, давайте рассмотрим разные

### Аутентификация сессией

Основана на данных сессии, которые мы уже рассматривали, авторизация происходит один раз, после чего информация о
пользователе хранится в "куках" и передаётся при каждом запросе.

В чём недостатки такого подхода для REST API?

Во-первых, для того что бы выполнять любые не безопасные методы POST, PUT, PATCH, DELETE необходимо использовать CSRF
Token, а это значит, что для выполнения таких запросов, необходимо каждый раз делать дополнительный запрос, для
получения токена.

Во вторых такой подход подразумевает, что сервер хранит информацию, о сессиях, такой подход не будет RESTfull.

### Базовая аутентификация

Аутентификация основанная на том, что в каждом запросе, в хедере запроса будет передаваться логин и пароль необходимого
пользователя. Чаще всего для использования такого вида аутентификации в запрос добавляется хедер `Authorization` со
значением состоящим из слова `Basic` и кодированного при помощи base64 сообщения вида `username:password` например:

`Authorization`: `Basic bXl1c2VyOm15cGFzc3dvcmQ=` для `username` - `myuser`, `password` - `mypassword`

Такая авторизация требует подключения по `https`, так как при обычном `http` запрос легко будет перехватить, и
посмотреть данные авторизации.

### Аутентификация по токену

Базовая аутентификация имеет большое кол-во плюсов перед сессионной, как минимум отсутствием необходимости делать
дополнительные запросы, но каждый раз передавать логин и пароль это не самый удобный, с точки зрения безопасности способ
передачи данных.

Поэтому самым частым видом авторизации является авторизация по токену. Что это значит?

Токен это специальный вычисляемый набор символов уникальный для каждого пользователя.

Токен может быть как постоянным (практически никогда не используется), так и временным, может перегенерироваться по
времени, так и по запросу.

Алгоритм генерации самого токена тоже может быть практически любым (Чаще всего просто генерация большой случайной hex(
шестнадцатеричной) строки), как и данные на которых он основан (при случайном входных данных нет, но может быть основан
на каких либо личных данных, на метках времени итд.)

### Внешняя аутентификация

Благодаря механизму токенов, за авторизацию может отвечать вообще не ваш сервер, допустим если взять классическую
авторизацию через соц сети, то генератором токена является сама соцсеть, мы лишь предоставляем данные для авторизации
соц сети. В ответ получаем токен, при этом мы понятия не имеем как именно его генерирует условный фейсбук, но вы всегда
можно убедится в его правильности, обратившись к API соц сети.

По такому же принципу сервером авторизации может быть практически любой внешний сервер, с которым есть предварительная
договорённость. Допустим вы работаете с командой которая его разрабатывает, и можете узнать как этим пользоваться. Для
открытых соц сетей обычно есть документация по использованию их API, где подробно написано как пользоваться их
авторизацией. Так же для таких механизмов существует большое количество уже написанных packages.

## Реализация и использование в Django REST Framework

Из-за CSRF токенов, авторизация через сессию практически не используется, поэтому мы не будем подробно её рассматривать

### Basic Аутентификация

Для того что бы использовать Basic Аутентификацию достаточно добавить в настройку `REST_FRAMEWORK`, в `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
    ]
}
```

Если нам необходимо использовать несколько аутентификаций, мы можем указать их в списке, например:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}
```

Этого достаточно что бы при любом запросе сначала проверялся хедер авторизации, и в случае правильных логина и пароля,
пользователь добавлялся в реквест.

Если необходимо добавить классы авторизация прям во вью можно указать их через аттрибут `authentication_classes`, для
класс бейз вью и такой же декоратор для функциональной вью

```python
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)
```

```python
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': unicode(request.user),  # `django.contrib.auth.User` instance.
        'auth': unicode(request.auth),  # None
    }
    return Response(content)
```

### Авторизаци по токену

Если необходимо использовать токен авторизацию, то DRF предоставляет нам такой функционал "из коробки", для этого нужно
добавить `rest_framework.authtoken` в `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    ...
    'rest_framework.authtoken'
]
```

И указать необходимую авторизацию в `settings.py`

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        ...
        'rest_framework.authentication.TokenAuthentication',
    ]
}
```

После этого обязательно нужно провести миграции этого приложения `python manage.py migrate`

Что бы создать токены для уже существующих юзеров, нужно сделать это вручную (или написать дата миграцию)

```
from rest_framework.authtoken.models import Token

token = Token.objects.create(user=...)
print(token.key)
```

После этого можно использовать авторизацию токеном

`Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b`

#### Генерация токенов

Чаще всего генерацию токенов "вешают" на сигналы:

```python
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
```

#### Получение токена

Для получения токена можно использовать стандартную вью, для этого нужно добавить в урлы `obtain_auth_token`:

```python
from rest_framework.authtoken import views

urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]
```

Если необходимо изменить логику получения токена, то это можно сделать отнаследовавшись
от `from rest_framework.authtoken.views import ObtainAuthToken`

```python
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
```

Не забыв заменить урлы:

```python
urlpatterns += [
    path('api-token-auth/', CustomAuthToken.as_view())
]
```

### Кастомная авторизация

Кроме своего токена и своего способа его получения, можно так же расписать и свою собственную авторизацию, для этого
нужно отнаследоваться от базовой и описать нужные методы:

```python
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions


class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('HTTP_X_USERNAME')
        if not username:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)
```

### Менедж команда drf_create_token

```python manage.py drf_create_token <username>```

Принимает параметр `username` и генерирует токен для такого юзера, если необходимо то можно перегенерировать при помощи
флага `-r`

```
python manage.py drf_create_token -r <username>
```

### Немного о реальности

На практике практически всегда необходимо переписать токен под свои задачи, как минимум ограничить его время для жизни и
сделать перегенерацию по истечении времени жизни, сделаем это как практику на этом занятии.

### Внешние сервисы

По сути каждый отдельный сервис имеет свою логику, чаще всего у нас будут специальные пекеджи для использования таких
аутентификаций, а если нет, то их всегда можно написать :)

### Авторизация для тестирования через браузер

В рест фреймворк встроена возможность тестировать апи через браузер используя сессионную авторизацию, для этого
достаточно добавить встроенные урлы, и перейти по этому адресу, после этого по вашим апи урлам, вы будете переходить как
уже авторизированный пользователь:

```python
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
```

## Пермишены

Задать разрешения можно на уровне проекта, и на уровне ресурса.

Что бы задать на уровне проекта, в `settings.py` необходимо добавить:

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

Для описания на уровне объектов используется аргумент permission_classes:

```python
from rest_framework import permissions


class ExampleModelViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
```

Существует достаточно много заготовленных пермишенов.

```
AllowAny - можно всем
IsAuthenticated - только авторизированным пользователям
IsAdminUser - только администраторам
IsAuthenticatedOrReadOnly - залогиненым или только на чтение
```

Все они изначально наследуются от `rest_framework.permissons.BasePermission`

Но если нам нужны кастомные то мы можем создать их отнаследовавшись от `permissions.BasePermission` и переписав один из,
или оба метода `has_permisson` и `has_object_permission`

Например владельцу можно выполнять любые действия, а остальным только чтение объекта:

```python
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user

    def has_permission(self, request, view):
        return True
```

`has_permission` - отвечает за доступ к спискам объектов
`has_object_permission` - отвечает за доступ к конкретному объекту

Пермишены можно указывать через запятую если их несколько

```python
permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
```

Если у вас нет доступов, вы получите вот такой ответ:

```
{
    "detail": "Authentication credentials were not provided."
}
```

### Кеширование

Используется декоратор `method_decorator` и методы `cache_page` и `vary_on_cookie`

```python
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets


class UserViewSet(viewsets.ViewSet):

    # Cache requested url for each user for 2 hours
    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_cookie)
    def list(self, request, format=None):
        content = {
            'user_feed': request.user.get_user_feed()
        }
        return Response(content)


class PostView(APIView):

    # Cache page for the requested url
    @method_decorator(cache_page(60*60*2))
    def get(self, request, format=None):
        content = {
            'title': 'Post title',
            'body': 'Post content'
        }
        return Response(content)
```
`cache_page` декоратор кеширует только `GET` и `HEAD` запросы, со статусом 200.

### Пример использования авторизации в ресурсах

```python
class SomeModelViewSet(ModelViewSet):
    serializer_class = SomeSerializer
    queryset = SomeModel.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
```

Таким образом мы можем добавлять объект юзера при сохранении нашего сериалайзера.


## Практика

1. Пишем бейсик авторизацию

2. Пишем токен авторизацию

3. Пишем вьюсеты для моделей из модуля, и создаём 2 покупки и 1 возврат, через постман.

4. Пишем собственный токен, который перестаёт действовать через 10 минут.
