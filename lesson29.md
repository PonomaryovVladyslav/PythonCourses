# Лекция 29. REST-аутентификация. Авторизация. Permissions. Фильтрация.

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
  - ▶ **Лекция 29. REST-аутентификация. Авторизация. Permissions. Фильтрация**
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

`Authorization`: `Basic bXl1c2VyOm15cGFzc3dvcmQ=` для `username` — `myuser`, `password` — `mypassword`

Такая авторизация требует подключения по `https`, так как при обычном `http` запрос легко будет перехватить и
посмотреть данные авторизации.

### Аутентификация по токену

Базовая аутентификация имеет большое количество плюсов перед сессионной, как минимум отсутствие необходимости делать
дополнительные запросы, но каждый раз передавать логин и пароль это не самый удобный с точки зрения безопасности способ
передачи данных.

Поэтому самым частым видом авторизации является авторизация по токену. Что это значит?

**Токен** — это специальный вычисляемый набор символов, уникальный для каждого пользователя.

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

Если необходимо добавить классы авторизации прямо во вью, можно указать их через атрибут `authentication_classes` для
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

Если необходимо использовать токен-аутентификацию, то DRF предоставляет нам такой функционал «из коробки», для этого нужно
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

Чаще всего генерацию токенов «вешают» на сигналы:

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

JWT решает задачу срока жизни и обновления токенов «из коробки».
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

JWT (JSON Web Token) — это компактный самодостаточный токен вида `HEADER.PAYLOAD.SIGNATURE` (Base64URL), подписанный алгоритмом (например, HS256/RS256).

- Header: метаданные токена (тип, алгоритм)
- Payload (claims): утверждения, например `sub` (ид пользователя), `exp` (время истечения), `iat` (время выпуска), `nbf` (не раньше)
- Signature: подпись для проверки целостности и подлинности

Ключевые особенности:
- Stateless: сервер не хранит состояние каждого access-токена; проверка — через подпись и время жизни
- Access vs Refresh: короткоживущий access (минуты) и более долгоживущий refresh (часы/дни) для обновления пары
- Ротация refresh-токенов и blacklist: для отзыва/компрометации используйте чёрный список (SimpleJWT поддерживает)
- Хранение токена: обычно в заголовке `Authorization: Bearer <access>`; для браузеров — возможны HttpOnly+Secure cookie (учтите CSRF)
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
`include('rest_framework.urls')` добавляет формы логина/логаута для Browsable API; в продакшене оставляйте только при необходимости.

```python
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
```

## Permissions

Документация: https://www.django-rest-framework.org/api-guide/permissions/

Permissions (права доступа) определяют, кто может выполнять какие действия с API.

### Настройка на уровне проекта

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

### Настройка на уровне View

```python
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from blog.models import Article
from blog.serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
```

### Базовые permissions

| Permission                  | Описание                                             |
|-----------------------------|------------------------------------------------------|
| `AllowAny`                  | Доступ разрешён всем (по умолчанию)                  |
| `IsAuthenticated`           | Только аутентифицированным пользователям             |
| `IsAdminUser`               | Только пользователям с `is_staff=True`               |
| `IsAuthenticatedOrReadOnly` | Аутентифицированным — всё, остальным — только чтение |
| `DjangoModelPermissions`    | Права на основе Django permissions модели            |
| `DjangoObjectPermissions`   | Object-level permissions (требует django-guardian)   |

### SAFE_METHODS

DRF определяет безопасные методы, которые не изменяют данные:

```python
from rest_framework.permissions import SAFE_METHODS

# SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Чтение разрешено всем
        if request.method in SAFE_METHODS:
            return True
        # Запись — только автору
        return obj.author == request.user
```

### has_permission vs has_object_permission

```python
from rest_framework import permissions


class ArticlePermission(permissions.BasePermission):
    """
    has_permission — проверяется для ВСЕХ запросов (list, create, retrieve, update, delete)
    has_object_permission — проверяется только для действий с конкретным объектом
    """

    def has_permission(self, request, view):
        """
        Вызывается ПЕРВЫМ для каждого запроса.
        Проверяет общий доступ к ресурсу.
        """
        # Чтение разрешено всем
        if request.method in permissions.SAFE_METHODS:
            return True
        # Создание — только аутентифицированным
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Вызывается ПОСЛЕ has_permission для retrieve, update, partial_update, destroy.
        Проверяет доступ к конкретному объекту.

        ВАЖНО: Не вызывается для list и create!
        """
        # Чтение разрешено всем
        if request.method in permissions.SAFE_METHODS:
            return True
        # Редактирование — только автору
        return obj.author == request.user
```

