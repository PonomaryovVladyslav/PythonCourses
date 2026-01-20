# Лекция 27. Что такое API. REST и RESTful. Django REST Framework.

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

  - ▶ **Лекция 27. Что такое API. REST и RESTful. Django REST Framework**
  - [Лекция 28. @api_view, APIView, ViewSets, Pagination, Routers](lesson28.md)
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

![](https://project-static-assets.s3.amazonaws.com/APISpreadsheets/APIMemes/ServersCooksExample.jpeg)

## Что же такое API?

Итак, начнём с определения. API (Application Programming Interface) — это интерфейс программирования, интерфейс создания
приложений.

В нашем конкретном случае под API практически всегда будет подразумеваться REST API, о котором мы поговорим дальше.
Сейчас для нас — это endpoint (url, на который можно отправить запрос), который выполняет какие-либо действия или
возвращает нам информацию.

## Что такое REST?

![](https://images.ctfassets.net/vwq10xzbe6iz/5sBH4Agl614xM7exeLsTo7/9e84dce01735f155911e611c42c9793f/rest-api.png)

REST (Representational State Transfer — «передача состояния представления») — это архитектурный стиль
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

   4.3) **Self-descriptive messages (самоописательные сообщения)**. Под самоописательностью имеется в виду, что
   запрос и ответ должны хранить в себе всю необходимую информацию для их обработки. Не должны быть дополнительные
   сообщения или кеши для обработки одного запроса. Другими словами, отсутствие состояния, сохраняемого между запросами
   к
   ресурсам. Это очень важно для масштабирования системы.

   4.4) **HATEOAS (hypermedia as the engine of application state)**. Статус ресурса передается через содержимое body,
   параметры строки запроса, заголовки запросов и запрашиваемый URI (имя ресурса). Это называется гипермедиа (или
   гиперссылки с гипертекстом). HATEOAS также означает, что в случае необходимости ссылки могут содержаться в теле
   ответа (или заголовках) для поддержки URI, извлечения самого объекта или запрошенных объектов.
Примечание: в практических DRF‑проектах HATEOAS используют редко — это полезная теоретическая концепция, но её реализация в API не обязательна.


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
Дополнения по методам и статусам:
- Безопасные: GET, HEAD, OPTIONS, TRACE — не изменяют состояние, по определению безопасны и тем самым идемпотентны.
- Идемпотентные: PUT, DELETE — повторные вызовы не меняют результат на сервере; POST — не идемпотентен; PATCH обычно не идемпотентен.
- Рекомендации по статусам:
  - POST (создание) → 201 Created и заголовок Location на ресурс
  - PUT/PATCH (обновление) → 200 OK с телом или 204 No Content без тела
  - DELETE → 204 No Content (без тела)


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
Полезные ссылки:
- Методы HTTP (MDN): https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
- Коды ответов (MDN): https://developer.mozilla.org/en-US/docs/Web/HTTP/Status


