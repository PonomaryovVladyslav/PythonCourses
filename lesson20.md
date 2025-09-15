# Лекция 20. Templates. Static

### Оглавление курса

- Блок 1 — Python Basic (1–6):
  - [Лекция 1. Введение. Типизации. Переменные. Строки и числа. Булева алгебра. Ветвление](lesson01.md)
  - [Лекция 2. Обработка исключений. Списки, строки детальнее, срезы, циклы.](lesson02.md)
  - [Лекция 3: None. Range, list comprehension, sum, max, min, len, sorted, all, any. Работа с файлами](lesson03.md)
  - [Лекция 4. Хэш таблицы. Set, frozenset. Dict. Tuple. Немного об импортах. Namedtuple, OrderedDict](lesson04.md)
  - [Лекция 5. Функции, типизация, lambda. Map, zip, filter.](lesson05.md)
  - [Лекция 6. Рекурсия. Алгоритмы. Бинарный поиск, сортировки](lesson06.md)
- Блок 2 — Git (7–8):
  - [Лекция 7. Git. История системы контроля версий. Локальный репозиторий. Базовые команды управления репозиторием.](lesson07.md)
  - [Лекция 8. Git. Удаленный репозиторий. Remote, push, pull. GitHub, Bitbucket, GitLab, etc. Pull request.](lesson08.md)
- Блок 3 — Python Advanced (9–14):
  - [Лекция 9. Введение в ООП. Основные парадигмы ООП. Классы и объекты.](lesson09.md)
  - [Лекция 10. Множественное наследование. MRO. Magic methods.](lesson10.md)
  - [Лекция 11. Imports. Standard library. PEP8](lesson11.md)
  - [Лекция 12. Декораторы. Декораторы с параметрами. Декораторы классов (staticmethod, classmethod, property)](lesson12.md)
  - [Лекция 13. Тестирование](lesson13.md)
  - [Лекция 14. Проектирование. Паттерны. SOLID.](lesson14.md)
- Блок 4 — SQL (15–17):
  - [Лекция 15. СУБД. PostgreSQL. SQL. DDL. Пользователи. DCL. DML. Связи.](lesson15.md)
  - [Лекция 16. СУБД. DQL. SELECT. Индексы. Group by. Joins.](lesson16.md)
  - [Лекция 17. СУБД. Нормализация. Аномалии. Транзакции. ACID. TCL. Backup](lesson17.md)
- [Лекция 18. Virtual env. Pip. Устанавливаемые модули. Pyenv.](lesson18.md)
- Блок 5 — Django (19–26):
  - [Лекция 19. Знакомство с Django](lesson19.md)
  - ▶ **Лекция 20. Templates. Static**
  - [Лекция 21. Модели. Связи. Meta. Abstract, proxy.](lesson21.md)
  - [Лекция 22. Django ORM.](lesson22.md)
  - [Лекция 23. Forms, ModelForms. User, Authentication.](lesson23.md)
  - [Лекция 24. ClassBaseView](lesson24.md)
  - [Лекция 25. NoSQL. Куки, сессии, кеш](lesson25.md)
  - [Лекция 26. Логирование. Middleware. Signals. Messages. Manage commands](lesson26.md)
- Блок 6 — Django Rest Framework (27–30):
  - [Лекция 27. Что такое API. REST и RESTful. Django REST Framework.](lesson27.md)
  - [Лекция 28. @api_view, APIView, ViewSets, Pagination, Routers](lesson28.md)
  - [Лекция 29. REST аутентификация. Авторизация. Permissions. Фильтрация.](lesson29.md)
  - [Лекция 30. Тестирование. Django, REST API.](lesson30.md)
- Блок 7 — Python async (31–33):
  - [Лекция 31. Celery. Multithreading. GIL. Multiprocessing](lesson31.md)
  - [Лекция 32. Асинхронное программирование в Python. Корутины. Asyncio.](lesson32.md)
  - [Лекция 33. Сокеты. Django channels.](lesson33.md)
- Блок 8 — Deployment (34–35):
  - [Лекция 34. Linux. Все что нужно знать для деплоймента.](lesson34.md)
  - [Лекция 35. Deployment](lesson35.md)