### Кастомные permissions для блога

#### IsAuthorOrReadOnly — только автор может редактировать

```python
# blog/permissions.py
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Автор может редактировать и удалять свои статьи.
    Остальные — только читать.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
```

#### IsPublishedOrAuthor — черновики видит только автор

```python
class IsPublishedOrAuthor(permissions.BasePermission):
    """
    Опубликованные статьи видят все.
    Черновики — только автор.
    """

    def has_object_permission(self, request, view, obj):
        if obj.status == 'published':
            return True
        return obj.author == request.user
```

#### CanModerateComments — модератор может удалять комментарии

```python
class CanModerateComments(permissions.BasePermission):
    """
    Удалять комментарии может автор комментария,
    автор статьи или модератор.
    """

    def has_object_permission(self, request, view, obj):
        if request.method != 'DELETE':
            return True

        user = request.user
        # Автор комментария
        if obj.author == user:
            return True
        # Автор статьи
        if obj.article.author == user:
            return True
        # Модератор (группа или флаг)
        if user.groups.filter(name='moderators').exists():
            return True

        return False
```

### DjangoModelPermissions

Использует стандартные Django permissions (`add_`, `change_`, `delete_`, `view_`):

```python
from rest_framework.permissions import DjangoModelPermissions


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [DjangoModelPermissions]

    # Требует у пользователя:
    # - blog.view_article для GET
    # - blog.add_article для POST
    # - blog.change_article для PUT/PATCH
    # - blog.delete_article для DELETE
```

### get_permissions() — разные права для разных действий

```python
from rest_framework.permissions import AllowAny, IsAuthenticated
from blog.permissions import IsAuthorOrReadOnly


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        """
        Разные permissions для разных действий.
        """
        if self.action in ['list', 'retrieve']:
            # Чтение — всем
            return [AllowAny()]
        elif self.action == 'create':
            # Создание — только аутентифицированным
            return [IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            # Редактирование/удаление — только автору
            return [IsAuthenticated(), IsAuthorOrReadOnly()]
        elif self.action == 'publish':
            # Публикация — только автору
            return [IsAuthenticated(), IsAuthorOrReadOnly()]

        return [IsAuthenticated()]
```

### Комбинирование permissions

Несколько permissions работают по логике AND: все должны вернуть `True`:

```python
permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
# Пользователь должен быть аутентифицирован И быть автором
```

Для логики OR создайте кастомный permission:

```python
class IsAuthorOrModerator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user or
            request.user.groups.filter(name='moderators').exists()
        )
```

### 401 vs 403 — разница в ответах

| Код                  | Когда возвращается                        | Пример                                     |
|----------------------|-------------------------------------------|--------------------------------------------|
| **401 Unauthorized** | Аутентификация отсутствует или невалидна  | Нет токена, токен истёк                     |
| **403 Forbidden**    | Аутентификация есть, но прав недостаточно | Пользователь пытается удалить чужую статью  |

```python
# 401 — нет токена
{"detail": "Authentication credentials were not provided."}

# 403 — нет прав
{"detail": "You do not have permission to perform this action."}
```

### Полный пример ArticleViewSet с permissions

```python
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from blog.models import Article
from blog.serializers import ArticleSerializer
from blog.permissions import IsAuthorOrReadOnly, IsPublishedOrAuthor


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        """Фильтрация: опубликованные для всех, черновики для автора."""
        user = self.request.user
        if user.is_authenticated:
            return Article.objects.filter(
                models.Q(status='published') | models.Q(author=user)
            )
        return Article.objects.filter(status='published')

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny(), IsPublishedOrAuthor()]
        elif self.action == 'create':
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsAuthorOrReadOnly()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        article = self.get_object()  # Автоматически проверит permissions
        article.status = 'published'
        article.save()
        return Response({'status': 'Статья опубликована'})
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

DRF предоставляет мощные возможности для фильтрации данных.

### Настройка фильтров

#### На уровне проекта

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}
```

#### На уровне ViewSet

```python
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
```

### SearchFilter — полнотекстовый поиск

```python
class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content', 'author__username']
```

Примеры запросов:

```
GET /api/articles/?search=python
GET /api/articles/?search=django+rest
```

#### Модификаторы поиска

| Префикс | Описание                           | Пример                         |
|---------|------------------------------------|--------------------------------|
| (без)   | `icontains` — частичное совпадение | `search_fields = ['title']`     |
| `^`     | `istartswith` — начинается с       | `search_fields = ['^title']`    |
| `=`     | `iexact` — точное совпадение       | `search_fields = ['=status']`   |
| `@`     | Полнотекстовый поиск (PostgreSQL)  | `search_fields = ['@content']`  |
| `$`     | Regex-поиск                        | `search_fields = ['$title']`    |

