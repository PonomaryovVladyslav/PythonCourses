# Лекция 21. Модели. Связи. Meta. Abstract, proxy.

![](https://www.meme-arsenal.com/memes/ec0eba9bc1a90ba417d786f9096cce72.jpg)

### Нет, не такие :)

На этом этапе вы должны были уже выполнить все инструкции из
вот [этой](https://github.com/PonomaryovVladyslav/PythonCourses/blob/master/before_postgres.md) ссылки

Но на всякий случай, вкратце еще раз.

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

## Что сегодня учим?

![mvc_models.png](pictures/mvc_models.png)

## Конфигурация Django

Открываем проект и в нём файл `settings.py`

Находим строку `DATABASES`

Если вы ничего не меняли, то выглядеть она должна так:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/sqllitedb.png)

Заменяем на

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
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
python -m pip install "psycopg[binary]"  # актуальный драйвер (psycopg 3)
# альтернативно: python -m pip install psycopg2-binary
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
дока [Тут](https://docs.djangoproject.com/en/stable/topics/db/models/)

Что такое класс модель? Это таблица для базы данных, где атрибуты - это её поля.

Давайте создадим модель!

В файле `myapp/models.py`

Напишем вот это:

```python
from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
``` 

Мы создали нашу первую модель, состоящую из **3** полей: `name`, `text` и `id`, причём поле `id` было создано
автоматически без нашего участия, и она автоматически стало primary key. Поле `name` не может содержать более 100
символов.
Поле `text` может быть "пустым" или отсутствовать полностью.

> Как проконтролировать id, рассмотрим дальше

Чтобы наши изменения попали в базу, нужно создать и применить миграцию.

#### Команда makemigrations

#### Что вообще такое миграция?

Это файл, который отвечает за изменение **структуры** базы данных.

> Новые таблицы, новые поля в таблице, изменения в таблицах или полях. По сути все что касается `DDL`

#### Как это работает?

Когда мы хотим внести изменения в структуру таблицы, мы вносим изменения в python код, описывающий изменения. И Django,
по команде, читает текущую структуру базы данных, читает наш код, находит различия. И на их основе, создает файл,
который описывает какие именно изменения в структуре данных необходимо внести.

> Технически, через пару "прокладок" генерирует `SQL` код, который пока не выполняется, только заготавливается

#### Пример

Теперь мы применим команду

`python manage.py makemigrations`

И увидим нечто похожее на:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/makemigrations.png)

Django радостно нам сообщает, что миграция была создана. Давайте проверим, откроем папку `myapp/migrations` и увидим там
новый файл `0001_initial.py`

Выглядеть он будет вот так:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/init_migration.png)

Где мы можем убедиться, что Django действительно создала за нас поле `id`

> Этот файл и является описанием изменения структуры в БД

#### Команда showmigrations

> Создать миграцию не значит ее применить! Мы только заготовили код, который после будет применен!

Чтобы убедиться, что миграция не применена/применена, используется команда

`python manage.py showmigrations`

Результат:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/showmigrations.png)

Как мы можем видеть, наша миграция существует, но не применена, давайте применим её командой

`python manage.py migrate`

Результат:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/migrate_init.png)

И сравним `showmigrations` теперь:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/showmigrations_after.png)

## Админка

> Django предоставляет нам возможность взаимодействия с базой данных через удобный интерфейс, вместо того что бы
> пользоваться `SQL`

Самый быстрый и удобный способ смотреть на объекты моделей (Записи в БД) - это админка. Чтобы ей пользоваться, нужно
сделать две вещи:

- В `urls.py` добавить встроенный урл админки.
- Создать суперпользователя (Администатора).

#### Команда создания суперпользователя:

`python manage.py createsuperuser`

Вводим всё, что от нас требует консоль, и юзер будет создан:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson35/createsuperuser.png)

> Имейл не является обязательным, можно просто нажать энтер на пустое поле

