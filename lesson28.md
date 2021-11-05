# Урок 28. Знакомство с Django

![](https://the-flow.ru/uploads/images/resize/830x0/adaptiveResize/06/04/56/59/17/253344b40cd7.jpg)

## Request-response, протокол http

Практически любой интернет ресурс работает на принципе **запрос-ответ**, наша задача, как программистов, правильно
описывать логику того, что должно происходить при определенном запросе.

![](https://www.iguides.ru/upload/medialibrary/a60/a60857ccc094b4bfd975d0fa842bcb1c.png)

### Краткое описание http запросов

Из чего состоит http запрос можно почитать [тут](https://developer.mozilla.org/ru/docs/Web/HTTP/Messages), но если
вкратце, то из тела, где хранятся данные, и хедеров, где хранится служебная информация.

#### Метод GET

Используется для запроса содержимого указанного ресурса. Например получить данные, файл или любую другую информацию,
браузер (Chrome, Mozzila, etc.) при наборе url (https://ru.wikipedia.org/,
https://www.youtube.com/watch?v-WdZJ-QUItHw&t-7974s) использует именно GET запрос, может передавать переменные в query
параметре (в примере с ютубом ?v-WdZJ-QUItHw&t-7974s это query параметры, начинается с символа ?, следующий параметр
добавляется при помощи символа & в данном примере, параметр {'v': 'WdZJ-QUItHw', 't': '7974s'})

Обычно не используется для отправки данных, только для получения определенной информации. Например получение
комментариев к посту в блоге.

#### Метод POST

Применяется для передачи пользовательских данных заданному ресурсу. Например, в блогах посетители обычно могут вводить
свои комментарии к записям в HTML-форму, после чего они передаются серверу методом POST и он помещает их на страницу.
При этом передаваемые данные (в примере с блогами — текст комментария) включаются в тело запроса. Аналогично с помощью
метода POST обычно загружаются файлы на сервер. Может содержать много данных или файлов (или и то, и другое).

#### Метод PUT

Применяется для обновления данных по заданному ресурсу **целиком**, например, изменение комментария. Может содержать
много данных или файлов (или и то и другое).

#### Метод PATCH

Почти аналогичен методу PUT, но применяется для **частичного** изменения объекта. Допустим изменения данных в профиле в
соц сети, при изменении имейла, нам не нужно изменять весь профиль, только поле имейл. Может содержать много данных или
файлов (или и то и другое).

#### Метод DELETE

Используется для удаления объектов, обычно не принимает данные, как и метод гет. Пример, все тот же комментарий.

Существуют и другие запросы, которые используют реже и с другими назначениями, их и более подробно эти запросы, мы
рассмотрим на другом занятии.

Описанные запросы используют, для стандартных CRUD операций, Create - POST, Retrieve - GET, Update - PUT/PATCH, Delete -
DELETE

## Шаблон проектирования MVC

Для разработки любых сложных решений используются шаблоны проектирования.

Для нас, в данный момент, самым важных из них является **MVC (Model - View - Controller) (Модель - Отображение -
Контроллер)**

Что же это такое?

Это разделение обязанностей между тремя зависимыми блоками.

Представте себе работу ресторана.

Моделью в таком примере является склад продуктов, на нем есть определенные продукты, но сами по себе они не меняются,
без внешнего воздействия (повар взял продукты, или поставщик добавил).

Отображением будет блюдо, вы как клиент (пользователь) можете прийти и заказать себе еду, но вы понятия не имеете какие
именно продукты есть сейчас на складе, и можете только догадываться как именно эти продукты будут обрабатываться, так
как у вас есть меню, и вы можете посмотреть список доступных блюд.

Контроллер, в этом случае, это персонал ресторана, принимают заказы, смотрят, смогут ли они их выполнить, обрабатывают
продукты и подают за стол, и если нужно заказывают еще продукты.

Сегодня изучим как именно формируется "меню".

![](https://miro.medium.com/max/1304/1*la8KCs0AKSzVGShoLQo2oQ.png)

По этому же принципу работает и Django, но с немного другим названием, паттерн называется MVT (Model - View - Template),
где View играет роль контроллера, а Template роль отображения, но суть при этом сохраняется.

## Что же такое все таки Django?

**Django** - веб-фреймворк, а фреймворк это по своей сути конструктор, который помогает нам собирать блоки, часто даже
не задумываясь как именно это работает под капотом.

![](https://www.meme-arsenal.com/memes/07d78e429e60f57b09f8afb5e4446bd1.jpg)

Основной информационный ресурс [Django](https://www.djangoproject.com/)

## Наконец-то практика

Создадим новый проект, для этого, **создадим новое виртуальное окружение**, и установим туда Django

```pip install django```

```django-admin startproject mysite```

Эта команда создаёт новый проект, и заполняет его базово нужными файлами, давайте рассмотрим их.

Структура файлов:

```
mysite /
    manage.py
    mysite /
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

**manage.py** - файл-утилка при помощи которого мы будем взаимодействовать со многими частями Django из консоли

Внутри папки mysite:

**\_\_init__.py** - Пустой файл, который говорит Python-у, что этот каталог должен рассматриваться как пакет Python-а

**settings.py** - Настройки и конфигурации проекта.

**urls.py** - URL-ы для этого проекта; «оглавление» вашего сайта на платформе Django.

**wsgi.py** - Файл отвечающий за входную точку сервера (Позволяет запускать код как сайт)

Проверим работоспособность.

В консоли запустим локальный "сервер" из папки с нашим "сайтом" (в моём примере mysite)

```python manage.py runserver```

В консоли должна появиться примерно такая надпись.

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson33/runserver.png)

Не закрывая консоль (сервер должен работать), открываем в браузере http://127.0.0.1:8000/

`127.0.0.1` это локальный хост а `:8000` это номер порта на котором запущен процесс. `127.0.0.1` можно заменить
на `0.0.0.0` или слово `localhost`, все три варианта практически взаимозаменяемы.

Если вы всё сделали правильно, то в браузере должны увидеть, что-то такое:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson33/worked.png)

## Создаём приложение

Настройки и конфигурации это замечательно, но правильная архитектура проекта, подразумевает использование отдельных
модулей как части сайта (бывает один на весь сайт, а бывают и тысячи), такие модули называются приложениями, и именно в
них пишется "суть" сайта.

Через консоль, и уже известную нам `manage.py` создадим приложение

```python manage.py startapp myapp```

Команда создаст вам папку с вашим приложением, давайте разберем её подробнее

```
myapp/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

**\_\_init__.py** - Пустой файл, который говорит Python-у, что этот каталог должен рассматриваться как пакет Python-а

**admin.py** - заготовка под админку

**apps.py** - информация о приложении (нужно при большом коле-ве приложений, для удобства)

**папка migrations** - Тут будут миграции базы данных.

**models.py** - Модели.

**tests.py** - Тесты.

**views.py** - Контроллер приложения.

## Наш первый URL

Теперь у нас всё готово для того, что бы начать создавать наш сайт. Сегодня мы будем разбираться, как работают urls.

При любом запросе к запущенному Django приложению запущенный сервер при обработке в первую очередь заходит в
файл `settings.py` и ищет там переменную `URL_CONF`, по умолчанию там будет указан файл `urls.py` который находится в
той же папке где и `settings.py`.

Внутри этого файла Django ожидает наличие переменной `urlpatterns`, которая содержит коллекцию (например список)
состоящую из специальных объектов `path` или `re_path`.

На самом деле эти объекты появились в Django только после версии, 2.0, сейчас актуальная версия это 3.2, но потенциально
вы можете встретить и версии ниже, например 1.11, поэтому ниже разберем и более старые варианты урлов. До 2.0 там были
коллекции из объектов `url`, и все они работали на регулярных выражениях, о них позже.

Всё основная логика обработки запросов пишется в приложениях, в файлах `views.py`, у нас всего одно приложение поэтому
всю логику (сегодня она будет простейшая) мы будем писать в файл `myapp/views.py`.

Для начала изменим файл `views.py`

```python
from django.http import HttpResponse


def main(request):
    return HttpResponse("Hey! It's your main view!!")
```

Мы создали функцию, которая принимает один параметр `request` и возвращает объект `HttpResponse`.

Это нужно потому что вся веб-инфраструктура работает на `request-response` системе, мы тоже не будем её нарушать, и
будем принимать запросы, и возвращать ответы.

Объект `HttpResponse` мы импортировали из Django, и на данном этапе нас совершенно не интересует как он работает.

По сути эта функция является контролером, но не спешите, контролеры мы будем изучать детально.

Для использования этого контролера в качестве логики, он должен быть описан в файле `urls.py`:

```python
from django.urls import path
from myapp.views import main

urlpatterns = [
    path('', main)
]
```

Мы импортировали `path` из django и метод `main` из нашего `views.py`

Объект `path`, принимает два обязательных параметра:

1) строка с адресом, пустая обозначает `home page`, на сленге "хомяк", страница, которая открывается при открытии сайта,
   в нашем случае, http://127.0.0.1:8000/, не пустые случаи рассмотрим далее
2) обработчик, что именно должно происходить при запросе на такой адрес.

Так же может принимать атрибут `name=`, который нужен дня автоматической генерации адресов, будем изучать на следующем
занятии.

Если мы перезагрузим (ну или запустим) сервер и откроем страницу, то мы увидим, что-то такое:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson28/main_home.png)

Список урлов проекта называется роутинг. Роутинг можно строить так как вам удобно, или как того требует задание.

Напишем еще один контролер, для "другой" страницы. В файле `myapp/views.py`

```python
from django.http import HttpResponse


def main(request):
    return HttpResponse("Hey! It's your main view!!")


def another(request):
    return HttpResponse("It's another page!!")

```

А в файле `mysite/urls.py` импортируем эту функции и добавим маршрут в список, что бы получилось так:

```python
from django.urls import path
from myapp.views import main, another

urlpatterns = [
    path('', main),
    path('some_url/', another)
]
```

То что написано в строке до контролера это путь к урлу, а значит, что бы увидеть обработку этого контролера нужно
открыть страницу http:/127.0.0.1:8000/some_url/

Открываем [эту](http:/127.0.0.1:8000/some_url/) страницу и видим результат:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson28/another_page.png)

## Урлы с параметрами

Урл может заведомо принимать параметры, самый простой способ, это описание параметра через синтаксис `<type:variable>`

Обновим наш `urls.py`:

```python
from django.urls import path
from myapp.views import main, another, main_article, uniq_article, article

urlpatterns = [
    path('', main),
    path('some_url/', another),
    path('article/', main_article, name='mail_article'),
    path('article/33/', uniq_article, name='uniq_article'),
    path('article/<int:article_id>/', article, name='article'),
]
```

Обратите внимание, часть урлов теперь имеет параметр `name`, он понадобится на следующем занятии

А в последнем url мы указали параметр <int:article_id>, значение до двоеточия, это тип данных который принимает
параметр, а после это имя параметра который можно будет использовать в контролере, что бы получить значение этого
параметра.

Всего существует 5 таких типов:

- str - Ищет не пустую строку, без символа `/`

- int - Ноль или любое положительное число.

- slug - по сути это тоже строка, которая состоит из букв, цифр, нижних подчеркиваний, дефисов, символов плюс,
  например `building-your-1st-django-site` отличается от обычной строки тем, что обычно этот урл берет данные из уже
  существующих данных, название статьи, уникальный номер товара итд.

- uuid - Ищет соответствие UUID, это специальный формат состоящий из шестнадцатиричных цифр и букв и дефисов, дефисы
  должны быть обязательно, буквы маленькие. Например, 075194d3-6885-417e-a8a8-6c931e272f00.

- path - Строка с символом/лами '/'

```Обратите внимание что url `article/33/` попадает так же и под `article/<int:article_id>/` потому что 33 это тоже цифра, в этом случае будет использован тот который находится в списке первым. Урлы считываются сверху вниз ```

Изменим `myapp/views.py`:

```python
from django.http import HttpResponse


def main(request):
    return HttpResponse("Hey! It's your main view!!")


def another(request):
    return HttpResponse("It's another page!!")


def main_article(request):
    return HttpResponse('There will be a list with articles')


def uniq_article(request):
    return HttpResponse('This is uniq answer for uniq value')


def article(request, article_id):
    return HttpResponse(f"This is an article #{article_id}.")
```

Обратите внимание в функцию `article` я добавил параметр `article_id` для получения значения в контролере.

Давайте посмотрим на результат при заходе на разные страницы.

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson33/static_url.png)

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson33/static_const_url.png)

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson28/page_article_with_num.png)

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson28/page_article_with_str.png)