![](https://project-static-assets.s3.amazonaws.com/APISpreadsheets/APIMemes/StatusCodeBad.jpeg)

### Postman

На практике обычно backend-разработчики вообще не имеют отношения к тому, что происходит на фронте (если ты не
fullstack `:)`). А только подготавливают для фронта API для различных действий, чаще всего CRUD.

Для проверки API часто используют Postman — скачать: https://www.postman.com/downloads/. Альтернативы: curl/httpie (CLI), VS Code REST Client.

> Это программа, которая позволяет создавать запросы любой сложности к серверу. Рекомендую тщательно разобраться, как
> этим
> пользоваться.


> Хоть REST и не является протоколом, но в современном вебе это почти всегда HTTP и JSON.

> JSON (JavaScript Object Notation) - текстовый формат обмена данными, легко читается, очень похож на словарь в Python.

---

## Альтернативы REST: GraphQL и gRPC

REST — не единственный способ построения API. Существуют и другие подходы, каждый со своими преимуществами. Рассмотрим два наиболее популярных.

### GraphQL

![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/GraphQL_Logo.svg/220px-GraphQL_Logo.svg.png)

**GraphQL** — это язык запросов для API, разработанный Facebook в 2012 году и открытый в 2015. В отличие от REST, где сервер определяет структуру ответа, в GraphQL клиент сам указывает, какие данные ему нужны.

#### Как это работает

В REST для получения статьи с автором и комментариями нужно несколько запросов:

```
GET /api/articles/1/
GET /api/users/5/
GET /api/articles/1/comments/
```

В GraphQL — один запрос:

```graphql
query {
  article(id: 1) {
    title
    content
    author {
      username
      email
    }
    comments {
      text
      author {
        username
      }
    }
  }
}
```

Сервер вернёт ровно те поля, которые запросил клиент — ни больше, ни меньше.

#### Ключевые концепции

- **Query** — запрос данных (аналог GET)
- **Mutation** — изменение данных (аналог POST/PUT/DELETE)
- **Subscription** — подписка на изменения в реальном времени
- **Schema** — строго типизированная схема API

#### Пример Mutation

```graphql
mutation {
  createArticle(input: {
    title: "Новая статья"
    content: "Содержимое..."
  }) {
    id
    title
    createdAt
  }
}
```

#### Преимущества GraphQL

| Преимущество              | Описание                             |
|---------------------------|--------------------------------------|
| **Нет over-fetching**     | Клиент получает только нужные поля   |
| **Нет under-fetching**    | Все связанные данные в одном запросе |
| **Строгая типизация**     | Схема описывает все типы и их связи  |
| **Самодокументируемость** | Схема служит документацией           |
| **Один endpoint**         | Все запросы идут на `/graphql`       |

#### Недостатки GraphQL

| Недостаток                | Описание                                        |
|---------------------------|-------------------------------------------------|
| **Сложность кеширования** | HTTP-кеширование не работает (все запросы POST) |
| **N+1 проблема**          | Требует DataLoader для оптимизации              |
| **Сложнее в реализации**  | Больше кода на сервере                          |
| **Безопасность**          | Сложные запросы могут перегрузить сервер        |

#### GraphQL в Python/Django

- **Graphene-Django** — популярная библиотека для Django
- **Strawberry** — современная альтернатива с поддержкой type hints

```python
# Пример с Graphene-Django
import graphene
from graphene_django import DjangoObjectType
from blog.models import Article


class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'created_at']


class Query(graphene.ObjectType):
    articles = graphene.List(ArticleType)
    article = graphene.Field(ArticleType, id=graphene.Int())

    def resolve_articles(self, info):
        return Article.objects.filter(status='published')

    def resolve_article(self, info, id):
        return Article.objects.get(pk=id)
```

---

### gRPC

![](https://grpc.io/img/logos/grpc-icon-color.png)

**gRPC** (Google Remote Procedure Call) — это высокопроизводительный фреймворк для удалённого вызова процедур, разработанный Google. Использует Protocol Buffers (protobuf) для сериализации и HTTP/2 для транспорта.

#### Как это работает

В отличие от REST (ресурсо-ориентированный) и GraphQL (запросо-ориентированный), gRPC — это **процедурно-ориентированный** подход. Вы вызываете методы на удалённом сервере как локальные функции.

#### Определение сервиса (Protocol Buffers)

```protobuf
// blog.proto
syntax = "proto3";

service BlogService {
  rpc GetArticle(ArticleRequest) returns (Article);
  rpc ListArticles(ListRequest) returns (ArticleList);
  rpc CreateArticle(CreateArticleRequest) returns (Article);
}

message ArticleRequest {
  int32 id = 1;
}

message Article {
  int32 id = 1;
  string title = 2;
  string content = 3;
  string author = 4;
}

message ArticleList {
  repeated Article articles = 1;
}
```

#### Вызов на клиенте (Python)

```python
import grpc
import blog_pb2
import blog_pb2_grpc

# Подключение к серверу
channel = grpc.insecure_channel('localhost:50051')
stub = blog_pb2_grpc.BlogServiceStub(channel)

# Вызов метода как локальной функции
response = stub.GetArticle(blog_pb2.ArticleRequest(id=1))
print(response.title)
```

#### Преимущества gRPC

| Преимущество                   | Описание                                        |
|--------------------------------|-------------------------------------------------|
| **Высокая производительность** | Бинарный формат protobuf в 10x быстрее JSON     |
| **HTTP/2**                     | Мультиплексирование, сжатие заголовков          |
| **Строгая типизация**          | Контракт в .proto файле                         |
| **Streaming**                  | Поддержка потоковой передачи данных             |
| **Кодогенерация**              | Автоматическая генерация клиентов на 10+ языках |

#### Недостатки gRPC

| Недостаток           | Описание                              |
|----------------------|---------------------------------------|
| **Не для браузеров** | Нужен gRPC-Web прокси                 |
| **Сложнее отладка**  | Бинарный формат не читается человеком |
| **Инфраструктура**   | Требует дополнительных инструментов   |
| **Кривая обучения**  | Нужно изучить protobuf                |

#### Типы RPC в gRPC

```protobuf
service BlogService {
  // Unary — один запрос, один ответ
  rpc GetArticle(ArticleRequest) returns (Article);

  // Server streaming — один запрос, поток ответов
  rpc ListArticles(ListRequest) returns (stream Article);

  // Client streaming — поток запросов, один ответ
  rpc UploadImages(stream Image) returns (UploadResult);

  // Bidirectional streaming — поток в обе стороны
  rpc Chat(stream Message) returns (stream Message);
}
```

---

### Сравнение REST, GraphQL и gRPC

| Критерий               | REST                  | GraphQL             | gRPC                |
|------------------------|-----------------------|---------------------|---------------------|
| **Формат данных**      | JSON (текст)          | JSON (текст)        | Protobuf (бинарный) |
| **Протокол**           | HTTP/1.1 или HTTP/2   | HTTP/1.1 или HTTP/2 | HTTP/2              |
| **Типизация**          | Опционально (OpenAPI) | Строгая (Schema)    | Строгая (Protobuf)  |
| **Производительность** | Средняя               | Средняя             | Высокая             |
| **Кеширование**        | Простое (HTTP)        | Сложное             | Сложное             |
| **Браузеры**           | ✅ Полная поддержка    | ✅ Полная поддержка  | ⚠️ Через gRPC-Web   |
| **Streaming**          | ❌ (нужен WebSocket)   | ✅ Subscriptions     | ✅ Встроенный        |
| **Кривая обучения**    | Низкая                | Средняя             | Высокая             |

### Когда что использовать?

| Сценарий                 | Рекомендация                                 |
|--------------------------|----------------------------------------------|
| **Публичный API**        | REST — простой, понятный, хорошо кешируется  |
| **Мобильное приложение** | GraphQL — экономия трафика, гибкие запросы   |
| **Микросервисы**         | gRPC — высокая производительность, streaming |
| **Real-time**            | GraphQL Subscriptions или gRPC Streaming     |
| **Браузерный клиент**    | REST или GraphQL                             |
| **IoT / Embedded**       | gRPC — компактный бинарный формат            |

> **Важно:** В этом курсе мы фокусируемся на REST API с Django REST Framework, так как это наиболее распространённый подход для веб-разработки. Однако понимание альтернатив поможет вам выбрать правильный инструмент для конкретной задачи.

---

## Как это работает на практике и при чём тут Django?

Для Django существует несколько различных пакетов для применения REST архитектуры, но основным является **Django REST
Framework**. Документация: https://www.django-rest-framework.org/

### Установка

```pip install djangorestframework```

Не забываем добавить в INSTALLED_APPS **'rest_framework'**

Примечания:
- DRF по умолчанию рендерит Python-представление данных (serializer.data) в JSON через настроенный рендерер.
- serializer.data — это уже Python-структура (dict/list). В JSON она превращается при возврате Response(serializer.data).

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

Сериалайзер в DRF — это класс для преобразования данных из того, который пришёл от пользователя в реквесте, в понятный для
Python и наоборот.

Мы будем использовать модели блога, которые создали в предыдущих лекциях. Напомним модель `Article`:

```python
from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    """Статья блога"""
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Черновик'
        PUBLISHED = 'published', 'Опубликовано'
        ARCHIVED = 'archived', 'В архиве'

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    topics = models.ManyToManyField('Topic', related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

#### Сериалайзер на основе `Serializer`

Обычный `Serializer` требует явного указания всех полей. И описания того как мы собираемся создавать или обновлять
объекты.

```python
from rest_framework import serializers


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    slug = serializers.SlugField(max_length=200)
    content = serializers.CharField()
    status = serializers.ChoiceField(choices=['draft', 'published', 'archived'])
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.content = validated_data.get('content', instance.content)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
```

#### Сериализация данных

```python
article = Article.objects.get(id=1)
serializer = ArticleSerializer(article)
print(serializer.data)
```

Я могу передать в сериалайзер объект модели и он автоматически преобразует его в `JSON` (Если я не поменял стандартные
настройки, могут быть и другие форматы)

Код выше вернет нам такую структуру данных

```python
{
    "id": 1,
    "title": "Введение в Django REST Framework",
    "slug": "intro-to-drf",
    "content": "Django REST Framework — это мощный инструмент...",
    "status": "published",
    "author": 1,
    "created_at": "2024-01-15T10:30:00Z"
}
```

#### Десериализация данных

```python
data = {
    "title": "Новая статья о Python",
    "slug": "new-python-article",
    "content": "В этой статье мы рассмотрим...",
    "status": "draft"
}

serializer = ArticleSerializer(data=data)
if serializer.is_valid():
    article = serializer.save(author=request.user)  # Передаём автора при сохранении
    print(article)  # Article object
else:
    print(serializer.errors)
```

Обратите внимание мы использовали тот же самый сериалайзер!

Что изменилось?

- Мы использовали `data=`, именованный аргумент дает сериалайзеру понять, что мы десериализуем данные!
- Нам необходимо валидировать данные. Данные полученные от пользователя обязательно нужно валидировать! (об этом дальше)
- У сериалайзера есть метод `.save()`, который вызовет `.create()` или `.update()`, в зависимости от переданных в него
  параметров.
- Мы передали `author=request.user` в метод `save()` — это позволяет добавить данные, которые не приходят от пользователя.

> На практике: удобно валидировать с исключением и не разбирать ошибки вручную
```python
serializer = ArticleSerializer(data=data)
serializer.is_valid(raise_exception=True)
article = serializer.save(author=request.user)
```
Примеры на практике:
```python
# Частичное обновление (например, только статус)
serializer = ArticleSerializer(instance=article, data={'status': 'published'}, partial=True)
serializer.is_valid(raise_exception=True)
serializer.save()

# Передача контекста (например, для доступа к request в сериалайзере)
serializer = ArticleSerializer(data=data, context={'request': request})
serializer.is_valid(raise_exception=True)
serializer.save(author=request.user)
```

### Сериалайзер на основе `ModelSerializer`

`ModelSerializer` упрощает работу, автоматически генерируя поля на основе модели.

```python
from rest_framework import serializers


class ArticleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'content', 'status', 'author', 'created_at']
```

Пример настроек Meta: read_only_fields и extra_kwargs
```python
class ArticleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'content', 'status', 'author', 'created_at']
        read_only_fields = ['id', 'author', 'created_at']
        extra_kwargs = {
            'slug': {'required': False},  # Можно генерировать автоматически
            'content': {'min_length': 10}
        }
