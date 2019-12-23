# Урок 35. Модели

![](https://www.meme-arsenal.com/memes/ec0eba9bc1a90ba417d786f9096cce72.jpg)

### Нет, не такие :)

## Установка базы

В наших примерах, мы будем использовать PostgreSQL, для этого предварительно нужно эту базу установить.

Скачать, если не установлена: [Тут](https://www.postgresql.org/download/)

## Cоздание базы и пользователя базы

[Прекрасная статья по этому поводу под Linux](https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e)

Предположим, что база у вас установлена, и пароль для пользователя `postgres` создан.

Заходим в консоль базы данных

Под Windows:

`psql -U postgres`

Под Linux:

`sudo -u postgres psql`

Под Windows вы должны увидеть нечто похожее:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/psql.png)

Создаём базу с кодировкой 'UTF8', что бы избежать проблем с русским и другими языками в базе.

`create database mydb with encoding 'UTF8';`

Создаём пользователя для пользования этой базой.

`create user myuser with password 'mypass'`

Даём новому пользователю права для использования новой базой.

`grant all on database mydb to myuser`

Консоль в конце должна выглядеть так:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/database_and_user.png)

Для выхода из консоли наберите `\q` и нажмите Enter.

## Конфигурация Django

Открываем проект, и в нём файл `settings.py`

И находим строку `DATABASES`

Если вы ничего не меняли то выглядеть должна так:

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
Где `ENGINE` это "движок" он же модуль отвечающий за работу базы данных, `NAME` это имя базы, `USER` это имя пользователя, `PASSWORD` это пароль пользователя, `HOST` это хост(урл, расположение базы), `PORT` это порт (5432 стандартный порт для postgres, если вы его изменили при установке, укажите свой).

Для того, что бы это работало, нужно установить тот самый "движок".

`pip install psycopg2`

**Не забывайте про venv**

Если вы всё сделали правильно, то при запуске сервера (`python manage.py runserver`) вы должны увидеть, что-то такое:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/working.png)


## Команда migrate

Обратите внимание на вот эту надпись:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/migrate_text.png)

Когда мы создаём Django проект, мы создаём приложения для своих нужд, но на самом деле, внутри уже есть несколько приложений для общих нужд, для версии Django 2.2 это `admin`, `auth`, `contenttype`, `session`.

Все их мы разберем немного позже, в данный момент критичным является то, что в каждом из этих приложений находится информация о том что должно храниться в базе, а наша свежая, только что созданная база, не имеет нужных таблиц, в соответствии с моделями описаными в этих приложениях, описания того что должно быть в базе называются **Миграции**.

При применения миграций, в базе создаются нужные таблицы, поля, связи итд.
 
Для применения нужно выполнить команду 

`python manage.py migrate`

Если всё ок, то результат выполнения должен выглядеть примерно так:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/migrate.png)

## Приложения

Для того что бы Django увидела какие-либо изменения нужно добавлять каждое своё приложение в `settings.py`

Находим в этом файле `INSTALLED_APPS`

и дописываем наше приложение, что бы получилось:

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

Теперь всё готово, для того что бы начинать разработку собственных моделей!!

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/start.jpg)
 
## Создание моделей 
 
Всё еще лучше чем официальная документация еще никто и ничего не придумал, офф дока [Тут](https://docs.djangoproject.com/en/2.2/topics/db/models/)
 
Давайте создадим модель!

В файле `myapp/models.py` 

Напишем вот это:

```python
from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
``` 

Мы создали нашу первую модель, состоящую из **3** полей, поля `name`, `text`, `id`, при чём айди создался автоматически без нашего участия, автоматически стало primary key.
Поле `name` не может содержать более 100 символов
Поле `text` может быть "пустым" или отсутсвовать полностью.

Для того, что бы наши изменения попали в базу, нужно создать и применить миграцию.

#### Команда makemigrations

Теперь мы применим команду 

`python manage.py makemigrations`

И увидим нечто похожее на:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/makemigrations.png)


Django радостно нам сообщает, что миграция была создана, давайте проверим, откроем папку `myapp/migrations` и увидим там новый файл `0001_initial.py`

Выглядеть он будет вот так:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/init_migration.png)

Где мы можем убедиться, что Django действительно создала за нас поле `id`
 
#### Команда showmigrations

Что бы убедиться, что миграция не пременена/пременена используется команда

`python manage.py showmigratons`

Результат:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/showmigrations.png)
 
Как мы можем видеть, наша миграция существует, но не применена, давайте применим её, при помощи `migrate`

Результат:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/migrate_init.png)

И сравним `showmigrations` теперь:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/showmigrations_after.png)

## Админка

Самый быстрый и удобный способ смотреть на объекты моделей это админка, для того, что бы ей пользоваться нужно сделать две вещи, в урлы добавить встроенный урл админки, и создать суперпользователя.

