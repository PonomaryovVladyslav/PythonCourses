# Лекция 29. REST аутентификация. Авторизация. Permissions. Фильтрация.

### Оглавление курса

<details>
  <summary>Блок 1 — Python Basic (1–6)</summary>

  - [Лекция 1. Введение. Типизации. Переменные. Строки и числа. Булева алгебра. Ветвление](lesson01.md)
  - [Лекция 2. Обработка исключений. Списки, строки детальнее, срезы, циклы.](lesson02.md)
  - [Лекция 3: None. Range, list comprehension, sum, max, min, len, sorted, all, any. Работа с файлами](lesson03.md)
  - [Лекция 4. Хэш таблицы. Set, frozenset. Dict. Tuple. Немного об импортах. Namedtuple, OrderedDict](lesson04.md)
  - [Лекция 5. Функции, типизация, lambda. Map, zip, filter.](lesson05.md)
  - [Лекция 6. Рекурсия. Алгоритмы. Бинарный поиск, сортировки](lesson06.md)
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

<details open>
  <summary>Блок 6 — Django Rest Framework (27–30)</summary>

  - [Лекция 27. Что такое API. REST и RESTful. Django REST Framework](lesson27.md)
  - [Лекция 28. @api_view, APIView, ViewSets, Pagination, Routers](lesson28.md)
  - ▶ **Лекция 29. REST аутентификация. Авторизация. Permissions. Фильтрация**
  - [Лекция 30. Тестирование. Django, REST API.](lesson30.md)
</details>

<details>
  <summary>Блок 7 — Python async (31–33)</summary>

  - [Лекция 31. Celery. Multithreading. GIL. Multiprocessing](lesson31.md)
  - [Лекция 32. Асинхронное программирование в Python. Корутины. Asyncio.](lesson32.md)
  - [Лекция 33. Сокеты. Django channels.](lesson33.md)
</details>

<details>
  <summary>Блок 8 — Deployment (34–35)</summary>

  - [Лекция 34. Linux. Все что нужно знать для деплоймента.](lesson34.md)
  - [Лекция 35. Deployment](lesson35.md)
</details>

- [Лекция 36. Методологии разработки. CI/CD. Монолит и микросервисы. Docker](lesson36.md)


![](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQ_cLOesie903fmPPbl2YbqawKsycva_owf6Q&usqp=CAU)

## Аутентификация и её виды

Мы с вами разобрали аутентификацию для работы классического веб-приложения, на самом деле, это был лишь один из видов
существующих аутентификаций, давайте рассмотрим разные.

### Аутентификация сессией

Основана на данных сессии, которые мы уже рассматривали. Авторизация происходит один раз, после чего информация о
пользователе хранится в "куках" и передаётся при каждом запросе.

В чём недостатки такого подхода для REST API?

Во-первых, для того чтобы выполнять любые небезопасные методы `POST`, `PUT`, `PATCH`, `DELETE` необходимо использовать
CSRF Token, а это значит, что для выполнения таких запросов необходимо каждый раз делать дополнительный запрос для
получения токена.

Во‑вторых такой подход подразумевает, что сервер хранит информацию о сессиях, такой подход не будет RESTful.

### Базовая аутентификация

Аутентификация основанная на том, что в каждом запросе в хедере запроса будет передаваться логин и пароль необходимого
пользователя. Чаще всего для использования такого вида аутентификации в запрос добавляется хедер `Authorization` со
значением, состоящим из слова `Basic` и кодированного при помощи base64 сообщения вида `username:password` например:

`Authorization`: `Basic bXl1c2VyOm15cGFzc3dvcmQ=` для `username` - `myuser`, `password` - `mypassword`

Такая авторизация требует подключения по `https`, так как при обычном `http` запрос легко будет перехватить и
посмотреть данные авторизации.

### Аутентификация по токену

