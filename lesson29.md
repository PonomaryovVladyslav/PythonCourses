# Лекция 29. Что такое API. REST и RESTful. Django REST Framework.

![](https://project-static-assets.s3.amazonaws.com/APISpreadsheets/APIMemes/ServersCooksExample.jpeg)

## Что же такое API?

Итак, начнём с определения. API (Application Programming Interface) — это интерфейс программирования, интерфейс создания
приложений.

В нашем конкретном случае под API практически всегда будет подразумеваться REST API, о котором мы поговорим дальше.  
Сейчас для нас - это endpoint (url, на который можно отправить запрос), который выполняет какие-либо действия или
возвращает нам информацию.

## Что такое REST?

![](https://images.ctfassets.net/vwq10xzbe6iz/5sBH4Agl614xM7exeLsTo7/9e84dce01735f155911e611c42c9793f/rest-api.png)

REST (Representational State Transfer — «передача состояния представления») - это архитектурный стиль
(рекомендации к разработке), но это в теории, практику рассмотрим дальше.

![](https://automated-testing.info/uploads/default/original/2X/e/eaf77634076d45e18c501abf936a9a8ad1913bb4.png)

### Свойства REST архитектуры.

Свойства архитектуры, которые зависят от ограничений, наложенных на REST-системы:

1. **Client-Server**. Система должна быть разделена на клиентов и на сервер(ы). Разделение интерфейсов означает, что
   клиенты не связаны с хранением данных, которое остается внутри каждого сервера, так что мобильность кода
   клиента улучшается. Серверы не связаны с интерфейсом пользователя или состоянием, так что серверы могут быть проще и
   масштабируемы. Серверы и клиенты могут быть заменяемы и разрабатываться независимо, пока интерфейс не изменяется.

2. **Stateless**. Сервер не должен хранить какой-либо информации о клиентах. В запросе должна храниться вся необходимая
   информация для обработки запроса и, если необходимо, идентификации клиента.

3. **Cache**․ Каждый ответ должен быть отмечен, является ли он кэшируемым или нет, для предотвращения повторного
   использования клиентами устаревших или некорректных данных в ответ на дальнейшие запросы.

4. **Uniform Interface**. Единый интерфейс определяет интерфейс между клиентами и серверами. Это упрощает и отделяет
   архитектуру, которая позволяет каждой части развиваться самостоятельно.

   Четыре принципа единого интерфейса:

   4.1) **Identification of resources (основан на ресурсах)**. В REST ресурсом является все то, чему можно дать имя.
   Например, пользователь, изображение, предмет (майка, голодная собака, текущая погода) и т. д. Каждый ресурс в REST
   должен быть идентифицирован посредством стабильного идентификатора, который не меняется при изменении состояния
   ресурса. Идентификатором в REST является URI.

   4.2) **Manipulation of resources through representations. (Манипуляции над ресурсами через представления)**.
   Представление в REST используется для выполнения действий над ресурсами. Представление ресурса представляет собой
   текущее или желаемое состояние ресурса. Например, если ресурсом является пользователь, то представлением может
   являться XML или HTML описание этого пользователя.

   4.3) **Self-descriptive messages (само-документируемые сообщения)**. Под само-описательностью имеется в виду, что
   запрос и ответ должны хранить в себе всю необходимую информацию для их обработки. Не должны быть дополнительные
   сообщения или кэши для обработки одного запроса. Другими словами, отсутствие состояния, сохраняемого между запросами
   к
   ресурсам. Это очень важно для масштабирования системы.

   4.4) **HATEOAS (hypermedia as the engine of application state)**. Статус ресурса передается через содержимое body,
   параметры строки запроса, заголовки запросов и запрашиваемый URI (имя ресурса). Это называется гипермедиа (или
   гиперссылки с гипертекстом). HATEOAS также означает, что в случае необходимости ссылки могут содержаться в теле
   ответа (или заголовках) для поддержки URI, извлечения самого объекта или запрошенных объектов.

