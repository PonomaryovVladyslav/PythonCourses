# Лекция 30. Тестирование. Django, REST API.

![](https://preview.redd.it/aom6ubb0b4e71.jpg?width=640&crop=smart&auto=webp&s=d9094222a89d1f8cb0f43285d4ff9c81f274cfee)

## Общая информация

Тестирование - это огромная, нет **ОГРОМНАЯ** тема, настолько огромная, что порождает два отдельных класса сотрудников в
IT индустрии.

## Уровни тестирования

Напомним себе про пирамиду тестирования

![](https://habrastorage.org/storage2/ec3/825/c7f/ec3825c7f0710f9fed6814c89b794ded.jpg)

Существует 4 основных уровня тестирования функционала.

**Модульные тесты (Unit Tests)** - это тесты, проверяющие функционал конкретного модуля минимального размера.
Если вы переписали метод `get_context_data()`, то юнит тестом будет попытка вызвать этот метод с разными входными
данными, и посмотреть на то, что вернёт результат.

**Интеграционные тесты (Integration Tests)** - это вид тестирования, когда проверяется целостность работы системы, без
сторонних средств. Например, вы переписали метод `get_context_data()`, выполняем запрос при помощи кода, и смотрим,
изменилась ли переменная `context` в ответе на наш запрос.

**Приёмочные тесты (Acceptance Tests)** - вид тестов с полной имитацией действий пользователя. При помощи специальных
средств (например, Selenium) мы прописываем код открытия браузера, поиска необходимых элементов на странице, имитируем
ввод данных, нажатие кнопок, переход по ссылкам и т. д.

**Ручные тесты (Manual Tests)** - вид тестов, когда мы полностью повторяем потенциальные действия пользователя.

## Современный инструментарий: pytest и pytest-django

pytest стал стандартом де-факто для тестов в Django/DRF за счёт простоты, фикстур и полезных плагинов.

Установка:
```bash
pip install pytest pytest-django pytest-cov
```

Базовый пример:
```python
import pytest

@pytest.mark.django_db
def test_animals_can_speak(animal_factory):
    lion = animal_factory(name="lion", sound="roar")
    assert lion.speak() == 'The lion says "roar"'
```

Запуск:
```bash
pytest -q
pytest -k speak   # фильтр по имени
pytest --cov=yourpkg --cov-report=term-missing
```

В pytest-django доступны фикстуры: client (Django client), db/transactional_db, settings, monkeypatch и др.

## Тестирование в Django

Вы знаете о существовании `unittest.TestCase`, от которого нужно наследоваться, чтобы создать обычный тест.

У него могут быть метод `setUp()` и `tearDown()` для описания данных, которые нужно выполнить до каждого теста и после
соответственно.

И методы, начинающиеся со слова `test_`, которые описывают сами тесты, для чего используется ключевое слово `assert` или
основанные на нём встроенные методы.

В рамках Django есть свой собственный тест кейс, наследованный от базового `unittest.TestCase`.

![](https://docs.djangoproject.com/en/2.2/_images/django_unittest_classes_hierarchy.svg)

### SimpleTestCase

`SimpleTestCase` наследуется от базового.

#### Что добавляет?

Добавляет `settings.py` в структуру теста и возможность переписать или изменить `settings.py` для теста.

Добавляет `Client`, который используется для написания интеграционных тестов (через него мы будем отправлять запросы).

Добавляет новые методы `assert`:

`assertRedirects` - проверка на то, что URL, на который мы попали, совпадёт с ожидаемым.

`assertContains` - проверка на то, что страница содержит ожидаемую переменную.

`assertNotContains` - проверка на то, что страница не содержит ожидаемую переменную.

`assertFormError` - проверка на то, что форма содержит нужную ошибку.

`assertFormsetError` - проверка на то, что formset содержит нужную ошибку.

`assertTemplateUsed` - проверка на то, что был использован ожидаемый шаблон.

`assertTemplateNotUsed` - проверка на то, что не был использован ожидаемый шаблон.

`assertRaisesMessage` - проверка на то, что на странице присутствует определённое сообщение.

`assertFieldOutput` - проверка на то, что определённое поле содержит ожидаемое значение.

`assertHTMLEqual` - проверка на то, что полученный HTML соответствует ожидаемому.

`assertHTMLNotEqual` - проверка на то, что полученный HTML не соответствует ожидаемому.

Важно: TransactionTestCase заметно медленнее TestCase, так как выполняет полноценную очистку БД между тестами. Используйте его, когда нужно проверить реальное поведение транзакций (commit/rollback, select_for_update, взаимодействие с внешними транзакционными системами).


`assertJSONEqual` - проверка на то, что полученный JSON соответствует ожидаемому.

`assertJSONNotEqual` - проверка на то, что полученный JSON не соответствует ожидаемому.

`assertXMLEqual` - проверка на то, что полученный XML соответствует ожидаемому.

`assertXMLNotEqual` - проверка на то, что полученный XML не соответствует ожидаемому.

### TransactionTestCase


`TransactionTestCase` наследуется от `SimpleTestCase`.

#### Что добавляет?

Добавляет возможность выполнять транзакции в базу данных в рамках теста.

Добавляет атрибут `fixtures` для возможности загружать базовые условия теста из фикстур.

Добавляет атрибут `reset_sequences`, который позволяет сбрасывать последовательности для каждого теста (каждый созданный
объект всегда будет начинаться с id=1)

Добавляет новые методы `assert`:

`assertQuerysetEqual` - проверка на то, что полученный кверисет совпадает с ожидаемым.

`assertNumQueries` - проверка на то, что выполнение функции делает определённое количество запросов в базу.

### TestCase из модуля Django

`TestCase` наследуется от `TransactionTestCase`.

#### Что добавляет?

По сути ничего. :) Немного по другому выполняет запросы в базу (с использованием атомарности), из-за чего
предпочтительнее.

Дополнительный метод `setUpTestData()` для описания данных для теста. Не обязательный.

Это самый часто используемый вид тестов.


Примечание: Django обычно автоматически создаёт тестовую БД (например, `test_<NAME>` для PostgreSQL). Явное указание TEST.NAME требуется редко; убедитесь, что у пользователя БД есть права на создание/удаление.

### LiveServerTestCase

`LiveServerTestCase` наследуется от `TransactionTestCase`.


Ключевые свойства TestCase:
- Каждый тест запускается в транзакции и откатывается (rollback) — быстро и изолированно.
- setUpTestData() выполняется один раз на класс и экономит время на подготовке данных.
- Если нужно проверить поведение транзакций — используйте TransactionTestCase.

#### Что добавляет?

Запускает реальный сервер для возможности открыть проект в браузере. Необходим для написания Acceptance Tests.

Чаще всего в таких тестах запускается сервер и имитация браузера (например, Selenium).

### База данных для тестирования

Для тестов используется отдельная база данных, которая будет указана в переменной `TEST` в переменной `DATABASES` в
файле `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'mydatabaseuser',
        'NAME': 'mydatabase',
        'TEST': {
            'NAME': 'mytestdatabase',
        },
    },
}
```

Эта база будет изначально пустая и будет очищаться после каждого выполненного тест кейса.

**Ваш юзер должен иметь права на создание и очистку базы данных**

### Расположение тестов

Несмотря на то, что Django создаёт для нас в приложении файл `tests.py`, им практически никогда не пользуются.

Существует два самых распространённых способа хранения тестов. Если вам повезло и на вашем проекте есть специальные
тестировщики, то ваша задача - это только юнит тесты.

И тогда в папке приложения создаётся еще одна папка `tests`, в которой уже создаются файлы для тестов различных частей,
например, `test_models.py`, `test_forms.py` и т. д.

![](https://drive.google.com/uc?export=view&id=1E_Tf8H2spWJbSOaaxvWOMiLk4c0bgvUT)

Если вам не повезло, и на проекте вы за автоматических тестеров, то тогда в этой же папке (`tests`) создаётся еще 3
папки `unit`, `integration` и `acceptance`, и уже в них описываются различные тесты.

### Запуск через pytest (рекомендовано)

```bash
pytest -q                 # все тесты
pytest tests/unit -q      # каталог
pytest -k "animals and speak"  # отбор по выражению
pytest --maxfail=1 --disable-warnings -q
pytest --cov=yourpkg --cov-report=term-missing
```


### Запуск тестов

### Выбор инструмента: RequestFactory vs Client и APIRequestFactory vs APIClient

- RequestFactory / APIRequestFactory — юнит-уровень: вызываем view напрямую, middleware и маршрутизация не участвуют. Быстро и изолировано.
- Client / APIClient — интеграционный уровень: запрос проходит через URLConf и middleware. Для API используйте APIClient (форматы, JSON, удобные методы).
- Рекомендация: начинать с APIClient/Client для «сквозных» проверок и использовать *RequestFactory для узконаправленных юнит-тестов view/permission/serializer.


Предположим, что у нас в приложении `animals` есть папка `tests`, в ней папка `unit` и в ней файл `test_models`.

```python
from django.test import TestCase
from myapp.models import Animal


class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
```

То для запуска тестов используется manage-команда `test`

```
# Запустить все тесты в приложении в папке тестов
$./manage.py test animals.tests

# Запустить все тесты в приложении
$./manage.py test animals

# Запустить один тест кейс
$./manage.py test animals.tests.unit.test_models.AnimalTestCase

# Запустить один тест из тест кейса
$./manage.py test animals.tests.unit.test_models.AnimalTestCase.test_animals_can_speak
```

## Специальные инструменты тестирования

### Client

Для проведения `интеграционного` тестирования Django приложения нам необходимо отправлять запросы с клиента (браузера),
функционал для этого нам предоставлен из коробки, и мы можем им воспользоваться:

```python
from django.test import Client

c = Client()
response = c.post('/login/', {'username': 'john', 'password': 'smith'})
response.status_code
200
response = c.get('/customer/details/')
response.content
```

Такой запрос не будет требовать CSRF токен (хотя это тоже можно изменить, если необходимо).

Поддерживает метод `login()`

```python
c = Client()
c.login(username='fred', password='secret')
```

После чего запросы будут от аутентифицированного пользователя.

Метод `force_login()`, принимающий объект юзера, а не логин и пароль.

Метод `logout()`, что делает, догадайтесь сами)

Естественно клиент при желании можно переписать под свои нужды.

Клиент сразу есть в тест кейсе, его нет необходимости создавать, к нему можно обратиться через `self.client`.

```python
class SimpleTest(TestCase):
    def test_details(self):
        response = self.client.get('/customer/details/')
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        response = self.client.get('/customer/index/')
        self.assertEqual(response.status_code, 200)
```

### Загрузка фикстур

Всё очень просто, если у вас лежит файл с фикстурами, то достаточно его просто указать в атрибутах.

```python
from myapp.models import Animal


class AnimalTestCase(TestCase):
    fixtures = ['mammals.json', 'birds']

    def setUp(self):
        # Test definitions as before.
        call_setup_methods()

    def test_fluffy_animals(self):
        # A test that uses the fixtures.
        call_some_test_code()
```

Загрузится файл `mammals.json`, и из него фикстура `birds`.

### Теги для тестов

Существует возможность поставить "тег" на каждый тест, а после запускать только те, что с определённым тегом.

```python

class SampleTestCase(TestCase):

    @tag('fast')
    def test_fast(self):
        ...

    @tag('slow')
    def test_slow(self):
        ...

    @tag('slow', 'core')
    def test_slow_but_core(self):
        ...
```

Или даже целый тесткейс:

```python
@tag('slow', 'core')
class SampleTestCase(TestCase):
    ...
```

После чего запускать с указанием тега.

```
./manage.py test --tag=fast
```

### Тестирование manage-команд

Для этого используется специальный метод `call_command()`:

```python
from io import StringIO
from django.core.management import call_command
from django.test import TestCase


class ClosePollTest(TestCase):
    def test_command_output(self):
        out = StringIO()
        call_command('closepoll', stdout=out)
        self.assertIn('Expected output', out.getvalue())
```

### Пропуск тестов

Тесты можно пропускать в зависимости от условий и деталей запуска.
Дока [тут](https://docs.python.org/3/library/unittest.html#unittest.skipIf)

## Фабрики и юнит тестирование

### Паттерн фабрика

Фабричный метод — если умным текстом, то это порождающий паттерн проектирования, который определяет общий интерфейс для
создания объектов в суперклассе, позволяя подклассам изменять тип создаваемых объектов.

Если по смыслу, то это возможность создать необходимую нам сущность внутри вызова метода.

В Django есть встроенная фабрика для реквеста, зачем это нужно? Нам не для всех проверок нужно делать запрос, часто нам
нужно его только имитировать. Для написания юнит тестов - это самый главный инструмент.

```python
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from .views import MyView, my_view


class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/customer/details')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = my_view(request)
        # Use this syntax for class-based views.
        response = MyView.as_view()(request)
        self.assertEqual(response.status_code, 200)
```

### Тестирование отдельных методов CBV

Для тестирования отдельных методов мы можем использовать метод `setup()`.

Например, если мы заменили `get_context_data()`, то можно сделать так:

```python
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'myapp/home.html'

    def get_context_data(self, **kwargs):
        kwargs['environment'] = 'Production'
        return super().get_context_data(**kwargs)
```

```python
from django.test import RequestFactory, TestCase
from .views import HomeView


class HomePageTest(TestCase):
    def test_environment_set_in_context(self):
        request = RequestFactory().get('/')
        view = HomeView()
        view.setup(request)
        context = view.get_context_data()
        self.assertIn('environment', context)
```

## Тестирование REST API

В Django REST Framework есть достаточно много внутренних похожих процедур и классов, например, своя фабрика реквестов:

```python
from rest_framework.test import APIRequestFactory

# Using the standard RequestFactory API to create a form POST request
factory = APIRequestFactory()
request = factory.post('/notes/', {'title': 'new idea'})
```

По дефолту формат JSON, но это можно изменить:

```python
# Create a JSON POST request
factory = APIRequestFactory()
request = factory.post('/notes/', {'title': 'new idea'}, format='json')
```

А можно вообще указать content type:

```python
request = factory.post('/notes/', json.dumps({'title': 'new idea'}), content_type='application/json')
```

### force_authenticate()

Часто нам необходимо проверять запросы из-под необходимого типа пользователя, но сам по себе логин уже покрыт тестами,
а это значит, что второй раз его проверять нет необходимости, можем просто логиниться.

```python
from rest_framework.test import force_authenticate

factory = APIRequestFactory()
user = User.objects.get(username='olivia')
view = AccountDetail.as_view()

# Make an authenticated request to the view...
request = factory.get('/accounts/django-superstars/')
force_authenticate(request, user=user)
response = view(request)
```

### APIClient

В DRF есть свой клиент для запросов, в котором уже прописаны все необходимые методы запросов (`get()`, `post()`,
и т. д.)

```python
from rest_framework.test import APIClient

client = APIClient()
client.post('/notes/', {'title': 'new idea'}, format='json')
```

### APITestCase (DRF)

Удобный базовый класс, комбинирующий TestCase и APIClient:
```python
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class NotesTests(APITestCase):
    def test_list_anon(self):
        url = reverse('notes-list')
        res = self.client.get(url)
        assert res.status_code == status.HTTP_200_OK
```

#### Авторизация через клиента

Поддерживает метод `login()`, `logout()`и `credentials()`. Метод `login()` принимает логин и пароль, метод
`credentials()` принимает хедеры.

Примеры:

```python
# Make all requests in the context of a logged in session.
client = APIClient()
client.login(username='lauren', password='secret')
```

```python
# Log out
client.logout()
```

```python
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

# Include an appropriate `Authorization:` header on all requests.
token = Token.objects.get(user__username='lauren')
client = APIClient()
client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
```

Также поддерживает форсированную аутентификацию:

```python
user = User.objects.get(username='lauren')
client = APIClient()
client.force_authenticate(user=user)
```

Также можно включить CSRF на этапе создания клиента:

```python
client = APIClient(enforce_csrf_checks=True)
```

Для изменения хедеров можно использовать или стандартные классы, или просто обновлять как словарь:

```python
from requests.auth import HTTPBasicAuth

client.auth = HTTPBasicAuth('user', 'pass')
client.headers.update({'x-test': 'true'})
```

Если вы включили CSRF и хотите им пользоваться при проверках, это можно сделать так:

```python
client = RequestsClient()

# Obtain a CSRF token.
response = client.get('http://testserver/homepage/')
assert response.status_code == 200
csrftoken = response.cookies['csrftoken']

# Interact with the API.
response = client.post('http://testserver/organisations/', json={
    'name': 'MegaCorp',
    'status': 'active'
}, headers={'X-CSRFToken': csrftoken})
assert response.status_code == 200
```

Можно настроить форматы и обработчики для таких тестов.

```python
REST_FRAMEWORK = {
    ...
'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}
```

```python
REST_FRAMEWORK = {
    ...
'TEST_REQUEST_RENDERER_CLASSES': [
    'rest_framework.renderers.MultiPartRenderer',
    'rest_framework.renderers.JSONRenderer',
    'rest_framework.renderers.TemplateHTMLRenderer'
]
}
```


#### Рекомендовано: DjangoModelFactory и SubFactory

```python
import factory
from factory.django import DjangoModelFactory
from django.contrib.auth import get_user_model

User = get_user_model()

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda o: f"{o.username}@example.com")

class PurchaseFactory(DjangoModelFactory):
    class Meta:
        model = Purchase
    owner = factory.SubFactory(UserFactory)
```

## Фабрики для генерации данных

### FactoryBoy

```
pip install factory_boy
```

#### Рекомендовано: DjangoModelFactory и SubFactory

Используйте DjangoModelFactory для моделей Django и SubFactory для связей между моделями — это упростит подготовку данных для API‑тестов и тестов тротлинга.

```python
import factory
from factory.django import DjangoModelFactory
from django.contrib.auth import get_user_model

User = get_user_model()

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda o: f"{o.username}@example.com")

class PurchaseFactory(DjangoModelFactory):
    class Meta:
        model = Purchase
    owner = factory.SubFactory(UserFactory)
```


Прописывание в `setUp()` создание новых объектов может занимать очень много времени. Чтобы это ускорить, упростить и
автоматизировать, можно написать свою фабрику:

```python
import factory
from app.models import User


class UserFactory(factory.Factory):
    firstname = "John"
    lastname = "Doe"

    class Meta:
        model = User
```

На один класс можно создавать несколько объектов фабрик

```
>>>john = UserFactory()
<User: John Doe>
>>>jack = UserFactory(firstname="Jack")
<User: Jack Doe>
```

Также можно использовать разные фабрики в разных местах

```python
class EnglishUserFactory(factory.Factory):
    class Meta:
        model = User

    firstname = "John"
    lastname = "Doe"
    lang = 'en'


class FrenchUserFactory(factory.Factory):
    class Meta:
        model = User

    firstname = "Jean"
    lastname = "Dupont"
    lang = 'fr'
```

```
EnglishUserFactory()
<User: John Doe (en)>
>>> FrenchUserFactory()
<User: Jean Dupont (fr)>
```

Атрибутом может быть другая фабрика. Например, при создании фабрики покупки мы можем указать в качестве покупателя
фабрику юзера

```python
class PurchaseFactory(factory.Factory):
    class Meta:
        model = Purchase

    owner = EnglishUserFactory()
```

```
PurchaseFactory()
<Purchase: 1 John Doe>
```

Можно передавать специальный объект последовательности, при создании каждого нового объекта будет добавляться единица.
Для текущего примера юзернеймы всех созданных юзеров будут `user1`, `user2`, `user3` и т. д.

Sequences

```python
class UserFactory(factory.Factory):
    class Meta:
        model = models.User

    username = factory.Sequence(lambda n: 'user%d' % n)
```

Можно передать специальный объект, который будет вызывать функцию при создании объекта, например, текущее время.

`LazyFunction()`

```python
class LogFactory(factory.Factory):
    class Meta:
        model = models.Log

    timestamp = factory.LazyFunction(datetime.now)
```

```
LogFactory()
<Log: log at 2016-02-12 17:02:34>

# при вызове можно переписать
LogFactory(timestamp=now - timedelta(days=1))
<Log: log at 2016-02-11 17:02:34>
```

Иногда нужно заполнять одни поля на основании других, для этого тоже есть специальный объект.

`LazyAttribute`
Некоторые поля могут быть заполнены при помощи других, например, электронная почта на основе имени пользователя.
`LazyAttribute` обрабатывает такие случаи: он должен получить функцию, принимающую создаваемый объект и
возвращающую значение для поля:

```python
class UserFactory(factory.Factory):
    class Meta:
        model = models.User

    username = factory.Sequence(lambda n: 'user%d' % n)
    email = factory.LazyAttribute(lambda obj: '%s@example.com' % obj.username)
```

```
UserFactory()
<User: user1 (user1@example.com)>

# можно переписать источник
UserFactory(username='john')
<User: john (john@example.com)>

# а можно и само поле
>>> UserFactory(email='doe@example.com')
<User: user3 (doe@example.com)>
```

Наследование фабрик

```python
class UserFactory(factory.Factory):
    class Meta:
        model = User

    firstname = "John"
    lastname = "Doe"


class AdminFactory(UserFactory):
    admin = True
```

### Генерация фейковых данных

#### Fuzzy attributes

Fuzzy позволяет генерировать фейковые данные:

```python
from factory import fuzzy

...


def setUp(self):
    self.username = fuzzy.FuzzyText().fuzz()
    self.password = fuzzy.FuzzyText().fuzz()
    self.user_id = fuzzy.FuzzyInteger(1).fuzz()
```

#### Faker

Faker пришел на замену Fuzzy и в нём гораздо больше всего, его нужно устанавливать.

```
pip install Faker
```

```python
from faker import Faker

fake = Faker()

fake.name()

# 'Lucy Cechtelar'

fake.address()

# '426 Jordy Lodge

# Cartwrightshire, SC 88120-6700'

fake.text()

# 'Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi

# beatae sint laudantium consequatur. Magni occaecati itaque sint et sit tempore. Nesciunt

# amet quidem. Iusto deleniti cum autem ad quia aperiam.

# A consectetur quos aliquam. In iste aliquid et aut similique suscipit. Consequatur qui

# quaerat iste minus hic expedita. Consequuntur error magni et laboriosam. Aut aspernatur

# voluptatem sit aliquam. Dolores voluptatum est.

# Aut molestias et maxime. Fugit autem facilis quos vero. Eius quibusdam possimus est.

# Ea quaerat et quisquam. Deleniti sunt quam. Adipisci consequatur id in occaecati.

# Et sint et. Ut ducimus quod nemo ab voluptatum.'

```

### Использование с Factory Boy

```python
import factory
from myapp.models import Book


class BookFactory(factory.Factory):
    class Meta:
        model = Book

    title = factory.Faker('sentence', nb_words=4)
    author_name = factory.Faker('name')
```

#### Providers

У Faker есть большое количество шаблонов, которые расположены в так называемых провайдерах:

```python
from faker import Faker
from faker.providers import internet

fake = Faker()
fake.add_provider(internet)
fake.ipv4_private()
'10.10.11.69'
fake.ipv4_private()
'10.86.161.98'
```


## Мокирование и изоляция внешних сервисов

```python
from unittest.mock import patch

def do_payment(amount):
    # обёртка над внешним SDK
    from app.payments.gateway import charge
    return charge(amount).get('ok')

@patch('app.payments.gateway.charge', return_value={'ok': True})
def test_charge_ok(mock_charge):
    assert do_payment(100) is True
    mock_charge.assert_called_once_with(100)
```


### Тестирование тротлинга (429 Too Many Requests)

```python
from django.test import override_settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class ThrottleTests(APITestCase):
    @override_settings(REST_FRAMEWORK={
        'DEFAULT_THROTTLE_CLASSES': ['rest_framework.throttling.AnonRateThrottle'],
        'DEFAULT_THROTTLE_RATES': {'anon': '2/min'}
    })
    def test_throttle_for_anon(self):
        # При необходимости подготовьте данные через фабрики (см. раздел про DjangoModelFactory)
        url = reverse('notes-list')
        assert self.client.get(url).status_code == status.HTTP_200_OK
        assert self.client.get(url).status_code == status.HTTP_200_OK
        assert self.client.get(url).status_code == status.HTTP_429_TOO_MANY_REQUESTS
```