Базовая аутентификация имеет большое количество плюсов перед сессионной, как минимум отсутствие необходимости делать
дополнительные запросы, но каждый раз передавать логин и пароль это не самый удобный с точки зрения безопасности способ
передачи данных.

Поэтому самым частым видом авторизации является авторизация по токену. Что это значит?

**Токен** - это специальный вычисляемый набор символов, уникальный для каждого пользователя.

Токен может быть как постоянным (практически никогда не используется), так и временным, может перегенерироваться по
времени, так и по запросу.

Алгоритм генерации самого токена тоже может быть практически любым (Чаще всего просто генерация большой случайной hex
(шестнадцатеричной) строки), как и данные, на которых он основан (при случайном токен входных данных нет, но может быть
основан на каких-либо личных данных, на метках времени и т. д.)

### Внешняя аутентификация

Благодаря механизму токенов, за авторизацию может отвечать вообще не ваш сервер. Допустим, если взять классическую
авторизацию через соцсети, то генератором токена является сама соцсеть, мы лишь предоставляем данные для авторизации
соцсети. В ответ получаем токен, при этом мы понятия не имеем, как именно его генерирует условный фейсбук, но всегда
можно убедится в его правильности, обратившись к API соцсети.

По такому же принципу сервером авторизации может быть практически любой внешний сервер, с которым есть предварительная
договорённость. Допустим, вы работаете с командой, которая его разрабатывает, и можете узнать, как этим пользоваться.
Для открытых соцсетей обычно есть документация по использованию их API, где подробно написано, как пользоваться их
авторизацией. Также для таких механизмов существует большое количество уже написанных packages.

## Реализация и использование в Django REST Framework

Документация: https://www.django-rest-framework.org/api-guide/authentication/

Из-за CSRF токенов авторизация через сессию практически не используется, поэтому мы не будем подробно её рассматривать

Безопасность и нюансы:
- Всегда используйте HTTPS.
- С SessionAuthentication в браузере учитывайте CSRF.
- Token/JWT обычно передаются через заголовок Authorization и не требуют CSRF для небраузерных клиентов.

### Basic Аутентификация

Чтобы использовать Basic аутентификацию, достаточно добавить в настройку `REST_FRAMEWORK`, в `settings.py`:

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

Этого достаточно, чтобы при любом запросе сначала проверялся хедер авторизации, и в случае правильных логина и пароля
пользователь добавлялся в реквест.

Если необходимо добавить классы авторизация прям во вью, можно указать их через аттрибут `authentication_classes` для
Class-Based View и такой же декоратор для функциональной вью.

```python
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView


class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)
```

```python
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def example_view(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content)
```

### Аутентификация по токену
Документация: https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication

Если необходимо использовать токен-аутентификацию, то DRF предоставляет нам такой функционал "из коробки", для этого нужно
добавить `rest_framework.authtoken` в `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    ...
    'rest_framework.authtoken'
]
```

И указать необходимую авторизацию в `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        ...
        'rest_framework.authentication.TokenAuthentication',
    ]
}
```

После этого обязательно нужно провести миграции этого приложения `python manage.py migrate`

Чтобы создать токены для уже существующих юзеров, нужно сделать это вручную (или написать дата миграцию).

```python
from rest_framework.authtoken.models import Token

token = Token.objects.create(user=...)
print(token.key)
```

После этого можно использовать аутентификацию токеном:

```Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b```

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

Для получения токена можно использовать стандартную вью, для этого нужно добавить в URL `obtain_auth_token`:

```python
from rest_framework.authtoken import views

urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]
```

Если необходимо изменить логику получения токена, то это можно сделать, отнаследовавшись
от `from rest_framework.authtoken.views import ObtainAuthToken`:

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

Не забыв заменить URL:

```python
urlpatterns += [
    path('api-token-auth/', CustomAuthToken.as_view())
]

```
### JWT (SimpleJWT) кратко

JWT решает задачу срока жизни и обновления токенов из коробки.
Документация: https://django-rest-framework-simplejwt.readthedocs.io/