```


> И в нем уже прописаны `create` и `update`

Пользоваться точно так же как и обычным

`ModelSerializer` значительно упрощает создание сериалайзеров, автоматически генерируя поля на основе модели.
Обычный `Serializer` предоставляет больше контроля, но требует явного описания каждого поля и методов `create`
и `update`. Оба подхода позволяют эффективно работать с сериализацией и десериализацией данных в Django.

## Поля и их особенности

Документация:
- Поля: https://www.django-rest-framework.org/api-guide/fields/
- Связи: https://www.django-rest-framework.org/api-guide/relations/
- Валидаторы: https://www.django-rest-framework.org/api-guide/validators/

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

### Примеры использования

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
   from django.utils import timezone
   from datetime import timedelta

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
from rest_framework import serializers

document = serializers.DictField(child=serializers.CharField())
```

HiddenField - скрытое поле, может быть нужно для валидаций.

```python
from django.utils import timezone
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
        fields = ['id', 'username', 'days_since_joined']

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
from rest_framework.validators import UniqueTogetherValidator

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

Продолжим работать с моделями нашего блога. Напомню модель `Comment`:

```python
class Comment(models.Model):
    """Комментарий к статье"""
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Комментарий от {self.author.username}'
```

Чтобы получить в сериалайзере статьи все её комментарии, мы можем сделать, например, так:

```python
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'text', 'created_at']


class ArticleWithCommentsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'content', 'author', 'comments']
```

Но есть и другие варианты получения данных.

### StringRelatedField()

```python
class ArticleSerializer(serializers.ModelSerializer):
    comments = serializers.StringRelatedField(many=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'comments']
```

Вернёт значение dunder-метода `__str__` для каждого объекта:

```json
{
  "id": 1,
  "title": "Введение в Django REST Framework",
  "author": 1,
  "comments": [
    "Комментарий от ivan",
    "Комментарий от maria",
    "Комментарий от alex"
  ]
}
```

### PrimaryKeyRelatedField()

```python
class ArticleSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'comments']
```

Вернёт `id`:

```json
{
  "id": 1,
  "title": "Введение в Django REST Framework",
  "author": 1,
  "comments": [
    15,
    16,
    17
  ]
}
```

Для записи используйте queryset:
```python
class ArticleWriteSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())

    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'comments']
```

### HyperlinkedRelatedField()

```python
class ArticleSerializer(serializers.ModelSerializer):
    comments = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='comment-detail'
    )

    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'comments']
```

Вернёт ссылку на обработку объекта. О том, как работает эта магия, поговорим на следующем занятии.

```json
{
  "id": 1,
  "title": "Введение в Django REST Framework",
  "author": 1,
  "comments": [
    "http://www.example.com/api/comments/15/",
    "http://www.example.com/api/comments/16/",
    "http://www.example.com/api/comments/17/"
  ]
}
```
Примечание: для HyperlinkedRelatedField нужен корректный `view_name`, а также наличие `request` в контексте сериалайзера (во ViewSet/GenericAPIView передаётся автоматически; вне CBV передавайте вручную через `context={'request': request}`). Для гиперссылок удобно использовать HyperlinkedModelSerializer.


### SlugRelatedField()

```python
class ArticleSerializer(serializers.ModelSerializer):
    # Получаем username автора вместо id
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'status']
```

Вернёт то, что указано в атрибуте `slug_field`.

```json
{
  "id": 1,
  "title": "Введение в Django REST Framework",
  "author": "ivan_petrov",
  "status": "published"
}
```

## Пример чтения и записи вложенных сериалайзеров

Рассмотрим пример с моделями нашего блога: `Topic` (тема) и `Article` (статья). Одна тема может содержать много статей.

### Напоминание о моделях

```python
from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """Тема/категория для статей"""
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    """Статья блога"""
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Черновик'
        PUBLISHED = 'published', 'Опубликовано'
        ARCHIVED = 'archived', 'В архиве'

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    topics = models.ManyToManyField(Topic, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

Здесь у модели `Article` есть связь ManyToMany с `Topic` — одна статья может относиться к нескольким темам.

### Чтение данных с вложенными сериализаторами

Для сериализации данных сначала определим базовые сериализаторы для наших моделей:

```python
from rest_framework import serializers


class ArticleShortSerializer(serializers.ModelSerializer):
    """Краткая информация о статье для вложенного отображения"""
    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'created_at']


class TopicWithArticlesSerializer(serializers.ModelSerializer):
    articles = ArticleShortSerializer(many=True, read_only=True)  # Вложенный сериализатор

    class Meta:
        model = Topic
        fields = ['id', 'name', 'articles']
```

Здесь мы используем `ArticleShortSerializer` внутри `TopicWithArticlesSerializer`, чтобы включить список статей темы в ответ. Поле `articles`
имеет атрибут `many=True`, потому что одна тема может содержать несколько статей. Кроме того, `read_only=True` говорит о том,
что это поле только для чтения.

Теперь, если мы запросим данные о теме, мы получим что-то вроде этого:

```json
{
  "id": 1,
  "name": "Python",
  "articles": [
    {
      "id": 1,
      "title": "Введение в Django REST Framework",
      "slug": "intro-to-drf",
      "created_at": "2024-01-15T10:30:00Z"
    },
    {
      "id": 2,
      "title": "Продвинутые сериализаторы в DRF",
      "slug": "advanced-drf-serializers",
      "created_at": "2024-01-20T14:00:00Z"
    }
  ]
}
```

### Запись данных с вложенными сериализаторами

Для того чтобы создать статью с комментариями, нам нужно настроить десериализацию. Рассмотрим пример создания статьи вместе с комментариями:

```python
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text']


class ArticleWithCommentsSerializer(serializers.ModelSerializer):
    comments = CommentCreateSerializer(many=True, required=False)

    class Meta:
        model = Article
        fields = ['title', 'slug', 'content', 'comments']

    def create(self, validated_data):
        comments_data = validated_data.pop('comments', [])
        # author передаётся через save(author=request.user)
        article = Article.objects.create(**validated_data)
        for comment_data in comments_data:
            Comment.objects.create(
                article=article,
                author=self.context['request'].user,
                **comment_data
            )
        return article

    def update(self, instance, validated_data):
        comments_data = validated_data.pop('comments', None)
        instance.title = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.content = validated_data.get('content', instance.content)
        instance.save()

        if comments_data is not None:
            # Удаление старых комментариев и создание новых
            instance.comments.all().delete()
            for comment_data in comments_data:
                Comment.objects.create(
                    article=instance,
                    author=self.context['request'].user,
                    **comment_data
                )

        return instance
```

Здесь мы переопределили методы `create` и `update`, чтобы обрабатывать вложенные данные. Мы сначала создаем статью,
затем создаем каждый комментарий, связанный с этой статьёй.

### Пример запроса на создание статьи с комментариями

Теперь мы можем создать статью и её комментарии за один запрос:

```json
{
  "title": "Новая статья о Django",
  "slug": "new-django-article",
  "content": "В этой статье мы рассмотрим...",
  "comments": [
    {
      "text": "Отличная статья!"
    },
    {
      "text": "Спасибо за подробное объяснение"
    }
  ]
}
```

Этот запрос будет обработан нашим `ArticleWithCommentsSerializer`, который создаст статью и её комментарии.

> **Замечание про вложенные сериалайзеры:**
> - DRF не выполняет сложные операции с вложенными записями «из коробки». Частичное обновление списков, сопоставление по id и удаление/создание требуют явной логики.
> - Для нетривиальных случаев рассматривайте отдельные endpoints для вложенных ресурсов или сторонние пакеты (например, `drf-writable-nested`).
> - Обязательно покрывайте такие операции тестами.


## Пример с OneToOne связью: Profile

В нашем блоге у пользователя есть профиль (связь OneToOne). Рассмотрим, как сериализовать такие данные:

```python
class Profile(models.Model):
    """Профиль пользователя"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return f'Профиль {self.user.username}'
```

### Сериализатор профиля

```python
class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'bio', 'avatar', 'website']
        read_only_fields = ['id']
```

Здесь мы используем `source` для доступа к полям связанной модели `User`.

### Вложенный профиль в сериализаторе пользователя

```python
class UserWithProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']
```

Результат:
```json
{
  "id": 1,
  "username": "ivan_petrov",
  "email": "ivan@example.com",
  "profile": {
    "id": 1,
    "username": "ivan_petrov",
    "email": "ivan@example.com",
    "bio": "Python-разработчик",
    "avatar": "/media/avatars/ivan.jpg",
    "website": "https://ivan.dev"
  }
}
```


## SerializerMethodField — вычисляемые поля

`SerializerMethodField` позволяет добавлять вычисляемые поля, которых нет в модели:

```python
class ArticleDetailSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    comments_count = serializers.SerializerMethodField()
    is_recent = serializers.SerializerMethodField()
    topics_list = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'content', 'author', 'author_name',
                  'comments_count', 'is_recent', 'topics_list', 'created_at']

    def get_comments_count(self, obj):
        """Количество комментариев к статье"""
        return obj.comments.count()

    def get_is_recent(self, obj):
        """Статья опубликована за последние 7 дней?"""
        from django.utils import timezone
        from datetime import timedelta
        return obj.created_at >= timezone.now() - timedelta(days=7)

    def get_topics_list(self, obj):
        """Список названий тем"""
        return list(obj.topics.values_list('name', flat=True))
```

Результат:
```json
{
  "id": 1,
  "title": "Введение в Django REST Framework",
  "slug": "intro-to-drf",
  "content": "...",
  "author": 1,
  "author_name": "ivan_petrov",
  "comments_count": 15,
  "is_recent": true,
  "topics_list": ["Python", "Django", "REST API"],
  "created_at": "2024-01-15T10:30:00Z"
}
```

> **Важно:** `SerializerMethodField` всегда `read_only`. Для записи используйте обычные поля или переопределяйте `create`/`update`.

### Оптимизация SerializerMethodField

При использовании `SerializerMethodField` с запросами к БД важно избегать N+1 проблемы:

```python
# Плохо: N+1 запросов
articles = Article.objects.all()
serializer = ArticleDetailSerializer(articles, many=True)

# Хорошо: используем annotate
from django.db.models import Count

articles = Article.objects.annotate(
    comments_count=Count('comments')
).prefetch_related('topics')

# И в сериализаторе используем аннотированное значение:
def get_comments_count(self, obj):
    # Если есть аннотация — используем её
    if hasattr(obj, 'comments_count'):
        return obj.comments_count
    return obj.comments.count()
```


## Немного забегая вперед

Давайте я покажу вам, сколько нужно написать кода, чтобы получить RESTful API для одной модели. (Смотрим на экран, тут кода не будет `:)`)


## Итоги

В этой лекции мы изучили:

1. **Что такое REST и RESTful API** — архитектурный стиль для построения веб-сервисов
2. **Django REST Framework** — мощный инструмент для создания API в Django
3. **Сериализаторы** — преобразование данных между Python-объектами и JSON:
   - `Serializer` — полный контроль, явное описание полей
   - `ModelSerializer` — автоматическая генерация на основе модели
4. **Валидация данных** — встроенные и кастомные валидаторы
5. **Связи в сериализаторах** — различные способы представления связанных объектов:
   - `PrimaryKeyRelatedField` — только id
   - `StringRelatedField` — строковое представление
   - `SlugRelatedField` — конкретное поле
   - `HyperlinkedRelatedField` — ссылки на ресурсы
   - Вложенные сериализаторы — полные данные связанных объектов
6. **SerializerMethodField** — вычисляемые поля
7. **Работа с OneToOne связями** — сериализация профилей пользователей


## Домашнее задание

### Практика на занятии

1. Создайте `ArticleSerializer` с использованием `ModelSerializer` для модели `Article`
2. Добавьте поле `author_name` через `source`
3. Добавьте `SerializerMethodField` для подсчёта комментариев

### Домашняя работа

1. **TopicSerializer** — создайте сериализатор для модели `Topic`:
   - Поля: `id`, `name`, `created_at`
   - Добавьте `articles_count` через `SerializerMethodField`

2. **CommentSerializer** — создайте сериализатор для модели `Comment`:
   - Поля: `id`, `article`, `author`, `text`, `created_at`
   - `author` должен отображаться как username (используйте `SlugRelatedField`)
   - Добавьте валидацию: текст комментария минимум 10 символов

3. **ArticleDetailSerializer** — расширенный сериализатор статьи:
   - Все поля статьи
   - Вложенные комментарии через `CommentSerializer`
   - Список тем через `StringRelatedField`
   - Поле `is_published` (True если status == 'published')

4. **ProfileSerializer** — сериализатор профиля пользователя:
   - Поля профиля + username и email из связанного User
   - Количество статей пользователя
   - Количество комментариев пользователя

5. **Валидация** — добавьте в `ArticleSerializer`:
   - Валидатор уникальности slug
   - Проверку что title не содержит запрещённых слов
   - Кросс-валидацию: если status='published', content должен быть не менее 100 символов

---

[← Лекция 26: Логирование. Middleware. Signals. Messages. Manage commands](lesson26.md) | [Лекция 28: @api_view, APIView, ViewSets, Pagination, Routers →](lesson28.md)
