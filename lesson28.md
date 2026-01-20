# Лекция 28. @api_view, APIView, ViewSets, Pagination, Routers

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
  - ▶ **Лекция 28. @api_view, APIView, ViewSets, Pagination, Routers**
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


Все мы помним, что веб в первую очередь — это Request-Response система.

## Request

Что нового в request.

Документация: https://www.django-rest-framework.org/api-guide/requests/

Два новых параметра `.data` и `.query_params`

`.data` — данные, если запрос POST, PUT или PATCH, аналог `request.POST` или `request.FILES`

`.query_params` — данные, если запрос GET, аналог `request.GET`

Также доступны `request.user` и `request.auth`. Детали аутентификации/авторизации рассмотрим на следующей лекции.
Практические нюансы:
- `request.data` объединяет данные из JSON/формы/файлов в зависимости от подключённых парсеров (JSONParser, FormParser, MultiPartParser)
- `request.query_params` — это QueryDict (поддерживает несколько значений для одного ключа)
- Полезные атрибуты: `request.content_type`, `request.accepted_renderer`, `request.accepted_media_type`
- Расширяйте DEFAULT_PARSER_CLASSES, если нужны формы/файлы

Пример настройки парсеров (частично):
```python
REST_FRAMEWORK = {
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.MultiPartParser",
        "rest_framework.parsers.FormParser",
    ],
}
```

## Response

Документация: https://www.django-rest-framework.org/api-guide/responses/

В отличие от классической Django, ответом в REST системе будет обычный HTTP-ответ, содержащий набор данных, чаще
всего JSON (но бывает и нет).

Классическая Django тоже может возвращать HTTP-ответ и быть обработчиком REST архитектуры, но существующий пакет
сильно упрощает эти процессы.

Для обработки такого ответа есть специальный объект:

```Response(data, status=None, template_name=None, headers=None, content_type=None)```

Пример ответа при создании ресурса (201 + Location):
```python
from rest_framework import status
# после serializer.save() -> obj
return Response(serializer.data, status=status.HTTP_201_CREATED, headers={"Location": obj.get_absolute_url()})
```

где `data` — данные,

`status` — код ответа (200, 404, 503),

`template_name` — возможность указать темплейт, если необходимо вернуть страницу, а не просто набор данных,

`headers` и `content_type` — заголовки и тип содержимого запроса.


### Коротко на практике
- `request.data` — тело запроса (JSON/форма/файлы)
- `request.query_params` — параметры строки запроса (?page=1&search=...)
- `request.FILES` — загружаемые файлы
- Возвращайте Response(data, status=...) и используйте константы из rest_framework.status, например status.HTTP_201_CREATED
- Если отключить BrowsableAPIRenderer, «Browsable API» исчезнет и ответы будут только в JSON

## Настройка для получения JSON

Если нужно указать явно формат для получения или отправки, то можно указать его в `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ]
}
```

## @api_view

Документация: https://www.django-rest-framework.org/api-guide/views/#api_view

Для описания `endpoint` функционально нужно указать декоратор `api_view` и методы, которые он может принимать.
Возвращает всё также объект ответа. Для использования возьмём модель `Article` и сериалайзер `ArticleSerializer` из нашего блога:

```python
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Article
from blog.serializers import ArticleSerializer


@api_view(['GET', 'POST'])
def article_list(request):
    """
    Список всех статей или создание новой статьи.
    """
    if request.method == 'GET':
        # Показываем только опубликованные статьи
        articles = Article.objects.filter(status='published')
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

Обратите внимание, в пакете REST фреймворка сразу есть заготовленные объекты статуса для ответа.

Если попытаться получить доступ методом, который не разрешен, запрос будет отклонён с ответом `405 Method not allowed`

Для передачи параметров используются аргументы функции. (Очень похоже на обычную Django вью)

```python
from django.shortcuts import get_object_or_404

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    """
    Получение, обновление или удаление статьи.
    """
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

URL для таких методов описываются точно так же, как и для стандартной Django вью:

```python
from blog.views import article_list, article_detail

urlpatterns = [
    path('articles/', article_list),
    path('articles/<int:pk>/', article_detail),
]
```