settings.py:
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```

urls.py:
```python
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns += [
    path('api/jwt/token/', TokenObtainPairView.as_view()),
    path('api/jwt/refresh/', TokenRefreshView.as_view()),
]
```

Примеры:
- получить пару токенов: POST /api/jwt/token/ { "username": "...", "password": "..." }
- обновить access по refresh: POST /api/jwt/refresh/ { "refresh": "<REFRESH>" }

Используйте HTTPS; токены передавайте в заголовке Authorization: Bearer <token>.


#### Немного теории о JWT

JWT (JSON Web Token) — это компактный самодостаточный токен вида `HEADER.PAYLOAD.SIGNATURE` (Base64Url), подписанный алгоритмом (например, HS256/RS256).

- Header: метаданные токена (тип, алгоритм)
- Payload (claims): утверждения, например `sub` (ид пользователя), `exp` (время истечения), `iat` (время выпуска), `nbf` (не раньше)
- Signature: подпись для проверки целостности и подлинности

Ключевые особенности:
- Stateless: сервер не хранит состояние каждого access-токена; проверка — через подпись и время жизни
- Access vs Refresh: короткоживущий access (минуты) и более долгоживущий refresh (часы/дни) для обновления пары
- Ротация refresh-токенов и blacklist: для отзыва/компрометации используйте «чёрный список» (SimpleJWT поддерживает)
- Хранение токена: обычно в заголовке Authorization: `Bearer <access>`; для браузеров — возможны HttpOnly+Secure cookie (учтите CSRF)
- Безопасность: всегда HTTPS, минимальные сроки жизни, ограничение областей применения (scopes), ограничение аудитории (aud), clock skew

JWT не шифрует данные, а подписывает их: содержимое видно клиенту. Не кладите в токен чувствительные данные.

### Кастомная авторизация

Кроме своего токена и своего способа его получения, можно также расписать и свою собственную авторизацию, для этого
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

### Manage-команда drf_create_token

```python manage.py drf_create_token <username>```

Принимает параметр `username` и генерирует токен для такого юзера, если необходимо, то можно перегенерировать при помощи
флага `-r`

```
python manage.py drf_create_token -r <username>
```

### Немного о реальности

На практике практически всегда необходимо переписать токен под свои задачи, как минимум ограничить его время для жизни и
сделать перегенерацию по истечении времени жизни, сделаем это как практику на этом занятии.
Документация: https://www.django-rest-framework.org/topics/browsable-api/#log-in-and-log-out

### Внешние сервисы

По сути, каждый отдельный сервис имеет свою логику, чаще всего у нас будут специальные пакеты для использования таких
аутентификаций, а если нет, то их всегда можно написать. :)

### Авторизация для тестирования через браузер
Документация: https://www.django-rest-framework.org/topics/browsable-api/#log-in-and-log-out

В REST фреймворк встроена возможность тестировать API через браузер, используя сессионную авторизацию. Для этого
достаточно добавить встроенные URL и перейти по этому адресу; после этого по вашим API URL вы будете переходить как
уже авторизованный пользователь:
include('rest_framework.urls') добавляет формы логина/логаута для Browsable API; в продакшене оставляйте только при необходимости.

```python
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
```

## Permissions
Документация: https://www.django-rest-framework.org/api-guide/permissions/

Они же права доступа.

Задать разрешения можно на уровне проекта и на уровне ресурса.

Чтобы задать на уровне проекта, в `settings.py` необходимо добавить:

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

- По умолчанию (если DEFAULT_PERMISSION_CLASSES не задан), действует AllowAny.
- SAFE_METHODS = {"GET", "HEAD", "OPTIONS"} — считаются методами только для чтения.
- 401 Unauthorized — отсутствует/невалидна аутентификация; 403 Forbidden — аутентификация есть, но прав недостаточно.


Для описания на уровне объектов используется аргумент `permission_classes`:

```python
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet


class ExampleModelViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
```

Существует достаточно много заготовленных пермишенов.

```
AllowAny - можно всем
IsAuthenticated - только аутентифицированным пользователям
IsAdminUser - только администраторам
IsAuthenticatedOrReadOnly - аутентифицированным пользователям или только на чтение
```

Все они изначально наследуются от `rest_framework.permissions.BasePermission`.

Но если нам нужны кастомные, то мы можем создать их, отнаследовавшись от `permissions.BasePermission` и переписав один
или оба метода `has_permission()` и `has_object_permission()`

Например, владельцу можно выполнять любые действия, а остальным только чтение объекта:

```python
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only owners of an object to edit it.
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

`has_permission()` - отвечает за доступ к спискам объектов
`has_object_permission()` - отвечает за доступ к конкретному объекту

Пермишены можно указывать через запятую, если их несколько:

```python
permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
```

Пример per-action (разные права для разных действий):
```python
from rest_framework.permissions import AllowAny, IsAuthenticated

class NotesViewSet(ModelViewSet):
    ...
    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAuthenticated(), DeleteOnlyOwner()]
```


Если у вас нет доступов, вы получите вот такой ответ:

```
{
    "detail": "Authentication credentials were not provided."
}
```

### Кеширование

Используется декоратор `method_decorator` и методы `cache_page()` и `vary_on_cookie()`:

Документация: https://www.django-rest-framework.org/api-guide/throttling/
```python
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets


class UserViewSet(viewsets.ViewSet):

    # Cache requested url for each user for 2 hours
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request, format=None):
        content = {
            'user_feed': request.user.get_user_feed()
        }
        return Response(content)


class PostView(APIView):

    # Cache page for the requested url
    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, format=None):
        content = {
            'title': 'Post title',
            'body': 'Post content'
        }
        return Response(content)

## Тротлинг (Throttling)
Документация: https://www.django-rest-framework.org/api-guide/throttling/



Тротлинг ограничивает частоту запросов, защищая API от злоупотреблений (brute force, DoS) и сглаживая нагрузку.

Настройка глобально в settings.py:
```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.ScopedRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',      # для неаутентифицированных
        'user': '1000/day',     # для аутентифицированных
        'auth-endpoint': '10/min',  # пример для scope
    },
}
```

На уровне вью: можно задать конкретные классы или использовать scope для ScopedRateThrottle:
```python
from rest_framework.throttling import ScopedRateThrottle

class NotesViewSet(ModelViewSet):
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'auth-endpoint'  # будет применена ставка из DEFAULT_THROTTLE_RATES
```

Поведение:
- При превышении лимита возвращается 429 Too Many Requests (часто с заголовком `Retry-After`).
- По умолчанию используется кеш бэкенд Django; в продакшене используйте общий кеш (например, Redis) для нескольких инстансов.

Кастомный тротлинг:
```python
from rest_framework.throttling import SimpleRateThrottle

class LoginThrottle(SimpleRateThrottle):
    scope = 'login'
    def get_cache_key(self, request, view):
        ident = request.user.pk if request.user.is_authenticated else self.get_ident(request)
        return f"throttle_login_{ident}"
```
Регистрируем ставку `login` в DEFAULT_THROTTLE_RATES, применяем к нужным вью.

`cache_page` декоратор кеширует только `GET` и `HEAD` запросы со статусом 200.

### Пример использования авторизации в ресурсах

```python
class SomeModelViewSet(ModelViewSet):
    serializer_class = SomeSerializer
    queryset = SomeModel.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