- [Лекция 36. Методологии разработки. CI/CD. Монолит и микросервисы. Docker](lesson36.md)


![](https://imgflip.com/s/meme/Boardroom-Meeting-Suggestion.jpg)

## Что сегодня учим?

![mvc_templates.png](pictures/mvc_templates.png)

## Шаблоны

Что же такое шаблон? В бытовом понимании - это заготовка под что-то, что потом будет использоваться, в Django это почти
также.

Шаблонами мы называем заготовленные html страницы, в которые мы можем добавить необходимые нам данные и логику.

Но как это работает?

Откроем начатый проект с прошлого занятия.

Создадим новую папку на уровне корня проекта и назовём её `templates` (название может быть любым, но принято называть
именно так.) Чтобы получилась вот такая структура:

```
mysite/
myapp/
templates/
manage.py
```

Чтобы обрабатывать шаблоны, мы должны "рассказать" Django, где именно искать эти самые шаблоны. Для этого нужно
открыть `mysite/settings.py` и отредактировать его.

В данный момент нас интересует переменная `TEMPLATES`, выглядит она примерно так:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson34/templates_var.png)

В ключ `DIRS` добавим нашу папку с шаблонами, чтобы получилось так:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson34/templates_filled.png)

Пример минимальной настройки DIRS:

```python
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES[0]["DIRS"] = [BASE_DIR / "templates"]
# APP_DIRS=True также ищет шаблоны в myapp/templates/
```

> Для шаблонов приложений удобно использовать неймспейсы: `myapp/templates/myapp/index.html` и вызывать `render(request, 'myapp/index.html')`.

Ключи:

`BACKEND`: путь к классу, который отвечает за обработку данных и логику. (Замена требуется очень редко.)

`DIRS`: список папок, в которых Django будет искать шаблоны.

`APP_DIRS`: булевое поле, которое отвечает за то, нужно ли искать папки с шаблонами внутри папки с приложениями,
например,
в нашей структуре, если значение `False`, то поиск будет только в папке `templates` на уровне файла `manage.py`, а если
значение `True`, то в папках `/templates` и `/myapp/templates/`.

`OPTIONS`: дополнительные настройки, будем рассматривать позже.

В режиме разработки runserver автоматически перезагружает сервер при изменениях кода и шаблонов; при изменении некоторых настроек может потребоваться ручной перезапуск (`python manage.py runserver`).

Мы "рассказали" Django, где именно искать шаблоны, но пока ни одного не создали. Давайте сделаем это!

В папке `templates` нужно создать html файл, назовём его `index.html` (название не имеет значения, главное, чтобы
формат был `html`).

```
mysite/
myapp/
templates/
    index.html
manage.py
```

Содержимое файла `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

That's template!

</body>
</html>
```

Итак, теперь у нас есть один шаблон, но мы его не используем, давайте переделаем нашу `view` для обработки шаблонов.

В файле `myapp/views.py` нужно импортировать обработчик шаблонов, в начало файла добавляем

```python
from django.shortcuts import render
```

> Функция render возвращает объект типа HttpResponse

И перепишем функцию `index`:

```python
def index(request):
    return render(request, 'index.html')
```

Перезапустим сервер и увидим результат на главной странице `http://127.0.0.1:8000/`

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson34/render_template.png)

Мы отрендерили шаблон! Но в нём нет никаких переданных данных, для передачи данных нужно в метод render добавить третий
аргумент в виде словаря.

Для демонстрации основных типов данных я допишу функцию `index` и передам большое количество значений в словаре:

```python
class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s

def index(request):
    my_num = 33
    my_str = 'some string'
    my_dict = {"some_key": "some_value"}
    my_list = ['list_first_item', 'list_second_item', 'list_third_item']
    my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
    my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
    my_class = MyClass('class string')
    return render(request, 'index.html', {
        'my_num': my_num,
        'my_str': my_str,
        'my_dict': my_dict,
        'my_list': my_list,
        'my_set': my_set,
        'my_tuple': my_tuple,
        'my_class': my_class,
    })
```

Значения переданы, но пока они никак не используются, давайте же посмотрим, как отобразить переменные в шаблоне!

Для вывода данных в Django темплейте используются фигурные скобки `{{ }}`

```
{{first_name}}
{{last_name}}
```

