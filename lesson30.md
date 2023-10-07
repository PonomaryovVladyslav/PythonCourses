# Урок 30. Модели

![](https://www.meme-arsenal.com/memes/ec0eba9bc1a90ba417d786f9096cce72.jpg)

### Нет, не такие :)

## Установка базы

В наших примерах мы будем использовать PostgreSQL, для этого предварительно нужно эту базу установить.

Скачать, если не установлена: [Тут](https://www.postgresql.org/download/)

## Создание базы и пользователя базы

[Прекрасная статья по этому поводу под Linux](https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e)

Предположим, что база у вас установлена, и пароль для пользователя `postgres` создан.

Заходим в консоль базы данных

Под Windows:

`psql -U postgres`

Под Linux:

`sudo -u postgres psql`

Под Windows вы должны увидеть нечто похожее:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/psql.png)

Создаём базу с кодировкой 'UTF8', чтобы избежать проблем с русским и другими языками в базе.

`create database mydb with encoding 'UTF8';`

Создаём пользователя для пользования этой базой.

`create user myuser with password 'mypass';`

Даём новому пользователю права на использование новой базы.

`grant all on database mydb to myuser;`

Консоль в конце должна выглядеть так:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/database_and_user.png)


**Если вы используете Postgres 15 и новее**

Необходимо выполнить дополнительное действие после предоставления прав к базе данных.

Нужно предоставить вашему пользователю права к схеме `public` в новой базе данных.

Для этого нужно подключиться к новой базе:

`\c mydb` - где `mydb` это имя созданной базы данных

После чего выполнить команду:

`grant all on schema public to myuser;`

Для выхода из консоли наберите `\q` и нажмите Enter.

## Конфигурация Django

Открываем проект и в нём файл `settings.py`

Находим строку `DATABASES`

Если вы ничего не меняли, то выглядеть она должна так:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/sqllitedb.png)

Заменяем на

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'mypass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Где `ENGINE` - это "движок", он же модуль, отвечающий за работу базы данных.

`NAME` - это имя базы,

`USER` - это имя пользователя,

`PASSWORD` - это пароль пользователя,

`HOST` - это хост (урл, расположение базы),

`PORT` - это порт (5432 стандартный порт для PostgreSQL, если вы его изменили при установке, укажите свой).

Чтобы это работало, нужно установить тот самый "движок", соответствующий вашей операционной системе:

```
pip install psycopg2  # windows
pip install psycopg2-binary  # unix
```

**Не забывайте про venv**

Если вы всё сделали правильно, то при запуске сервера (`python manage.py runserver`) вы должны увидеть, что-то такое:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/working.png)

## Команда migrate

Обратите внимание на вот эту надпись:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/migrate_text.png)

Когда мы создаём Django проект, мы создаём приложения для своих нужд, но на самом деле внутри уже есть несколько
приложений для общих нужд, `admin`, `auth`, `contenttype`, `session`.

Все их мы разберем немного позже. В данный момент критичным является то, что в каждом из этих приложений находится
информация о том, что должно храниться в базе. А наша свежая, только что созданная база не имеет нужных таблиц, в
соответствии с моделями описанными в этих приложениях. Описания того, что должно быть в базе, называются **Миграции**.

При применении миграций в базе создаются нужные таблицы, поля, связи и т. д.

Для применения нужно выполнить команду

`python manage.py migrate`

Если всё ок, то результат выполнения должен выглядеть примерно так:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/migrate.png)

## Приложения

Чтобы Django увидела какие-либо изменения, нужно добавлять каждое своё приложение в `settings.py`