```

Таким образом, мы можем добавлять объект юзера при сохранении нашего сериалайзера.

## Фильтрация
Документация:
- Filtering: https://www.django-rest-framework.org/api-guide/filtering/
- SearchFilter: https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
- OrderingFilter: https://www.django-rest-framework.org/api-guide/filtering/#orderingfilter
- django-filter: https://django-filter.readthedocs.io/

DRF предоставляет нам огромные возможности для фильтрации, практически не дописывая для этого специальный код.

### SearchFilter

Как и с другими параметрами, у нас есть два варианта указания фильтрации, общая для всего проекта или конкретная для
определённого класса или функции.

Для указания общего фильтра на весь проект необходимо добавить в `settings.py` в переменную `REST_FRAMEWORK`:

```python
REST_FRAMEWORK = {
    ...
'DEFAULT_FILTER_BACKENDS': ['rest_framework.filters.SearchFilter']
}
```

Для указания в конкретном классе необходимо использовать аргумент `filter_backends`. Принимает коллекцию из фильтров,
например:

```python
from rest_framework.filters import SearchFilter, OrderingFilter


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]

```

Или же соответствующий декоратор для использования в функциях.

#### Как пользоваться?

Для использования необходимо добавить в класс параметр `search_fields`

```python
class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'label']
```

Этот параметр также принимает коллекцию, состоящую из списка полей, по которым необходимо производить поиск.

Теперь у нас есть возможность добавить query параметр `search=` (ключевое слово можно поменять через `settings.py`,
чтобы искать по указанным полям).

Например:

```
http://127.0.0.1:9000/api/group/?search=Pyt
```

Результат будет отфильтрован так, чтобы отобразить только те данные, у которых хотя бы в одном из указанных полей будет
найдено частичное совпадение без учёта регистра (`lookup icontains`).

Если нам необходим более специфический параметр поиска, существует 4 специальных настройки в параметре `search_fields`:

- `^` Поиск только в начале строки
- `=` Полное совпадение
- `@` Поиск по полному тексту (работает на основе индексов, работает только для postgres)
- `$` Поиск регулярного выражения

Например:

```python
class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['=name', '^label']
```

### OrderingFilter

Точно также можно добавить ordering фильтр для того, чтобы указывать ordering в момент запроса через query параметр
`ordering=` (также можно заменить через `settings.py`)

Необходимо указать параметр `ordering_fields`, также принимает коллекцию из полей. Также может принимать специальное
значение `__all__` для возможности сортировать по любому полю.

```python
class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['name', 'label']
```

В query параметре может принимать символ `-` или список полей через запятую.

Примеры:

```
http://example.com/api/users?ordering=username

http://example.com/api/users?ordering=-username

http://example.com/api/users?ordering=account,username
```
### DjangoFilterBackend (рекомендовано)

Документация: https://django-filter.readthedocs.io/

Установка: pip install django-filter

Добавьте в INSTALLED_APPS:

```python
INSTALLED_APPS = [
    ...,
    'django_filters',
]
```
Declarative-фильтрация без написания кода:

settings.py:
```python
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}

```python
import django_filters as df
from .models import User

class UserFilter(df.FilterSet):
    min_age = df.NumberFilter(field_name='age', lookup_expr='gte')
    class Meta:
        model = User
        fields = ['min_age', 'city']
```

views.py:
```python
class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    filterset_fields = ['name', 'label']  # ?name=py&label=basic
    search_fields = ['^name', 'label']
    ordering_fields = ['name', 'label']
```


### Свой собственный фильтр

Как и со всем остальным, можно написать свой собственный фильтр, для этого необходимо наследоваться от
`rest_framework.filters.BaseFilterBackend` и описать один метод `filter_queryset`, в котором можно описать любую логику.

Например, этот фильтр будет отображать только те объекты, которые принадлежат юзеру.

```python
class IsOwnerFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(owner=request.user)
```

## Сложные комплексные фильтры

На самом деле, бывают и значительно более сложные фильтры, для которых существуют специальные пакеты.

Например:

```
pip install django-filter
pip install djangorestframework-filters
pip install djangorestframework-word-filter
```

Все они легко настраиваются и значительно расширяют возможность использования фильтров. Изучите их самостоятельно.

## Живой пример с заметками на DRF

Напоминаю условия.