Для доступа к вложенным структурам используется точка:

```
{{my_dict.key}}
{{my_object.attribute}}
{{my_list.0}}
```

Изменим наш `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div>
    <div style="border: 1px darkblue solid">
        {{ my_num }}
    </div>
    <div style="border: 1px darkseagreen solid">
        {{ my_str }}
    </div>
    <div style="border: 1px fuchsia solid">
        {{ my_set }}
    </div>
    <div style="border: 1px firebrick solid">
        {{ my_dict.some_key }}
    </div>

    <div style="border: 1px cyan solid">
        {{ my_class.string }}
    </div>
    <div style="border: 1px cyan solid">
        {{ my_list.0 }}
    </div>
    <div style="border: 1px burlywood solid">
        {{ my_tuple.1 }}
    </div>
</div>
</body>
</html>
```

Обновим страницу и увидим.

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson34/render_variables.png)

### Логические операторы и циклы

![](http://risovach.ru/upload/2013/01/mem/kakoy-pacan_7772237_orig_.jpeg)

> После всех логических операторов и циклов в шаблонах нужно ставить соответствующий закрывающий тег!
> Например, `{% for ...%} {% endfor %}`, `{% if ... %} {% endif %}`.

#### Логические операторы

В шаблонах можно оперировать не только переменными, но и несложной логикой, такой как логические операторы и циклы.

Давайте добавим в наши параметры переменную `display_num` и назначим ей значение `False`.

`myapp/views.py`

```python
 return render(request, 'index.html', {
    'my_num': my_num,
    'my_str': my_str,
    'my_dict': my_dict,
    'my_list': my_list,
    'my_set': my_set,
    'my_tuple': my_tuple,
    'my_class': my_class,
    'display_num': False
})
```

Для логических условий и циклов используются другие скобки `{% %}`

Изменим наш шаблон с использованием логики:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div>
    {% if display_num %}
    {{ my_num }}
    {% else %}
    <span> We don't display num </span>
    {% endif %}
</div>
</body>
</html>
```

> Отступы тут не имеют никакого значения, просто так удобнее читать

Обновим страницу и увидим:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson34/If_statement.png)

А если в файле `views.py` изменим переменную `display_num` с `False` на `True`:

`myapp/views.py`

```python
 return render(request, 'index.html', {
    'my_num': my_num,
    'my_str': my_str,
    'my_dict': my_dict,
    'my_list': my_list,
    'my_set': my_set,
    'my_tuple': my_tuple,
    'my_class': my_class,
    'display_num': True
})
```

То увидим:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson34/if_true.png)

Т.к. значение переменной `display_num` True, то мы видим значение переменной `my_num`

#### Циклы

Также, как и в Python, мы можем использовать циклы в шаблонах, но только цикл `for` — цикла `while` в шаблонах не существует.

Изменим наш `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div>
    {% for item in my_list %}
    <span>{{ item }}</span>
    <br>
    {% endfor %}
</div>
</body>
</html>
```

Обновим страницу и увидим:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson34/basic_for.png)

> Еще раз, логика через `{% %}`, данные через `{{ }}`

Давайте скомбинируем!

Внутри цикла `for` Джанго уже генерирует некоторые переменные, например, переменную `{{ forloop.counter0 }}`,

в которой хранится индекс текущей итерации, давайте не будем выводить в цикле второй элемент.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div>
    {% for item in my_list %}
    {% if forloop.counter0 != 1 %}
    <span>{{ item }}</span>
    <br>
    {% endif %}
    {% endfor %}
</div>
</body>
</html>
```

`{% if forloop.counter0 != 1 %}`

Символ != это не равно, а значение 1, потому что индекс начинается с 0.

Обновляем страницу и видим:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson34/for_if.png)

## Встроенные темплейт теги.

На самом деле все ключевые слова используемые внутри `{% %}` называются template tags, и их существует огромное
множество.