Последнее это пример работы если урл не был описан (Всем известная страница 404, в дебаг режиме, она может рассказать
много подробностей об ошибке) В данном примере, ошибка говорит, о том, что контролера для указанного запроса не
существует.

Так как параметры в функции могут быть не обязательными, мы можем воспользоваться и этим свойством тоже.

`views.py`

```python
from django.http import HttpResponse


def main(request):
    return HttpResponse("Hey! It's your main view!!")


def another(request):
    return HttpResponse("It's another page!!")


def main_article(request):
    return HttpResponse('There will be a list with articles')


def uniq_article(request):
    return HttpResponse('This is uniq answer for uniq value')


def article(request, article_id, name=''):
    return HttpResponse(
        "This is an article #{}. {}".format(article_id, "Name of this article is {}".format(
            name) if name else "This is unnamed article"))
```

`urls.py`

```python
from django.urls import path
from myapp.views import main, another, main_article, uniq_article, article

urlpatterns = [
    path('', main),
    path('some_url/', another),
    path('article/', main_article, name='mail_article'),
    path('article/33/', uniq_article, name='uniq_article'),
    path('article/<int:article_id>/', article, name='article'),
    path('article/<int:article_id>/<slug:name>', article, name='article_name'),
]
```

Результаты некоторых запросов:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson28/unnamed_article.png)

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson28/named_article.png)

