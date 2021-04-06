# Урок 40. Тестирование. Python, Django, REST API.

![](https://pics.me.me/your-code-cant-fail-unit-tests-openim-if-you-dont-14499557.png)

## Общая информация

Тестирование это огромная, нет **ОГРОМНАЯ** тема, настолько огромная, что порождает два отдельных класса сотрудников в
IT индустрии.

## Виды тестирования

![](https://qastart.by/images/speasyimagegallery/albums/2/images/-.png)

Таблица достаточно понятна, не будем вдаваться в детали.

Главное, что нужно извлечь из неё, это то что тестировщики делятся на мануальных(ручных) и автоматизированных.

Мануальные занимаются тем что в ручную проверяют весь доступный функционал. Автоматизаторы, пишут код для тестирования
продукта.

## Уровни тестирования

![](https://habrastorage.org/storage2/ec3/825/c7f/ec3825c7f0710f9fed6814c89b794ded.jpg)

Существует 4 основных уровня тестирования функционала.

Модульные тесты (они же юнит) - это тесты проверяющие функционал конкретного модуля минимального размера. Если вы
переписали метод `get_context_data`, то юнит тестом будет попытка вызвать этот метод с разными входными данными, и
посмотреть на то, что вернёт результат.

Интеграционные тесты - это вид тестирования когда проверяется целостность работы системы, без сторонних средств.
Например, вы переписали метод `get_context_data`, выполняем запрос при помощи кода, и смотрим, изменилась ли
переменная `context` в ответе на наш запрос.

Приёмочные тесты (они же ацептанс) - Вид тестов с полной имитацией действий пользователя. При помощи специальных
средств (например Selenium), мы прописываем код открытия браузера, поиска необходимых элементов на странице, имитация
ввода данных, нажатие кнопок, перехода по ссылкам итд.

Ручные тесты (они же мануальные) - Вид тестов, когда мы полностью повторяем потенциальные действия пользователя.

### Как это вообще работает.

Теоретически можно написать рабочий проект вообще без единого теста (ваш модуль тому пример). Но чем больше и сложнее
система, тем дороже стоимость ошибки, или объем затраченного времени на поиск причины этой ошибки.

В реальности даже не сильно большой проект, не может существовать без тестирования.

#### Кто пишет юнит тесты

Юнит тесты, это тесты конкретно написанной функции или метода. А значит что знание о там как это работает, есть только у
разработчика, а значит пишет разработчик.

`Идеальный мир` - Разработчик покрывает всё тестами.

`Реальность` - Разработчик покрывает основной функционал и тонкие места тестами.

`Худший случай` - Юнит тестов нет, что приводит к усложнению написания и модификации проекта в несколько раз.

#### Кто пишет интеграционные тесты

`Идеальный мир` - Автоматизированые тестировщики, причём вполне возможно что на другом языке программирования,
приложения не важно кто отправляет HTTP запрос, с какой платфомы и языка.

`Реальность` - Автоматизаторы если они есть, разработчики если автоматизаторов нет.

`Худший случай` - Нет интеграционных тестов. Что приводит к тому, что при внедрении новых фич, можно не узнать о том,
что сломалась старая, что приводит к тому, что функционал будет отваливаться быстрее чем разробатываться

#### Кто пишет ацептанс тесты

`Идеальный мир` - Всё те же автоматизаторы.

`Реальность` - У кого есть время и желание, чаще всего этот вид тестирования либо игнорируется, либо выполняется когда
уже всё остальное написано. Так же бывает когда через такой вид тестирования мануальщиков обучают и привлекают к
автоматизации

`Худший случай` - Ацептансов нет, и в случае отсутствия мануальной проверки, можно не узнать, что функционал в браузере
больше не работает.

#### Кто выполняет ручные тесты

`Идеальный мир` - Мануальные тестировщики.

`Реальность` - Если есть мануальные тестировщики, то они, если нет, то автоматизаторы, если и их нет, то разработчики в
процессе разработки.

`Худший случай` - Не проводятся, уверенность, что функционал работает равен нулю.

### Исследовательское тестирование и планирование

Хорошая новость в том, что вы, вероятно, уже создавали тесты, не осознавая этого. Помните, когда вы запускали приложение
и использовали его впервые? Вы проверяли функции и экспериментировали с ними? Это называется исследовательское
тестирование и является формой ручного тестирования.

Исследовательское тестирование — это форма тестирования, которая проводится без плана. В таком виде тестирования вы
просто изучаете приложение.

Чтобы получить полный набор ручных тестов, все, что вам нужно сделать, это составить список всех функций, которыми
обладает ваше приложение, список различных типов входных данных, которые оно может принять, и все ожидаемые результаты.
Теперь, каждый раз, когда вы будете вносите изменения в свой код, вам нужно просмотреть каждый элемент в этом списке и
проверить его правильность.

Это не особо прикольно?

Вот где приходит на помощь **тест план**.

Тест план, это разделение вашего приложения на минимальные части и описание ожидаемой работы функционала каждой части,
порядка их выполнения, и ожидаемые результаты.

Если у вас есть тест план, вы можете каждый раз проходить по всем его пунктам и быть уверенным, что вы проверили всё, в
случае обновления приложения, необходимо обновить и план.

## Test Case

Чёткого определения у тест кейса нет. Но в общем случае, тест кейс это минимальная единица проверки чего либо.

На практике, это чаще всего набор методов в классе проверяющий какой-либо функционал. Например в одном вьюсете
переписано, 3 метода, тесты описывающие все проверки будут в одном тест кейсе.

## Тестирование в Django

Вы знаете о существовании `unittest.TestCase`, от которого нужно наследоваться, что бы создать обычный тест.

У него могут быть метод `setUp` и `tearDown` для описания данных которые нужно выполнить до каждого теста, и после
соответсвенно.

И методы называющиеся со слова `test_` которые описывают сами тесты, для чего используется ключевое слово `assert` или
основанные на нём встроенные методы.

В рамках Django, есть свой собственный тест кейс, наследованный от базового `unittest.TestCase`

![](https://docs.djangoproject.com/en/2.2/_images/django_unittest_classes_hierarchy.svg)

### SimpleTestCase

`SimpleTestCase` наследуется от базового

#### Что добавляет?

Добавляет `settings.py` в структуру теста и возможность переписать или изменить `settings.py` для теста.

Добавляет `Client` который используется для написания интеграционных тестов (через него мы будем отправлять запросы)

Добавляет новые методы ассертов:

`assertRedirects` - Проверка на то, что урл на который мы попали совпадает с ожидаемым.

`assertContains` - Проверка на то, что страница содержит ожидаемую переменную.

`assertNotContains` - Проверка на то, что страница не содержит ожидаемую переменную.

`assertFormError` - Проверка на то, что форма содержит нужную ошибку.

`assertFormsetError` - Проверка на то, что формсет содержит нужную ошибку.

`assertTemplateUsed` - Проверка на то, что был использован ожидаемый шаблон.

`assertTemplateNotUsed` - Проверка на то, что не был использован ожидаемый шаблон.

`assertRaisesMessage` - Проверка на то, что на странице присутствует определённое сообщение.

`assertFieldOutput` - Проверка на то, что определённое поле содержит ожидаемое значение.

`assertHTMLEqual` - Проверка на то, что полученный HTML соответствует ожидаемому.

`assertHTMLNotEqual` - Проверка на то, что полученный HTML не соответствует ожидаемому.

`assertJSONEqual` - Проверка на то, что полученный JSON соответствует ожидаемому.

`assertJSONNotEqual` - Проверка на то, что полученный JSON не соответствует ожидаемому.

`assertXMLEqual` - Проверка на то, что полученный XML соответствует ожидаемому.

`assertXMLNotEqual` - Проверка на то, что полученный XML не соответствует ожидаемому.

### TransactionTestCase

`TransactionTestCase` наследуется от SimpleTestCase

#### Что добавляет?

Добавляет возможность выполнять транзакции в базу данных в рамках теста.

Добавляет атрибут `fixtures` для возможности загружать базовые условия теста из фикстур.

Добавляет атрибут `reset_sequences` который позволяет сбрасывать последовательности для каждого теста (каждый созданный
объект всегда будет начинаться с id=1)

Добавляет новые методы ассертов:

`assertQuerysetEqual` - Проверка на то, что полученный кверисет совпадает с ожидаемым.

`assertNumQueries` - Проверка на то, что что выполнение функции делает определённое кол-во запросов в базу.

### TestCase из модуля Django

`TestCase` наследуется от TransactionTestCase

#### Что добавляет?

По сути ничего :) Немного по другому выполняет запросы в базу (с использованием атомарности), из-за чего
предпочтительнее

Дополнительный метод `setUpTestData`, для описания данных для теста. Не обязательный.

Это самый часто используемый вид тестов.

### LiveServerTestCase

`LiveServerTestCase` наследуется от TransactionTestCase

#### Что добавляет?

Запускает реальный сервер для возможности открыть проект в браузере. Необходим для написания ацептанс тестов.

Чаще всего в таких тестах, запускается сервер и имитация браузера (например Selenium)

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

Эта база будет изначально пустая, и будет очищаться после каждого выполненного тест кейса

**Ваш юзер должен иметь права на создание и очистку базы данных**

### Расположение тестов

Несмотря на то, что Django создаёт для нас в приложении файл `tests.py`, им практически никогда не пользуются.

Существует два самых распространённых способа хранения тестов, если вам повезло и на вашем проекте есть специальные
тестировщики. То ваша задача, это только юнит тесты.

И тогда в папке приложения создаётся еще одна папка `tests` в которой уже создаются файлы для тестов различных частей,
например `test_models.py`, `test_forms.py` итд.

![](https://drive.google.com/uc?export=view&id=1E_Tf8H2spWJbSOaaxvWOMiLk4c0bgvUT)

Если вам не повезло, и на проекте вы и за автотестеров, то тогда в этой же папке (`tests`) создаётся еще 3 папки `unit`
, `integration` и `acceptance` и уже в них описываются различные тесты.

### Запуск тестов

Предположим, что у нас в приложении `animals`, есть папка `tests`, в ней папка `unit` и в ней файл `test_models`.

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

То для запуска тестов используется менедж команда `test`

```
# Запустить все тесты в приложении, в папке тестов
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

Для проведения интеграционного тестирования джанго приложения нам необходимо отправлять запросы с клиента (браузера),
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

Такой запрос не будет требовать CSRF токен (хотя это тоже можно изменить, если необходимо)

Поддерживает метод `login()`

```python
c = Client()
c.login(username='fred', password='secret')
```

После чего запросы будут от авторизированого пользователя

Метод `force_login` принимающий объект юзера, а не логин и пароль.

Метод `logout()` что делает догадайтесь сами)

Естественно клиент при желании можно переписать под свои нужды

Клиент сразу есть в тест кейсе, его нет неоходимости создавать, к нему можно обратиться через `self.client`

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

Загрузится файл `mammals.json`, и из него фикстура `birds`

### Теганье тестов

Существует возможность поставить "тег" на каждый тест, а после запускать только те что с пределённым тегом.

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

Или даже целый тесткейс

```python
@tag('slow', 'core')
class SampleTestCase(TestCase):
    ...
```

После чего запускать с указанием тега.

```
./manage.py test --tag=fast
```

### Тестирование менедж команд

Для этого используется специальный метод `call_command`:

```python
from io import StringIO
from django.core.management import call_command
from django.test import TestCase


class ClosepollTest(TestCase):
    def test_command_output(self):
        out = StringIO()
        call_command('closepoll', stdout=out)
        self.assertIn('Expected output', out.getvalue())
```

### Пропуск тестов

Тесты можно пропускать в зависимости от условий и деталей запуска.
Дока [тут](https://docs.python.org/3/library/unittest.html#unittest.skipIf)

## Фабрики

### Паттерн фабрика

Фабричный метод — если умным текстом то это порождающий паттерн проектирования, который определяет общий интерфейс для
создания объектов в суперклассе, позволяя подклассам изменять тип создаваемых объектов.

Если по смыслу, то это возможность создать необходимую нам сущность внутри вызова метода.

В джанго есть встроенная фабрика для реквеста, зачем это нужно? Нам не для всех проверок нужно делать запрос, часто нам
нужно его только имитировать. Для написания юнит тестов это самый главный инструмент.

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

Для тестирования отдельных методов мы можем использовать метод `setup`

например, если мы заменили `get_context_data` то можно сделать так:

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

В Django REST Framework есть достаточно много внутренних похожих процедур и классов, например своя фабрика реквестов:

```python
from rest_framework.test import APIRequestFactory

# Using the standard RequestFactory API to create a form POST request
factory = APIRequestFactory()
request = factory.post('/notes/', {'title': 'new idea'})
```

По дефолту формат JSON, но это можно изменить

```python
# Create a JSON POST request
factory = APIRequestFactory()
request = factory.post('/notes/', {'title': 'new idea'}, format='json')
```

А можно вообще указать контент тайп

```python
request = factory.post('/notes/', json.dumps({'title': 'new idea'}), content_type='application/json')
```

### Форс логин

Часто нам необходимо проверять запросы из под необходимого типа полльзователя, но сам по себе логин уже покрыт тестами,
а это значит что второй раз его проверять нет неоходимости, можем просто логинится.

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

В DRF есть свой клиент для запросов в котором уже прописаны все необходимые методы запросов (`get()`, `post()`, итд.)

```python
from rest_framework.test import APIClient

client = APIClient()
client.post('/notes/', {'title': 'new idea'}, format='json')
```

#### Авторизация через клиент

Поддерживает метод логин, логаут и креденшиалс, логин принимает логин и пароль, криденшиалс, принимает хедеры.

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

Так же подерживает форсированую авторизацию

```python
user = User.objects.get(username='lauren')
client = APIClient()
client.force_authenticate(user=user)
```

Так же можно включить CSRF, на этапе создания клиента

```python
client = APIClient(enforce_csrf_checks=True)
```

Для изменения хедеров, можно использовать или стандартные классы, или просто обновлять как словарь

```python
from requests.auth import HTTPBasicAuth

client.auth = HTTPBasicAuth('user', 'pass')
client.headers.update({'x-test': 'true'})
```

Если вы включили CSRF и хотите им пользоваться при проверках это можно сделать так:

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

## Фабрики для генерации данных

### FactoryBoy

```
pip install factory_boy
```

Прописывание в setUp создание новых объектов может занимать очень много времени. Что-бы это ускорить, упростить и
автоматизировать, можно написать свою фабрику

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

Так же можно использовать разные фабрики в разных местах

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

Атрибутом может быть другая фабрика. Например при создании фабрики покупки мы можем указать в качестве покупателя,
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

Можно передавать специальный объект последовательности, при создании каждого нового объекта, будет добавляться единица,
для текущего примера, юзернеймы всех созданных юзеров будут `user1`, `user2`, `user3` итд.

Sequences

```python
class UserFactory(factory.Factory):
    class Meta:
        model = models.User

    username = factory.Sequence(lambda n: 'user%d' % n)
```

Можно передать специальный объект, который будет вызывать ффункцию при создании объекта, например текущее время.

LazyFunction

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

Иногда нужно заполнять другие поля на основании других, для этого тоже есть специальный объект

LazyAttribute Некоторые поля могут быть заполнены при помощи других, например электронная почта на основе имени
пользователя. LazyAttribute обрабатывает такие случаи: он должен получить функцию, принимающую создаваемый объект и
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

Fuzzy позволяет генерировать фейковые данные

```python
from factory import fuzzy

...


def setUp(self):
    self.username = fuzzy.FuzzyText().fuzz()
    self.password = fuzzy.FuzzyText().fuzz()
    self.user_id = fuzzy.FuzzyInteger(1).fuzz()
```

#### Faker

Faker пришел на замену Fuzzy и в нём гораздо больше всего, его нужно устанавливать

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

У Faker есть большое количество шаблонов, которые расположены в так называемых провайдерах

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

## Mock

Мок это фиктивные объекты. Очень часто мы попадаем в такие ситуации когда в тесте мы не можем выполнить какое-либо
действие, например HTTP запрос к стороннему сервису, в этом случае мы можем имитировать выполнение этого запроса, что бы
не прерывать суть теста, тут нам и поможет мок.

**Для версий питона 3.3 и старше, мок является частью стандартной библиотеки, установка не требуется**

Для использования с версией ниже чем 3.3 необходимо установить пекедж мок

```
pip install mock
```

Можно создать мок объект и заменить им всё что угодно :)

```
from unittest.mock import Mock
mock = Mock()
mock
< Mock id = '4561344720' >
```

Мы можем использовать фейковый объект в качестве аргумента или целиком заменяя сущность

```python
# Pass mock as an argument to do_something()
do_something(mock)

# Patch the json library
json = mock
```

у фейкового объекта могут быть как атрибуты так и методы

```
mock.some_attribute
< Mock name = 'mock.some_attribute' id = '4394778696' >
mock.do_something()
< Mock name = 'mock.do_something()' id = '4394778920' >
```

Есть достаточно много способов использовать мок, очень хорошая статья [Тут](https://realpython.com/python-mock-library/)

Рассмотрим основные

### Контроль возвращаемого результата

Предположим вам нужно убедиться что ваш код в рабочие и в выходные дни ведёт себя по-разному, а код подразумевает
использование встроенной библиотеки `datetime`

Для упрощения, пока, засунем все в один файл:

```python
from datetime import datetime


def is_weekday():
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return 0 <= today.weekday() < 5


# Test if today is a weekday
assert is_weekday()
```

Если мы запустим этот тест в воскресенье, то мы получим эксепшен, что же с этим делать? Замокать... Мок объект может
возвращать по вызову любой функции необходимое нам значение, по средством заполнения `return_value`

```python
import datetime
from unittest.mock import Mock

# Save a couple of test days
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

# Mock datetime to control today's date
datetime = Mock()


def is_weekday():
    today = datetime.datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return 0 <= today.weekday() < 5


# Mock .today() to return Tuesday
datetime.datetime.today.return_value = tuesday
# Test Tuesday is a weekday
assert is_weekday()
# Mock .today() to return Saturday
datetime.datetime.today.return_value = saturday
# Test Saturday is not a weekday
assert not is_weekday()
```

Если нам необходимо, что бы после повторного вызова мы получали другие результаты то, нам поможет `side_effect`, ратает
так же как и `return_value` только принимает перебираемый объект и с каждым вызовом возвращает следующее значение.

```
mock_poll = Mock(side_effect=[None, 'data'])
mock_poll()
None
mock_poll()
'data'
```

Или как на прошлом примере

```python
import datetime
from unittest.mock import Mock

# Save a couple of test days
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

# Mock datetime to control today's date
datetime = Mock()


def is_weekday():
    today = datetime.datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return 0 <= today.weekday() < 5


# Mock .today() to return Tuesday first time and Saturday second time
datetime.datetime.today.side_effect = [tuesday, saturday]
assert is_weekday()
assert not is_weekday()
```

### декоратор patch

Допустим у нас есть класс где мы имитируем какие-то длинные вычисления:

```python
import time


class Calculator:
    def sum(self, a, b):
        time.sleep(10)  # long running process
        return a + b
```

И тест к этой функции:

```python
from unittest import TestCase
from main import Calculator


class TestCalculator(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        answer = self.calc.sum(2, 4)
        self.assertEqual(answer, 6)
```

Этот тест будет идти 10 секунд, имитирую длительный процесс, но мы можем имитировать выполнение этого метода.

```python
from unittest import TestCase
from unittest.mock import patch


class TestCalculator(TestCase):
    @patch('main.Calculator.sum', return_value=9)
    def test_sum(self, sum):
        self.assertEqual(sum(2, 3), 9)
```

или

```python
from unittest import TestCase
from unittest.mock import patch


class TestCalculator(TestCase):
    @patch('main.Calculator.sum')
    def test_sum(self, sum):
        sum.return_value = 9
        self.assertEqual(sum(2, 3), 9)
```

Пропатченные методы попадают в аргументы метода теста.

### Пример с использованием API

Будем использовать классический пекедж для питона, для выполнения запросов.

```
pip install requests
```

Допустим у нас есть такой код:

```python
import requests


class Blog:
    def __init__(self, name):
        self.name = name

    def posts(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")

        return response.json()

    def __repr__(self):
        return '<Blog: {}>'.format(self.name)
```

То можно описать тест так:

```python
from unittest import TestCase
from unittest.mock import patch, Mock


class TestBlog(TestCase):
    @patch('main.Blog')
    def test_blog_posts(self, MockBlog):
        blog = MockBlog()

        blog.posts.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'Test Title',
                'body': 'Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy\ lies a small unregarded yellow sun.'
            }
        ]

        response = blog.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)
```

## Целая замена методов через side_effect

Если в сайд эффект засунуть метод, то вместо оригинального метода будет выполняться новый, например:

```python
from unittest import TestCase
from unittest.mock import patch


def mock_sum(a, b):
    # mock sum function without the long running time.sleep
    return a + b


class TestCalculator(TestCase):
    @patch('main.Calculator.sum', side_effect=mock_sum)
    def test_sum(self, sum):
        self.assertEqual(sum(2, 3), 5)
        self.assertEqual(sum(7, 3), 10)
```

# К практике!

1. Напишите юнит тесты для логина и для покупки товара.

2. Напишите интеграционные тесты, для логина, и для покупки товара.

3. (Задание до выдачи задания на диплом) Покройте тестами весь остальной код