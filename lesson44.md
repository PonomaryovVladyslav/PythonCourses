# @api_view, APIView, Permissions, ViewSets, Routers

По аналогии с обычным View, у джанго рест фреймворка есть два подхода к написанию эндпоинтов, функциональный и Class Based.

## @api_view

Для описания эндпоинта функционально нужно указать декоратор api_view и методы которые он может принимать.

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

Важным объектом является `Response`, он принимает словарь, и преобразует его в JSON, так же принимает статус (Обратите внимание в пакете рест фреймворка сразу есть заготовленные объекты статуса для ответа)

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
    path('snippets/<int:pk>', snippet_detail),
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

## APIView

Так же мы можем описать это же через Class Base View, для этого нам нужно наследоваться от APIView

```python
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.http import Http404
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

В таком случае название метода будет совпадать с методом запроса.

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
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]
```

## Пермишены

Для описания пермишенов в ДРФ используется аргумент permission_classes:

```python
from rest_framework import permissions

permission_classes = [permissions.IsAuthenticatedOrReadOnly]
```

Существует достаточно много заготовленных пермишенов. Но если нам нужны кастомные то мы можем создать их отнаследовавшись от `permissions.BasePermission` и переписав один из, или оба метода `has_permisson` и `has_object_permission`

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

пермишены можно указывать через запятую если их несколько

```python
permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
```

Если у вас нет доступов, вы получите вот такой ответ:

```python
http POST http://127.0.0.1:8000/snippets/ code="print(123)"

{
    "detail": "Authentication credentials were not provided."
}
```

Для добавления урлов для авторизации, достаточно добавить встроенные:

```python
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
```

## Линкованые урлы.

В сериалайзере можно указать не только модель, но и имя урла к которому можно обратиться (параметр `name`, в переменной path)


```python
class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
```

Если у вас есть урл с именем `snippet-detail` такой запрос будет обрабатываться через него.


## Пагинация

Можно указать пагинацию для всех объектов системы в `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

Или указав пагинацию в классе явно, для этого используется класс пагинации:

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

```python
class BillingRecordsView(generics.ListAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingRecordsSerializer
    pagination_class = LargeResultsSetPagination
```

Ответ с пагинацией выглядит вот так:

```json
{
    "count": 1023,
    "next": "https://api.example.org/accounts/?page=5",
    "previous": "https://api.example.org/accounts/?page=3",
    "results": [
       …
    ]
}
```

Это один из вариантов! Пагинация бывает разная.

## ViewSet
```python
from rest_framework.response import Response

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
```


Вьюсет это класс, описывающий все стандартные CRUD HTTP методы (GET, POST, PUT, PATCH, DELETE)

По аналогии с Class Base View нам достаточно переписать или заменить стандартный метод, для изменения стандартной логики.

Методы HTTP к методам класса:

Все данные возвращаются сериализованными!

GET с указанием pk - retrieve(self, request, pk=None) - получить один объект
GET без указания pk - list(self, request) - получить список объектов
POST (pk нет) - create(self, request) - создать объект
PUT (pk обязателен) - update(self, request, pk=None) - обновить объект полностью
PATCH (pk обязателен) - partial_update(self, request, pk=None) - обновить объект частично
DELETE (pk обязателен) - destroy(self, request, pk=None) - удалить объект

Важные методы:

perform_create - действие с сериалайзером, для создания
perform_update - действие с сериалайзером, при обновлении
perform_destroy - действие с инстансом, при удалении
get_queryset - получение кверисета
get_serializer_class - получение класса сериалайзера

Их намного больше!

Если нам нужно добавить действие связанное с моделью но не попадающее в список стандартных крудов, мы можем сделать это при помощи декоратора action:

```python
from rest_framework.decorators import action
from rest_framework.response import Response

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, methods=['post'])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
```

Декоратор экшен добавляет еще один эндпоинт, принимает параметр detail, описывающий нужно ли нам обрабатывать pk, и параметр methods - принивающий список http методов.

Любой вьюсет это набор миксинов! Мы можем их использовать отдельно от вьюсета, если это необходимо!

## Routers

Для добавления урлов к вьюсетам, используются роутеры.

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
```

Когда мы регистрируем вьюсет в роутере, он автоматически собирает все возможные урлы, для данного вьюсета.

В нашем случае, мы создали такой набор урлов:

```python
/snippets/
/snippets/<int:pk>/
/snippets/<int:pk>/highlight/
/users/
/users/<int:pk>/
```

принимающие разные методы.


### К практике!

# Домашнее задание:

К своему последнему модулю, создать вьюсеты (хотя бы к двум моделям), которые будут реализовывать все базовые CRUD HTTP методы.