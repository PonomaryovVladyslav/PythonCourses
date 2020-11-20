# Урок 40. Тестирование. Python, Django, REST API.

![](https://pics.me.me/your-code-cant-fail-unit-tests-openim-if-you-dont-14499557.png)

## Общая информация

Тестирование это огромная, нет **ОГРОМНАЯ** тема, настолько огромная, что порождает два отвельных класса сотрудников в IT индустрии.

### Автоматизированное и ручное тестирование

Хорошая новость в том, что вы, вероятно, уже создавали тесты, не осознавая этого. Помните, когда вы запускали приложение и использовали его впервые? Вы проверяли функции и экспериментировали с ними? Это называется исследовательское тестирование и является формой ручного тестирования.

Исследовательское тестирование — это форма тестирования, которая проводится без плана. В таком виде тестирования вы просто изучаете приложение.

Чтобы получить полный набор ручных тестов, все, что вам нужно сделать, это составить список всех функций, которыми обладает ваше приложение, список различных типов входных данных, которые оно может принять, и все ожидаемые результаты. Теперь, каждый раз, когда вы будете вносите изменения в свой код, вам нужно просмотреть каждый элемент в этом списке и проверить его правильность.

Это не особо прикольно?

Вот где приходит на помощь **тест план**. 

Тест план, это разделение вашего приложения на минимальные части и описание ожидаемой работы функционала каждой части, порядка их выполнения, и ожидаемые результаты.

Если у вас есть тест план, вы можете каждый раз проходить по всем его пунктам и быть уверенным, что вы проверили всё, в случае обновления приложения, необходимо обновить и план.

### Модульные (юнит) тесты против интеграционных тестов

Подумайте, как вы можете проверить свет в автомобиле. Вы должны включить свет (это будет называться один шаг теста (test step)), далее нужно выйти из машины или попросить друга проверить, включены ли огни (это называется утверждение теста (test assertion)). Тестирование нескольких компонентов называется интеграционным тестированием (integration testing). Основная проблема с интеграционным тестированием — это когда интеграционный тест не дает правильного результата. Иногда очень трудно диагностировать проблему, не имея возможности определить, какая часть системы вышла из строя. Если свет не включился, то, возможно сломаны лампы или разряжен аккумулятор. А как насчет генератора? Или может быть сломан компьютер машины?

Если у вас модный современный автомобиль, он сообщит вам, когда ваши лампочки вышли из строя. Это делается с помощью модульных тестов (unit test).

Модульный тест — это как правило небольшой тест, который проверяет правильность работы отдельного компонента. Модульный тест поможет вам выделить то, что сломано в вашем приложении, и быстро это исправить.

Вы только что рассмотрели два типа тестов:

1. Интеграционный тест, который проверяет, что компоненты в вашем приложении правильно работают друг с другом.
2. Модульный тест (unit test), который проверяет отдельный компонент в вашем приложении.

В Python вы можете написать как интеграционные, так и модульные тесты. Чтобы написать модульный тест для встроенной функции sum(), вы должны сравнить выходные данные sum() с ожидаемыми выходными данными.

Например, чтобы проверить, что сумма чисел 1, 2, 3 равна 6, можно написать это:

```python
assert sum([1, 2, 3]) == 6, "Should be 6"
```

Клюевое слово `assert`, проверяет выражение на булевое значение, если выражение равно `True` то не сделает ничего, а если `False` то будет зарейжена ошибка, на этом и основанно всё тестироование в python.

В нашем примере значение истина, поэтому всё будет хорошо, но если заменить на:

```python
assert sum([1, 1, 1]) == 6, "Should be 6"
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    AssertionError: Should be 6
```

Естественно вы можете обернуть асерт в функцию или в метод, и всё это будет работать.

Если набор тестов является частью одного элемента, то такой набор называется **Test Case**, если взять как пример фару автомобиля, то тест кейсом будет проверка, что лампочка целая, что провода функционируют, и что генератор работает. И при этом во всех случаях нам необходимо убедиться, что машина заведена и что мы переключили тумблер для включения фар.

Тесты практически всехгда пишут в виде тест кейсов, причём разделяя модульные и интеграционные.

Для запуска тестов используются так называемые `test runner`, это специальное приложение которое умеет искать и запускать тесты.

Их существует достаточно много, но основные всё таки:

```
unittest
nose или nose2
pytest
```

unittest встроенна в python и не требует дополнительных установок, мы будем пользоваться именно им.

Остальные действуют по тем же принципам с немного другим синтаксисом.

Во встроенном в python модуле `unittest` есть класс `TestCase` все тесты должны быть описанны в его наследниках.

Вместо обычного ассерта юниктест использует свои сразу заготовленные методы, вот некоторые из них:

```python
.assertEqual(a, b) # a == b

.assertTrue(x) # bool(x) is True

.assertFalse(x) #bool(x) is False

.assertIs(a, b) # a is b

.assertIsNone(x) # x is None

.assertIn(a, b) # a in b

.assertIsInstance(a, b) # isinstance(a, b)
```

Каждый тестовый метод должен начинаться со слова `test` иначе сборщик тестов его не увидит.

```python
import unittest

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
```

Теперь если мы запустим файл в котором это написано, мы увидим следующее:

```
$ python test_sum_unittest.py
.F
======================================================================
FAIL: test_sum_tuple (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_sum_unittest.py", line 9, in test_sum_tuple
    self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
AssertionError: Should be 6
----------------------------------------------------------------------
Ran 2 tests in 0.001s
FAILED (failures=1)
```

Один тест успешен, и один упал.

### Методы setUp и tearDown

Если добавить методы `setUp` и `tearDown` то код из них будет исполняться перед каждым тестом, и после кажого теста соответсвенно.

```python
import unittest

class TestSum(unittest.TestCase):
    
    def setUp(self):
        self.my_num = 5

    def test_odd(self):
        self.assertTrue(self.my_num % 2, "Number is odd")

    def tearDown(self):
        self.my_num += 1

if __name__ == '__main__':
    unittest.main()
```

### Пропуск тестов

в пакете `unittest` есть декораторы `skip` и `skipIf`, `skipUnless`

необходимы для пропуска не нужных на данном этапе тестов

```
class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass
```

### Запуск и поиск тестов

Для запуска тестов, можно использовать встроенную команду:

```
python -m unittest <file_name>
```

Указав имя файла, или указав слово `discover`

```
python -m unittest discover
```

этот скрипт будет искать все тесты внутри всех файлов и папок в директории и запускать их.

## Тестирование в Django

В Django есть свой собственный модуль `TestCase` который расширяет стандартный тест кейс, кому интересно чем читать [Тут](https://docs.djangoproject.com/en/3.1/topics/testing/tools/)

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

### Запуск тестов

Для запуска тестов используется менедж команда `test`

```python
# Run all the tests in the animals.tests module
$ ./manage.py test animals.tests

# Run all the tests found within the 'animals' package
$ ./manage.py test animals

# Run just one test case
$ ./manage.py test animals.tests.AnimalTestCase

# Run just one test method
$ ./manage.py test animals.tests.AnimalTestCase.test_animals_can_speak
```

так же можно искать все тесты в папке, например `animals`:

```python
./manage.py test animals/
```

### База данных для тестирования

Для тестов используется отдельная база данных, которая будет указана в переменной `TEST` в переменной `DATABASES` в файле `settings.py`:

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

## Специальные инструменты тестирования

### Client

Для проведения интеграционного тестирования джанго приложенния нам необходимо отправлять запросы с клиента (браузера), функционал для этого нам предоставлен из коробки, и мы можем им воспользоваться:

```python
>>> from django.test import Client
>>> c = Client()
>>> response = c.post('/login/', {'username': 'john', 'password': 'smith'})
>>> response.status_code
200
>>> response = c.get('/customer/details/')
>>> response.content
```


Такой запрос не будет требовать CSRF токен (хотя это тоже можно изменить, если необходимо)

Поддердивает метод `login()`

```python
c = Client()
c.login(username='fred', password='secret')
```

после чего запросы буд от авторизированого пользователя

и метод `force_login` принимающий объект юзера, а не логин и пароль.

и метод `logout()` что делает догадайтесь сами)

Естественно клиент при желании можно переписать под свои нужды

Так же можно заменять сеттинги или манипулировать базами данных во время выполнения тестов, подробнее в доке.

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

## Mock

Мок это фиктивные объекты. Очень часто мы попадаем в такие ситуации когда в тесте мы не можем выполнить какое-либо действие, например HTTP запрос к стороннему сервису, в этом случае мы можем имитировать выполнение этого запроса, что бы не прерывать суть теста, тут нам и поможет мок.

**Для версий питона 3.3 и старше, мок является частью стандартной библиотеки, установка не требуется**

Для использования с версией ниже чем 3.3 необходимо установить пекедж мок

```
pip install mock
```

Можно создать мок объект и заменить им всё что угодно :)