### include

На самом деле path, может принимать не только обработчик, но и специальный параметр `include`, который позволяет
добавить урлы из другого файла к основному.

Например, вы видите, что у нас есть 4 урла которые начинаются на `article/`, а значит что удобным вариантом было бы
вынести урлы в отдельный файл, обычно такие файлы создаются на уровне приложений, а основной файл с урлами содержит
только инклюды

Для того, что бы перенести часть урлов, нам необходимо создать файл `urls.py` в приложении `myapp` (на самом деле мы
могли и назвать его как угодно, и сложить его куда угодно, но так просто удобнее и читаемее), и обязательно в этом файле
создать переменную `urlpatterns` содержащую коллекцию урлов.

Посмотрим на измененные\добавленные файлы:

`myapp/urls.py`

```python
from django.urls import path
from .views import main_article, uniq_article, article

urlpatterns = [
    path('', main_article, name='mail_article'),
    path('33/', uniq_article, name='uniq_article'),
    path('<int:article_id>/', article, name='article'),
    path('<int:article_id>/<slug:name>', article, name='article_name'),
]
```

`mysite/urls.py`

```python
from django.urls import path, include
from myapp.views import main, another

urlpatterns = [
    path('', main),
    path('some_url/', another),
    path('article/', include('myapp.urls'))
]
```

