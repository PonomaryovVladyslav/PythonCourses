# Лекция 30. Тестирование. Django, REST API.

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
  - [Лекция 28. @api_view, APIView, ViewSets, Pagination, Routers](lesson28.md)
  - [Лекция 29. REST-аутентификация. Авторизация. Permissions. Фильтрация](lesson29.md)
  - ▶ **[Лекция 30. Тестирование. Django, REST API.](lesson30.md)**
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


![](https://preview.redd.it/aom6ubb0b4e71.jpg?width=640&crop=smart&auto=webp&s=d9094222a89d1f8cb0f43285d4ff9c81f274cfee)

## Общая информация

Тестирование — это огромная, нет **ОГРОМНАЯ** тема, настолько огромная, что порождает два отдельных класса сотрудников в
IT-индустрии.

## Уровни тестирования

Напомним себе про пирамиду тестирования

![](https://habrastorage.org/storage2/ec3/825/c7f/ec3825c7f0710f9fed6814c89b794ded.jpg)

Существует 4 основных уровня тестирования функционала.

**Модульные тесты (Unit Tests)** — это тесты, проверяющие функционал конкретного модуля минимального размера.
Если вы переписали метод `get_context_data()`, то юнит тестом будет попытка вызвать этот метод с разными входными
данными, и посмотреть на то, что вернёт результат.

**Интеграционные тесты (Integration Tests)** — это вид тестирования, когда проверяется целостность работы системы без
сторонних средств. Например, вы переписали метод `get_context_data()`, выполняем запрос при помощи кода, и смотрим,
изменилась ли переменная `context` в ответе на наш запрос.

**Приёмочные тесты (Acceptance Tests)** — вид тестов с полной имитацией действий пользователя. При помощи специальных
средств (например, Selenium) мы прописываем код открытия браузера, поиска необходимых элементов на странице, имитируем
ввод данных, нажатие кнопок, переход по ссылкам и т. д.

**Ручные тесты (Manual Tests)** — вид тестов, когда мы полностью повторяем потенциальные действия пользователя.

### Базовые концепции unittest

Вы знаете о существовании `unittest.TestCase`, от которого нужно наследоваться, чтобы создать обычный тест.

У него могут быть метод `setUp()` и `tearDown()` для описания данных, которые нужно выполнить до каждого теста и после
соответственно.

И методы, начинающиеся со слова `test_`, которые описывают сами тесты, для чего используется ключевое слово `assert` или
основанные на нём встроенные методы.

### Иерархия тест-кейсов Django

В рамках Django есть свой собственный тест-кейс, наследованный от базового `unittest.TestCase`.

![](https://docs.djangoproject.com/en/stable/_images/django_unittest_classes_hierarchy.svg)

### SimpleTestCase

`SimpleTestCase` наследуется от базового.

#### Что добавляет?

Добавляет `settings.py` в структуру теста и возможность переписать или изменить `settings.py` для теста.

Добавляет `Client`, который используется для написания интеграционных тестов (через него мы будем отправлять запросы).

Добавляет новые методы `assert`:

`assertRedirects` — проверка на то, что URL, на который мы попали, совпадёт с ожидаемым.

`assertContains` — проверка на то, что страница содержит ожидаемую переменную.

`assertNotContains` — проверка на то, что страница не содержит ожидаемую переменную.

`assertFormError` — проверка на то, что форма содержит нужную ошибку.

`assertFormsetError` — проверка на то, что formset содержит нужную ошибку.

`assertTemplateUsed` — проверка на то, что был использован ожидаемый шаблон.

`assertTemplateNotUsed` — проверка на то, что не был использован ожидаемый шаблон.

`assertRaisesMessage` — проверка на то, что на странице присутствует определённое сообщение.

`assertFieldOutput` — проверка на то, что определённое поле содержит ожидаемое значение.

`assertHTMLEqual` — проверка на то, что полученный HTML соответствует ожидаемому.

`assertHTMLNotEqual` — проверка на то, что полученный HTML не соответствует ожидаемому.

`assertJSONEqual` — проверка на то, что полученный JSON соответствует ожидаемому.

`assertJSONNotEqual` — проверка на то, что полученный JSON не соответствует ожидаемому.

`assertXMLEqual` — проверка на то, что полученный XML соответствует ожидаемому.

`assertXMLNotEqual` — проверка на то, что полученный XML не соответствует ожидаемому.

### TransactionTestCase

`TransactionTestCase` наследуется от `SimpleTestCase`.

#### Что добавляет?

Добавляет возможность выполнять транзакции в базу данных в рамках теста.

Добавляет атрибут `fixtures` для возможности загружать базовые условия теста из фикстур.

Добавляет атрибут `reset_sequences`, который позволяет сбрасывать последовательности для каждого теста (каждый созданный
объект всегда будет начинаться с id=1)

Добавляет новые методы `assert`:

`assertQuerysetEqual` — проверка на то, что полученный кверисет совпадает с ожидаемым.

`assertNumQueries` — проверка на то, что выполнение функции делает определённое количество запросов в базу.

**Важно:** `TransactionTestCase` заметно медленнее `TestCase`, так как выполняет полноценную очистку БД между тестами.
Используйте его, когда нужно проверить реальное поведение транзакций (`commit`/`rollback`, `select_for_update`, взаимодействие с внешними транзакционными системами).

### TestCase из модуля Django

`TestCase` наследуется от `TransactionTestCase`.

#### Что добавляет?

По сути ничего. :) Немного по другому выполняет запросы в базу (с использованием атомарности), из-за чего
предпочтительнее.

Дополнительный метод `setUpTestData()` для описания данных для теста. Не обязательный.

Это самый часто используемый вид тестов.

**Ключевые свойства TestCase:**

- Каждый тест запускается в транзакции и откатывается (rollback) — быстро и изолированно.
- `setUpTestData()` выполняется один раз на класс и экономит время на подготовке данных.
- Если нужно проверить поведение транзакций — используйте `TransactionTestCase`.

### LiveServerTestCase

`LiveServerTestCase` наследуется от `TransactionTestCase`.

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

Эта база будет изначально пустая и будет очищаться после каждого выполненного тест-кейса.

**Ваш юзер должен иметь права на создание и очистку базы данных**

> **Примечание:** Django обычно автоматически создаёт тестовую БД (например, `test_<NAME>` для PostgreSQL). Явное указание `TEST.NAME` требуется редко; убедитесь, что у пользователя БД есть права на создание/удаление.

### Расположение тестов

Несмотря на то, что Django создаёт для нас в приложении файл `tests.py`, им практически никогда не пользуются.

Существует два самых распространённых способа хранения тестов. Если вам повезло и на вашем проекте есть специальные
тестировщики, то ваша задача — это только юнит-тесты.

И тогда в папке приложения создаётся еще одна папка `tests`, в которой уже создаются файлы для тестов различных частей,
например, `test_models.py`, `test_forms.py` и т. д.

![](https://drive.google.com/uc?export=view&id=1E_Tf8H2spWJbSOaaxvWOMiLk4c0bgvUT)

Если вам не повезло, и на проекте вы за автоматических тестеров, то тогда в этой же папке (`tests`) создаётся еще 3
папки `unit`, `integration` и `acceptance`, и уже в них описываются различные тесты.

> Примечание: запуск через pytest см. в финальном разделе «Современный инструментарий: pytest и pytest-django».

### Запуск тестов

Для запуска тестов используется manage-команда `test`:

```bash
# Запустить все тесты в приложении
$./manage.py test animals

# Запустить все тесты в папке tests
$./manage.py test animals.tests

# Запустить один тест-кейс
$./manage.py test animals.tests.unit.test_models.AnimalTestCase

# Запустить один тест из тест-кейса
$./manage.py test animals.tests.unit.test_models.AnimalTestCase.test_animals_can_speak
```

---
## Тестирование в Django — основы

Документация: https://docs.djangoproject.com/en/stable/topics/testing/
Инструменты: https://docs.djangoproject.com/en/stable/topics/testing/tools/

### Обзор инструментов тестирования

| Тип теста       | Инструмент                      | Что проверяет                                  | Скорость     |
|-----------------|---------------------------------|------------------------------------------------|--------------|
| **Unit**        | `RequestFactory`                | Отдельный метод view/модели, без middleware    | ⚡ Быстро     |
| **Integration** | `Client`                        | Полный цикл запрос → middleware → view → ответ | 🐢 Медленнее |
| **Acceptance**  | `LiveServerTestCase` + Selenium | Браузер + UI                                   | 🐌 Медленно  |

## Unit-тестирование в Django

Unit-тесты проверяют отдельные компоненты в изоляции: методы моделей, отдельные view, формы. Они быстрые и не требуют полного цикла запроса.

### RequestFactory — имитация запросов без middleware

`RequestFactory` создаёт объект запроса, который можно передать напрямую во view. Middleware и URL-маршрутизация **не участвуют**: это делает тесты быстрыми и изолированными.

```python
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from .views import MyView, my_view


class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@example.com', password='top_secret')

    def test_details(self):
        # Создаём GET-запрос
        request = self.factory.get('/customer/details')

        # Middleware не работает — устанавливаем user вручную
        request.user = self.user

        # Или анонимный пользователь
        request.user = AnonymousUser()

        # Вызываем view напрямую (function-based)
        response = my_view(request)

        # Для class-based views
        response = MyView.as_view()(request)

        self.assertEqual(response.status_code, 200)
```

### Тестирование отдельных методов CBV

Для тестирования отдельных методов класса view используйте метод `setup()`:

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

### Пример unit-теста модели

```python
from django.test import TestCase
from myapp.models import Animal


class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Проверяем метод speak() модели Animal"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
```

---

## Интеграционное тестирование в Django

Интеграционные тесты проверяют полный цикл: запрос проходит через URL-маршрутизацию, middleware, view и возвращает ответ.

### Client — полный цикл запроса

`Client` имитирует браузер и отправляет HTTP-запросы через весь стек Django:

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

Загрузятся два файла фикстур: `mammals.json` и `birds` (Django автоматически найдёт `birds.json` или `birds.yaml`).

### Теги для тестов

Существует возможность поставить «тег» на каждый тест, а после запускать только те, что с определённым тегом.

```python
from django.test import tag


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

---

## Acceptance-тестирование в Django

Acceptance-тесты (приёмочные) имитируют реальные действия пользователя: открытие страниц, клики, ввод текста, проверку отображения элементов. Это самый медленный, но и самый «честный» уровень тестирования — проверяется то, что видит пользователь.

### WebDriver и Selenium

**WebDriver** — это стандартизированный API для программного управления браузером. Позволяет открывать страницы, кликать по элементам, заполнять формы и проверять результат.

**Selenium** — популярная библиотека, реализующая WebDriver для Python.

```bash
pip install selenium
```

Также нужен драйвер для конкретного браузера:
- Chrome → `chromedriver`
- Firefox → `geckodriver`
- Edge → `msedgedriver`

> **Совет:** Используйте `webdriver-manager` для автоматической загрузки драйверов:
> ```bash
> pip install webdriver-manager
> ```

### LiveServerTestCase + Selenium

`LiveServerTestCase` запускает реальный Django-сервер на случайном порту, к которому можно обращаться через Selenium:

```python
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class LoginAcceptanceTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Автоматическая загрузка chromedriver
        cls.browser = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        cls.browser.implicitly_wait(5)  # Ожидание элементов до 5 сек

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def setUp(self):
        self.user = User.objects.create_user('john', password='secret123')

    def test_login_page_loads(self):
        """Проверяем, что страница логина открывается"""
        self.browser.get(f'{self.live_server_url}/login/')
        self.assertIn('Login', self.browser.title)

    def test_user_can_login(self):
        """Полный сценарий: пользователь логинится и попадает на главную"""
        self.browser.get(f'{self.live_server_url}/login/')

        # Заполняем форму
        self.browser.find_element(By.NAME, 'username').send_keys('john')
        self.browser.find_element(By.NAME, 'password').send_keys('secret123')
        self.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # Проверяем результат
        self.assertIn('Dashboard', self.browser.title)
        welcome = self.browser.find_element(By.CLASS_NAME, 'welcome-message')
        self.assertIn('john', welcome.text)
```

### Когда использовать Acceptance-тесты

| ✅ Используйте для                          | ❌ Не используйте для     |
|--------------------------------------------|--------------------------|
| Критические сценарии (регистрация, оплата) | Проверки бизнес-логики   |
| Сложные JS-взаимодействия                  | Валидации форм           |
| Smoke-тесты перед релизом                  | Покрытия всех edge-cases |

> **Важно:** Acceptance-тесты медленные и хрупкие (ломаются при изменении вёрстки). Держите их количество минимальным — только для самых важных сценариев.

---

## Тестирование REST API (DRF)

Документация: https://www.django-rest-framework.org/api-guide/testing/

### Обзор инструментов DRF

| Тип теста       | Инструмент                  | Что проверяет                         | Когда использовать          |
|-----------------|-----------------------------|---------------------------------------|-----------------------------|
| **Unit**        | `APIRequestFactory`         | View, serializer, permission отдельно | Быстрые изолированные тесты |
| **Integration** | `APIClient` / `APITestCase` | Endpoint через URLConf и middleware   | Проверка полного цикла API  |

### Unit-тестирование API

#### APIRequestFactory

`APIRequestFactory` — аналог Django `RequestFactory` для DRF. Создаёт объект запроса без прохождения через URL-маршрутизацию и middleware.

```python
from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()
request = factory.post('/api/articles/', {'title': 'Новая статья'})
```

По умолчанию используется формат `multipart` (как HTML-форма). Для отправки JSON нужно указать явно:

```python
factory = APIRequestFactory()
request = factory.post('/api/articles/', {'title': 'Новая статья'}, format='json')
```

Или указать content-type напрямую:

```python
import json
request = factory.post('/api/articles/', json.dumps({'title': 'Новая статья'}), content_type='application/json')
```

#### force_authenticate()

Для unit-тестов не нужно проходить реальную аутентификацию — используйте `force_authenticate()`:

```python
from rest_framework.test import APIRequestFactory, force_authenticate
from django.contrib.auth.models import User
from .views import ArticleViewSet


factory = APIRequestFactory()
user = User.objects.get(username='author')
view = ArticleViewSet.as_view({'get': 'retrieve'})

request = factory.get('/api/articles/1/')
force_authenticate(request, user=user)
response = view(request, pk=1)
```

#### Пример unit-теста view

```python
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase
from .views import ArticleViewSet
from .models import Article


class ArticleViewUnitTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user('author', password='testpass')
        self.article = Article.objects.create(
            title='Тестовая статья',
            slug='testovaya-statya',
            content='Содержимое статьи',
            author=self.user,
            status='published'
        )

    def test_retrieve_returns_article(self):
        """Unit-тест: проверяем только метод retrieve"""
        view = ArticleViewSet.as_view({'get': 'retrieve'})
        request = self.factory.get(f'/api/articles/{self.article.pk}/')
        force_authenticate(request, user=self.user)

        response = view(request, pk=self.article.pk)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Тестовая статья')
```

### Интеграционное тестирование API

#### APIClient

`APIClient` — полноценный HTTP-клиент для DRF. Запросы проходят через URL-маршрутизацию и middleware.

```python
from rest_framework.test import APIClient

client = APIClient()
response = client.post('/api/articles/', {'title': 'Новая статья'}, format='json')
```

#### APITestCase

Удобный базовый класс, комбинирующий `TestCase` и `APIClient`:

```python
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Article


class ArticleIntegrationTests(APITestCase):
    def test_list_articles_anonymous(self):
        """Интеграционный тест: анонимный пользователь видит список статей"""
        url = reverse('article-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_article_authenticated(self):
        """Интеграционный тест: создание статьи авторизованным пользователем"""
        user = User.objects.create_user('author', password='testpass')
        self.client.force_authenticate(user=user)

        url = reverse('article-list')
        data = {
            'title': 'Новая статья',
            'slug': 'novaya-statya',
            'content': 'Содержимое статьи',
            'status': 'draft'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Article.objects.count(), 1)
        self.assertEqual(Article.objects.first().author, user)
```

#### Авторизация через APIClient

`APIClient` поддерживает несколько способов авторизации:

```python
from rest_framework.test import APIClient

client = APIClient()

# Способ 1: login (session-based)
client.login(username='lauren', password='secret')

# Способ 2: force_authenticate (без проверки пароля)
client.force_authenticate(user=user)

# Способ 3: credentials (для token/JWT)
from rest_framework.authtoken.models import Token
token = Token.objects.get(user__username='lauren')
client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

# Способ 4: logout (сброс авторизации)
client.logout()
```

#### Дополнительные заголовки

Для передачи заголовков в каждом запросе:

```python
client = APIClient()
client.get('/api/articles/', HTTP_X_CUSTOM_HEADER='value')
```

#### CSRF в тестах

Для включения проверки CSRF:

```python
client = APIClient(enforce_csrf_checks=True)
```

### Настройки DRF для тестов

Можно настроить форматы по умолчанию для тестов в `settings.py`:

```python
REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'TEST_REQUEST_RENDERER_CLASSES': [
        'rest_framework.renderers.MultiPartRenderer',
        'rest_framework.renderers.JSONRenderer',
    ]
}
```

---

## Генерация тестовых данных

Создание тестовых данных вручную в `setUp()` занимает много времени и делает тесты громоздкими. Для автоматизации используются специальные библиотеки.

### FactoryBoy

Документация: https://factoryboy.readthedocs.io/

```bash
pip install factory_boy
```

FactoryBoy — библиотека для создания тестовых объектов. Позволяет описать «шаблон» объекта и генерировать экземпляры с нужными вариациями.

#### Базовое использование

```python
import factory
from app.models import User


class UserFactory(factory.Factory):
    class Meta:
        model = User

    firstname = "John"
    lastname = "Doe"
```

```python
>>> john = UserFactory()
<User: John Doe>
>>> jack = UserFactory(firstname="Jack")
<User: Jack Doe>
```

#### DjangoModelFactory (рекомендуется для Django)

Для моделей Django используйте `DjangoModelFactory` — он автоматически сохраняет объекты в БД:

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
```

#### SubFactory: связи между моделями

Для связанных моделей используйте `SubFactory`:

```python
class PurchaseFactory(DjangoModelFactory):
    class Meta:
        model = Purchase

    owner = factory.SubFactory(UserFactory)
```

```python
>>> purchase = PurchaseFactory()
<Purchase: 1 John Doe>
>>> purchase.owner
<User: user0>
```

> **Важно:** Используйте `factory.SubFactory()`, а не прямой вызов фабрики. Иначе будет создан один и тот же объект для всех экземпляров.

#### Наследование фабрик

Можно создавать специализированные фабрики:

```python
class EnglishUserFactory(UserFactory):
    firstname = "John"
    lastname = "Doe"
    lang = 'en'


class FrenchUserFactory(UserFactory):
    firstname = "Jean"
    lastname = "Dupont"
    lang = 'fr'
```

#### Sequence: уникальные значения

Для генерации уникальных значений используйте `Sequence`:

```python
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
```

#### LazyFunction: динамические значения

Для значений, вычисляемых в момент создания объекта:

```python
from datetime import datetime


class LogFactory(DjangoModelFactory):
    class Meta:
        model = Log

    timestamp = factory.LazyFunction(datetime.now)
```

```python
>>> LogFactory()
<Log: log at 2016-02-12 17:02:34>
>>> LogFactory(timestamp=datetime.now() - timedelta(days=1))  # можно переопределить
<Log: log at 2016-02-11 17:02:34>
```

#### LazyAttribute: зависимые поля

Для полей, зависящих от других полей объекта:

```python
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')
```

```python
>>> UserFactory()
<User: user1 (user1@example.com)>
>>> UserFactory(username='john')
<User: john (john@example.com)>
```

### Faker

Документация: https://faker.readthedocs.io/

```bash
pip install Faker
```

Faker генерирует реалистичные тестовые данные: имена, адреса, тексты, даты и многое другое.

#### Базовое использование

```python
from faker import Faker

fake = Faker()

fake.name()       # 'Lucy Cechtelar'
fake.address()    # '426 Jordy Lodge\nCartwrightshire, SC 88120-6700'
fake.email()      # 'john.doe@example.com'
fake.text()       # Случайный текст
```

#### Интеграция с FactoryBoy

Faker отлично интегрируется с FactoryBoy через `factory.Faker`:

```python
import factory
from factory.django import DjangoModelFactory
from django.utils.text import slugify
from blog.models import Article


class ArticleFactory(DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.Faker('sentence', nb_words=5)
    slug = factory.LazyAttribute(lambda o: slugify(o.title))
    content = factory.Faker('paragraphs', nb=3, ext_word_list=None)
    status = 'published'
    author = factory.SubFactory('blog.tests.factories.UserFactory')
```

### Фабрики для моделей блога

Создадим полный набор фабрик для нашего блога:

```python
# blog/tests/factories.py
import factory
from factory.django import DjangoModelFactory
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from blog.models import Article, Topic, Comment

User = get_user_model()


class UserFactory(DjangoModelFactory):
    """Фабрика для создания пользователей"""
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda o: f'{o.username}@example.com')
    password = factory.PostGenerationMethodCall('set_password', 'testpass123')


class TopicFactory(DjangoModelFactory):
    """Фабрика для создания тем"""
    class Meta:
        model = Topic

    name = factory.Sequence(lambda n: f'Тема {n}')


class ArticleFactory(DjangoModelFactory):
    """Фабрика для создания статей"""
    class Meta:
        model = Article

    title = factory.Faker('sentence', nb_words=5, locale='ru_RU')
    slug = factory.LazyAttribute(lambda o: slugify(o.title))
    content = factory.Faker('text', max_nb_chars=500, locale='ru_RU')
    status = 'published'
    author = factory.SubFactory(UserFactory)

    @factory.post_generation
    def topics(self, create, extracted, **kwargs):
        """Добавление тем к статье (ManyToMany)"""
        if not create:
            return
        if extracted:
            for topic in extracted:
                self.topics.add(topic)


class CommentFactory(DjangoModelFactory):
    """Фабрика для создания комментариев"""
    class Meta:
        model = Comment

    text = factory.Faker('paragraph', nb_sentences=2, locale='ru_RU')
    author = factory.SubFactory(UserFactory)
    article = factory.SubFactory(ArticleFactory)
```

#### Использование фабрик в тестах

```python
from blog.tests.factories import ArticleFactory, TopicFactory, UserFactory


class ArticleTests(APITestCase):
    def setUp(self):
        self.author = UserFactory()
        self.topic = TopicFactory(name='Python')
        # Статья с конкретным автором и темой
        self.article = ArticleFactory(
            author=self.author,
            topics=[self.topic]
        )

    def test_article_has_author(self):
        self.assertEqual(self.article.author, self.author)

    def test_article_has_topic(self):
        self.assertIn(self.topic, self.article.topics.all())
```

#### Специализированные фабрики

```python
class DraftArticleFactory(ArticleFactory):
    """Фабрика для черновиков"""
    status = 'draft'


class PublishedArticleFactory(ArticleFactory):
    """Фабрика для опубликованных статей"""
    status = 'published'
```

---

## Полный пример: тестирование ArticleViewSet

Соберём всё вместе — полный набор тестов для API статей блога.

### Структура тестов

```
blog/
├── tests/
│   ├── __init__.py
│   ├── factories.py          # Фабрики (см. выше)
│   ├── test_models.py        # Unit-тесты моделей
│   ├── test_serializers.py   # Unit-тесты сериализаторов
│   └── test_views.py         # Интеграционные тесты API
```

### Тесты CRUD операций

```python
# blog/tests/test_views.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.tests.factories import ArticleFactory, UserFactory, TopicFactory
from blog.models import Article


class ArticleCRUDTests(APITestCase):
    """Тесты CRUD операций для статей"""

    def setUp(self):
        self.author = UserFactory()
        self.other_user = UserFactory()
        self.topic = TopicFactory(name='Django')
        self.article = ArticleFactory(author=self.author, topics=[self.topic])

    # === CREATE ===
    def test_create_article_authenticated(self):
        """Авторизованный пользователь может создать статью"""
        self.client.force_authenticate(user=self.author)
        url = reverse('article-list')
        data = {
            'title': 'Новая статья',
            'slug': 'novaya-statya',
            'content': 'Содержимое статьи',
            'status': 'draft'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Article.objects.count(), 2)
        new_article = Article.objects.get(slug='novaya-statya')
        self.assertEqual(new_article.author, self.author)

    def test_create_article_anonymous_forbidden(self):
        """Анонимный пользователь не может создать статью"""
        url = reverse('article-list')
        data = {'title': 'Статья', 'slug': 'statya', 'content': 'Текст'}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # === READ ===
    def test_list_articles_anonymous(self):
        """Анонимный пользователь видит список опубликованных статей"""
        ArticleFactory(status='draft', author=self.author)  # Черновик
        ArticleFactory(status='published', author=self.author)  # Опубликована

        url = reverse('article-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Видим только опубликованные (1 из setUp + 1 новая)
        self.assertEqual(len(response.data['results']), 2)

    def test_retrieve_article(self):
        """Получение детальной информации о статье"""
        url = reverse('article-detail', kwargs={'pk': self.article.pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.article.title)

    # === UPDATE ===
    def test_update_own_article(self):
        """Автор может редактировать свою статью"""
        self.client.force_authenticate(user=self.author)
        url = reverse('article-detail', kwargs={'pk': self.article.pk})
        data = {'title': 'Обновлённый заголовок'}

        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.article.refresh_from_db()
        self.assertEqual(self.article.title, 'Обновлённый заголовок')

    def test_update_other_user_article_forbidden(self):
        """Другой пользователь не может редактировать чужую статью"""
        self.client.force_authenticate(user=self.other_user)
        url = reverse('article-detail', kwargs={'pk': self.article.pk})
        data = {'title': 'Попытка изменить'}

        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # === DELETE ===
    def test_delete_own_article(self):
        """Автор может удалить свою статью"""
        self.client.force_authenticate(user=self.author)
        url = reverse('article-detail', kwargs={'pk': self.article.pk})

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Article.objects.filter(pk=self.article.pk).exists())

    def test_delete_other_user_article_forbidden(self):
        """Другой пользователь не может удалить чужую статью"""
        self.client.force_authenticate(user=self.other_user)
        url = reverse('article-detail', kwargs={'pk': self.article.pk})

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
```

### Тесты Permissions

```python
class ArticlePermissionTests(APITestCase):
    """Тесты прав доступа"""

    def setUp(self):
        self.author = UserFactory()
        self.admin = UserFactory(is_staff=True)
        self.draft = ArticleFactory(author=self.author, status='draft')
        self.published = ArticleFactory(author=self.author, status='published')

    def test_draft_visible_only_to_author(self):
        """Черновик виден только автору"""
        url = reverse('article-detail', kwargs={'pk': self.draft.pk})

        # Анонимный пользователь — 404
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Автор — 200
        self.client.force_authenticate(user=self.author)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_can_delete_any_article(self):
        """Администратор может удалить любую статью"""
        self.client.force_authenticate(user=self.admin)
        url = reverse('article-detail', kwargs={'pk': self.published.pk})

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
```

### Тесты фильтрации и поиска

```python
class ArticleFilterTests(APITestCase):
    """Тесты фильтрации и поиска"""

    def setUp(self):
        self.python_topic = TopicFactory(name='Python')
        self.django_topic = TopicFactory(name='Django')
        self.author1 = UserFactory(username='alice')
        self.author2 = UserFactory(username='bob')

        self.article1 = ArticleFactory(
            title='Введение в Python',
            author=self.author1,
            topics=[self.python_topic]
        )
        self.article2 = ArticleFactory(
            title='Django для начинающих',
            author=self.author2,
            topics=[self.django_topic, self.python_topic]
        )

    def test_filter_by_topic(self):
        """Фильтрация по теме"""
        url = reverse('article-list')

        response = self.client.get(url, {'topics': self.django_topic.pk})

        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Django для начинающих')

    def test_filter_by_author(self):
        """Фильтрация по автору"""
        url = reverse('article-list')

        response = self.client.get(url, {'author': self.author1.pk})

        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['author']['username'], 'alice')

    def test_search_by_title(self):
        """Поиск по заголовку"""
        url = reverse('article-list')

        response = self.client.get(url, {'search': 'Python'})

        self.assertEqual(len(response.data['results']), 1)
        self.assertIn('Python', response.data['results'][0]['title'])

    def test_ordering_by_created_at(self):
        """Сортировка по дате создания"""
        url = reverse('article-list')

        response = self.client.get(url, {'ordering': '-created_at'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверяем, что статьи отсортированы по убыванию даты
        dates = [a['created_at'] for a in response.data['results']]
        self.assertEqual(dates, sorted(dates, reverse=True))
```

### Тесты с pytest

```python
# blog/tests/test_views_pytest.py
import pytest
from django.urls import reverse
from rest_framework import status
from blog.tests.factories import ArticleFactory, UserFactory


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def author(db):
    return UserFactory()


@pytest.fixture
def article(db, author):
    return ArticleFactory(author=author)


@pytest.mark.django_db
class TestArticleAPI:
    def test_list_articles(self, api_client, article):
        url = reverse('article-list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_create_article_authenticated(self, api_client, author):
        api_client.force_authenticate(user=author)
        url = reverse('article-list')
        data = {'title': 'Новая статья', 'slug': 'novaya-statya', 'content': 'Текст', 'status': 'draft'}

        response = api_client.post(url, data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['author']['username'] == author.username

    @pytest.mark.parametrize('status_code,user_authenticated', [
        (status.HTTP_401_UNAUTHORIZED, False),
        (status.HTTP_201_CREATED, True),
    ])
    def test_create_article_auth_required(
        self, api_client, author, status_code, user_authenticated
    ):
        if user_authenticated:
            api_client.force_authenticate(user=author)

        url = reverse('article-list')
        response = api_client.post(url, {'title': 'Test', 'slug': 'test', 'content': 'Text'}, format='json')

        assert response.status_code == status_code
```

#### Providers: дополнительные генераторы

Faker имеет множество провайдеров для разных типов данных:

```python
from faker import Faker
from faker.providers import internet

fake = Faker()
fake.add_provider(internet)

fake.ipv4_private()  # '10.10.11.69'
fake.url()           # 'https://example.com/path'
fake.user_name()     # 'john_doe'
```

## Мокирование и изоляция внешних сервисов

Документация: https://docs.python.org/3/library/unittest.mock.html

- Патчьте точку использования (where it’s used), а не место определения.
- Пригодится autospec=True и проверка вызовов: mock.assert_called_once_with(...)

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
        url = reverse('article-list')
        assert self.client.get(url).status_code == status.HTTP_200_OK
        assert self.client.get(url).status_code == status.HTTP_200_OK
        assert self.client.get(url).status_code == status.HTTP_429_TOO_MANY_REQUESTS
```

> Совет: для предсказуемости очищайте кеш между тестами или используйте отдельный cache alias для тестов:

```python
from django.core.cache import cache


def teardown_function():
    cache.clear()
```

В многосерверной среде используйте общий backend кеша (например, Redis) для тротлинга.

## Современный инструментарий: pytest и pytest-django

pytest стал стандартом де-факто для тестов в Django/DRF за счёт простоты, фикстур и полезных плагинов.
Документация: https://docs.pytest.org/
pytest-django: https://pytest-django.readthedocs.io/

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

Совет: для ускорения повторных прогонов используйте ключ --reuse-db (плагин pytest-django).

Пример pytest.ini:

```ini
[pytest]
DJANGO_SETTINGS_MODULE = project.settings
python_files = tests.py test_*.py *_tests.py
```

#### Фикстуры в conftest.py

Повторно используйте фикстуры в корневом файле conftest.py, чтобы не импортировать их в каждом тесте:

```python
# conftest.py
import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()
```

#### Дополнительные фикстуры: user и auth_client

```python
# conftest.py
@pytest.fixture
def user(db, user_factory):
    return user_factory()


@pytest.fixture
def auth_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client
```

В pytest-django доступны фикстуры: client (Django client), db/transactional_db, settings, monkeypatch и др.

#### Расширенный pytest.ini

```ini
[pytest]
DJANGO_SETTINGS_MODULE = project.settings
python_files = tests.py test_*.py *_tests.py
# Флаги по умолчанию
addopts = -q --strict-markers --disable-warnings
# Где искать тесты
testpaths = tests
```

#### База данных в тестах

```python
import pytest


@pytest.mark.django_db
def test_uses_db():
    # Обычные ORM-операции в рамках транзакции TestCase
    ...


@pytest.mark.django_db(transaction=True)
def test_needs_transactions():
    # Для кейсов, где нужна настоящая транзакция (например, тесты celery/task или raw SQL)
    ...
```

#### Параметризация тестов

```python
import pytest


@pytest.mark.parametrize(
    "a,b,expected",
    [(1, 2, 3), (2, 3, 5)],
    ids=["1+2", "2+3"],
)
def test_add(a, b, expected):
    assert a + b == expected
```

#### Переопределение настроек и окружения

```python
def test_override_settings(settings):
    settings.DEBUG = False
```

```python
def test_env(monkeypatch):
    monkeypatch.setenv("FEATURE_X", "1")
```

#### Полезные инструменты: caplog и tmp_path

```python
import logging


def test_logging(caplog):
    with caplog.at_level(logging.INFO):
        ...
    assert "Started" in caplog.text
```

```python
def test_tmp_path(tmp_path):
    p = tmp_path / "data.txt"
    p.write_text("hello")
    assert p.read_text() == "hello"
```

#### Маркеры pytest и контроль запуска

Документация: https://docs.pytest.org/en/stable/reference/reference.html#marks

pytest.ini:

```ini
[pytest]
markers =
    slow: медленные тесты
    api: API-тесты
```

Использование:

```python
import pytest


@pytest.mark.slow
def test_something():
    ...
```

xfail и skipif:

```python
import pytest, sys


@pytest.mark.skipif(sys.platform == 'win32', reason='no Windows support')
def test_only_unix():
    ...


@pytest.mark.xfail(reason='bug #123', strict=True)
def test_known_bug():
    assert 1 == 2
```

---

## Итоги

В этой лекции мы изучили:

1. **Уровни тестирования**:
   - Unit-тесты: проверка отдельных компонентов в изоляции
   - Интеграционные тесты: проверка взаимодействия компонентов
   - Acceptance-тесты: имитация действий пользователя

2. **Иерархия TestCase в Django**:
   - `SimpleTestCase`: без БД, с Client
   - `TransactionTestCase`: с реальными транзакциями
   - `TestCase`: с откатом транзакций (рекомендуется)
   - `LiveServerTestCase`: для Selenium-тестов

3. **Инструменты Django**:
   - `RequestFactory`: unit-тесты view без middleware
   - `Client`: интеграционные тесты с полным циклом запроса

4. **Инструменты DRF**:
   - `APIRequestFactory`: unit-тесты API view
   - `APIClient` / `APITestCase`: интеграционные тесты API
   - `force_authenticate()`: авторизация без проверки пароля

5. **Генерация тестовых данных**:
   - FactoryBoy: фабрики для создания объектов
   - Faker: генерация реалистичных данных
   - `SubFactory`, `Sequence`, `LazyAttribute`

6. **pytest и pytest-django**:
   - Фикстуры и `conftest.py`
   - Маркеры `@pytest.mark.django_db`
   - Параметризация тестов

---

## Домашнее задание

### Практика на занятии

1. Создайте фабрики `UserFactory`, `ArticleFactory`, `TopicFactory` для блога
2. Напишите тест создания статьи авторизованным пользователем
3. Напишите тест, проверяющий, что анонимный пользователь не может создать статью

### Домашняя работа

1. **Полный набор CRUD-тестов для ArticleViewSet**:
   - Тесты создания, чтения, обновления, удаления
   - Проверка кодов ответа (200, 201, 204, 400, 401, 403, 404)
   - Проверка данных в ответе

2. **Тесты Permissions**:
   - `IsAuthorOrReadOnly`: автор может редактировать, остальные только читать
   - `IsPublishedOrAuthor`: черновики видит только автор
   - Администратор: может удалять любые статьи

3. **Тесты фильтрации и поиска**:
   - Фильтрация по теме, автору, статусу
   - Поиск по заголовку и содержимому
   - Сортировка по дате создания

4. **Тесты CommentViewSet**:
   - Создание комментария к статье
   - Удаление своего комментария
   - Модератор может удалять любые комментарии

5. **Перевод тестов на pytest**:
   - Создайте `conftest.py` с фикстурами
   - Используйте `@pytest.mark.django_db`
   - Добавьте параметризацию для тестов авторизации

---

## Вопросы для самопроверки

1. В чём разница между `RequestFactory` и `Client`?
2. Когда использовать `TransactionTestCase` вместо `TestCase`?
3. Что делает `force_authenticate()` и когда его использовать?
4. Чем `APIRequestFactory` отличается от `APIClient`?
5. Как создать фабрику для модели со связью ManyToMany?
6. Что такое `SubFactory` и зачем он нужен?
7. Как использовать Faker с FactoryBoy?
8. Что такое фикстуры в pytest и как их определять?
9. Для чего нужен маркер `@pytest.mark.django_db`?
10. Как тестировать throttling в DRF?

---

[← Лекция 29: REST-аутентификация. Авторизация. Permissions. Фильтрация.](lesson29.md) | [Лекция 31: Celery. Multithreading. GIL. Multiprocessing →](lesson31.md)