[Ссылка на доку](https://docs.djangoproject.com/en/stable/ref/templates/builtins/)

Их очень много, часть мы рассмотрим, часть вам придется изучить самостоятельно.

## Tag URL

Тег url позволяет нам сгенерировать урл по его имени. Это очень удобно, если адрес меняется, а его имя нет.

Давайте сгенерируем две ссылки на два наших урла.

`mysite/urls.py`

Назначим имя `index`

```python
path('', index, name='index')
```

`myapp/urls.py`

Назначим имя `first`

```python
path('', first, name='first'),
```

Добавим в наш шаблон ссылку на вторую страницу:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div>
    <a href="{% url 'first' %}">Another page</a>
</div>
</body>
</html>
```

```html
<a href="{% url 'article' 33 %}">Article #33</a>
```

Наш индекс пейдж:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson34/index_link.png)

После клика:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson34/first_link.png)

### Наследование шаблонов

![](https://i.pinimg.com/originals/43/3e/8f/433e8f7ebb982220a6f43b829679dd5d.jpg)

#### Extends и block

Теги наследования шаблонов `extends`, `block`

Зачем нам это надо?

Наследование шаблонов нужно, чтобы не писать одно и то же отображение много раз. Как часто вы видели сайты, где сверху,
снизу, слева, справа и т. д. всегда одно и тоже, а меняется только "середина"? Самый простой способ так сделать - это
наследование.

Тут нам и помогут наши волшебные теги!

Создадим в папке `templates` новые файлы `base.html` и `first.html` и изменим файлы `templates/index.html` и
функцию `first` в `myapp/views.py`

`templates/base.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div style="background-color: aqua">
    {% block content %}
    {% endblock %}
</div>
</body>
</html>
```

`templates/index.html`

```html
{% extends 'base.html' %}

{% block content %}
<div style="padding: 20px; background-color: fuchsia"> Extended template index!</div>
<a href="{% url 'first' %}">To the first page</a>
{% endblock %}
```

`templates/first.html`

```html
{% extends 'base.html' %}

{% block content %}
<div style="padding: 20px; background-color: chocolate"> Extended template first!</div>
<a href="{% url 'index' %}">To the index page</a>
{% endblock %}
```

Функция `first` в `myapp/views.py`

```python
def first(request):
    return render(request, 'first.html')
```

Смотрим результаты произошедшего и пытаемся их понять. (ссылки добавлены для удобства)

Индекс страница

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson34/extended_index.png)

Первая страница

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson34/extended_first.png)

Что произошло?

Мы создали базовый шаблон `base.html`, в котором описали то, что будет во всех шаблонах (и покрасили в голубенький, для
наглядности), которые от него наследуются, и обозначили `{% block content %}` (здесь block - это тэг, а content -
присвоенное ему название, его можно выбрать произвольно) вся нужная нам информация будет наследоваться именно в
указанный блок, на странице разных блоков может
быть сколько угодно главное, что бы они имели разные названия.

Наш индекс пейдж рендерит страницу `index.html`, в ней мы отнаследовались от нашей `base.html`, вписали такой же
блок `content`, чтобы передать в него нужные нам данные, в нашем случае это просто текст и ссылка, текст мы перекрасили,
чтобы было видно, что это данные из нового файла, а ссылку нет, чтобы было видно, что цвет из `base.html`
отнаследовался, то же самое произошло и с `first.html`.

#### Include

А теперь представим обратную ситуацию: нам нужно в разные части сайта "засунуть" один и тот же блок (рекламу, например)

Тут нас спасает тег `include` который позволяет "внедрить" нужную часть страницы куда угодно

Создадим в папке `templates` еще один файл с названием `add.html`

`templates/add.html`

 ```html

<div style="padding: 20px; background-color: chartreuse"> That's included html!</div>
```

И теперь добавим этот файл к страницам `index.html` и `first.html`, но в разные места, чтобы получилось

`templates/index.html`

```html
{% extends 'base.html' %}

{% block content %}
{% include 'add.html' %}
<div style="padding: 20px; background-color: fuchsia"> Extended template index!</div>
<a href="{% url 'first' %}">To the first page</a>
{% endblock %}
```

`templates/first.html`

```html
{% extends 'base.html' %}

{% block content %}
<div style="padding: 20px; background-color: chocolate"> Extended template first!</div>
<a href="{% url 'index' %}">To the index page</a>
{% include 'add.html' %}
{% endblock %}
```

Смотрим на результат:

`index.html`:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson34/include_index.png)

`first.html`:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson34/include_first.png)

В добавленную станицу можно передать переменные при помощи тега `with`

Изменим файл `templates/add.html`

```html

<div style="padding: 20px; background-color: chartreuse"> Hello {{ name }} !</div>
```

И файл `templates/index.html`

```html
{% extends 'base.html' %}

{% block content %}
{% include 'add.html' with name='Vlad' %}
<div style="padding: 20px; background-color: fuchsia"> Extended template index!</div>
<a href="{% url 'first' %}">To the first page</a>
{% endblock %}
```

Смотрим на результат:

`index.html`

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson34/include_var.png)

`first.html`

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson34/include_non_var.png)

В первом случае мы видим добавленную переменную, во втором - ничего, так как мы ничего не передавали.

Давайте добавим проверку на наличие переменной!

`templates/add.html`

```html
<div style="padding: 20px; background-color: chartreuse">{% if name %} Hello {{ name }} ! {% else %} Sorry, I don't know your name {% endif %}</div>
```

Смотрим на first page

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson34/first_no_var.png)

Переменной нет, срабатывает if

Также можно передавать эту переменную из view; в with передаём имя переменной без фигурных скобок.

Пример:

```html
{% include 'add.html' with name=my_str %}
```

## Фильтры

![](https://a.d-cd.net/egAAAgNDHeA-1920.jpg)

Что это такое, и зачем это нужно?

Фильтры - это возможность видоизменить данные перед их отображением. Давайте попробуем ими воспользоваться, для этого
во `view` добавим сверху файла

```python
from datetime import datetime
```

`myapp/views.py` функция `index`

```python
def index(request):
    my_num = 33
    my_str = 'some string'
    my_dict = {"some_key": "some_value"}
    my_list = ['list_first_item', 'list_second_item', 'list_third_item']
    my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
    my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
    my_class = MyClass('class string')
    return render(request, 'index.html', {
        'my_num': my_num,
        'my_str': my_str,
        'my_dict': my_dict,
        'my_list': my_list,
        'my_set': my_set,
        'my_tuple': my_tuple,
        'my_class': my_class,
        'display_num': True,
        'now': datetime.now()
    })
```

А `index.html` изменим так

```html
{% extends 'base.html' %}

{% block content %}
<div>{{ now| date:"SHORT_DATE_FORMAT" }}</div>
<div>{{ now|date:"D d M Y" }} {{ now|time:"H:i" }}</div>
<div>{{ not_exist|default:"nothing" }}</div>
<div>{{ my_str | capfirst }}</div>
<div>{{ my_list | join:"**" }}</div>
{% endblock %}
```

Смотрим на результат

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson34/filters.png)

Каждый фильтр имеет свои особенности и правила написания, подробнее можно посмотреть по ссылке выше.

Кроме того, для данных существуют встроенные фильтры.

Например `date`, `default`, `join`, `capfirst`. На самом деле их огромное количество, весь список встроенных фильтров
можно
посмотреть [Тыц](https://docs.djangoproject.com/en/stable/ref/templates/builtins/)

## Кастомные темплейт теги и фильтры

На самом деле, стандартным набором дело не ограничивается, и в случае необходимости можно дописать свои теги и фильтры,
почитать об этом можно вот [тут](https://docs.djangoproject.com/en/stable/howto/custom-template-tags/)

![](https://i.ytimg.com/vi/gF060AIFiB8/hqdefault.jpg)

# Работа со статикой

## Что такое статические файлы?

Прежде чем перейти к рассмотрению template tag, давайте разберемся, что такое статические файлы. В контексте
веб-разработки статические файлы — это те файлы, которые не изменяются на сервере, а напрямую передаются пользователю. К
ним относятся:

- CSS файлы, отвечающие за стилизацию веб-страниц.
- JavaScript файлы, добавляющие интерактивность страницам.
- Изображения, иконки, шрифты и другие медиафайлы.

В Django эти файлы не хранятся в базе данных и не генерируются динамически, как HTML-контент. Они должны быть доступны
для всех клиентов в неизменном виде.

## Настройка Django для работы со статическими файлами

Прежде чем мы сможем использовать `{% static %}`, необходимо правильно настроить Django для работы со статическими
файлами. Основные шаги включают:

- Указание директории для хранения статических файлов.
- Настройка URL для доступа к статическим файлам.

В файле `settings.py` вы найдете (или добавите) следующие параметры:

- `STATIC_URL`: Этот параметр определяет URL, по которому будут доступны статические файлы. Обычно это `/static/`.
- Убедитесь, что приложение 'django.contrib.staticfiles' есть в INSTALLED_APPS (в новых проектах добавляется по умолчанию).

  ```python
  STATIC_URL = '/static/'
  ```

> Этот параметр скорее всего указан автоматически, он отвечает за то, что бы ваши статические файлы можно было бы
> получить по адресу `http://127.0.0.1:8000/static/` на самом деле там много деталей и нюансов, но их мы будем
> рассматривать гораздо позже.

> Для того что бы у вас отрабатывали статические файлы нужно что бы у вас в `settings.py` был указан `DEBUG=True`, что
> это и зачем опять же дальше по курсу

- `STATICFILES_DIRS`: Этот параметр указывает на дополнительные директории, в которых Django будет искать статические
  файлы. Это полезно, если у вас есть несколько источников для статических файлов.

  ```python
  STATICFILES_DIRS = [BASE_DIR / "static"]
  ```

```text
project/
  static/
    css/styles.css
  templates/
    base.html
```

> Просто указываете папку куда вы сложили свои статические файлы.

- `STATIC_ROOT`: Этот параметр используется для указания директории, куда Django будет собирать все статические файлы
  при выполнении команды `collectstatic`. Это полезно для деплоя на продакшн сервер.

  ```python
  STATIC_ROOT = BASE_DIR / "staticfiles"
  ```

> Этот параметр вам пока не нужен! Он используется для запуска приложений на реальных серверах

## Использование template tag `{% static %}`

Теперь, когда мы настроили Django для работы со статическими файлами, давайте рассмотрим, как используется template
tag `{% static %}`. Этот тег позволяет нам генерировать правильные URL для статических файлов в шаблонах.

### Загрузка библиотеки static

Прежде чем использовать тег `{% static %}`, необходимо загрузить соответствующую библиотеку в вашем шаблоне. Это
делается с помощью тега `{% load static %}`. Этот тег должен быть расположен в верхней части вашего шаблона, как
правило, до использования `{% static %}`.

> Обычно записывается в самом верху, по аналогии с `import` в python

Пример:

```html
{% load static %}
```

### Основной синтаксис

Синтаксис тега `{% static %}` выглядит следующим образом:

```html
{% static 'path/to/your/static/file.ext' %}
```

Здесь `'path/to/your/static/file.ext'` — это путь к файлу относительно одной из директорий, указанных
в `STATICFILES_DIRS`.

### Пример использования

Предположим, у вас есть файл `styles.css`, находящийся в директории `static/css/`. Чтобы подключить этот файл в шаблоне,
вам нужно использовать следующий код:

```html
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static 'css/styles.css' %}">
```

Django автоматически преобразует это в правильный URL, который будет выглядеть как `/static/css/styles.css`.

### Использование в различных контекстах

Тег `{% static %}` можно использовать не только для CSS, но и для других типов файлов, например, изображений или
JavaScript:

```html
{% load static %}
<img src="{% static 'images/logo.png' %}" alt="Logo">
<script src="{% static 'js/main.js' %}"></script>
```

## Практическое значение и важность

Преимущество использования `{% static %}` заключается в том, что он обеспечивает правильное разрешение путей к
статическим файлам независимо от того, где они находятся. Это особенно важно при деплое (отправке кода на настоящий
сервер) приложения, когда может измениться базовый URL для статических файлов.

Кроме того, использование `{% static %}` делает ваш код более устойчивым к изменениям. Например, если вы решите
переместить свои статические файлы в другую директорию, вам не придется изменять все шаблоны — достаточно будет обновить
настройки.

## Практические рекомендации

1. **Всегда загружайте библиотеку static.** Не забывайте добавлять `{% load static %}` в начало ваших шаблонов, где
   используются статические файлы.

2. **Не хардкодьте пути к статическим файлам.** Всегда используйте `{% static %}` для создания ссылок на статические
   файлы.

3. **Организуйте свои статические файлы логически.** Размещайте их в соответствующих поддиректориях,
   например, `css`, `js`, `images`.
