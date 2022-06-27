# Урок 37. Что такое API. REST и RESTful. Django REST Framework.

![](https://www.meme-arsenal.com/memes/6200d14d795eab11d26a3afabed68439.jpg)

## Что же такое API?

Итак, начнём с определения. API (Application Programming Interface) — это интерфейс программирования, интерфейс создания
приложений.

В нашем конкретном случае, под API практически всегда будет подразумеваться REST API о котором дальше, но для нас это
эндпоинт (урл, на который можно отправить запрос) который выполняет какие-либо действия, или возвращает нам какую либо
информацию.

## Что такое REST?

![](https://i1.wp.com/www.ybouglouan.pl/wp-content/uploads/2017/04/rest_api_sortof.jpg)

REST (Representational State Transfer — «передача состояния представления») - по сути, это архитектурный стиль
(рекомендации к разработке), но это в теории, практику рассмотрим дальше.

### Свойства REST архитектуры.

Свойства архитектуры, которые зависят от ограничений, наложенных на REST-системы:

1. **Client-Server**. Система должна быть разделена на клиентов, и на сервер(ы). Разделение интерфейсов означает, что,
   например, клиенты не связаны с хранением данных, которое остается внутри каждого сервера, так что мобильность кода
   клиента улучшается. Серверы не связаны с интерфейсом пользователя или состоянием, так что серверы могут быть проще и
   масштабируемы. Серверы и клиенты могут быть заменяемы и разрабатываться независимо, пока интерфейс не изменяется.

2. **Stateless**. Сервер не должен хранить какой-либо информации о клиентах. В запросе должна храниться вся необходимая
   информация для обработки запроса и если необходимо, идентификации клиента.

3. **Cache**․ Каждый ответ должен быть отмечен является ли он кэшируемым или нет, для предотвращения повторного
   использования клиентами устаревших или некорректных данных в ответ на дальнейшие запросы.

4. **Uniform Interface**. Единый интерфейс определяет интерфейс между клиентами и серверами. Это упрощает и отделяет
   архитектуру, которая позволяет каждой части развиваться самостоятельно.

   Четыре принципа единого интерфейса:

   4.1) **Identification of resources (основан на ресурсах)**. В REST ресурсом является все то, чему можно дать имя.
   Например, пользователь, изображение, предмет (майка, голодная собака, текущая погода) и т.д. Каждый ресурс в REST
   должен быть идентифицирован посредством стабильного идентификатора, который не меняется при изменении состояния
   ресурса. Идентификатором в REST является URI.

   4.2) **Manipulation of resources through representations. (Манипуляции над ресурсами через представления)**.
   Представление в REST используется для выполнения действий над ресурсами. Представление ресурса представляет собой
   текущее или желаемое состояние ресурса. Например, если ресурсом является пользователь, то представлением может
   являться XML или HTML описание этого пользователя.

   4.3) **Self-descriptive messages (само-документируемые сообщения)**. Под само-описательностью имеется ввиду, что
   запрос и ответ должны хранить в себе всю необходимую информацию для их обработки. Не должны быть дополнительные
   сообщения или кэши для обработки одного запроса. Другими словами отсутствие состояния, сохраняемого между запросами к
   ресурсам. Это очень важно для масштабирования системы.

   4.4) **HATEOAS (hypermedia as the engine of application state)**. Статус ресурса передается через содержимое body,
   параметры строки запроса, заголовки запросов и запрашиваемый URI (имя ресурса). Это называется гипермедиа (или
   гиперссылки с гипертекстом). HATEOAS также означает, что, в случае необходимости ссылки могут содержаться в теле
   ответа (или заголовках) для поддержки URI, извлечения самого объекта или запрошенных объектов.

5. Layered System. В REST допускается разделить систему на иерархию слоев, но с условием, что каждый компонент может
   видеть компоненты только непосредственно следующего слоя. Например, если вы вызываете службу PayPal, а он в свою
   очередь вызывает службу Visa, вы о вызове службы Visa ничего не должны знать.

6. Code-On-Demand (опционально). В REST позволяется загрузка и выполнение кода или программы на стороне клиента.

Если выполнены первые 4 пункта и не нарушены 5 и 6, такое приложение называется **RESTful**

