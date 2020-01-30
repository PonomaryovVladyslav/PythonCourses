# Что такое API. REST и RESTful. Django REST Framework.

![](https://www.meme-arsenal.com/memes/6200d14d795eab11d26a3afabed68439.jpg)

## Что же такое API?

Итак, начнём с определения. API (Application Programming Interface) — это интерфейс программирования, интерфейс создания приложений.

В нашем конкретном случае, под API практически всегда будет подразумеваться REST API о котором дальше, но бля нас это эндпоинт (урл на который можно отправить запрос) который выполняет какие-либо действия, или возвращает нам какую либо информацию.

## Что такое REST?

![](https://i1.wp.com/www.ybouglouan.pl/wp-content/uploads/2017/04/rest_api_sortof.jpg)

REST (Representational State Transfer — «передача состояния представления») - по сути, это архитектурный стиль (рекомендации к раззработке), но это в теории, практику рассмотрим дальше.

### Свойства REST архитектуры.

Свойства архитектуры, которые зависят от ограничений, наложенных на REST-системы:

1. **Client-Server**. Система должна быть разделена на клиентов и на серверов. Разделение интерфейсов означает, что, например, клиенты не связаны с хранением данных, которое остается внутри каждого сервера, так что мобильность кода клиента улучшается. Серверы не связаны с интерфейсом пользователя или состоянием, так что серверы могут быть проще и масштабируемы. Серверы и клиенты могут быть заменяемы и разрабатываться независимо, пока интерфейс не изменяется.

2. **Stateless**. Сервер не должен хранить какой-либо информации о клиентах. В запросе должна храниться вся необходимая информация для обработки запроса и если необходимо, идентификации клиента.

3. **Cache**․ Каждый ответ должен быть отмечен является ли он кэшируемым или нет, для предотвращения повторного использования клиентами устаревших или некорректных данных в ответ на дальнейшие запросы.

4. **Uniform Interface**. Единый интерфейс определяет интерфейс между клиентами и серверами. Это упрощает и отделяет архитектуру, которая позволяет каждой части развиваться самостоятельно.

    Четыре принципа единого интерфейса:

    4.1) **Identification of resources (основан на ресурсах)**. В REST ресурсом является все то, чему можно дать имя. Например,пользователь, изображение, предмет (майка, голодная собака, текущая погода) и т.д. Каждый ресурс в REST должен быть идентифицирован посредством стабильного идентификатора, который не меняется при изменении состояния ресурса. Идентификатором в REST является URI.

    4.2) **Manipulation of resources through representations. (Манипуляции над ресурсами через представления)**. Представление в REST используется для выполнения действий над ресурсами. Представление ресурса представляет собой текущее или желаемое состояние ресурса. Например, если ресурсом является пользователь, то представлением может являться XML или HTML описание этого пользователя.

    4.3) **Self-descriptive messages (само-документируемые сообщения)**. Под само-описательностью имеется ввиду, что запрос и ответ должны хранить в себе всю необходимую информацию для их обработки. Не должны быть дополнительные сообщения или кэши для обработки одного запроса. Другими словами отсутствие состояния, сохраняемого между запросами к ресурсам. Это очень важно для масштабирования системы.

    4.4) **HATEOAS (hypermedia as the engine of application state)**. Статус ресурса передается через содержимое body, параметры строки запроса, заголовки запросов и запрашиваемый URI (имя ресурса). Это называется гипермедиа (или гиперссылки с гипертекстом). HATEOAS также означает, что, в случае необходимости ссылки могут содержатся в теле ответа (или заголовках) для поддержки URI , извлечения самого объекта или запрошенных объектов.

5. Layered System. В REST допускается разделить систему на иерархию слоев но с условием, что каждый компонент может видеть компоненты только непосредственно следующего слоя. Например, если вы вызывайте службу PayPal а он в свою очередь вызывает службу Visa, вы о вызове службы Visa ничего не должны знать.

6. Code-On-Demand (опционально). В REST позволяется загрузка и выполнение кода или программы на стороне клиента.

Если выполнены первые 4 пункта и не нарушены 5 и 6, такое приложение называется **RESTful**

**Важно!** Сама архитектура REST не привязана к конкретным технологиям и протоколам, но в реалиях современного Веб, построение RESTful API почти всегда подразумевает использование HTTP и каких-либо распространенных форматов представления ресурсов, например JSON, или, менее популярного сегодня, XML.

### Идемпотентность