5. Layered System. В REST допускается разделить систему на иерархию слоев, но с условием, что каждый компонент может
   видеть компоненты только непосредственно следующего слоя. Например, если вы вызываете службу PayPal, а она в свою
   очередь вызывает службу Visa, вы о вызове службы Visa ничего не должны знать.

6. Code-On-Demand (опционально). В REST позволяется загрузка и выполнение кода или программы на стороне клиента.

Если выполнены первые 4 пункта и не нарушены 5 и 6, такое приложение называется **RESTful**

**Важно!** Сама архитектура REST не привязана к конкретным технологиям и протоколам, но в реалиях современного WEB,
построение RESTful API почти всегда подразумевает использование HTTP и каких-либо распространенных форматов
представления ресурсов, например, JSON, или менее популярного сегодня XML.

### Идемпотентность

![](http://risovach.ru/upload/2015/12/mem/kot-bezyshodnost_100253424_orig_.jpg)

С точки зрения RESTful-сервиса операция (или вызов сервиса) идемпотентна тогда, когда клиенты могут делать один и тот
же вызов неоднократно при одном и том же результате на сервере. Другими словами, создание большого количества идентичных
запросов имеет такой же эффект, как и один запрос. Заметьте, что в то время, как идемпотентные операции производят один
и тот же результат на сервере, ответ сам по себе может не быть тем же самым (например, состояние ресурса может
измениться между запросами).

Методы PUT и DELETE по определению идемпотентны. Тем не менее есть один нюанс с методом DELETE. Проблема в том, что
успешный DELETE-запрос возвращает статус 200 (OK) или 204 (No Content), но для последующих запросов будет все время
возвращать 404 (Not Found). Состояние на сервере после каждого вызова DELETE то же самое, но ответы разные.

Методы GET, HEAD, OPTIONS и TRACE определены как безопасные. Это означает, что они предназначены только для получения
информации и не должны изменять состояние сервера. Они не должны иметь побочных эффектов, за исключением безобидных
эффектов таких как: логирование, кеширование, показ баннерной рекламы или увеличение веб-счетчика.

По определению, безопасные операции идемпотентны, так как они приводят к одному и тому же результату на сервере.
Безопасные методы реализованы как операции только для чтения. Однако безопасность не означает, что сервер должен
возвращать тот же самый результат каждый раз.

### Коды состояний HTTP (основные)

![](http://img1.reactor.cc/pics/post/http-status-code-it-http-%D0%BA%D0%BE%D1%82%D1%8D-4397611.jpeg)

Полный список кодов состояний [тут](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml).

#### 1xx: Information

100: Continue

#### 2xx: Success

200: OK

201: Created

202: Accepted

204: No Content

#### 3xx: Redirect

301: Moved Permanently

307: Temporary Redirect

#### 4xx: Client Error

400: Bad Request

401: Unauthorized

403: Forbidden

404: Not Found

#### 5xx: Server Error

500: Internal Server Error

501: Not Implemented

502: Bad Gateway

503: Service Unavailable

504: Gateway Timeout

![](https://project-static-assets.s3.amazonaws.com/APISpreadsheets/APIMemes/StatusCodeBad.jpeg)

### Postman

На практике обычно backend-разработчики вообще не имеют отношения к тому, что происходит на фронте (если ты не
fullstack`:)`). А только подготавливают для фронта API для различных действий, чаще всего CRUD.

Для проверки работоспособности API чаще всего используется **postman** скачать можно [ТУТ](https://www.getpostman.com/)

> Это программа, которая позволяет создавать запросы любой сложности к серверу. Рекомендую тщательно разобраться, как
> этим
> пользоваться.


> Хоть REST и не является протоколом, но в современном вебе это почти всегда HTTP и JSON.

> JSON (JavaScript Object Notation) - текстовый формат обмена данными, легко читается, очень похож на словарь в Python.

## Как это работает на практике и при чём тут Django?

Для Django существует несколько различных пакетов для применения REST архитектуры, но основным является **Django REST
Framework** дока [тут](https://www.django-rest-framework.org/).

### Установка

```pip install djangorestframework```

Не забываем добавить в INSTALLED_APPS **'rest_framework'**

## Сериализация

![](https://miro.medium.com/v2/resize:fit:1200/1*-vfzWQ94BCBPJ1T4s2YbVA.png)

Что такое сериализация?

**Сериализация** и **десериализация** — это процессы, связанные с преобразованием данных, которые часто используются в
веб-разработке для обмена информацией между сервером и клиентом или между различными системами.

Сериализация — это процесс преобразования сложных объектов (например, объектов в языке программирования, таких как
словари, списки, классы) в формат, который можно передать или сохранить, например, в строку. Этот формат может быть
отправлен через сеть, записан в файл или сохранен в базе данных.

В вебе наиболее часто используются следующие форматы сериализации:

- **JSON (JavaScript Object Notation)**: Чаще всего используется в веб-разработке. Пример:
  объект `{"name": "John", "age": 30}` преобразуется в строку `'{ "name": "John", "age": 30 }'`.
- **XML (eXtensible Markup Language)**: Менее популярен в современном вебе, но все еще используется в некоторых
  системах.

### Десериализация

Десериализация — это обратный процесс, при котором строка или другой формат данных преобразуется обратно в объект или
структуру данных, которую может использовать программа. Например, строка JSON может быть десериализована в объект
JavaScript или Python, который затем можно использовать в коде.

### Пример использования в вебе

1. **Сериализация**: Допустим, у вас есть объект на сервере, который вы хотите отправить клиенту через HTTP. Этот объект
   нужно сначала сериализовать в JSON:
   ```python
   user = {"name": "John", "age": 30}
   user_json = json.dumps(user)
   # user_json = '{"name": "John", "age": 30}'
   ```

2. **Десериализация**: Когда клиент получает этот JSON, он может десериализовать его обратно в объект:
   ```javascript
   let user = JSON.parse('{"name": "John", "age": 30}');
   // user = {name: "John", age: 30}
   ```

Эти процессы важны для взаимодействия между разными частями системы или даже между разными системами, так как они
позволяют передавать сложные структуры данных в стандартных форматах, которые понимают и сервер, и клиент.

### Сериалайзер в DRF

Сериалайзер в DRF - это класс для преобразования данных из того который пришел от пользователя в реквесте в понятный для
python-а и наоборот.

Допустим у нас есть такая модель:

```python
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
```

#### Сериалайзер на основе `Serializer`

Обычный `Serializer` требует явного указания всех полей. И описания того как мы собираемся создавать или обновлять
объекты.

```python
from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255)
    published_date = serializers.DateField()
    isbn = serializers.CharField(max_length=13)
    price = serializers.DecimalField(max_digits=6, decimal_places=2)

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
```

#### Сериализация данных

```python
book = Book.objects.get(id=1)
serializer = BookSerializer(book)
print(serializer.data)
```

Я могу передать в сериалайзер объект модели и он автоматически преобразует его в `JSON` (Если я не поменял стандартные
настройки, могут быть и другие форматы)

Код выше вернет нам такую структуру данных

```python
{
    "title": "Example Book",
    "author": "John Doe",
    "published_date": "2023-08-10",
    "isbn": "1234567890123",
    "price": "19.99"
}
```

#### Десериализация данных

```python
data = {
    "title": "New Book",
    "author": "Jane Smith",
    "published_date": "2024-08-12",
    "isbn": "9876543210123",
    "price": "25.50"
}

serializer = BookSerializer(data=data)
if serializer.is_valid():
    book = serializer.save()
    print(book)  # Book object
else:
    print(serializer.errors)
```

Обратите внимание мы использовали тот же самый сериалайзер!

Что изменилось?

- Мы использовали `data=`, именованый аргумент дает сериалайзеру понять, что мы десериализуем данные!
- Нам необходимо валидировать данные. Данные полученные от пользователя обязательно нужно валидировать! (об этом дальше)
- У сериалайзера есть метод `.save()`, который вызовет `.create()` или `.update()`, в зависимости от переданных в него
  параметров.

### Сериалайзер на основе `ModelSerializer`

`ModelSerializer` упрощает работу, автоматически генерируя поля на основе модели.

```python
from rest_framework import serializers


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn', 'price']
```

> И в нем уже прописаны `create` и `update`

Пользоваться точно так же как и обычным

`ModelSerializer` значительно упрощает создание сериалайзеров, автоматически генерируя поля на основе модели.
Обычный `Serializer` предоставляет больше контроля, но требует явного описания каждого поля и методов `create`
и `update`. Оба подхода позволяют эффективно работать с сериализацией и десериализацией данных в Django.

## Поля и их особенности

Дока [тут](https://www.django-rest-framework.org/api-guide/fields/)

Любое из полей может иметь такие аргументы:

`read_only` - поле только для чтения. Используется для полей, которые не планируются к заполнению (например, время
создания комментария), но планируются к чтению (например, отобразить, когда был написан комментарий). Такие поля не
принимаются при создании или изменении. По дефолту False.

`write_only` - ровно наоборот. Поля, не планируемые для отображения, но необходимые для записи (пароль, номер карточки,
и т. д.). По дефолту False.

`required` - обязательность поля. Поле, которое можно не указывать при создании/изменении, но его же может не быть при
чтении, допустим, отчества. По дефолту True.

`default` - значение по умолчанию, если не указано ничего другого. Не поддерживается при частичном обновлении.

`allow_null` - позволить значению поля быть None. По дефолту False.

`validators` - список валидаторов, о нём поговорим ниже.

`error_messages` - словарь с кодом ошибок.

### source - о нем детальнее

1. **Переименование поля**: Если поле в модели имеет одно имя, но вы хотите, чтобы в API оно отображалось под другим
   именем.

2. **Доступ к вложенным объектам**: Можно обращаться к полям, которые находятся глубже в иерархии связанных объектов.

3. **Вызов метода**: Позволяет использовать метод объекта вместо простого поля.

4. **Использование аннотированных полей**: Можно передать имя аннотированного поля, которое было добавлено в queryset с
   помощью `annotate()`.

###№ Примеры использования

1. **Переименование поля**

   Допустим, у нас есть модель `Book`, у которой есть поле `title`, но в API мы хотим, чтобы это поле отображалось
   как `book_title`:

   ```python
   from rest_framework import serializers

   class BookSerializer(serializers.ModelSerializer):
       book_title = serializers.CharField(source='title')

       class Meta:
           model = Book
           fields = ['book_title', 'author', 'published_date']
   ```

   В этом случае, поле `title` в модели будет переименовано в `book_title` в ответе API.

2. **Доступ к вложенному объекту**

   Пусть есть связанные модели `Author` и `Book`, где каждая книга связана с автором через ForeignKey:

   ```python
   class Author(models.Model):
       name = models.CharField(max_length=100)

   class Book(models.Model):
       title = models.CharField(max_length=200)
       author = models.ForeignKey(Author, on_delete=models.CASCADE)
   ```

   Если вы хотите показать имя автора вместе с данными книги, используя поле `author_name` в сериалайзере:

   ```python
   class BookSerializer(serializers.ModelSerializer):
       author_name = serializers.CharField(source='author.name')

       class Meta:
           model = Book
           fields = ['title', 'author_name']
   ```

   Здесь `source='author.name'` позволяет получить значение поля `name` модели `Author`, связанной с `Book`.

3. **Вызов метода**

   Иногда вам нужно использовать метод модели, чтобы вычислить значение для поля сериалайзера:

   ```python
   class Book(models.Model):
       title = models.CharField(max_length=200)
       publication_date = models.DateField()

       def is_recently_published(self):
           return self.publication_date >= timezone.now() - timedelta(days=30)

   class BookSerializer(serializers.ModelSerializer):
       recently_published = serializers.BooleanField(source='is_recently_published')

       class Meta:
           model = Book
           fields = ['title', 'recently_published']
   ```

   В этом примере `source='is_recently_published'` позволяет использовать метод `is_recently_published` для определения
   значения поля `recently_published`.

Есть и другие, но эти наиболее используемые.

У разных полей могут быть свои атрибуты, такие как максимальная длина, или количество знаков после запятой.

Виды полей по аналогии с моделями и формами могут быть практически какими угодно, за деталями в доку.

### Специфичные поля

`ListField` - поле для передачи списка.
Сигнатура `ListField(child=<A_FIELD_INSTANCE>, allow_empty=True, min_length=None, max_length=None)`

```python
scores = serializers.ListField(
    child=serializers.IntegerField(min_value=0, max_value=100)
)
```

DictField - поле для передачи словаря. Сигнатура `DictField(child=<A_FIELD_INSTANCE>, allow_empty=True)`

```python
document = DictField(child=CharField())
```

HiddenField - скрытое поле, может быть нужно для валидаций.

```python
modified = serializers.HiddenField(default=timezone.now)
```

`SerializerMethodField` - поле, основанное на методе.

Сигнатура: `SerializerMethodField(method_name=None)`, `method_name` - название метода, по дефолту `get_<field_name>`

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

По аналогии с формами мы можем добавить валидацию каждого отдельного поля при помощи метода `validate_<field_name>`

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

Возвращает значение или возбуждает ошибку валидации.

Также валидация может быть осуществлена на уровне объекта. Метод `validate()`.

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

Также можно прописать валидаторы как отдельные функции:

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

Также мы можем передать в сериалайзер список или queryset из объектов, указав при этом атрибут `many=True`

```python
serializer = SnippetSerializer(Snippet.objects.all(), many=True)
serializer.data
# [OrderedDict([('id', 1), ('title', ''), ('code', 'foo = "bar"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 2), ('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 3), ('title', ''), ('code', 'print("hello, world")'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])]
```

### Вложенные сериалайзеры:

Сериалайзер может быть полем другого сериалайзера. Такие сериалайзеры называются вложенными.

```python
class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)


class CommentSerializer(serializers.Serializer):
    user = UserSerializer()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
```

Совмещаем с предыдущими знаниями и получаем вложенное поле с атрибутом `many=True`, а значит оно принимает список или
queryset таких объектов:

```python
class CommentSerializer(serializers.Serializer):
    user = UserSerializer(required=False)
    edits = EditItemSerializer(many=True)  # A nested list of 'edit' items.
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
```

### Еще раз, сериализация и десериализация:

Обратите внимание, что когда мы обрабатываем данные, полученные от пользователя (например запрос), то мы передаём
данные в сериалайзер через атрибут, `data=` и после этого обязаны провалидировать данные, так как там могут быть ошибки:

```python
serializer = CommentSerializer(data={'user': {'email': 'foobar', 'username': 'doe'}, 'content': 'baz'})
serializer.is_valid()
# False
serializer.errors
# {'user': {'email': ['Enter a valid e-mail address.']}, 'created': ['This field is required.']}
```

Если ошибок нет, то данные будут находиться в атрибуте `validated_data`.

Но если мы сериализуем данные, которые мы взяли из базы, то у нас нет необходимости их валидировать. Мы передаём их без
каких-либо атрибутов, данные будут находиться в атрибуте `data`:

```python
comment = Comment.objects.first()
serializer = CommentSerializer(comment)
serializer.data
```

### Метод save()

У Serializer по аналогии с ModelForm есть метод `save()`, но в отличие от ModelForm дополнительные данные
можно передать прямо в атрибуты метода `save()`.

```python
e = EventSerializer(data={'start': "05/05/2021", 'finish': "06/05/2021"})
e.save(description='bla-bla')
```

> Не надо никаких `commit=False`!!

## Связи в сериалайзерах

Все мы знаем, что бывают связи в базе данных. Данные нужно каким-то образом получать, но в случае сериализации нам
часто нет необходимости получать весь объект, а нужны, допустим, только `id` или название. DRF это предусмотрел.

Предположим, у нас есть вот такие модели:

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

Чтобы получить в сериалайзере альбома все его треки, мы можем сделать, например, так:

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

Но есть и другие варианты получения данных.

### StringRelatedField()

```python
class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']
```

Вернёт значение dunder-метода `__str__` для каждого объекта:

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

### PrimaryKeyRelatedField()

```python
class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']
```

Вернёт `id`:

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

### HyperlinkedRelatedField()

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

Вернёт ссылку на обработку объекта. О том, как работает эта магия, поговорим на следующем занятии.

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

### SlugRelatedField()

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

Вернёт то, что указано в атрибуте `slug_field`.

```json
{
  "album_name": "Dear John",
  "artist": "Loney Dear",
  "tracks": [
    "Airport Surroundings",
    "Everything Turns to You",
    "I Was Only Going Out"
  ]
}
```

## Пример чтения и записи вложенных сериалайзеров

Например, если у нас есть модели `Author` и `Book`, где каждый автор может иметь несколько книг, вложенный сериализатор
поможет нам включить информацию о книгах автора в его сериализатор.

### Пример моделей

Допустим, у нас есть две модели: `Author` и `Book`.

```python
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()


class Book(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
```

Здесь у модели `Book` есть внешний ключ `author`, указывающий на модель `Author`.

### Чтение данных с вложенными сериализаторами

Для сериализации данных сначала определим базовые сериализаторы для наших моделей:

```python
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'published_date', 'id']


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Вложенный сериализатор

    class Meta:
        model = Author
        fields = ['name', 'birthdate', 'books']
```

Здесь мы используем `BookSerializer` внутри `AuthorSerializer`, чтобы включить список книг автора в ответ. Поле `books`
имеет атрибут `many=True`, потому что один автор может иметь несколько книг. Кроме того, `read_only=True` говорит о том,
что это поле только для чтения.

Теперь, если мы запросим данные об авторе, мы получим что-то вроде этого:

```json
{
  "name": "J.K. Rowling",
  "birthdate": "1965-07-31",
  "books": [
    {
      "title": "Harry Potter and the Philosopher's Stone",
      "published_date": "1997-06-26",
      "id": 1
    },
    {
      "title": "Harry Potter and the Chamber of Secrets",
      "published_date": "1998-07-02",
      "id": 2
    }
  ]
}
```

### Запись данных с вложенными сериализаторами

Для того чтобы создать или обновить вложенные объекты, нам нужно настроить десериализацию. В этом
случае `BookSerializer` будет использоваться для обработки вложенных данных, когда мы создаем или обновляем автора.

```python
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Author
        fields = ['name', 'birthdate', 'books']

    def create(self, validated_data):
        books_data = validated_data.pop('books')
        author = Author.objects.create(**validated_data)
        for book_data in books_data:
            Book.objects.create(author=author, **book_data)
        return author

    def update(self, instance, validated_data):
        books_data = validated_data.pop('books')
        instance.name = validated_data.get('name', instance.name)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.save()

        # Удаление старых книг
        instance.books.all().delete()

        # Создание новых книг
        for book_data in books_data:
            Book.objects.create(author=instance, **book_data)

        return instance
```

Здесь мы переопределили методы `create` и `update`, чтобы обрабатывать вложенные данные. Мы сначала создаем автора,
затем создаем каждую книгу, связанную с этим автором. В методе `update` мы сначала удаляем старые записи книг и
добавляем новые.

### Пример запроса на создание автора с книгами

Теперь мы можем создать автора и его книги за один запрос:

```json
{
  "name": "George R. R. Martin",
  "birthdate": "1948-09-20",
  "books": [
    {
      "title": "A Game of Thrones",
      "published_date": "1996-08-06"
    },
    {
      "title": "A Clash of Kings",
      "published_date": "1998-11-16"
    }
  ]
}
```

Этот запрос будет обработан нашим `AuthorSerializer`, который создаст автора и его книги.

## Немного забегая вперед

Давайте я покажу вам сколько нужно написать кода, что бы получить RestFull API для одной модели. (Смотрим на экран, тут кода не будет `:)`)