**Важно!** Сама архитектура REST не привязана к конкретным технологиям и протоколам, но в реалиях современного Веб,
построение RESTful API почти всегда подразумевает использование HTTP и каких-либо распространенных форматов
представления ресурсов, например JSON, или, менее популярного сегодня, XML.

### Идемпотентность

![](http://risovach.ru/upload/2015/12/mem/kot-bezyshodnost_100253424_orig_.jpg)

С точки зрения RESTful-сервиса, операция (или вызов сервиса) идемпотентна тогда, когда клиенты могут делать один и тот
же вызов неоднократно при одном и том же результате на сервере. Другими словами, создание большого количества идентичных
запросов имеет такой же эффект, как и один запрос. Заметьте, что в то время, как идемпотентные операции производят один
и тот же результат на сервере, ответ сам по себе может не быть тем же самым (например, состояние ресурса может
измениться между запросами).

Методы PUT и DELETE по определению идемпотентны. Тем не менее есть один нюанс с методом DELETE. Проблема в том, что
успешный DELETE-запрос возвращает статус 200 (OK) или 204 (No Content), но для последующих запросов будет все время
возвращать 404 (Not Found), Состояние на сервере после каждого вызова DELETE то же самое, но ответы разные.

Методы GET, HEAD, OPTIONS и TRACE определены как безопасные. Это означает, что они предназначены только для получения
информации и не должны изменять состояние сервера. Они не должны иметь побочных эффектов, за исключением безобидных
эффектов, таких как: логирование, кеширование, показ баннерной рекламы или увеличение веб-счетчика.

По определению, безопасные операции идемпотентны, так как они приводят к одному и тому же результату на сервере.
Безопасные методы реализованы как операции только для чтения. Однако безопасность не означает, что сервер должен
возвращать тот же самый результат каждый раз.

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

На практике обычно бекенд разработчики вообще не имеют отношения к тому что происходит на фронте (Если ты не фулстек:).
А только подготавливают для фронта апи для различных действий, чаще всего CRUD.

Для проверки работоспособности API чаще всего используется **postman** скачать можно [ТУТ](https://www.getpostman.com/)

Это программа, которая позволяет создавать запросы любой сложности к серверу. Рекомендую разобраться как этим
пользоваться подробно.

### Общая информация.

Хоть REST не является протоколом, но в современном вебе это почти всегда HTTP и JSON.

### JSON

JSON (JavaScript Object Notation) - Текстовый формат обмена данными, легко читается, очень похож на словарь в python.

## Как это работает на практике и при чём тут Django

Для Django существует несколько различных пакетов для применения REST архитектуры, но основным является **Django REST
Framework** дока [тут](https://www.django-rest-framework.org/)

### Установка

```pip install djangorestframework```

Не забываем добавить в INSTALLED_APPS **'rest_framework'**

## Сериалайзеры

Сериалайзер в DRF - это класс для преобразования данных в требуемый формат (Обычно JSON).

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

Как мы можем этим пользоваться, в shell:

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

string = json.dumps(serializer.data)  # Преобразовать JSON в строку
# {'id': 2, 'title': '', 'code': 'print("hello, world")\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}
json.loads(string)  # # Преобразовать cтроку в JSON
# {'id': 2, 'title': '', 'code': 'print("hello, world")\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}
```

## Поля и их особенности

Дока [тут](https://www.django-rest-framework.org/api-guide/fields/)

Любое из полей может иметь такие аргументы:

`read_only` - Поле только для чтения, используется для полей которые не планируются к заполнению (например время
создания комментария), но планируются к чтению (например отобразить когда был написан комментарий). Такие поля не
принимаются при создании или изменении. По дефолту False

`write_only` - Ровно наоборот, поля не планируемые для отображения, но необходимые для записи (Пароль, номер карточки,
итд.). По дефолту False

`required` - Обязательность поля, поле которое можно не указывать при создании\изменении, но его же может и не быть при
чтении, допустим отчества. По дефолту True

`default` - Значение по умолчанию, если не указано ничего другого. Не поддерживается при частичном обновлении,

`allow_null` - Позволить значению поля быть None. По дефолту False.

`source` - Поле значение которого необходимо получить в модели, допустим при помощи какого-то метода (вычисление полного
адреса из его частей при помощи метода модели и декоратора property, `CharField(source='get_full_address')`), или из
какого-то вложенного объекта (Foreign Key на юзера, но необходим только его имейл, а не целый
объект, `EmailField(source='user.email')`). Имеет спец значение `*` обозначает что источник данных будет передан позже,
тогда его нужно будет указать в необходимых методах. По дефолту, это имя поля.

`validators` - Список валидаторов, о нём поговорим ниже

`error_messages` - Словарь с кодом ошибок.

Есть и другие, но это наиболее используемые.

У разных полей могут быть свои атрибуты, такие как максимальная длинна, или кол-знаков после запятой.

Виды полей, по аналогии с моделями и формами, могут быть практически какими угодно, за деталями в доку.

### Специфичные поля

ListField - поле для передачи списка.
Сигнатура `ListField(child=<A_FIELD_INSTANCE>, allow_empty=True, min_length=None, max_length=None)`

```python
scores = serializers.ListField(
    child=serializers.IntegerField(min_value=0, max_value=100)
)
```

DictField - Поле для передачи словаря. Сигнатура `DictField(child=<A_FIELD_INSTANCE>, allow_empty=True)`

```python
document = DictField(child=CharField())
```

HiddenField - Скрытое поле, может быть нужно для валидаций.

```python
modified = serializers.HiddenField(default=timezone.now)
```

SerializerMethodField - Поле основанное на методе

Сигнатура `SerializerMethodField(method_name=None)`, `method_name` - название метода, по дефолту `get_<field_name>`

```python
from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = User

    def get_days_since_joined(self, obj):
        return (now() - obj.date_joined).days
```

## Валидация

```python
serializer.is_valid()
serializer.validated_data
# OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
serializer.save()
# <Snippet: Snippet object>
# True
```

По аналогии с формами, мы можем добавить валидацию каждого отдельного поля, при помощи метода `validate_<field_name>`

```python
from rest_framework import serializers


class BlogPostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()

    def validate_title(self, value):
        """
        Check that the blog post is about Django.
        """
        if 'django' not in value.lower():
            raise serializers.ValidationError("Blog post is not about Django")
        return value
```

Возвращает значение, или рейзит ошибку валидации.

Так же валидация может быть осуществлена на уровне объекта. Метод `validate`.

```python
from rest_framework import serializers


class EventSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=100)
    start = serializers.DateTimeField()
    finish = serializers.DateTimeField()

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['start'] > data['finish']:
            raise serializers.ValidationError("finish must occur after start")
        return data
```

Так же можно прописать валидаторы как отдельные функции:

```python
def multiple_of_ten(value):
    if value % 10 != 0:
        raise serializers.ValidationError('Not a multiple of ten')


class GameRecord(serializers.Serializer):
    score = IntegerField(validators=[multiple_of_ten])
    ...
```

Или указать в Meta, используя уже существующие валидаторы:

```python
class EventSerializer(serializers.Serializer):
    name = serializers.CharField()
    room_number = serializers.IntegerField(choices=[101, 102, 103, 201])
    date = serializers.DateField()

    class Meta:
        # Each room only has one event per day.
        validators = [
            UniqueTogetherValidator(
                queryset=Event.objects.all(),
                fields=['room_number', 'date']
            )
        ]
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

Если создать сериалайзер в таком виде, то:

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

### Вложенные сериалайзеры:

Сериалайзер, может полем другого сериалайзера, такие сериалайзеры, называются вложенными.

```python
class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)


class CommentSerializer(serializers.Serializer):
    user = UserSerializer()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
```

Совмещаем с предыдущими знаниями, и получаем вложенное поле с атрибутом many=True, а значит что оно принимает список или
кверисет таких объектов:

```python
class CommentSerializer(serializers.Serializer):
    user = UserSerializer(required=False)
    edits = EditItemSerializer(many=True)  # A nested list of 'edit' items.
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
```

### Передача данных в разные стороны:

Обратите внимание, что когда мы обрабатываем данные полученные от пользователя(например запрос), то мы передаём данные в
сериалайзер через атрибут, `data=`, и после этого обязаны провалидировать данные, так как там могут быть ошибки:

```python
serializer = CommentSerializer(data={'user': {'email': 'foobar', 'username': 'doe'}, 'content': 'baz'})
serializer.is_valid()
# False
serializer.errors
# {'user': {'email': ['Enter a valid e-mail address.']}, 'created': ['This field is required.']}
```

Если ошибок нет, то данные будут находиться в атрибуте `validated_data`

Но если мы сериализуем данные которые мы взяли из базы то у нас нет необходимости их валидировать. Мы передаём их без
каких либо аттрибутов, данные будут находиться в аттрибуте `data`:

```python
comment = Comment.objects.first()
serializer = CommentSerializer(comment)
serializer.data
```

### Метод save

У моделсериалайзеров, по аналогии с моделформами есть метод `save()`, но в отличие от моделформ, дополнительные данные
можно передать прямо в атрибуты метода `save`.

```python
e = EventSerializer(data={'start': "05/05/2021", 'finish': "06/05/2021"})
e.save(description='bla-bla')
```

## Связи в сериалайзерах

Все мы знаем, что бывают связи в базе данных. Данные нужно каким то образом получать, но в случае сериализации нам,
часто нет необходимости получать весь объект, а нужны, допустим, только id, или название. DRF это предусмотрел.

Предположим у нас есть вот такие модели:

```python
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)


class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)
```

Что бы получить в сериалайзере альбома все его треки, мы можем сделать, например, так:

```python
class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['title', 'duration']


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']
```

Но, есть и другие варианты получение данных.

### StringRelatedField

```python
class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']
```

Вернёт значение меджик метода __str__ для каждого объекта:

```json
{
  "album_name": "Things We Lost In The Fire",
  "artist": "Low",
  "tracks": [
    "1: Sunflower",
    "2: Whitetail",
    "3: Dinosaur Act"
  ]
}
```

### PrimaryKeyRelatedField

```python
class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']
```

Вернёт id:

```json
{
  "album_name": "Undun",
  "artist": "The Roots",
  "tracks": [
    89,
    90,
    91
  ]
}
```

### HyperlinkedRelatedField

```python
class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='track-detail'
    )

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']
```

Вернёт ссылку на обработку объекта, как работает эта магия поговорим на следующем занятии.

```json
{
  "album_name": "Graceland",
  "artist": "Paul Simon",
  "tracks": [
    "http://www.example.com/api/tracks/45/",
    "http://www.example.com/api/tracks/46/",
    "http://www.example.com/api/tracks/47/"
  ]
}
```

### SlugRelatedField

```python
class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']
```

Вернёт то, что указано в атрибуте `slug_field`

```json
{
    "album_name": "Dear John",
    "artist": "Loney Dear",
    "tracks": [
        "Airport Surroundings",
        "Everything Turns to You",
        "I Was Only Going Out",
        ...
    ]
}
```

И другие. О том как сделать записываемые вложенные сериалайзеры и многое другое, читайте в документации.

## Немного забегая вперёд

Далее мы будем подробно рассматривать все особенности DRF и как превратить код в API, но в данный момент самым важным
для нас является то, что DRF предоставляет для нас полный функционал работы с API, самый простой пример использования
API выглядит так:

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

# Практика / Домашнее задание:

1. Создать сериалайзер для обработки данных из 1 задания из лекции про формы (Напишите форму, в которой можно указать
   имя, пол, возраст и уровень владения английским (выпадающим списком), если введенные данные это парень старше 20-и (
   включительно) и уровнем английского B2 выше, или девушка старше 22-ух и уровнем выше чем B1 то перейти на страницу
   где будет написано, что вы нам подходите, или что не подходит соответственно.)

   1.1 Зайти в shell. Заполнить сериалайзер через `data=` данными. Убедиться что валидация работает в соответствии с требованиями. Прислать мне скрины.

2. Создать сериалайзеры для Юзера, Покупки, Товара.

   2.1 Создать объект Юзера, Товара, Покупки, связанных между собой (данные передать через `data=`), прислать мне скрины

   2.2 Получить объекты из базы, передать в сериалайзер без `data=`, посмотреть что у них хранится в атрибуте `.data`

3. Написать сериалайзер для Покупки (новый), который будет хранить вложенный сералайзер Юзера.
   
   3.1 Получить данные любого товара вместе с данными о юзере. Прислать скрины.

4. Написать сериалайзер для Юзера, который будет хранить все его Покупки и выдавать их списком из словарей. (`many=True`)

   4.1 Получить данные любого юзера, прислать скрины.

5*. Дописать сериалайзеры из пунктов 4 и 5 так, что бы можно было создавать объекты. (Это сложно)