```python
class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    search_fields = ['^title', 'content', 'author__username']
    # title — поиск в начале, content — частичное совпадение
```

### OrderingFilter — сортировка

```python
class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['created_at', 'title', 'author__username']
    ordering = ['-created_at']  # Сортировка по умолчанию
```

Примеры запросов:

```
GET /api/articles/?ordering=title
GET /api/articles/?ordering=-created_at
GET /api/articles/?ordering=author__username,-created_at
```

### DjangoFilterBackend — точная фильтрация

Установка:

```bash
pip install django-filter
```

```python
# settings.py
INSTALLED_APPS = [
    ...,
    'django_filters',
]
```

#### Простая фильтрация через filterset_fields

```python
class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'author', 'topics']
```

Примеры запросов:

```
GET /api/articles/?status=published
GET /api/articles/?author=1
GET /api/articles/?topics=5&topics=7
```

#### FilterSet для статей блога

```python
# blog/filters.py
import django_filters as filters
from blog.models import Article


class ArticleFilter(filters.FilterSet):
    """
    Фильтр для статей блога.
    """
    # Фильтр по статусу
    status = filters.ChoiceFilter(choices=Article.STATUS_CHOICES)

    # Фильтр по автору (по id или username)
    author = filters.NumberFilter(field_name='author__id')
    author_username = filters.CharFilter(field_name='author__username', lookup_expr='iexact')

    # Фильтр по темам (ManyToMany)
    topics = filters.ModelMultipleChoiceFilter(
        field_name='topics__name',
        to_field_name='name',
        queryset=Topic.objects.all()
    )
    topic_id = filters.NumberFilter(field_name='topics__id')

    # Фильтр по дате
    created_after = filters.DateFilter(field_name='created_at', lookup_expr='gte')
    created_before = filters.DateFilter(field_name='created_at', lookup_expr='lte')

    # Фильтр по году/месяцу
    year = filters.NumberFilter(field_name='created_at', lookup_expr='year')
    month = filters.NumberFilter(field_name='created_at', lookup_expr='month')

    # Поиск в заголовке
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Article
        fields = ['status', 'author', 'topics']
```

```python
# blog/views.py
from blog.filters import ArticleFilter


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ArticleFilter
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']
```

Примеры запросов:

```
GET /api/articles/?status=published&author=1
GET /api/articles/?topics=python&topics=django
GET /api/articles/?created_after=2024-01-01&created_before=2024-12-31
GET /api/articles/?year=2024&month=6
GET /api/articles/?title=django&ordering=-created_at
```

### Полный пример ArticleViewSet с фильтрацией

```python
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from blog.models import Article
from blog.serializers import ArticleSerializer
from blog.filters import ArticleFilter
from blog.permissions import IsAuthorOrReadOnly


class ArticleViewSet(viewsets.ModelViewSet):
    """
    ViewSet для статей с полной фильтрацией.

    Фильтры:
    - ?status=published — по статусу
    - ?author=1 — по автору (id)
    - ?topics=Python — по теме (name)
    - ?search=django — полнотекстовый поиск
    - ?ordering=-created_at — сортировка
    """
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ArticleFilter
    search_fields = ['title', 'content', 'author__username']
    ordering_fields = ['created_at', 'updated_at', 'title']
    ordering = ['-created_at']

    def get_queryset(self):
        """Оптимизация запросов + фильтрация по пользователю."""
        qs = Article.objects.select_related('author').prefetch_related('topics')

        user = self.request.user
        if user.is_authenticated:
            # Авторизованный видит опубликованные + свои черновики
            return qs.filter(
                models.Q(status='published') | models.Q(author=user)
            )
        # Анонимный видит только опубликованные
        return qs.filter(status='published')

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return []
        return [IsAuthorOrReadOnly()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
```

### Кастомный фильтр

```python
from rest_framework import filters


class IsAuthorFilterBackend(filters.BaseFilterBackend):
    """
    Фильтр, показывающий только объекты текущего пользователя.
    """

    def filter_queryset(self, request, queryset, view):
        if request.user.is_authenticated:
            return queryset.filter(author=request.user)
        return queryset.none()
```

Использование:

```python
class MyArticlesViewSet(viewsets.ReadOnlyModelViewSet):
    """Только статьи текущего пользователя."""
    serializer_class = ArticleSerializer
    filter_backends = [IsAuthorFilterBackend]
    queryset = Article.objects.all()
```

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