```python
>>> from unittest.mock import Mock
>>> mock = Mock()
>>> mock
<Mock id='4561344720'>
```

Мы можем использовать фейковый объект в качестве аргумента или целиком заменяя сущность

```python
# Pass mock as an argument to do_something()
do_something(mock)

# Patch the json library
json = mock
```

у фейкового объекта могут быть как атрибуты так и методы

```python
>>> mock.some_attribute
<Mock name='mock.some_attribute' id='4394778696'>
>>> mock.do_something()
<Mock name='mock.do_something()' id='4394778920'>
```

Есть достаточно много способов использовать мок, очень хорошая статья [Тут](https://realpython.com/python-mock-library/)

Рассмотрим основные

### Контроль возвращаемого результата

Предположим вам нужно убедиться что ваш код в рабочие и в выходные дни ведёт себя по разному, а код подразумевает использование встроенной библиотеки `datetime`

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

Если мы запустим этот тест в воскресенье, то мы получим эксепшен, что же с этим делать? Замокать... Мок объект может возвращать по вызову любой функции необходимое нам значение, по средством заполнения `return_value`

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

Если нам необходимо, что бы после повторного вызова мы получали другие результаты то, нам поможет `side_effect`, ратает так же как и `return_value` только принимает перебирираемый объект и с каждым вызовом возвращает следующее значение.

```
>>> mock_poll = Mock(side_effect=[None, 'data'])
>>> mock_poll()
None
>>> mock_poll()
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
        time.sleep(10) # long running process
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

этот тест будет идти 10 секунд, имитирую длительный процесс, но мы можем симитировать выполнение этого метода.

```python
from unittest import TestCase
from unittest.mock import patch

class TestCalculator(TestCase):
    @patch('main.Calculator.sum', return_value=9)
    def test_sum(self, sum):
        self.assertEqual(sum(2,3), 9)
```

или

```python
from unittest import TestCase
from unittest.mock import patch

class TestCalculator(TestCase):
    @patch('main.Calculator.sum')
    def test_sum(self, sum):
        sum.return_value = 9
        self.assertEqual(sum(2,3), 9)
```

пропатченные методы попадают в аргуметны метода теста.

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

Если в сайд эффект засуть метод, то вместо оригинального метода будет выполняться новый, например:

```python
from unittest import TestCase
from unittest.mock import patch

def mock_sum(a, b):
    # mock sum function without the long running time.sleep
    return a + b

class TestCalculator(TestCase):
    @patch('main.Calculator.sum', side_effect=mock_sum)
    def test_sum(self, sum):
        self.assertEqual(sum(2,3), 5)
        self.assertEqual(sum(7,3), 10)
```

## Фабрики


### Паттерн фабрика

Фабричный метод — если умным текстом то это порождающий паттерн проектирования, который определяет общий интерфейс для создания объектов в суперклассе, позволяя подклассам изменять тип создаваемых объектов.

Если по смыслу, то это возможность создать необходимую нам сущность внутри вызова метода.

В джанго есть встроенная фабрика для реквеста, зачем это нужно? Нам не для всех проверок нужно делать запрос, часто нам нужно его только имитировать.

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

## Factory boy

Внешний устанавливаемый пекедж, который предоставляет создавать объекты моделей, с заранее запоненными полями.

Подробная дока [Тут](https://factoryboy.readthedocs.io/en/stable/introduction.html)

```
pip install factory_boy
```

Поддерживает возможность базироваться на жданго моделях

```python
from django.utils import timezone

import factory

from fundedbyme.campaign.tests.factories import CampaignFactory
from fundedbyme.register.tests.factories import UserFactory

from ..models import Comment


class CommentFactory(factory.DjangoModelFactory):

    class Meta:
        model = Comment

    campaign = factory.SubFactory(CampaignFactory)
    user = factory.SubFactory(UserFactory)
    parent = None
    created_at = timezone.now()
    updated_at = timezone.now()
    hidden = False
    content = "I'm a comment"

```

Помогает создавть заготовки для использования в тестах

Пример из живого проекта

```python
class CommentDeleteViewTests(TestCase):
    def setUp(self, *args, **kwargs):
        self.client = Client()
        self.user = UserWithUserprofileFactory()
        self.campaign = LiveEquityCampaignFactory()
        self.comment = CommentFactory(user=self.user, campaign=self.campaign)

    def test_comment_delete_by_campaign_owner(self):
        self.client.login(username=self.campaign.owner.username, password='password')
        url = reverse("comment_delete", kwargs={"campaign_id": self.campaign.id})
        response = self.client.post(url, data={'comment_id': self.comment.id})
        self.assertEqual(response.content, '{"status": "error"}')

    def test_comment_delete_by_not_auth_user(self):
        url = reverse("comment_delete", kwargs={"campaign_id": self.campaign.id})
        response = self.client.post(url, data={'comment_id': self.comment.id})
        self.assertEqual(response.content, '{"status": "error"}')

    def test_comment_delete_by_simple_user(self):
        user = UserWithUserprofileFactory()
        self.client.login(username=user.username, password='password')
        url = reverse("comment_delete", kwargs={"campaign_id": self.campaign.id})
        response = self.client.post(url, data={'comment_id': self.comment.id})
        self.assertEqual(response.content, '{"status": "error"}')

    def test_comment_delete_by_comment_owner(self):
        self.client.login(username=self.user.username, password='password')
        url = reverse("comment_delete", kwargs={"campaign_id": self.campaign.id})
        response = self.client.post(url, data={'comment_id': self.comment.id})
        self.assertEqual(response.content, '{"status": "OK"}')

    def test_comment_delete_by_staff(self):
        user = UserWithUserprofileFactory(is_staff=True)
        self.client.login(username=user.username, password='password')
        url = reverse("comment_delete", kwargs={"campaign_id": self.campaign.id})
        response = self.client.post(url, data={'comment_id': self.comment.id})
        self.assertEqual(response.content, '{"status": "OK"}')
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

Часто нам необходимо проверять запросы из под необходимого типа полльзователя, но сам по себе логин уже покрыт тестами, а это значит что второй раз его проверять нет неоходимости, можем просто логинится.

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

Если необходимо проверить работу CSRF токена, это можно сделать на этапе создания фабрики

```python
factory = APIRequestFactory(enforce_csrf_checks=True)
```

И после этого все хапросы будут проверяться на CSRF

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

Для изменения хедером, можно использовать или стандартные классы, или просто обновлять как словарь

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

# К практике!