**После этого изменения ни один урл не изменился** - они просто стали по другому располагаться, в случае с 4 урлами не
до конца понятно зачем это может быть нужно, но когда у нас существует 20 приложений и в них 5000+ урлов, структура
становится очень важна, что бы ничего не потерять, поэтому правилом хорошего тона для django кода считается создание
файла с урлами в каждом приложении, а в основном хранить только инклюды на них (Если сделать `url` path('', include('
app.urls')), то можно перенести и те 2 урла которые мы сейчас оставили в основных урлах.)

## re_path

### Регулярные выражения

![](https://www.meme-arsenal.com/memes/d92b55ae26fca33c655197ce4c6a79b9.jpg)

Как говорит нам
википедия [Регуля́рные выраже́ния](https://ru.wikipedia.org/wiki/%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%BD%D1%8B%D0%B5_%D0%B2%D1%8B%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F) (
англ. regular expressions) — используемый в компьютерных программах, работающих с текстом, формальный язык поиска и
осуществления манипуляций с подстроками в тексте, основанный на использовании метасимволов (символов-джокеров, англ.
wildcard characters). Для поиска используется строка-образец (англ. pattern, по-русски её часто называют «шаблоном»,
«маской»), состоящая из символов и метасимволов и задающая правило поиска. Для манипуляций с текстом дополнительно
задаётся строка замены, которая также может содержать в себе специальные символы.

По факту это механизм который позволяет понять, соответствует ли наша строка каким либо задачам.

![](https://python-school.ru/wp-content/uploads/2020/12/2.jpg)

Например. Бывают случаи когда нам не подходит просто строка или просто число, а нужно указывать более сложные параметры.

Предположим, что нам нужно указать в качестве части урла три цифры и хотя бы 2 буквы (`123blabla`, `432fo`,`111aaaaa`
итд. но `12asd` не подходило)

![](https://miro.medium.com/max/660/0*NfcqRr1hjlXdl2lZ.jpg)

Для того, что бы собрать такую конструкцию нужно воспользоваться синтаксисом регулярных выражений, мне лично нравится
вот этот [сайт](https://regex101.com/), на неё можно изучить базовые принципы использования регулярных выражений.

Получаем необходимое регулярное выражение:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson28/regex.png)

Теперь давайте попробуем использовать его в url

`mysite/urls.py`:

```python
from django.urls import path, include, re_path
from myapp.views import main, another, regex

urlpatterns = [
    path('', main),
    path('some_url/', another),
    path('article/', include('myapp.urls')),
    re_path('\d{3}[a-zA-Z]{2,}', regex),
]
```

`views.py`

```python
from django.http import HttpResponse


def main(request):
    return HttpResponse("Hey! It's your main view!!")


def another(request):
    return HttpResponse("It's another page!!")


def main_article(request):
    return HttpResponse('There will be a list with articles')


def uniq_article(request):
    return HttpResponse('This is uniq answer for uniq value')


def article(request, article_id, name=''):
    return HttpResponse(
        "This is an article #{}. {}".format(article_id, "Name of this article is {}".format(
            name) if name else "This is unnamed article"))


def regex(request):
    return HttpResponse("it's regexp")

```

Обратите внимание мы используем не `path`, a `re_path`.

Такой url уже будет работать.

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson28/regex_url.png)

Но как нам получить значение именно этого регулярного выражения? Как бы не было ужасно, но завернуть его в другое регулярное выражение.

И после этого не забыть получать его в контролере

`mysite/urls.py`

```python
from django.urls import path, include, re_path
from myapp.views import main, another, regex


urlpatterns = [
    path('', main),
    path('some_url/', another),
    path('article/', include('myapp.urls')),
    re_path(r'^(?P<text>\d{3}[a-zA-Z]{2,}$)', regex),
]

```

`views.py`

```python
from django.http import HttpResponse


def main(request):
    return HttpResponse("Hey! It's your main view!!")


def another(request):
    return HttpResponse("It's another page!!")


def main_article(request):
    return HttpResponse('There will be a list with articles')


def uniq_article(request):
    return HttpResponse('This is uniq answer for uniq value')


def article(request, article_id, name=''):
    return HttpResponse(
        "This is an article #{}. {}".format(article_id, "Name of this article is {}".format(
            name) if name else "This is unnamed article"))


def regex(request, text):
    return HttpResponse(f"it's regexp with text: {text}")

```

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson28/regex_text.png)

Мы получили данные из урла.

Бывают и более сложные конструкции, рассмотрите их по [вот этой ссылке](https://docs.djangoproject.com/en/3.1/topics/http/urls/)

На практике редко встречаются более сложные конструкции, но джанго представляет нам такую возможность.


# Практика / Домашнее задание:

1. Создать новый проект и новое приложение

2. Создать в нём всю необходимую структуру, для урлов: 
* `http://127.0.0.1:8000/`, 
* `http://127.0.0.1:8000/acricles`, 
* `http://127.0.0.1:8000/acrticles/archive`, 
* `http://127.0.0.1:8000/users`

3. Создать структуру для динамических урлов: 
* `http://127.0.0.1:8000/article/<int:article_number>`, 
* `http://127.0.0.1:8000/article/<int:article_number>/archive`, 
* `http://127.0.0.1:8000/article/<int:article_number>/<slug:slug_text>`, 
* `http://127.0.0.1:8000/users/<int:user_number>`

4. Создать урл который будет принимать параметр вида 4 символа от 1 до 9, или от a до f, знак дефиса и еще 6 символов,
   например `/34f1-1ac498/`

5. Создать урл который будет принимать в качестве параметра корректный номер украинского мобильного телефона, 050123121 - корректно, 0751231212 - нет

Возвращать урлы, могут, всё что угодно, главное, что бы они работали!!!
Для урлов с регулярными выражениями, в ответе должно быть значение этого регулярного выражения