![](http://risovach.ru/upload/2015/12/mem/kot-bezyshodnost_100253424_orig_.jpg)

С точки зрения RESTful-сервиса, операция (или вызов сервиса) идемпотентна тогда, когда клиенты могут делать один и тот же вызов неоднократно при одном и том же результате на сервере. Другими словами, создание большого количества идентичных запросов имеет такой же эффект, как и один запрос. Заметьте, что в то время, как идемпотентные операции производят один и тот же результат на сервере, ответ сам по себе может не быть тем же самым (например, состояние ресурса может измениться между запросами).

Методы PUT и DELETE по определению идемпотентны. Тем не менее, есть один нюанс с методом DELETE. Проблема в том, что успешный DELETE-запрос возвращает статус 200 (OK) или 204 (No Content), но для последующих запросов будет все время возвращать 404 (Not Found), Состояние на сервере после каждого вызова DELETE то же самое, но ответы разные.

Методы GET, HEAD, OPTIONS и TRACE определены как безопасные. Это означает, что они предназначены только для получения информации и не должны изменять состояние сервера. Они не должны иметь побочных эффектов, за исключением безобидных эффектов, таких как: логирование, кеширование, показ баннерной рекламы или увеличение веб-счетчика.

По определению, безопасные операции идемпотентны, так как они приводят к одному и тому же результату на сервере. Безопасные методы реализованы как операции только для чтения. Однако безопасность не означает, что сервер должен возвращать тот же самый результат каждый раз.

### Коды состояний HTTP (основные)

![](http://img1.reactor.cc/pics/post/http-status-code-it-http-%D0%BA%D0%BE%D1%82%D1%8D-4397611.jpeg)

1xx: Information

100: Continue

2xx: Success

200: OK

201: Created

202: Accepted

204: No Content

3xx: Redirect

301: Moved Permanently

307: Temporary Redirect

4xx: Client Error

400: Bad Request

401: Unauthorized

403: Forbidden

404: Not Found

5xx: Server Error

500: Internal Server Error

501: Not Implemented

502: Bad Gateway

503: Service Unavailable

504: Gateway Timeout

### Postman

На практике обычно бекенд разработчики вообще не имеют отношения к тому что происходит на фронте (Если ты не фулстек:). А только подготавливают для фронта апи для стандартных CRUD действий.

Для проверки работоспособности API чаще всего используется **postman** скачать можно [ТУТ](https://www.getpostman.com/)

Это программа которая позволяет создавать запросы любой сложности к серверу. Рекомендую разобраться как этим пользоваться подробно.


### Общая информация.

Хоть REST не является протоколом, но в современном вебе это почти всегда HTTP и JSON.

### JSON

JSON (JavaScript Object Notation) - Текстовый формат обмена данными, легко читается, очень похож на словарь в python.

## Как это работает на практике и при чём тут Django

Для Django существует несколько различных пакетов для применения REST архитектуры, но основным является **Django REST Framework** дока [тут](https://www.django-rest-framework.org/)

### Установка

```python
pip install djangorestframework
```

Не забываем добавить в INSTALLED_APPS **'rest_framework'**

## Сериалайзеры

Сериалайзер в DRF - это класс для преобразования данных в требуемый формат (Обычно JSON) в котором могут быть описанны круд операции, валидации, итд.

Допустим у нас есть такая модель:

```python
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']
```

То мы можем описать сериалайзер так:

```python
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
```

Как мы можем этим пользвоатся, в shell:

```python
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print("hello, world")\n')
snippet.save()

serializer = SnippetSerializer(snippet)
serializer.data
# {'id': 2, 'title': '', 'code': 'print("hello, world")\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}
```

Преобразование

```python
import json

string = json.dumps(serializer.data) # Преобразовать JSON в строку
"{'id': 2, 'title': '', 'code': 'print("hello, world")\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}"
json.loads(string) # # Преобразовать cтроку в JSON
# {'id': 2, 'title': '', 'code': 'print("hello, world")\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}
```

Валидация

```python
serializer.is_valid()
serializer.validated_data
# OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
serializer.save()
# <Snippet: Snippet object>
# True
```

Так же мы можем передать в сериалайзер список или кверисет из объектов указав при этом атрибут `many=True`

```python
serializer = SnippetSerializer(Snippet.objects.all(), many=True)
serializer.data
# [OrderedDict([('id', 1), ('title', ''), ('code', 'foo = "bar"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 2), ('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 3), ('title', ''), ('code', 'print("hello, world")'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])]
```

По аналогии с Формами и МоделФормами, у сериалайзеров существуют МоделСериалайзеры

```python
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
```

если создать сериалайзер в таком виде то:

```python
from snippets.serializers import SnippetSerializer
serializer = SnippetSerializer()
print(repr(serializer))
# SnippetSerializer():
#    id = IntegerField(label='ID', read_only=True)
#    title = CharField(allow_blank=True, max_length=100, required=False)
#    code = CharField(style={'base_template': 'textarea.html'})
#    linenos = BooleanField(required=False)
#    language = ChoiceField(choices=[('Clipper', 'FoxPro'), ('Cucumber', 'Gherkin'), ('RobotFramework', 'RobotFramework'), ('abap', 'ABAP'), ('ada', 'Ada')...
#    style = ChoiceField(choices=[('autumn', 'autumn'), ('borland', 'borland'), ('bw', 'bw'), ('colorful', 'colorful')...
```

Чаще всего вы будете пользоваться именно сериалайзерами моделей.

Далее мы будем подробно рассматривать все особенности DRF и как превратить код в API, но в данный момент самым важным для нас является то, что DRF предоставляет для нас полный функционал работы с API, самый простой пример использрования API выглядит так:

```python
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```

### Практика и еще раз практика!

# Домашнее задание:

1. Перечитать теорию.

2. Создать сериалайзеры для 2 разных моделей из любого вашего кода (один модел сериалайзер, и один обычный), и прислать мне скрины создания и валидации объекта. Прислать скрин использования сериалайзера с атрибутом many=True