И также не забываем перед тем, как сделать миграции, добавить в настройки
приложение `rest_framework`, `rest_framework.authtoken` для авторизации.

### Регистрация

Для регистрации нам необходим сериалайзер и эндпойнт.

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

`api` — папка, в которой находятся все файлы, связанные с API

`notes` — название приложения

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

Но мы же хотели сделать так, чтобы токен «умирал» через 10 минут?

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

Отличный пример, когда мы можем либо создать свой класс и наследоваться от нужных миксинов, либо
ограничить `ModelViewSet`, давайте ограничим второй.

Я хочу, чтобы при чтении я видел имя пользователя.

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

Всё, можно проверять, весь функционал готов!

---

## Итоги

В этой лекции мы изучили:

1. **Виды аутентификации**:
   - Session Authentication: для браузеров, требует CSRF
   - Basic Authentication: логин:пароль в каждом запросе
   - Token Authentication: токен в заголовке Authorization
   - JWT: самодостаточные токены с временем жизни

2. **Настройка аутентификации в DRF**:
   - Глобально: через `DEFAULT_AUTHENTICATION_CLASSES`
   - На уровне View: через `authentication_classes`
   - Кастомная аутентификация: с временем жизни токена

3. **Permissions (права доступа)**:
   - Базовые: `AllowAny`, `IsAuthenticated`, `IsAdminUser`, `IsAuthenticatedOrReadOnly`
   - `SAFE_METHODS`: безопасные методы (GET, HEAD, OPTIONS)
   - `has_permission()` vs `has_object_permission()`
   - `DjangoModelPermissions`: интеграция с Django permissions
   - `get_permissions()`: разные права для разных действий

4. **Кастомные permissions**:
   - `IsAuthorOrReadOnly`: только автор может редактировать
   - `IsPublishedOrAuthor`: черновики видит только автор
   - `CanModerateComments`: модератор может удалять комментарии

5. **Фильтрация**:
   - `SearchFilter`: полнотекстовый поиск
   - `OrderingFilter`: сортировка
   - `DjangoFilterBackend`: точная фильтрация по полям
   - `FilterSet`: декларативные фильтры

6. **Throttling**: ограничение частоты запросов

7. **Кеширование**: `cache_page` и `vary_on_cookie`

---

## Домашнее задание

### Практика на занятии

1. Настройте Token Authentication для проекта блога
2. Создайте permission `IsAuthorOrReadOnly` и примените к `ArticleViewSet`
3. Добавьте `ArticleFilter` с фильтрацией по статусу и темам

### Домашняя работа

1. **JWT аутентификация**:
   - Установите `djangorestframework-simplejwt`
   - Настройте эндпоинты для получения и обновления токенов
   - Проверьте работу через Postman/curl

2. **Permissions для блога**:
   - `IsPublishedOrAuthor` — черновики видит только автор
   - `CanModerateComments` — модератор может удалять любые комментарии
   - Примените `get_permissions()` в `ArticleViewSet` для разных действий

3. **Фильтрация статей**:
   - Создайте `ArticleFilter` с полями: `status`, `author`, `topics`, `created_after`, `created_before`
   - Добавьте поиск по `title` и `content`
   - Добавьте сортировку по `created_at` и `title`

4. **Throttling**:
   - Настройте `AnonRateThrottle` (100 запросов/день)
   - Настройте `UserRateThrottle` (1000 запросов/день)
   - Создайте отдельный throttle для эндпоинта получения токена (10 запросов/минуту)

5. **Токен с временем жизни**:
   - Реализуйте `TokenExpireAuthentication` с временем жизни 1 час
   - Добавьте эндпоинт для обновления токена

---

## Вопросы для самопроверки

1. В чём разница между Session и Token аутентификацией?
2. Что такое JWT и чем он отличается от обычного токена?
3. Какие базовые permissions предоставляет DRF?
4. В чём разница между `has_permission()` и `has_object_permission()`?
5. Что такое `SAFE_METHODS` и как их использовать?
6. Как настроить разные permissions для разных действий ViewSet?
7. Чем отличаются коды ответа 401 и 403?
8. Как создать FilterSet для фильтрации по связанным моделям?
9. Для чего нужен Throttling и как его настроить?
10. Как реализовать токен с ограниченным временем жизни?

---

[← Лекция 28: @api_view, APIView, ViewSets, Pagination, Routers](lesson28.md) | [Лекция 30: Тестирование. Django, REST API. →](lesson30.md)