Ответ на GET-запрос в этом случае будет выглядеть так:

```json
[
    {
        "id": 1,
        "title": "Введение в Django REST Framework",
        "slug": "intro-to-drf",
        "status": "published",
        "created_at": "2024-01-15T10:30:00Z"
    },
    {
        "id": 2,
        "title": "Продвинутые сериализаторы",
        "slug": "advanced-serializers",
        "status": "published",
        "created_at": "2024-01-16T14:20:00Z"
    }
]
```

Поля будут зависеть от модели и сериалайзера соответственно.

Ответ на POST запрос (создание объекта):

```json
{
    "id": 3,
    "title": "Новая статья",
    "slug": "new-article",
    "status": "draft",
    "created_at": "2024-01-17T09:00:00Z"
}
```

## View

Справочник по CBV/DRF: https://www.cdrf.co/

## APIView


### Шпаргалка выбора: @api_view vs APIView vs GenericAPIView vs ViewSet
- Быстрое функциональное представление: @api_view — простые эндпоинты без классов, минимум кода
- Точная кастомизация: APIView — полный контроль над методами get/post/put/delete
- CRUD из коробки по одному ресурсу: GenericAPIView + миксины (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
- Полный набор CRUD и экшены + автоматический роутинг: ModelViewSet/ReadOnlyModelViewSet + Router (чаще всего на практике)

Документация: https://www.django-rest-framework.org/api-guide/views/#class-based-views

На уровне класса можно настраивать: parser_classes, renderer_classes, throttle_classes.
Также мы можем описать это же через Class-Based View, для этого нам нужно наследоваться от APIView:

```python
from blog.models import Article
from blog.serializers import ArticleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class ArticleListAPIView(APIView):
    """
    Список всех статей или создание новой.
    """

    def get(self, request, format=None):
        articles = Article.objects.filter(status='published')
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

Вынесем получение объекта в отдельный метод:

```python
from django.shortcuts import get_object_or_404

class ArticleDetailAPIView(APIView):
    """
    Получение, обновление или удаление статьи.
    """

    def get_object(self, pk):
        return get_object_or_404(Article, pk=pk)

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

URL описываются так же, как и для Django Class-Based View:

```python
urlpatterns = [
    path('articles/', ArticleListAPIView.as_view()),
    path('articles/<int:pk>/', ArticleDetailAPIView.as_view()),
]
```

## GenericAPIView и generic-классы

По аналогии с классической Django существуют заранее описанные CRUD действия.

Как это работает?

Существует класс `GenericAPIView`, который наследуется от обычного `APIView`.

В нём описаны такие поля как:

- `queryset` хранит кверисет;

- `serializer_class` хранит сериалайзер;

- `lookup_field = 'pk'` — название атрибута в модели, который будет отвечать за PK;

- `lookup_url_kwarg = None` — название атрибута в запросе, который будет отвечать за `pk`;

- `filter_backends = api_settings.DEFAULT_FILTER_BACKENDS` — фильтры запросов;

- `pagination_class = api_settings.DEFAULT_PAGINATION_CLASS` — пагинация запросов.

И методы:

- `get_queryset` — получение кверисета;

- `get_object` — получение одного объекта;

- `get_serializer` — получение объекта сериалайзера;

- `get_serializer_class` — получение класса сериалайзера;

- `get_serializer_context` — получить контекст сериалайзера;

- `filter_queryset` — отфильтровать кверисет;

- `paginator` — объект пагинации;

- `paginate_queryset` — пагинировать кверисет;

- `get_paginated_response` — получить пагинированный ответ.

*Такой класс не работает самостоятельно, только вместе с определёнными миксинами*

### Миксины

В DRF существует 5 миксинов:

```python
class CreateModelMixin(object):
    """
    Create a model instance.
    """

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
```

Рассмотрим подробнее.

Это миксин, и без сторонних классов этот функционал работать не будет.

При вызове метода `create()` мы предполагаем, что у нас был request.

Вызываем метод `get_serializer()` из класса `GenericAPIView` для получения объекта сериалайзера, обратите внимание, что
данные передаются через атрибут `data`, так как они получены от пользователя. Проверяем данные на валидность (обратите
внимание на атрибут `raise_exception`, если данные будут не валидны, код сразу вылетит в traceback, а значит нам не
нужно отдельно прописывать действия при не валидном сериалайзере), вызываем метод `perform_create`, который просто
сохраняет сериалайзер (вызывает `create` или `update` в зависимости от данных), получает хедеры, и возвращает response
с 201 кодом, создание успешно.

По аналогии мы можем рассмотреть остальные миксины.

```python
class RetrieveModelMixin(object):
    """
    Retrieve a model instance.
    """

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
```

Обратите внимание, метод называется `retrieve()` и внутри вызывает метод `get_object()` — это миксин одиночного объекта

```python
class UpdateModelMixin(object):
    """
    Update a model instance.
    """

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
```

Методы `update()`, `partial_update()`, `perform_update()` нужны для обновления объекта, обратите внимание на атрибут
`partial`. Помните разницу между PUT и PATCH?

```python
class DestroyModelMixin(object):
    """
    Destroy a model instance.
    """

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
```

Аналогично для удаления методы `destroy()`, `perform_destroy()`.

```python
class ListModelMixin(object):
    """
    List a queryset.
    """

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
```

Метод `list()` получает кверисет, дальше пытается его пагинировать, если получается, возвращает страницу, если нет —
целый ответ.

*Важно!* Ни в одном из миксинов не было методов `get()`,`post()`,`patch()`,`put()` или `delete()`, почему?

Потому что их вызов перенесен в дополнительные классы.

### Generic классы

Вот так выглядят классы, которые уже можно использовать. Как это работает? Эти классы наследуют логику работы с данными
из необходимого миксина, общие методы, которые актуальны для любого CRUD действия из `GenericAPIView` дальше описываем
методы тех видов запросов, которые мы хотим обрабатывать, в которых просто вызываем необходимый метод из миксина.

**Переписываются методы `create()`, `destroy()` и т. д., а не `get()`, `post()`!**

```python
class CreateAPIView(mixins.CreateModelMixin,
                    GenericAPIView):
    """
    Concrete view for creating a model instance.
    """

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

```

```python
class ListAPIView(mixins.ListModelMixin,
                  GenericAPIView):
    """
    Concrete view for listing a queryset.
    """

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
```

```python
class RetrieveAPIView(mixins.RetrieveModelMixin,
                      GenericAPIView):
    """
    Concrete view for retrieving a model instance.
    """

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
```

```python
class DestroyAPIView(mixins.DestroyModelMixin,
                     GenericAPIView):
    """
    Concrete view for deleting a model instance.
    """

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```

```python
class UpdateAPIView(mixins.UpdateModelMixin,
                    GenericAPIView):
    """
    Concrete view for updating a model instance.
    """

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
```

```python
class ListCreateAPIView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        GenericAPIView):
    """
    Concrete view for listing a queryset or creating a model instance.
    """

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

```python
class RetrieveUpdateAPIView(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            GenericAPIView):
    """
    Concrete view for retrieving, updating a model instance.
    """

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
```

```python
class RetrieveDestroyAPIView(mixins.RetrieveModelMixin,
                             mixins.DestroyModelMixin,
                             GenericAPIView):
    """
    Concrete view for retrieving or deleting a model instance.
    """

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```

```python
class RetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin,
                                   GenericAPIView):
    """
    Concrete view for retrieving, updating or deleting a model instance.
    """

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```

Допустим, мы хотим описать класс для получения списка комментариев к конкретной статье и создания новых комментариев:

```python
from rest_framework.generics import ListCreateAPIView
from blog.models import Comment
from blog.serializers import CommentSerializer