Допустим, нам нужен сайт, на котором можно зарегистрироваться, залогиниться, разлогиниться и написать заметку, если ты
залогинен. Заметки должны отображаться списком, последняя созданная отображается первой. Все пользователи видят все
заметки. Возле тех, которые создал текущий пользователь, должна быть кнопка удалить.

В случае с REST, кнопку заменяем просто на возможность это сделать для владельца заметки.

Дополнительно реализуем токен время жизни которого 10 минут, после чего необходимо получать новый.

### Модель сохраняется

`models.py`

```python
from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    class Meta:
        ordering = ['-created_at', ]
```

И так же не забываем перед тем как сделать миграции, добавить в настройки,
приложение, `rest_framework`, `rest_framework.authtoken`, для авторизации.

### Регистрация

Для регистрации, нам необходим сериалайзер и эндпоинт.

`api/serializers.py`

```python
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'id')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
```

`resources.py`

```python
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from notes.api.serializers import UserSerializer


class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]
```

`api` - папка в которой находятся все файлы связанные с API

`notes` - название приложения

Добавляем url:

`urls.py`

```python
from django.urls import path

from notes.api.resources import RegisterAPIView

urlpatterns = [
    path('api/register/', RegisterAPIView.as_view()),
]

```

### Аутентификация

Для аутентификации мы будем использовать стандартную аутентификацию по токену. Так что все что нам надо сделать, это добавить
урл для получения токена.

`urls.py`

```python
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from notes.api.resources import RegisterAPIView

urlpatterns = [
    path('api/register/', RegisterAPIView.as_view()),
    path('api/token/', obtain_auth_token)
]
```

Но мы же хотели сделать так, что бы токен "умирал" через 10 минут?

Для этого много способов, но самый простой, это написать собственную аутентификацию, основанную на базовой

`settings.py`

```python
...

TOKEN_EXPIRE_SECONDS = 600

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ("notes.api.authentication.TokenExpireAuthentication",),
}

```

`notes/api/authentication.py`

```python
from django.conf import settings
from django.utils import timezone
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication


class TokenExpireAuthentication(TokenAuthentication):
    def authenticate(self, request):
        try:
            user, token = super().authenticate(request=request)
        except exceptions.AuthenticationFailed as e:
            raise exceptions.AuthenticationFailed(e)
        except TypeError:
            return None
        else:
            if (timezone.now() - token.created).total_seconds() > settings.TOKEN_EXPIRE_SECONDS:
                token.delete()
                raise exceptions.AuthenticationFailed("Token expired")
            return user, token

```

### Заметки. Чтение, создание, удаление

Отличный пример когда мы можем либо создать свой класс и наследоваться от нужных миксинов, либо,
ограничить `ModelViewSet`, давайте ограничим второй.

Я хочу что бы при чтении я видел имя пользователя.

Также мне нужно ограничить удаление чужих объектов. Возможность создания, только зарегистрированным пользователем. И
добавление этого пользователя, напрямую из реквеста.

`api/permissions.py`

```python
from rest_framework.permissions import BasePermission


class DeleteOnlyOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE":
            return obj.author == request.user
        else:
            return True
```

`api/serializers.py`

```python
from django.contrib.auth.models import User
from rest_framework import serializers

from notes.models import Note


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'id')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Note
        fields = ['id', 'text', 'created_at', 'author']


```

`api/resources.py`

```python
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from notes.api.permissions import DeleteOnlyOwner
from notes.api.serializers import UserSerializer, NoteSerializer
from notes.models import Note


class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny,]


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    http_method_names = ['get', 'post', 'delete']
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, DeleteOnlyOwner]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
```

`urls.py`

```python
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from notes.api.resources import RegisterAPIView, NotesViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'notes', NotesViewSet)
urlpatterns = [
    path('api/register/', RegisterAPIView.as_view()),
    path('api/token/', obtain_auth_token),
    path('api/', include(router.urls)),
]
```

Все, можно проверять, весь функционал готов!