Если вы не стирали урл для админки, то он уже у вас есть, если стирали, то допишите в `myproject/urls.py`

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # другие маршруты
]
```

Перезапускаем сервер, и заходим в [админку](http://127.0.0.1:8000/admin)

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
и т. д. Подробно разбирать эту тему мы не будем. Сейчас попробуйте создать/изменить/удалить несколько объектов.

Админку можно кастомизировать. Чтобы изменить или добавить любое действие, используются специальные классы.

Ссылка на оф доку [тут](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)

Весь функционал описан в приложении `django.contrib.admin`, о котором мы говорили выше, оно добавлено в
наш проект по умолчанию.

### Пример кастомизации

```python
from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'text_short')

    def text_short(self, obj):
        return (obj.text or '')[:50]
    text_short.short_description = 'Preview'

admin.site.register(Article, ArticleAdmin)
```

## Основные типы полей и их стандартные атрибуты.

[Ссылка на все существующие типы полей](https://docs.djangoproject.com/en/stable/ref/models/fields/)

Когда вы создаёте модель, у неё автоматически появляется атрибут `id`. Он является `Primary Key` по умолчанию, если
это не было переписано явно.

`id` - это очень удобное поле, т. к. оно является автоматическим, и когда вы создаёте новый объект, ему сразу
назначается новый идентификационный номер, на один больше предыдущего.

> Мы рассматривали как это работает когда изучали базы данных. Но давайте еще раз.

> По умолчанию в Django первичный ключ — автоинкрементный BigAutoField.
> В PostgreSQL это реализуется через identity/sequence.

Так же все типы полей имеют встроенный атрибут `default`, который заполняется, если нужно указать значение по умолчанию.

Параметр `null` управляет тем, как поле ведет себя на уровне базы данных. Если для поля задан параметр `null=True`, это
означает, что в базе данных данное поле может принимать значение NULL. Важно понимать, что null применяется только к
столбцам базы данных и контролирует наличие NULL в этом столбце.

Параметр `blank`, позволяет хранить в качестве значения пустую строку (`""`)

Так же любое поле может быть индексировано, используя параметр `db_index=True`.

### BooleanField

Хранит True или False

```python
my_flag = models.BooleanField()
```

### CharField

Строковое поле, принимает обязательный аргумент max_length - максимальное количество символов

Часто используемые флаги `null` и `blank`: `null=True` — поле может быть `None`, `blank=True` — поле может быть пустой строкой `''`.

```python
my_char = models.CharField(max_length=120, null=True, blank=False)
```

### DateField и DateTimeField

Поля для хранения даты и даты и времени

Принимают аргументы `auto_now` и `auto_now_add`.
`auto_now_add` обозначает, что при создании объекта это поле будет автоматически заполнено текущей датой и временем.
`auto_now` будет обновляться каждый раз, когда объект сохраняется (и при создании и при обновлении).
(часто используют для сохранения даты создания и даты обновления объекта)

```python
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
```

### DecimalField

Десятичные числа с фиксированной точностью (Decimal). В отличие от FloatField не накапливает ошибок округления — подходит для денежных значений.

Обязательные параметры: `max_digits` — общее количество цифр, `decimal_places` — количество знаков после запятой.

```python
price = models.DecimalField(max_digits=12, decimal_places=2)
```

### EmailField

Такой же текстовый, как и CharField, с проверкой на валидность имейла

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

### Медиа

#### Что такое медиа-файлы?

Медиа-файлы в контексте Django — это файлы, загружаемые пользователями через веб-приложение. Примеры таких файлов
включают:

- Фотографии профиля пользователя
- Загруженные документы (PDF, DOCX)
- Видео и аудио файлы
- Другие типы файлов, которые пользователи могут загрузить на сайт.

Эти файлы обычно хранятся отдельно от кода и статических файлов, таких как CSS и JavaScript.

#### Настройка Django для работы с медиа-файлами

Для работы с медиа-файлами в Django необходимо выполнить несколько шагов.

Как мы рассматривали как работать со статическими файлами, так же нужно выполнить доп действия для работы с медиа
файлами.

#### Настройка `settings.py`

Первое, что нужно сделать, — это определить, где будут храниться ваши медиа-файлы, и как к ним будет осуществляться
доступ. В файле `settings.py` нужно добавить следующие параметры:

```python
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