class ArticleCommentListView(ListCreateAPIView):
    """
    Список комментариев к статье и создание нового комментария.
    """
    serializer_class = CommentSerializer

    def get_queryset(self):
        # Фильтруем комментарии по статье из URL
        article_pk = self.kwargs['article_pk']
        return Comment.objects.filter(article_id=article_pk)

    def perform_create(self, serializer):
        # Автоматически привязываем комментарий к статье и автору
        article_pk = self.kwargs['article_pk']
        serializer.save(
            article_id=article_pk,
            author=self.request.user
        )
```

URL для такого представления:

```python
urlpatterns = [
    path('articles/<int:article_pk>/comments/', ArticleCommentListView.as_view()),
]
```

Всё, этого достаточно для полноценного CRUD комментариев к статье!

## ViewSet

Документация: https://www.django-rest-framework.org/api-guide/viewsets/

Классы, которые отвечают за поведение нескольких запросов, и отличаются друг от друга только методом, называются
`ViewSet`.

Они на самом деле описывают методы, для получения списка действий (list, retrieve, и т. д.), и преобразования их в URL
(об этом дальше).

Например:

```python
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from myapps.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
```

Разные действия при наличии и отсутствии `PK`, при `GET` запросе.

Для описания URL можно использовать разные варианты:

```python
user_list = UserViewSet.as_view({'get': 'list'})
user_detail = UserViewSet.as_view({'get': 'retrieve'})
```

Хоть так никто и не делает, об этом дальше.

## ModelViewSet и ReadOnlyModelViewSet

Документация: https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset

Объединяем всё, что мы уже знаем.

И получаем класс `ModelViewSet`, он наследуется от `GenericViewSet` (`ViewSet` + `GenericAPIView`) и всех 5 миксинов, а
значит там описаны методы `list()`, `retrieve()`, `create()`, `update()`, `destroy()`, `perform_create()`,
`perform_update()` и т. д.

А значит мы можем описать сущность, которая принимает модель и сериалайзер, и уже может принимать любые типы запросов и
выполнять любые CRUD действия. Мы можем их переопределить, или дописать еще экшенов, всё что нам может быть необходимо
уже есть.

### Пример ArticleViewSet

```python
from rest_framework import viewsets
from blog.models import Article
from blog.serializers import ArticleSerializer, ArticleListSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    ViewSet для полного CRUD статей блога.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'  # можно использовать 'slug' для красивых URL
```

Этот простой класс уже предоставляет все CRUD операции:
- `GET /articles/` — список статей
- `POST /articles/` — создание статьи
- `GET /articles/{pk}/` — детали статьи
- `PUT /articles/{pk}/` — полное обновление
- `PATCH /articles/{pk}/` — частичное обновление
- `DELETE /articles/{pk}/` — удаление

### Per-action поведение

Разные сериалайзеры для разных действий:

```python
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer  # Краткая информация
        return ArticleSerializer  # Полная информация