Что бы создать пользователя нам поможет команда

`python manage.py createsuperuser`

Вводим всё что от нас требует консоль, и юзер будет создан:

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


Вбиваем свои криды, и видим:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/admin_first_login.png)

По дефолту, у джанго сразу есть две модели из "коробки", User и Group,

Но нет нашей модели, почему же? Потому что нужные модели нужно регистрировать, что бы не заполнять админку не нужными данными.

Для этого нам нужно в файле `admin.py` в вашем приложении импортировать вашу модель и зарегестрировать её

```python

from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article)

```

Открываем админку еще раз:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/add_model_to_admin.png)

Появилась наша модель, через админку мы можем добавлять, удалять, смотреть, редактировать наши модели. Возможности встроенной админки очень велики, но её можно дописывать, видоизменять, добавлять любые кастомные действия итд. Подробно разберем на одном из следующих занятий, сейчас попробуйте создать/изменить/удалить несколько объектов

## Основные типы филдов, и их стандарные атрибуты.

[Ссылка на все существующие типы филдов](https://docs.djangoproject.com/en/3.0/ref/models/fields/)

Когда вы создаёте любую модель, у неё автоматически появряется атрибут `id` он явзляется праймари кеем по умолчанию, если это не было переписано явно
 
Id это очень удобное поле, т.к. оно является автоматическим, и когда вы создаёте новый объект ему сразу назнчается новый идентификационный номер, на один больше предыдущего.

Так же все типы филов имеют встроенный атрибут default, который заполняется если нужно указать значение по умолчанию

### Boolean field

Хранит True или False

```python
my_flag = models.BooleanField()
```

### Char field

Строковое поле, принимает обязательный аргумент max_length - максимальное кол-во символов

Часто используемые флаги null и blank, null=True, означает, что поле может быть None, black=True, означает, что поле может быть пустрой строкой ''

```python
my_char = models.CharField(max_length=120, null=True, blank=False)
```

### Date и DateTime field

Поля для хранения даты, и даты и времени

Принимают аргументы auto_now и auto_now_add, auto_now_add обозначает, что при создании объекта это поле будет автоматически заполненно, текущей датой и временем. auto_now будет обновляться каждый раз когда объект сохраняется. (часто используют для сохрания даты создания и даты обновления объекта)


```python
created_at = models.DateField(auto_now=True)
updated_at = models.DateTimeField(auto_now_add=True)
```
### Decimal Field 

Хранение float чисел

Обязательніе параметры max_digits, decimal_places. Первое максимальное кол-во символов, второе кол-во знаков после запятой.

```python
    float_number = models.DecimalField(decimal_places=2, max_digits=12)
```

### EmailField

Такой же текстовый как и CharField о с проверкой на валидность имейла

### FileField

Для хранения файлов, можно указать upload_to - место для хранения файлов, если не указано, будет использованно, то, что в settings.py


```python
    my_file = models.FileField()
```

### Image Field 
Тоже что и файл филд, с валидацией на картинку

### IntegerField
Хранение целых числел от -2147483648 до 2147483647

```python
    int_number = models.IntegerField()
```

### URL Field 
Тесктовый тип, для хранения урлов.

```python
    my_url = models.URLField()
```


И многие другие, читайте доку.

#Связи

![](http://memesmix.net/media/created/jb8uel.jpg)


Модели могут быть связанны между собой, для этого существует 3 типа связей

OneToOne

ForeignKey

ManyToMany

### One to one

Связь один к одному, чаще всего используется для какого-либо однозначного определения разных моделей (Допустим пользователя, и модели где хранятся его настройки)

Для того, что бы сделать связь, нам нужно создать две модели и в одной из них указать зависимость

```python
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=120),
    age = models.IntegerField()
    

class CustomerSettings(models.Model):
    preferred_color = models.CharField()
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='cus')
```

Теперь эти модели связанны, что мы и увидим в админке.

### Foreign Key

Самая распространенная связь. Один ко многим. Допустим у нас есть книга, её написал конкретный автор, но это не значит, что этот автор написал только эту книгу.

```python
class Author(models.Model):
    name = models.CharField(max_length=120)
  
  
class Book(models.Model):
    name = models.CharField(max_length=120)
    year_of_public = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
```

### Many to Many 
Многие ко многим, допустим ваш пользователь состоит в какой-то группе "Любители варенья", но при этом ничего не мешает ему состоять и в группе "Профессионалы пива", такая связь называется ManyToMany

```python
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Person,
        through='Membership',
        through_fields=('group', 'person'),
    )
```

![](https://lendiplompro.ru/images/praktica/praktica.jpg)

# Домашнее задание:

Разработать набор моделей, для сайта-блога, на котором можно выставлять свои статьи, коментировать чужие, ставить лайк и дизлайк статье, и коментарию.

* Доделать так, что бы связи позволяли коментировать коментарии.