Находим в файле `settings.py` раздел `INSTALLED_APPS` и дописываем наше приложение, чтобы получилось:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp'
]
```

Теперь всё готово для того, чтобы начинать разработку собственных моделей.

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/start.jpg)

## Создание моделей

Ничего лучше, чем официальная документация, никто не придумал, офф
дока [Тут](https://docs.djangoproject.com/en/4.2/topics/db/models/)

Что такое класс модели? Это таблица для базы данных, где атрибуты - это её поля.

Давайте создадим модель!

В файле `myapp/models.py`

Напишем вот это:

```python
from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
``` 

Мы создали нашу первую модель, состоящую из **3** полей: `name`, `text` и `id`, причём поле `id` было создано автоматически
без нашего участия, и она автоматически стало primary key. Поле `name` не может содержать более 100 символов. Поле `text` может
быть "пустым" или отсутствовать полностью.

Чтобы наши изменения попали в базу, нужно создать и применить миграцию.

#### Команда makemigrations

Теперь мы применим команду

`python manage.py makemigrations`

И увидим нечто похожее на:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/makemigrations.png)

Django радостно нам сообщает, что миграция была создана. Давайте проверим, откроем папку `myapp/migrations` и увидим там
новый файл `0001_initial.py`

Выглядеть он будет вот так:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/init_migration.png)

Где мы можем убедиться, что Django действительно создала за нас поле `id`

#### Команда showmigrations

Чтобы убедиться, что миграция не применена/применена, используется команда

`python manage.py showmigrations`

Результат:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/showmigrations.png)

Как мы можем видеть, наша миграция существует, но не применена, давайте применим её командой `python manage.py migrate`

Результат:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/migrate_init.png)

И сравним `showmigrations` теперь:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/showmigrations_after.png)

## Админка

Самый быстрый и удобный способ смотреть на объекты моделей - это админка. Чтобы ей пользоваться, нужно сделать
две вещи: в урлы добавить встроенный урл админки и создать суперпользователя.

Команда создания суперпользователя:

`python manage.py createsuperuser`

Вводим всё, что от нас требует консоль, и юзер будет создан:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/createsuperuser.png)

Если вы не стирали урл для админки, то он уже у вас есть, если стирали, то допишите в `myproject/urls.py`

```python
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    ...
]
```

Перезапускаем сервер, и заходим на
[Админку](https://127.0.0.1:8000/admin)

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/admin_login.png)

Вбиваем имя и пароль созданного пользователя и видим:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/admin_first_login.png)

По дефолту, у Django сразу есть две модели из "коробки" - User и Group.

Но нет нашей модели, почему же? Потому что модели нужно регистрировать, чтобы не заполнять админку ненужными
данными.

Для этого нам нужно в файле `admin.py` в вашем приложении импортировать вашу модель и зарегистрировать её

```python
from django.contrib import admin
from .models import Article

admin.site.register(Article)
```

Открываем админку еще раз:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/add_model_to_admin.png)

Теперь наша модель появилась в админке, и мы можем добавлять, удалять, смотреть, редактировать наши модели.

## Кастомная админка

Возможности встроенной админки очень велики, но её можно дописывать, видоизменять, добавлять кастомные действия
и т. д. Подробно разберем на одном из следующих занятий, сейчас попробуйте создать/изменить/удалить несколько объектов.

Админку можно кастомизировать. Чтобы изменить или добавить любое действие, используются специальные классы.

Ссылка на оф доку [тут](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/)

Весь функционал описан в приложении `django.contrib.admin`, о котором мы говорили выше, оно добавлено в
наш проект по умолчанию.

```python
from .models import Article
from django.contrib import admin


class ArticleAdmin(admin.ModelAdmin):
    fields = ('name', 'title', 'create_date')

    def create_date(self, obj):
        return obj.created

    view_birth_date.empty_value_display = '???'


admin.site.register(Article, ArticleAdmin)
```

## Основные типы полей и их стандартные атрибуты.

[Ссылка на все существующие типы полей](https://docs.djangoproject.com/en/4.2/ref/models/fields/)

Когда вы создаёте модель, у неё автоматически появляется атрибут `id`. Он является Primary Key по умолчанию, если
это не было переписано явно.

`id` - это очень удобное поле, т. к. оно является автоматическим, и когда вы создаёте новый объект, ему сразу назначается новый
идентификационный номер, на один больше предыдущего.

Так же все типы полей имеют встроенный атрибут `default`, который заполняется, если нужно указать значение по умолчанию

### BooleanField

Хранит True или False

```python
my_flag = models.BooleanField()
```

### CharField

Строковое поле, принимает обязательный аргумент max_length - максимальное количество символов

Часто используемые флаги `null` и `blank`, `null=True` означает, что поле может быть `None`, `black=True` означает, что поле
может быть пустой строкой `''`.

```python
my_char = models.CharField(max_length=120, null=True, blank=False)
```

### DateField и DateTimeField

Поля для хранения даты и даты и времени

Принимают аргументы `auto_now` и `auto_now_add`. 
`auto_now_add` обозначает, что при создании объекта это поле будет автоматически заполнено текущей датой и временем. 
`auto_now` будет обновляться каждый раз, когда объект сохраняется. 
(часто используют для сохранения даты создания и даты обновления объекта)

```python
created_at = models.DateField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
```

### DecimalField

Хранение чисел типа Float

Обязательные параметры: `max_digits` - максимальное количество символов, `decimal_places` - количество знаков после запятой.

```python
    float_number = models.DecimalField(decimal_places=2, max_digits=12)