```

### ReadOnlyModelViewSet

Для ресурсов, которые можно только читать (например, темы блога):

```python
from blog.models import Topic
from blog.serializers import TopicSerializer


class TopicViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet только для чтения тем блога.
    Доступны только list и retrieve.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
```

### Кастомный ViewSet из миксинов

Можно собрать ViewSet для любых действий, комбинируя миксины:

```python
from rest_framework import mixins, viewsets


class CreateListRetrieveViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    """
    ViewSet с операциями create, list и retrieve.
    Без update и delete.
    """
    pass


# Использование
class CommentViewSet(CreateListRetrieveViewSet):
    """
    Комментарии можно создавать и читать, но не редактировать/удалять.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
```

Чаще всего используются обычные `ModelViewSet`.

### Пагинация

Документация: https://www.django-rest-framework.org/api-guide/pagination/

Как мы помним, для действия `list` используется пагинация. Как это работает?

Если у нас нет необходимости настраивать все вьюсеты отдельно, то мы можем указать такую настройку в `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100
}
```

Пример ответа пагинации (PageNumberPagination):
```json
{"count": 123, "next": ".../?page=3", "previous": null, "results": [ ... ]}
```

### Параметры запросов: PageNumber vs LimitOffset
- PageNumberPagination: page, page_size (пример: /api/books/?page=2&page_size=50)
- LimitOffsetPagination: limit, offset (пример: /api/books/?limit=50&offset=100)
- Советы: ограничивайте максимальный размер страницы (max_page_size), не давайте запрашивать слишком большие выборки

Там мы можем указать тип класса пагинации и размер одной страницы, и все наши запросы уже будут пагинированы.

Также мы можем создать классы пагинаторов, основываясь на нашей необходимости.

```python
from rest_framework.pagination import PageNumberPagination

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000
```

Если нужно указать пагинатор у конкретного вьюсета, то можно это сделать прямо в атрибутах.

```python
from rest_framework import generics

class BillingRecordsView(generics.ListAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingRecordsSerializer
    pagination_class = LargeResultsSetPagination
```

## Декоратор @action

Документация: https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing

Что делать, если вам нужно дополнительное действие, связанное с деталями вашей вью, но ни один из CRUD не подходит? Тут
можно использовать декоратор `@action`, чтобы описать новое действие в этом же вьюсете.

### Пример: публикация и архивирование статей

```python
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from blog.models import Article
from blog.serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    ViewSet для статей с дополнительными действиями.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        """
        Публикация статьи: POST /articles/{pk}/publish/
        """
        article = self.get_object()

        if article.status == 'published':
            return Response(
                {'error': 'Статья уже опубликована'},
                status=status.HTTP_400_BAD_REQUEST
            )

        article.status = 'published'
        article.save()

        serializer = self.get_serializer(article)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def archive(self, request, pk=None):
        """
        Архивирование статьи: POST /articles/{pk}/archive/
        """
        article = self.get_object()
        article.status = 'archived'
        article.save()

        return Response({'status': 'Статья архивирована'})

    @action(detail=False, methods=['get'])
    def published(self, request):
        """
        Список опубликованных статей: GET /articles/published/
        """
        published = self.get_queryset().filter(status='published')

        page = self.paginate_queryset(published)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(published, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def my_articles(self, request):
        """
        Статьи текущего пользователя: GET /articles/my_articles/
        """
        my_articles = self.get_queryset().filter(author=request.user)
        serializer = self.get_serializer(my_articles, many=True)
        return Response(serializer.data)
```

### Параметры @action

| Параметр | Описание |
|----------|----------|
| `detail` | `True` — действие над одним объектом (требует pk), `False` — над коллекцией |
| `methods` | Список HTTP методов: `['get']`, `['post']`, `['get', 'post']` |
| `url_path` | Кастомный путь URL (по умолчанию — имя метода) |
| `url_name` | Кастомное имя URL для `reverse()` |
| `permission_classes` | Отдельные permissions для этого action |
| `serializer_class` | Отдельный сериализатор для этого action |

Пример с кастомным URL:

```python
@action(detail=True, methods=['post'], url_path='set-featured')
def set_featured(self, request, pk=None):
    """
    URL будет: POST /articles/{pk}/set-featured/
    """
    article = self.get_object()
    article.is_featured = True
    article.save()
    return Response({'status': 'Статья добавлена в избранное'})
```

## Роутеры

Документация: https://www.django-rest-framework.org/api-guide/routers/

Роутер — это автоматический генератор URL-адресов для вьюсетов.

### Базовый пример для блога

```python
from rest_framework import routers
from blog.views import ArticleViewSet, TopicViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('articles', ArticleViewSet)
router.register('topics', TopicViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls
```

### SimpleRouter vs DefaultRouter

| Роутер | Особенности |
|--------|-------------|
| `SimpleRouter` | Базовый роутер, генерирует только URL-адреса для ViewSet |
| `DefaultRouter` | Добавляет API root (`/api/`) со списком всех эндпойнтов |

```python
# DefaultRouter создаёт красивую главную страницу API-интерфейса
router = routers.DefaultRouter()  # GET /api/ покажет все доступные эндпоинты
```

### Параметр basename

Если у ViewSet нет `queryset`, нужно указать `basename`:

```python
class ReportViewSet(viewsets.ViewSet):
    """ViewSet без queryset — генерирует отчёты динамически."""

    def list(self, request):
        # Генерация отчётов
        ...

router = routers.DefaultRouter()
router.register('reports', ReportViewSet, basename='report')
```

### Сгенерированные URL

Для `ArticleViewSet` роутер создаст:

```
URL pattern: ^articles/$           Name: 'article-list'
URL pattern: ^articles/{pk}/$      Name: 'article-detail'
URL pattern: ^articles/published/$ Name: 'article-published'  # @action
URL pattern: ^articles/{pk}/publish/$ Name: 'article-publish' # @action
```

### Подключение роутера к urls.py

```python
from django.urls import path, include
from rest_framework import routers
from blog.views import ArticleViewSet, TopicViewSet

router = routers.DefaultRouter()
router.register('articles', ArticleViewSet)
router.register('topics', TopicViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # Другие URL...
]
```

### Роутинг экстра экшенов

Для `@action` декораторов роутер автоматически генерирует URL:

```python
class ArticleViewSet(viewsets.ModelViewSet):
    ...

    @action(methods=['post'], detail=True)
    def publish(self, request, pk=None):
        ...
```

Роутер создаст URL `^articles/{pk}/publish/$` и имя `article-publish`.

### trailing_slash

```python
# По умолчанию URL-адреса заканчиваются на /
router = routers.SimpleRouter()  # /articles/

# Можно отключить
router = routers.SimpleRouter(trailing_slash=False)  # /articles
```

## Вложенные роутеры (Nested Routers)

Для URL-адресов вида `/articles/{article_pk}/comments/` можно использовать библиотеку `drf-nested-routers`:

```bash
pip install drf-nested-routers
```

```python
from rest_framework_nested import routers
from blog.views import ArticleViewSet, CommentViewSet

# Основной роутер
router = routers.DefaultRouter()
router.register('articles', ArticleViewSet)

# Вложенный роутер для комментариев
articles_router = routers.NestedDefaultRouter(router, 'articles', lookup='article')
articles_router.register('comments', CommentViewSet, basename='article-comments')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(articles_router.urls)),
]
```

Это создаст URL-адреса:
- `GET /api/articles/` — список статей
- `GET /api/articles/{pk}/` — детали статьи
- `GET /api/articles/{article_pk}/comments/` — комментарии к статье
- `POST /api/articles/{article_pk}/comments/` — создать комментарий

ViewSet для вложенного ресурса:

```python
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(article_id=self.kwargs['article_pk'])

    def perform_create(self, serializer):
        serializer.save(
            article_id=self.kwargs['article_pk'],
            author=self.request.user
        )
```


## Переопределение методов ViewSet

### `get_queryset()` — фильтрация по пользователю

Метод `get_queryset()` позволяет динамически фильтровать данные:

```python
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        user = self.request.user

        # Для списка — только опубликованные или свои
        if self.action == 'list':
            if user.is_authenticated:
                # Авторизованный видит опубликованные + свои черновики
                return Article.objects.filter(
                    Q(status='published') | Q(author=user)
                )
            # Анонимный видит только опубликованные
            return Article.objects.filter(status='published')

        # Для остальных действий — все статьи (проверка прав в permissions)
        return Article.objects.all()
```

### `perform_create()` — автоматическое добавление автора

Метод `perform_create()` вызывается при создании объекта:

```python
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        """Автоматически устанавливаем автора из request.user"""
        serializer.save(author=self.request.user)
```

### `perform_update()` — логика при обновлении

```python
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_update(self, serializer):
        """Сбрасываем статус при редактировании опубликованной статьи"""
        instance = serializer.instance
        if instance.status == 'published':
            serializer.save(status='draft')  # Требует повторной модерации
        else:
            serializer.save()
```

### `perform_destroy()` — мягкое удаление

```python
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_destroy(self, instance):
        """Мягкое удаление вместо физического"""
        instance.status = 'deleted'
        instance.save()
        # Или: instance.delete() для физического удаления
```

## Полный пример ArticleViewSet

```python
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import Article
from blog.serializers import ArticleSerializer, ArticleListSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    ViewSet для статей блога с полным CRUD и дополнительными действиями.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'

    def get_queryset(self):
        """Фильтрация: опубликованные для всех, черновики только для автора."""
        user = self.request.user

        if self.action == 'list':
            if user.is_authenticated:
                return Article.objects.filter(
                    Q(status='published') | Q(author=user)
                ).select_related('author').prefetch_related('topics')
            return Article.objects.filter(
                status='published'
            ).select_related('author').prefetch_related('topics')

        return Article.objects.all()

    def get_serializer_class(self):
        """Разные сериализаторы для списка и деталей."""
        if self.action == 'list':
            return ArticleListSerializer
        return ArticleSerializer

    def perform_create(self, serializer):
        """Автоматически устанавливаем автора."""
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        """Публикация статьи."""
        article = self.get_object()
        if article.author != request.user:
            return Response(
                {'error': 'Только автор может публиковать статью'},
                status=status.HTTP_403_FORBIDDEN
            )
        article.status = 'published'
        article.save()
        return Response(ArticleSerializer(article).data)

    @action(detail=False, methods=['get'])
    def my_drafts(self, request):
        """Черновики текущего пользователя."""
        drafts = Article.objects.filter(author=request.user, status='draft')
        serializer = ArticleListSerializer(drafts, many=True)
        return Response(serializer.data)
```

---

## Итоги

В этой лекции мы изучили:

1. **Request и Response в DRF**: `request.data`, `request.query_params`, объект `Response`

2. **@api_view**: декоратор для функциональных представлений API

3. **APIView**: базовый класс для Class-Based Views в DRF

4. **GenericAPIView и миксины**: готовые CRUD-операции:
   - `CreateModelMixin`, `ListModelMixin`, `RetrieveModelMixin`
   - `UpdateModelMixin`, `DestroyModelMixin`

5. **Generic-классы**: `ListCreateAPIView`, `RetrieveUpdateDestroyAPIView` и др.

6. **ViewSet и ModelViewSet**: объединение всех CRUD в одном классе

7. **@action**: дополнительные действия (`publish`, `archive`, `my_drafts`)

8. **Роутеры**: автоматическая генерация URL-адресов для ViewSet

9. **Вложенные роутеры**: URL-адреса вида `/articles/{pk}/comments/`

10. **Переопределение методов**: `get_queryset()`, `perform_create()`, `get_serializer_class()`

---

## Домашнее задание

### Практика на занятии

1. Создайте `ArticleViewSet` с полным CRUD для статей блога
2. Добавьте `@action` для публикации статьи
3. Настройте роутер и проверьте все эндпоинты через Browsable API

### Домашняя работа

1. **TopicViewSet** (ReadOnlyModelViewSet):
   - Только чтение тем
   - Добавьте `@action` `articles` для получения статей по теме

2. **CommentViewSet**:
   - CRUD для комментариев
   - `perform_create()` — автоматически добавлять автора
   - `get_queryset()` — фильтрация по статье из URL

3. **Вложенный роутинг**:
   - Настройте URL `/articles/{pk}/comments/`
   - Используйте `drf-nested-routers` или ручную настройку URL

4. **Дополнительные @action для ArticleViewSet**:
   - `archive` — архивирование статьи
   - `featured` — добавление в избранное
   - `by_topic` — фильтрация по теме (query param `?topic=python`)

5. **Пагинация**:
   - Создайте `ArticlePagination` с `page_size=10`
   - Примените к `ArticleViewSet`

---

## Вопросы для самопроверки

1. В чём разница между `@api_view` и `APIView`?
2. Какие миксины нужны для ViewSet только с `list` и `create`?
3. Что делает параметр `detail=True` в декораторе `@action`?
4. Чем `SimpleRouter` отличается от `DefaultRouter`?
5. Когда нужно указывать `basename` при регистрации ViewSet?
6. Как переопределить `get_queryset()` для фильтрации по текущему пользователю?
7. Для чего используется `perform_create()`?
8. Как создать URL вида `/articles/{pk}/comments/`?

---

[← Лекция 27: Что такое API. REST и RESTful. Django REST Framework.](lesson27.md) | [Лекция 29: REST-аутентификация. Авторизация. Permissions. Фильтрация. →](lesson29.md)
