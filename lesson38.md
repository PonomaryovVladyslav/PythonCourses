# Урок 38. @api_view, APIView, ViewSets, Pagination, Routers

Все мы помним, что веб это в первую очередь Request-Response система.

## Request

Что нового в реквесте.

Дока [тут](https://www.django-rest-framework.org/api-guide/requests/)

Два новых парамера `.data` и `.query_string`

`.data` - данные есть запрос POST, PUT или PATCH, аналог `request.POST` или `request.FILES`

`.query_string` - данные если запрос GET, аналог `request.GET`

И параметры `.auth` и `.authenticate` которые мы рассмотрим на следующей лекции. Она целиком про авторизацию и
пермишены (доступы).

## Response

Дока [тут](https://www.django-rest-framework.org/api-guide/responses/)

В отличие от классической Django, респонсом в рест системе, будет обычный HTTP респонс содержащий набор данных, чаще
всего JSON (но бывает и нет).

Классическая Джанго тоже может возвращать HTTP респонс и быть обработчиком рест архитектуры, но существующий пекедж
сильно упрощает эти процессы.

Для обработки такого респонса, есть специальный объект.

```Response(data, status=None, template_name=None, headers=None, content_type=None)```

Где `data` это данные,

`status` - код ответа (200, 404, 503),

`template_name` - возможность указать темплейт, если необходимо вернуть страницу, а не просто набор данных,

`headers` и `content_type` - хедеры и контент тайп запроса

## Настройка для получения JSON

В современной версии пекеджа DRF, по умолчанию не указан параметр для получения ответа в формате JSON. Это нужно указать
явно, для этого в `settings.py` необходимо добавить:

```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}
```

## @api_view

Дока [тут](https://www.django-rest-framework.org/api-guide/views/#api_view)

Для описания эндпоинта функционально нужно указать декоратор api_view и методы которые он может принимать. Возвращает
всё так же объект респонса.

```python
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

Обратите внимание в пакете рест фреймворка сразу есть заготовленные объекты статуса для ответа

Если попытаться получить доступ методом который не разрешен, запрос будет отклонён с ответом 405 method not allowed

Для передачи параметров используются аргументы функции. (Очень похоже на обычную джанго вью)

```python
@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

Урлы для таких методов описываются точно так же как и для стандартной джанго вью

```python
from snippets.view import snippet_list, snippet_detail

urlpatterns = [
    path('snippets/', snippet_list),
    path('snippets/<int:pk>/', snippet_detail),
]
```

Ответ на гет запрос в этому случае будет выглядеть так:

```json
[
  {
    "id": 1,
    "title": "",
    "code": "foo = \"bar\"\n",
    "linenos": false,
    "language": "python",
    "style": "friendly"
  },
  {
    "id": 2,
    "title": "",
    "code": "print(\"hello, world\")\n",
    "linenos": false,
    "language": "python",
    "style": "friendly"
  }
]
```

Поля будут зависеть от модели и сериалайзера соответсвенно.

Ответ на пост запрос (создание объекта):

```json
http --form POST http://127.0.0.1:8000/snippets/ code="print(123)"

{
"id": 3,
"title": "",
"code": "print(123)",
"linenos": false,
"language": "python",
"style": "friendly"
}
```

## View

Знакомимся с самым подробным сайтом по ДРФ классам [тут](http://www.cdrf.co/)

## APIView

Дока [тут](https://www.django-rest-framework.org/api-guide/views/#class-based-views)

Так же мы можем описать это же через Class Base View, для этого нам нужно наследоваться от APIView

```python
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

Вынесем получение объекта в отдельный метод:

```python
class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

Урлы описываются так же как и для джанго Class Base View:

```python
urlpatterns = [
    path('snippets/', SnippetList.as_view()),
    path('snippets/<int:pk>/', SnippetDetail.as_view()),
]
```

## GenericView

По аналогии с классической Django, существуют заранее описанные CRUD действия.

Как это работает.

Существует класс `GenericAPIView` который наследуется от обычного `APIView`

В нём описаны такие поля как:

- `queryset`, хранит кверисет

- `serializer_class`, хранит сериалайзер

- `lookup_field = 'pk'`, название атрибута в модели который будет отвечать за PK,

- `lookup_url_kwarg = None`, название атрибута в запросе который будет отвечать за `pk`

- `filter_backends = api_settings.DEFAULT_FILTER_BACKENDS`, - фильтры запросов

- `pagination_class = api_settings.DEFAULT_PAGINATION_CLASS`, - пагинация запросов

И методы:

- `get_queryset` - получение кверисета,

- `get_object` - получение одного объекта,

- `get_serializer` - получение объекта сериалайзера,

- `get_serializer_class` - получение класса сериалайзера,

- `get_serializer_context` - получить контекст сериалайзера,

- `filter_queryset` - отфильтровать кверисет,

- `paginator` - объект пагинации,

- `paginate_queryset` - пагинировать кверисет,

- `get_paginated_response` - получить пагинированый ответ.

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

Рассмотрим подробнее,

Это миксин, и без сторонних классов этот функционал работать не будет.

При вызове метода `create` мы предполагаем, что у нас был реквест.

Вызываем метод get_serializer() из класса GenericAPIView, для получения объекта сериалайзера, обратите внимание, что
данные передаются через аттрибут `data` так как, они получены от пользователя. Проверяем данные на валидность (обратите
внимание на атрибут raise_exception, если данные будут не валидны, код сразу вылетит в трейсбек, а значит нам не нужно
отдельно прописывать действия при не валидном сериалайзере), вызываем метод `perform_create` который просто сохраняет
сериалайзер(вызывает `create` или `update` в зависимости от данных), получает хедеры, и возвращает респонс с 201 кодом,
создание успешно.

По аналогии, мы можем рассмотреть остальные миксины.

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

Обратите внимание метод называется `retrieve` и внутри вызывает метод `get_object()` это миксин одиночного объекта

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

Методы `update`, `partial_update`, `perform_update` нужны для обновления объекта, обратите внимание на атрибут `partial`
помните разницу между PUT и PATCH?

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

Аналогично для удаления, методы `destroy` `perform_destroy`

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

Метод `list` получает кверисет, дальше пытается его пагинировать, если получается, возвращает страницу, если нет целый
ответ.

*Важно!* Ни в одном из миксинов не было методов `get`,`post`,`patch`,`put` или `delete`, почему?

Потому что их вызов перенесен в еще одни дополнительные классы

### Generic классы

Вот так выглядят классы которые уже можно использовать. Как это работает? Эти классы наследуют логику работы с данными
из необходимого миксина, общие методы которые актуальны для любого CRUD действия из `GenericAPIView` дальше описываем
методы тех видов запросов которые мы хотим обрабатывать, в которых просто вызываем необходимый метод из миксина.

**Переписываются методы `create`, `destroy` итд, а не `get`, `post`!**

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

Допустим мы хотим описать класс при GET запросе получение списка комментариев в которых есть буква `w`, если у нас уже
есть сериалайзер и модель, а при POST создание комментария.

```python
class CommentListView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return super().get_queryset().filter(text__icontains='w')
```

Всё, этого достаточно.

## ViewSet

Дока [тут](https://www.django-rest-framework.org/api-guide/viewsets/)

Классы, которые отвечают за поведение нескольких запросов, и отличаются друг от друга только методом, называются
ViewSet.

Они на самом деле описывают методы, для получения списка действий (list, retrieve, итд), и преобразования их в урлы (об
этом дальше).

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

Разные действия при наличии и отсутствии PK, при GET запросе.

Для описания урлов можно использовать разное описание:

```python
user_list = UserViewSet.as_view({'get': 'list'})
user_detail = UserViewSet.as_view({'get': 'retrieve'})
```

Хоть так никто и не делает, об этом дальше.

## ModelViewSet и ReadOnlyModelViewSet

Дока [тут](https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset)

Объединяем всё что мы уже знаем.

И получаем класс `ModelViewSet`, он наследуется от `GenericViewSet` (`ViewSet` + `GenericAPIView`) и всех 5 миксинов, а
значит там описаны методы `list`, `retrieve`, `create`, `update`, `destroy`, `perform_create`, `perform_update`, итд.

А значит мы можем описать сущность, которая принимает модель и сериалайзер, и уже может принимать любые типы запросов и
выполнять любые CRUD действия. Мы можем их переопределить, или дописать еще экшенов, всё что нам может быть необходимо
уже есть.

Пример:

```python
class AccountViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAccountAdminOrReadOnly]
```

Или если необходим такой же вьюсет только для получения объектов то:

```python
class AccountViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
```

На самом деле можно собрать такой же вьюсет для любых действий, добавляя и убирая миксины.

Например:

```python
from rest_framework import mixins


class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
    pass
```

Чаще всего используются обычные ModelViewSet.

### Пагинация

Дока [тут](https://www.django-rest-framework.org/api-guide/pagination/)

Для действия `list` как мы помним используется пагинация. Как это работает?

Если у нас нет необходимости настраивать все вьюсеты отдельно, то мы можем укать такую настройку в `settings.py`

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}
```

Там мы можем указать тип класса пагинации, и размер одной страницы, и все наши запросы уже будут пагинированы.

Так же мы можем создать классы пагинаторов основываясь на нашей необходимости.

```python
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
class BillingRecordsView(generics.ListAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingRecordsSerializer
    pagination_class = LargeResultsSetPagination
```

## Декоратор action

Дока [тут](https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing)

Что делать если вам нужно дополнительное действие связанное с деталями вашей вью, но ни один из крудов не походит? Тут
можно использовать декоратор @action, что бы описать новое действие в этом же вьюсете

```python
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from myapp.serializers import UserSerializer, PasswordSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False)
    def recent_users(self, request):
        recent_users = self.get_queryset().order_by('-last_login')

        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)
```

Принимает два основных параметра, `detail` - описывает должен ли этот экшен принимать PK (действие над всеми объектами
или над одним конкретным), и `methods` - список http методов, на которые должен срабатывать action.

Есть и другие, например классы пермишенов, или имя.

## Роутеры

Дока [тут](https://www.django-rest-framework.org/api-guide/routers/)

Роутер, это автоматический генератор урлов для вьюсетов.

```python
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'accounts', AccountViewSet)
urlpatterns = router.urls
```

В методе `register` принимает два параметра, на каком слове основывать урлы, и для какого вьюсета.

Если у вьюсета нет параметра `queryset`, то нужно указать поле `basename` если нет, то автоматически будет использовано
имя модели, маленькими буквами.

Урлы будут сгенерированы автоматически и им будут автоматически присвоены имена:

```
URL pattern: ^users/$ Name: 'user-list'
URL pattern: ^users/{pk}/$ Name: 'user-detail'
URL pattern: ^accounts/$ Name: 'account-list'
URL pattern: ^accounts/{pk}/$ Name: 'account-detail'
```

Чаще всего роутеры к урлам добавляются вот такими способами:

```python
urlpatterns = [
    path('forgot-password', ForgotPasswordFormView.as_view()),
    path('api/', include(router.urls)),
]
```

### Роутинг экстра экшенов

Допустим есть такой экстра экшен

```python
from rest_framework.decorators import action


class UserViewSet(ModelViewSet):
    ...

    @action(methods=['post'], detail=True)
    def set_password(self, request, pk=None):
        ...
```

то роутер автоматически сгенерирует урл `^users/{pk}/set_password/$` и имя `user-set-password`

Класс `SimpleRouter` может принимать параметр `trailing_slash=False` True или False, по дефолту тру, поэтому все апи,
должны принимать урлы заканчивающиеся на `/`, если указать явно, то будет принимать всё без `/`.

## Практика/домашка

Создать две модели. Книга и Автор связанные через ForeignKey, у автора есть имя и возраст. У книги есть название.

1) Полный круд для двух объектов, книга и автор, должны работать все виды запросов через постман

2) При создании книги добавлять в конце названия символ "!"

3) Для метода GET книги, добавить опциональный параметр author_age, если он указан, и там число, то отображать только
   книги, если возраст автора больше или равен указанного.

4) Для метода GET автора, добавить опциональный параметр book_name, для фильтрации авторов у которых есть книги, у
   которых название частично совпадают с указанным параметром. (Например, если у автора есть только одна книга "Азбука",
   то по запросу "бук" этот автор должен быть в списке, по запросу "ква", нет)

5) Добавить отдельный экшен, что бы получать объект автора с полем books, в котором будут лежать id всех книг этого
   автора