```

### EmailField

Такой же текстовый, как и CharField, с проверкой на валидность имейла

### FileField

Для хранения файлов, можно указать `upload_to` - место для хранения файлов, если не указано, будет использовано, то, что
в `settings.py`

```python
    my_file = models.FileField()
```

### ImageField

Тоже что и FileField с валидацией изображения.

### IntegerField

Хранение целых чисел от -2147483648 до 2147483647

```python
    int_number = models.IntegerField()
```

### URLField

Текстовый тип для хранения урлов.

```python
    my_url = models.URLField()
```

И многие другие, читайте доку.

# Связи

![](http://memesmix.net/media/created/jb8uel.jpg)

Модели могут быть связаны между собой, для этого существует 3 типа связей

OneToOne - связь один-к-одному

ForeignKey - связь один-ко-многим

ManyToMany - связь многие-ко-многим

### One to one

Связь один к одному чаще всего используется для какого-либо однозначного определения разных моделей (Допустим,
пользователя и модели, где хранятся его настройки)

Чтобы установить связь, нам нужно создать две модели и в одной из них указать зависимость

```python
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()


class CustomerSettings(models.Model):
    preferred_color = models.CharField()
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='cus')
```

Теперь эти модели связаны, что мы и увидим в админке.

### Foreign Key

Самая распространенная связь. Один ко многим. Допустим, у нас есть книга, её написал конкретный автор, но это не значит,
что этот автор написал только эту книгу.

```python
class Author(models.Model):
    name = models.CharField(max_length=120)


class Book(models.Model):
    name = models.CharField(max_length=120)
    year_of_public = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

```

### Many to Many

Многие ко многим, допустим, вы описываете базу для кинопоиска, один фильм может быть снят несколькими режиссерами, но при
этом каждый из режиссеров может снять больше одного фильма, такая связь называется ManyToMany. Для построения таких
связей мы используем связь ManyToMany:

```python
from django.db import models


class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline
```

На самом деле, "под капотом" создаётся дополнительная таблица, которая хранит информацию о связи между двумя видами
моделей.

Если нам нужно контролировать эту таблицу, мы можем сделать это при помощи специального слова ```through```

```python
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
```

## ContentTypes

На самом деле, существуют более сложные конструкции, например, фреймворк `ContentType`, который позволяет делать
зависимость полей динамической (Допустим, сделать лайк зависимым от динамического типа данных, например, хочешь ставить к
статье, а хочешь к комментарию, хотя это одна и та же модель)

Дока [Тут](https://docs.djangoproject.com/en/4.2/ref/contrib/contenttypes/)

Подробно мы не будем рассматривать этот функционал, но я бы очень рекомендовал ознакомиться.

Работает, основываясь на приложении `django.conrib.contenttype`, добавленное в наш проект по умолчанию.

![](https://lendiplompro.ru/images/praktica/praktica.jpg)

# Домашнее задание / Практика:

https://edu-python-course.github.io/_build/html/uk/appx/blog/spec.html#challenge-data-models

topic <--> blogpost = m2m: у blogpost должен быть хотя бы 1 topic

user <--> topic = m2m: 0 или больше с 2-х сторон

blogpost <--> user = fk: у поста 1 автор, автор может создать любое количество постов

comment <--> user = fk: то же самое, что и выше

comment <--> blogpost = fk: комментарий привязан к 1 посту, у поста столько угодно комментариев