# Путь к директории, где будут храниться загружаемые файлы
MEDIA_ROOT = BASE_DIR / 'media'

# URL, по которому файлы будут доступны
MEDIA_URL = '/media/'
```

Здесь `MEDIA_ROOT` указывает на директорию, где будут физически храниться файлы на сервере. `MEDIA_URL` — это URL, по
которому будут доступны медиа-файлы.

#### Настройка URL-ов

Чтобы медиа-файлы были доступны в режиме разработки, необходимо добавить обработку URL-ов для медиа-файлов в
файл `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Ваши URL-ы приложения
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Эта настройка позволяет Django обрабатывать медиа-файлы напрямую во время разработки.

> В продакшене (на боевом сервере) обычно используется отдельный сервер (например, Nginx или Apache) для обработки
> медиа-файлов. Рассмотрим это в самом конце курса.

### FileField

Для хранения файлов, можно указать `upload_to` - место для хранения файлов, если не указано, будет использовано, то, что
в `settings.py`

> Здесь `upload_to` определяет путь внутри директории `MEDIA_ROOT`, куда будут загружаться файлы. Например, если
> пользователь загружает аватар, он будет сохранен в `media/avatars/`.

```python
my_file = models.FileField()
```

### ImageField

Тоже что и FileField с валидацией изображения.

> И многие другие, читайте доку.

## Как сделать свой собственный параметр, который будет `primary key` вместо 'id'

В Django, по умолчанию, для каждой модели создается поле `id`, которое является автоинкрементируемым целым числом и
служит в качестве первичного ключа (Primary Key). Однако, Django предоставляет гибкие возможности для управления этим
параметром, если вам нужно заменить его или использовать другой тип данных для первичного ключа.

### Использование собственного поля в качестве Primary Key

Вы можете определить собственное поле в модели и использовать его в качестве Primary Key, просто установив
параметр `primary_key=True`. Например:

```python
from django.db import models


class MyModel(models.Model):
    custom_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100, db_index=True)
```

В этом примере поле `custom_id` будет использоваться в качестве первичного ключа вместо стандартного `id`.

Либо использовать AutoField

```python
from django.db import models


class MyModel(models.Model):
    custom_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
```

Тогда ваш `custom_id` - будет полной имитацией оригинального `id`

# Связи

![](http://memesmix.net/media/created/jb8uel.jpg)

> Мы рассматривали эту тему когда изучали базы данных. Давайте посмотрим как это работает в Django.

Модели могут быть связаны между собой, для этого существует 3 типа связей

- `OneToOne` - связь один-к-одному

- `ForeignKey` - связь один-ко-многим

- `ManyToMany` - связь многие-ко-многим

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
    preferred_color = models.CharField(max_length=32)
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

Многие ко многим, допустим, вы описываете базу для кинопоиска, один фильм может быть снят несколькими режиссерами, но
при этом каждый из режиссеров может снять больше одного фильма, такая связь называется ManyToMany. Для построения таких
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
зависимость полей динамической (Допустим, сделать лайк зависимым от динамического типа данных, например, хочешь ставить
к статье, а хочешь к комментарию, хотя это одна и та же модель)

Дока [Тут](https://docs.djangoproject.com/en/stable/ref/contrib/contenttypes/)

Подробно мы не будем рассматривать этот функционал, но я бы очень рекомендовал ознакомиться.

Работает, основываясь на приложении `django.contrib.contenttypes`, добавленном в наш проект по умолчанию.

## `class Meta` в моделях Django

Когда мы работаем с моделями в Django, нам часто нужно определять дополнительные настройки, которые не относятся
напрямую к полям модели, но оказывают влияние на её поведение в рамках ORM (Object-Relational Mapping). Для этого в
Django используется внутренняя классическая конструкция — `class Meta`. Этот класс позволяет нам задавать различные
метаданные для модели, такие как порядок сортировки, уникальные ограничения, имена таблиц, и многое другое.

> Например когда нам надо создать ограничение на несколько полей, только этот синтаксис сможет нам помочь

### Основные параметры `class Meta`

`class Meta` предоставляет множество параметров, но мы сосредоточимся на двух самых часто используемых: `ordering`
и `constraints`, `indexes`.

#### Параметр `ordering`

Параметр `ordering` позволяет задать порядок сортировки объектов модели по умолчанию, когда вы извлекаете данные из базы
данных.

**Пример:**

```python
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    class Meta:
        ordering = ['published_date']

# Теперь при выборке объектов модели Book они будут сортироваться по дате публикации
```

В этом примере объекты модели `Book` будут по умолчанию отсортированы по полю `published_date`. Вы также можете
использовать префикс `-`, чтобы указать обратный порядок:

```python
class Meta:
    ordering = ['-published_date']  # Сортировка по дате публикации от новых к старым
```

##### Параметр `constraints`

Параметр `constraints` позволяет задать составные уникальные ограничения на набор полей. Это означает, что
комбинация значений этих полей должна быть уникальной для каждой записи в таблице.

**Пример:**

```python
from django.db.models import UniqueConstraint


class StoreItem(models.Model):
    store = models.CharField(max_length=100)
    item = models.CharField(max_length=100)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['store', 'item'], name='unique_store_item')
        ]
```

### Параметр `indexes`

Помимо параметров `ordering` и `constraints`, которые мы уже рассмотрели, в Django также существует параметр `indexes`,
который позволяет создавать составные индексы для повышения производительности запросов, включающих несколько полей.

`indexes` используется для создания составных индексов на уровне базы данных. Составные индексы полезны, когда вы часто
делаете запросы, фильтруя данные сразу по нескольким полям. Наличие индекса на этих полях ускоряет выполнение таких
запросов.

**Пример:**

**Пример с использованием `indexes`:**

```python
from django.db.models import Index


class StoreItem(models.Model):
    store = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    class Meta:
        indexes = [
            Index(fields=['store', 'item']),
            Index(fields=['item', 'category']),
        ]
```

Этот способ позволяет не только задавать составные индексы, но и использовать дополнительные параметры, такие как `name`
для указания имени индекса, и `condition` для создания частичных индексов.

В этом примере создаются два составных индекса:

1. Индекс по полям `store` и `item`.
2. Индекс по полям `item` и `category`.

Это может значительно улучшить производительность при выполнении запросов, которые фильтруют данные по этим комбинациям
полей.

> Точно таким же способом можно вносить и другие ограничения которые касаются двух и более полей сразу!

### Абстрактные модели

Абстрактные модели используются в Django для того, чтобы создать базовый класс с полями и методами, который не будет
напрямую соответствовать таблице в базе данных, но может быть унаследован другими моделями. Это помогает избежать
дублирования кода и сделать проект более модульным и управляемым.

**Пример:**

```python
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    title = models.CharField(max_length=100)


class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
```

Здесь `TimeStampedModel` является абстрактной моделью, поэтому Django не создаст для нее отдельную таблицу в базе
данных. Модели `Post` и `Comment` унаследуют поля `created_at` и `updated_at` от абстрактной модели.

### Прокси-модели

Прокси-модели позволяют изменять поведение существующей модели без изменения ее базы данных. Прокси-модель использует ту
же таблицу базы данных, что и исходная модель, но может переопределять методы или добавлять новые.

**Пример:**

```python
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class PersonProxy(Person):
    class Meta:
        proxy = True
        ordering = ['name']

    def full_name(self):
        return f'Name: {self.name}, Age: {self.age}'
```

Здесь `PersonProxy` является прокси-моделью для модели `Person`. Она использует ту же таблицу в базе данных, но имеет
дополнительный метод `full_name` и переопределяет порядок сортировки по умолчанию.

> Абстрактные и прокси модели не существуют на уровне базы данных! Это уже надстройка на уровне Django