# Лекция 24. Django ORM. Объекты моделей и queryset, Meta моделей, прокси модели.

![](https://cs8.pikabu.ru/post_img/2016/09/12/5/og_og_1473660997242355939.jpg)

## Что сегодня учим?

![img.png](pictures/mvc_orm.png)

## ORM

Мы уже знаем про то, как хранить данные и как связать таблицы между собой. Давайте научимся извлекать, модифицировать и
удалять данные при помощи кода.

Допустим, что ваша модель выглядит так:

```python
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext as _

GENRE_CHOICES = (
    (1, _("Not selected")),
    (2, _("Comedy")),
    (3, _("Action")),
    (4, _("Beauty")),
    (5, _("Other"))
)


class Author(models.Model):
    pseudonym = models.CharField(max_length=120,
                                 blank=True,
                                 null=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               null=True,
                               related_name='articles')
    text = models.TextField(max_length=10000,
                            null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    genre = models.IntegerField(choices=GENRE_CHOICES,
                                default=1)

    def __str__(self):
        return f"Author - {self.author.name}, genre - {self.genre}, id - {self.id}"


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    article = models.ForeignKey(Article,
                                on_delete=models.DO_NOTHING)
    comment = models.ForeignKey('myapp.Comment',
                                null=True,
                                blank=True,
                                on_delete=models.DO_NOTHING,
                                related_name='comments')
    user = models.ForeignKey(User,
                             on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.text} by {self.user.username}"


class Like(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article,
                                on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"By user {self.user.username} to article {self.article.id}"

```

Рассмотрим некоторые новые возможности

```python
from django.contrib.auth.models import User
```

Это модель встроенного в Django юзера, её мы рассмотрим немного позже.

```python
from django.utils.translation import gettext as _
```

Стандартная функция перевода языка для Django. Допустим, что ваш сайт имеет функцию переключения языка, при которой
текст
может отображаться на русском, украинском и английском. Именно эта функция поможет нам в будущем указать значения
для всех трех языков. Подробнейшая информация по
переводам [Тут](https://docs.djangoproject.com/en/4.2/topics/i18n/translation/)

> Мы будем рассматривать это на отдельной лекции

```python
GENRE_CHOICES = (
    (1, _("Not selected")),
    (2, _("Comedy")),
    (3, _("Action")),
    (4, _("Beauty")),
    (5, _("Other"))
)
```

Переменная, состоящая из кортежа кортежей (могла быть любая коллекция коллекций), которая нужна для использования
choices значений, используется для хранения выбора чего-либо (в нашем случае жанра). То есть в базе будет храниться
только число, а пользователю будет выводиться уже текст.

Используем это вот тут:

```python
genre = models.IntegerField(choices=GENRE_CHOICES, default=1)
```

Рассмотрим вот эту строку

```python
return f"Author - {self.author.name}, genre - {self.genre}, id - {self.id}"
```

**self.author.name** - в базе по значению поля ForeignKey хранится **id**, но в коде мы можем получить доступ к
значениям
связанной модели, конкретно в этой ситуации мы берем значение поля **name** из связанной модели **author**.

Рассмотрим вот эту строку:

```python
comment = models.ForeignKey('myapp.Comment',
                            null=True,
                            blank=True,
                            on_delete=models.DO_NOTHING,
                            related_name='comments')
```

Модель можно передать не только как класс, но и по имени модели указав приложение `appname.Modelname` (да, мне было лень
переименовывать приложение из myapp во что-то читаемое).

> Это пример самоссылочной связи, помните еще из занятий по `SQL`?

При такой записи мы создаём связь один ко многим к самому себе, указав при этом black=True, null=True. Можно создать
коммент без указания родительского комментария, а если создать комментарий со ссылкой на другой, это будет комментарий к
комментарию, причем это можно сделать любой вложенности.

Кроме описания модели можно было бы использовать текст `self`. Это работает, когда нужно сделать ссылку именно на самого
себя

`related_name` - в этой записи нужен для того, чтобы получить выборку всех вложенных объектов. Мы рассмотрим их немного
дальше.

## objects и shell

Для доступа или модификации любых данных, у каждой модели есть атрибут `objects`, который позволяет производить
манипуляции с данными. Он называется менеджер, и при желании его можно переопределить.

Для интерактивного использования кода используется команда

```python manage.py shell```

Эта команда открывает нам консоль с уже импортированными стандартными, но не самописными модулями Django

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson36/clean_shell.png)

Предварительно я создал несколько объектов через админку.

Для доступа к моделям их нужно импортировать, я импортирую модель Comment.

Рассмотрим весь CRUD и дополнительные особенности. Очень подробная информация по всем возможным
операциям [тут](https://docs.djangoproject.com/en/4.2/topics/db/queries/)

### R - retrieve

Функции для получения объектов в Django могут возвращать два типа данных, **объект модели** или **queryset**

Объект - это единичный объект, queryset - это список объектов со своими встроенными методами.

#### all()

Для получения всех данных используется метод `all()`, который возвращает queryset со всеми существующими объектами этой
модели.

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson36/objects_all.png)

#### filter()

Для получения отфильтрованных данных мы используем метод `filter()`

Если указать `filter()` без параметров, то он сделает то же самое, что и `all()`.

Какие у фильтра могу быть параметры? Да практически любые, мы можем указать любые поля для фильтрации.
Например, фильтр по полю текст:

```python
Comment.objects.filter(text='Hey everyone')
```

Фильтр по вложенным объектам выполняется через двойное подчеркивание.

Фильтр по жанру статьи комментария:

```python
Comment.objects.filter(article__genre=3)
```

По псевдониму автора:

```python
Comment.objects.filter(article__author__pseudonym='The king')
```

По псевдониму автора и жанру (через запятую можно указать логическое И):

```python
Comment.objects.filter(article__author__pseudonym='The king', article__genre=3)
```

Кроме того, у каждого поля существуют встроенные системы лукапов. Синтаксис лукапов аналогичен синтаксису доступа к
вложенным
объектам `field__lookuptype=value`

Стандартные лукапы:

`lte` - меньше или равно

`gte` - больше или равно

`lt` - меньше

`gt` - больше

`startswith` - начинается с

`istartswith` - начинается с, без учёта регистра

`endswith` - заканчивается на

`iendswith` - заканчивается на, без учёта регистра

`range` - находится в диапазоне

`week_day` - день недели (для дат)

`year` - год (для дат)

`isnull` - является `null`

`contains` - частично содержит с учетом регистра ("Всем привет, я - Влад" содержит слово "Влад", но не содержит "влад")

`icontains` - то же самое, но без учета регистра, теперь найдется и второй вариант.

`exact` - совпадает (необязательный лукап, делает то же, что и знак равно)

`iexact` - совпадает без учета регистра (по запросу "привет" найдет и "Привет", и "прИвЕт")

`in` - содержится в каком-то списке

Их намного больше, читать [ТУТ](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups)

Примеры:

Псевдоним содержит слово 'king' без учета регистра:

```python
Comment.objects.filter(article__author__pseudonym__icontains='king')
```

Комменты к статье, созданной не позднее чем вчера:

```python
Comment.objects.filter(article__created_at__gte=date.today() - timedelta(days=1))
```

Комменты к статьям с жанрами, у которых `id = 2` и `id = 3`:

```python
Comment.objects.filter(article__genre__in=[2, 3])
```

#### exclude()

Функция обратная функции `filter` вытащит всё, что не попадает выборку.

Например, все комментарии к статьям, у которых жанр `id != 2` и `id != 3`:

```python
Comment.objects.exclude(article__genre__in=[2, 3])
```

`filter` и `exclude` можно совмещать. К любому queryset можно применить `filter` или `exclude` еще раз. Например, все
комменты
к статьям, созданным не позже чем вчера, с жанрами не 2 и не 3

```python
Comment.objects.filter(article__created_at__gte=date.today() - timedelta(days=1)).exclude(article__genre__in=[2, 3])
```

Все эти функции возвращают специальный объект называемый queryset. Он является коллекцией записей базы (которые
называются в этой терминологии instance), к любому кверисету можно применить любой метод менеджера модели (objects).
Например, к только что отфильтрованному кверисету можно применить фильтр еще раз и т. д.

#### order_by()

По умолчанию все модели сортируются по полю `id`, если явно не указанно иное. Однако часто нужно отсортировать данные
специальным
образом. Для этого используется метод order_by(). При сортировке можно указывать вложенные объекты и знак `-`, чтобы
указать сортировку в обратном порядке.

```python
Comment.objects.filter(article__created_at__gte=date.today() - timedelta(days=1)).order_by('-article__created_at').all()
```

#### `distinct()`

Метод `distinct()` используется для исключения дублирующихся записей из результата запроса. Он полезен, когда вам нужно
получить уникальные записи по одному или нескольким полям.

#### Пример использования:

Предположим, у нас есть модель `Book` с полями `title`, `author`, и `published_date`.

```python
from myapp.models import Book

# Получение уникальных авторов
unique_authors = Book.objects.distinct('author')
```

В этом примере запрос вернет уникальные записи на основе поля `author`. Если не указать поле, то метод `distinct()`
уберет дубликаты всех записей.

#### `values()`

Метод `values()` используется для создания набора запросов, который возвращает словари, где ключами являются имена
полей, а значениями — их значения. Это удобно, когда вам нужно получить определенные поля из базы данных, а не все поля
модели.

#### Пример использования:

```python
# Получение всех названий книг
book_titles = Book.objects.values('title')
```

Этот запрос вернет список словарей, где каждый словарь будет содержать ключ `title` и соответствующее ему значение.

#### `union()`

Метод `union()` позволяет объединять два или более QuerySets. Результат будет содержать уникальные записи, которые
присутствуют в любом из QuerySets.

#### Пример использования:

```python
from myapp.models import Book

# QuerySet с книгами, опубликованными до 2000 года
old_books = Book.objects.filter(published_date__lt="2000-01-01")

# QuerySet с книгами, опубликованными после 2020 года
new_books = Book.objects.filter(published_date__gt="2020-01-01")

# Объединение двух QuerySets
books_union = old_books.union(new_books)
```

В результате `books_union` будут содержаться книги, опубликованные либо до 2000 года, либо после 2020 года.

#### `intersection()`

Метод `intersection()` используется для получения пересечения двух или более QuerySets. В результате запроса будут
только те записи, которые присутствуют во всех QuerySets.

#### Пример использования:

```python
from myapp.models import Book

# QuerySet с книгами определенного автора
author_books = Book.objects.filter(author="J.K. Rowling")

# QuerySet с книгами, опубликованными до 2000 года
old_books = Book.objects.filter(published_date__lt="2000-01-01")

# Пересечение двух QuerySets
books_intersection = author_books.intersection(old_books)
```

В этом примере `books_intersection` вернет только те книги Дж. К. Роулинг, которые были опубликованы до 2000 года.

#### `difference()`

Метод `difference()` используется для получения разности между двумя QuerySets, то есть он возвращает записи, которые
присутствуют в одном QuerySet, но отсутствуют в другом.

#### Пример использования:

```python
from myapp.models import Book

# QuerySet со всеми книгами
all_books = Book.objects.all()

# QuerySet с книгами, опубликованными до 2000 года
old_books = Book.objects.filter(published_date__lt="2000-01-01")

# Разность между всеми книгами и старыми книгами
books_difference = all_books.difference(old_books)
```

В этом примере `books_difference` будет содержать все книги, которые были опубликованы после 2000 года.

Это далеко не всё, что можно сделать с queryset.

Все методы кверисетов
читаем [Тут](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#methods-that-return-new-querysets)

### Вставка объектов в методы

Помимо прочего во все фильтры(и не только) можно вставлять целые объекты, например:

```python
art = Article.objects.get(id=2)
comments = Comment.object.filter(article=art)
```

### Объектные методы

#### get()

В отличие от `filter` и `exclude` метод `get` получает сразу объект. Этот метод работает только в том случае, когда
можно
определить объект однозначно и он существует.

Можно применять те же условия, что и для `filter` и `exclude`

Например, получения объекта по `id`

```python
Comment.objects.get(id=3)
```

Если объект не найден или найдено больше одного объекта по заданным параметрам, вы получите исключение, которое
желательно всегда обрабатывать. Исключения уже находятся в самой модели.

```python
try:
    Comment.objects.get(article__genre__in=[2, 3])
except Comment.DoesNotExist:
    return "Can't find object"
except Comment.MultipleObjectsReturned:
    return "More than one object"
```

#### first() и last()

К кверисету можно применять методы `first` и `last`, чтобы получить первый или последний элемент кверисета

Например, получить первый коммент, написанный за вчера:

```python
Comment.objects.filter(article__created_at__gte=date.today() - timedelta(days=1)).first()
```

Информация по всем остальным
методам [Тут](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#methods-that-do-not-return-querysets)

### related_name

Атрибут `related_name`, который указывается для полей связи, является обратной связью и менеджером для объектов,
например, в нашей модели у поля `author` модели `Article` есть `related_name=articles`:

```python
a = Author.objects.first()
articles = a.articles.all()  # Тут будут все статьи конкретного автора в виде кверисета, т.к. all() возвращает кверисет
```

Можно ли получить объекты обратной связи без указания `related_name`? Можно. Связь появляется автоматически даже без
указания этого атрибута.

Обратный менеджер формируется из названия модели и конструкции `_set`. Допустим, у поля `article` модели `Comment` не
указано поле `related_name`:

```python
a = Article.objects.first()
a.comment_set.all()  # такой же менеджер, как в прошлом примере, вернёт кверисет комментариев, относящихся к этой статье.
```

### C - Create

Для создания новых объектов используется два возможных варианта: метод `create()` или метод `save()`

Создадим двух новых авторов при помощи разных методов:

```python
Author.objects.create(name='New author by create', pseudonym="Awesome author")

a = Author(name="Another new author", pseudonym="Gomer")
a.save()
```

В чём же разница? В том, что в первом случае при выполнении этой строки запрос в базу будет отправлен сразу, во втором -
только при вызове метода `save()`

Метод `save()` также является и методом для обновления значения поля, если применяется для уже существующего объекта. Мы
рассмотрим его подробнее немного дальше.

### U - Update

Для обновления значений полей используется метод `update()`

**Применяется только к кверисетам, к объекту применить нельзя**

Например, обновим текст в комментарии с `id = 3`:

```python
Comment.objects.filter(id=3).update(text='updated text')

ИЛИ

c = Comment.objects.get(id=3)
c.text = 'updated text'
c.save()
```

### D - Delete

Как можно догадаться, выполняется методом `delete()`.

Удалить все комменты от пользователя с `id = 2`:

```python
Comment.objects.filter(user__id=2).delete()
```

### Совмещенные методы

#### get_or_create(), update_or_create(), bulk_create(), bulk_update()

`get_or_create()` - это метод, который попытается создать новый объект. Если он не сможет найти нужный в базе, он
возвращает сам объект и булево значение, которое обозначает, что объект был создан или получен.

`update_or_create()` - обновит, если объект существует, создаст, если не существует.

`bulk_create()` - массовое создание; необходимо для того, чтобы избежать большого количества обращений в базу.

`bulk_update()` - массовое обновление (отличие от обычного в том, что при обычном на каждый объект создается запрос,
в этом случае запрос делается массово)

Подробно почитать про них [Тут](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#get-or-create)

## Подробнее о методе save()

> `SQL` запрос выполняется именно при вызове метода `save`, метода `delete` или изменении M2M о чем ниже.

Метод `save()` применяется при любых изменениях или создании данных, но очень часто нужно, чтобы при сохранении данных
выполнялись еще какие-либо действия, переписывание данных или запись логов и т. д. Для этого используется переписывание
метода `save()`. По сути является способом написать аналог триггера в базе данных.

Метод `save()` вызывают явно или неявно во время вызова методов создания или обновления, но без него запись в базу не
будет произведена.

Допустим, мы хотим делать время создания статьи на один день раньше, чем фактическая. Перепишем метод `save()` для
статьи:

```python
class MyAwesomModel(models.Model):
    name = models.CharField(max_lenght=100)
    created_at = models.DateField()

    def save(self, **kwargs):
        self.created_at = timezone.now() - timedelta(days=1)
        super().save(**kwargs)
```

Переопределяем значение и вызываем оригинальный `save()`, вуаля.

Чтобы переопределить логику при создании, но не трогать при изменении, или наоборот, используется особенность
данных. У уже созданного объекта `id` существует, у нового - нет. Так что фактически наш код сейчас обновляет это поле
всегда, и когда надо, и когда не надо. Допишем его.

```python
class MyAwesomModel(models.Model):
    name = models.CharField(max_lenght=100)
    created_at = models.DateField()

    def save(self, **kwargs):
        if not self.id:
            self.created_at = timezone.now() - timedelta(days=1)
        super().save(**kwargs)
```

Теперь поле будет переписываться только в момент создания, но не будет трогаться при обновлении.

Метод `delete()`, при удалении объекта `save()` не вызывается, а вызывается `delete()`. По аналогии мы можем его
переписать, например, для отправки имейла перед удалением.

```python
class MyAwesomModel(models.Model):
    name = models.CharField(max_lenght=100)
    created_at = models.DateField()

    def delete(self, **kwargs):
        send_email(id=self.id)
        super().delete(**kwargs)
```

## Использование в M2M

Допустим у нас есть вот такие модели:

```python
from django.db import models


class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ["headline"]

    def __str__(self):
        return self.headline
```

Для работы с М2М связями используются методы менеджера `add` и `remove`

Создадим несколько объектов:

```python
p1 = Publication(title="The Python Journal")
p1.save()
p2 = Publication(title="Science News")
p2.save()
p3 = Publication(title="Science Weekly")
p3.save()
```

> Мы могли сделать то же самое через `Publication.objects.create()`, но тут нам будет важно отследить `SQL` запросы

```python
a1 = Article(headline="Django lets you build web apps easily")
```

### Добавление объекта

Если не сохранить статью и попытаться вызвать изменения в M2M, то вы увидите вот такую ошибку:

```python
a1.publications.add(p1)
# Traceback (most recent call last):
# ValueError: "<Article: Django lets you build web apps easily>" needs to have a value for field "id" before this many-to-many relationship can be used.
```

Потому что объект `a1` пока что сущетствует только на уровне питона, но его нет на уровне базы данных.

Давайте сохраним объект и попробуем еще раз изменить M2M

```python
a1.save()
a1.publications.add(p1)  # Тут вызовется еще один `SQL` запрос
```

И еще пример:

```python
a2 = Article(headline="NASA uses Python")
a2.save()
a2.publications.add(p1, p2)
a2.publications.add(p3)
```

Как видите можно добавлять более чем один объект за раз

А что если добавить объект не того типа который ожидается?

```python
a2.publications.add(a1)
# TypeError: 'Publication' instance expected
```

Будет ошибка о неправильном типе!

> Можно создать и сразу добавить объект вот так

```python
new_publication = a2.publications.create(title="Highlights for Children")
```

Метод создаст объект, добавит его к М2М и вернет в новую переменную

### Получение объекта

В нашем случае `publications` является менеджером, а значит, что к нему применимы все действия как и к обычному
`objects`

```python
a1.publications.all()
# <QuerySet [<Publication: The Python Journal>]>
a2.publications.all()
# <QuerySet [<Publication: Highlights for Children>, <Publication: Science News>, <Publication: Science Weekly>, <Publication: The Python Journal>]>
```

> Естественно `all` в этом случае будет возвращать только те объекты которые связаны с запрашиваемым

И так же как и при связи через `FK`, мы можем использовать `related_name` для получения объектов в другом порядке (из
той модели, где менеджер не прописан)

```python
p2.article_set.all()
# <QuerySet [<Article: NASA uses Python>]>
p1.article_set.all()
# <QuerySet [<Article: Django lets you build web apps easily>, <Article: NASA uses Python>]>
Publication.objects.get(id=4).article_set.all()
# <QuerySet [<Article: NASA uses Python>]>
```

> `related_name` не прописан явно, поэтому мы используем стандартно сгенерированный

### `filter`, `distinct`, `count`

Так как ссылка является менеджером, это значит, что к ней применим весь спектр процессов доступных менеджеру. Например
`filter`, `distinct`  или `count`

```python
Article.objects.filter(publications__id=1)
# <QuerySet [<Article: Django lets you build web apps easily>, <Article: NASA uses Python>]>
Article.objects.filter(publications__pk=1)
# <QuerySet [<Article: Django lets you build web apps easily>, <Article: NASA uses Python>]>
Article.objects.filter(publications=1)
# <QuerySet [<Article: Django lets you build web apps easily>, <Article: NASA uses Python>]>
Article.objects.filter(publications=p1)
# <QuerySet [<Article: Django lets you build web apps easily>, <Article: NASA uses Python>]>
Article.objects.filter(publications__title__startswith="Science")
# <QuerySet [<Article: NASA uses Python>, <Article: NASA uses Python>]>
Article.objects.filter(publications__title__startswith="Science").distinct()
# <QuerySet [<Article: NASA uses Python>]>
Article.objects.filter(publications__title__startswith="Science").count()
# 2
Article.objects.filter(publications__title__startswith="Science").distinct().count()
# 1
Article.objects.filter(publications__in=[1, 2]).distinct()
# <QuerySet [<Article: Django lets you build web apps easily>, <Article: NASA uses Python>]>
Article.objects.filter(publications__in=[p1, p2]).distinct()
# <QuerySet [<Article: Django lets you build web apps easily>, <Article: NASA uses Python>]>
```

> Любые действия с менеджером доступны как напрямую, так и через `related_name`

### Удаление объектов

```python
a4.publications.remove(p2)
p2.article_set.all()
# <QuerySet [<Article: Oxygen-free diet works wonders>]>
a4.publications.all()
# <QuerySet []>
```

И с другой стороны

```python
p2.article_set.remove(a5)
p2.article_set.all()
# <QuerySet []>
a5.publications.all()
# <QuerySet []>
```

### Назначение списком или очистка

Можно назначить список который будет отображать связь:

```python
a4.publications.all()
# <QuerySet [<Publication: Science News>]>
a4.publications.set([p3])
a4.publications.all()
# <QuerySet [<Publication: Science Weekly>]>
```

Или очистить всю связь:

```python
p2.article_set.clear()
p2.article_set.all()
# <QuerySet []>
```

> Назаначение как и очистка так же работает с обоих концов, как и любое другое действие с менеджерами.

## Сложные SQL конструкции

Документация по этому разделу

[Тут](https://docs.djangoproject.com/en/4.2/ref/models/expressions/#django.db.models.F)
[Тут](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#django.db.models.Q)

На самом деле, мы не ограничены стандартными конструкциями. Мы можем применять предвычисления на уровне базы, добавлять
логические конструкции и т. д., давайте рассмотрим подробнее.

### Q объекты

Как вы могли заметить в случае фильтрации, мы можем выбрать объекты через логическое И при помощи запятой.

```python
Comment.objects.filter(article__author__pseudonym='The king', article__genre=3)
```

В этом случае у нас есть конструкция типа "выбрать объекты, у которых псевдоним автора статьи `The king` И жанр статьи
цифра 3"

Но что же нам делать, если нам нужно использовать логическое ИЛИ?

В этом нам поможет использование Q объекта. На самом деле, каждое из этих условий мы могли завернуть в такой объект:

```python
from django.db.models import Q

q1 = Q(article__author__pseudonym='The king')
q2 = Q(article__genre=3)
``` 

Теперь мы можем явно использовать логические `И` и `ИЛИ`.

```python
Comment.objects.filter(q1 & q2)  # И
Comment.objects.filter(q1 | q2)  # ИЛИ
```

### Aggregation

Агрегация в Django - это предвычисления.

Допустим, что у нас есть модели:

```python
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()


class Publisher(models.Model):
    name = models.CharField(max_length=300)


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher,
                                  on_delete=models.CASCADE)
    pubdate = models.DateField()


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
```

Мы можем совершить предвычисления каких-либо средних, минимальных, максимальных значений, вычислить сумму и т. д.

```python
from django.db.models import Avg

Book.objects.all().aggregate(Avg('price'))
# {'price__avg': 34.35}
```

На самом деле, `all()` не несёт пользы в этом примере:

```python
Book.objects.aggregate(Avg('price'))
# {'price__avg': 34.35}
```

Значение можно именовать:

```python
Book.objects.aggregate(average_price=Avg('price'))
# {'average_price': 34.35}
```

Можно вносить больше одной агрегации за раз:

```python
from django.db.models import Avg, Max, Min

Book.objects.aggregate(Avg('price'), Max('price'), Min('price'))
# {'price__avg': 34.35, 'price__max': Decimal('81.20'), 'price__min': Decimal('12.99')}
```

Если нам нужно, чтобы подсчитанное значение было у каждого объекта модели, мы используем метод `annotate()`

```python
# Build an annotated queryset
from django.db.models import Count

q = Book.objects.annotate(Count('authors'))
# Interrogate the first object in the queryset
q[0]
# "<Book: The Definitive Guide to Django>"
q[0].authors__count
# 2
# Interrogate the second object in the queryset
q[1]
# "<Book: Practical Django Projects>"
q[1].authors__count
# 1
```

Их тоже может быть больше одного:

```python
book = Book.objects.first()
book.authors.count()
# 2
book.store_set.count()
# 3
q = Book.objects.annotate(Count('authors'), Count('store'))
q[0].authors__count
# 6
q[0].store__count
# 6
```

Все эти вещи можно комбинировать:

```python
highly_rated = Count('book', filter=Q(book__rating__gte=7))
Author.objects.annotate(num_books=Count('book'), highly_rated_books=highly_rated)
```

c сортировкой (ordering):

```python
Book.objects.annotate(num_authors=Count('authors')).order_by('num_authors')
```

## F() выражения

В Django ORM (Object-Relational Mapping) для работы с базой данных часто возникает необходимость обновления полей
модели, сравнения значений полей между собой или выполнения арифметических операций на уровне базы данных. Для этих
целей в Django используется класс `F`.

### Что такое F объекты?

`F` объекты представляют собой способ обращения к полям модели без необходимости загружать их в память приложения.
Вместо этого операции с `F` объектами выполняются непосредственно на уровне базы данных, что может значительно повысить
производительность при выполнении запросов.

### Примеры использования F объектов

#### Обновление поля на основе его текущего значения

Рассмотрим простой пример: допустим, у нас есть модель `Product`, которая имеет поле `price`. Предположим, что нам нужно
увеличить цену каждого товара на 10%.

```python
from django.db.models import F

Product.objects.update(price=F('price') * 1.10)
```

Этот запрос обновит поле `price` для всех записей, увеличив его значение на 10%. При этом Django выполнит операцию
умножения на уровне базы данных, что исключит необходимость загружать все объекты в память.

#### Сравнение полей внутри одной записи

Предположим, у нас есть модель `Order` с полями `quantity` и `shipped_quantity`. Нам нужно найти все заказы, для которых
количество отгруженного товара меньше заказанного.

```python
from myapp.models import Order
from django.db.models import F

orders = Order.objects.filter(shipped_quantity__lt=F('quantity'))
```

Этот запрос вернет все заказы, где количество отгруженного товара (`shipped_quantity`) меньше заказанного (`quantity`).

#### Условное обновление поля

Рассмотрим пример, когда у нас есть модель `Employee` с полем `bonus`. Мы хотим увеличить бонус на 500 для всех
сотрудников, у которых текущий бонус менее 1000.

```python
from django.db.models import F, Q

Employee.objects.filter(bonus__lt=1000).update(bonus=F('bonus') + 500)
```

Этот запрос обновит поле `bonus`, прибавив к текущему значению 500 для всех сотрудников, у которых бонус меньше 1000.

#### Агрегатные функции с F объектами

Предположим, у нас есть модель `Sale` с полями `quantity` и `unit_price`, и мы хотим узнать общую стоимость каждого
товара, умножив количество на цену за единицу.

```python
from django.db.models import F, Sum

total_sales = Sale.objects.annotate(total_price=F('quantity') * F('unit_price'))
```

Этот запрос добавит к каждому объекту `Sale` дополнительное поле `total_price`, содержащее общую стоимость товара.

#### Использование F объектов в аннотациях

В некоторых случаях удобно использовать `F` объекты в аннотациях для создания вычисляемых полей. Например, предположим,
что у нас есть модель `Invoice` с полями `subtotal` и `discount`. Мы хотим добавить аннотацию с окончательной суммой
счета, учитывая скидку.

```python
from django.db.models import F, ExpressionWrapper, FloatField

invoices = Invoice.objects.annotate(
    total=ExpressionWrapper(F('subtotal') - F('discount'), output_field=FloatField())
)
```

Здесь мы используем `ExpressionWrapper`, чтобы указать Django тип возвращаемого значения, поскольку операции с `F`
объектами могут привести к неоднозначности типов данных.

## Select related и Prefetch related

### Введение

Когда вы работаете с базой данных в Django, важно учитывать, сколько запросов вы выполняете и насколько эффективны эти
запросы. Один из частых антипаттернов – это проблема "N+1 запросов", когда для получения данных выполняется множество
запросов, что замедляет работу приложения. Django предоставляет два мощных инструмента для оптимизации
запросов: `select_related` и `prefetch_related`.

### Проблема "N+1 запросов"

Предположим, у нас есть две модели `Author` и `Book`, связанные отношением "один ко многим":

```python
class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

Теперь, если вы хотите вывести список книг и их авторов:

```python
books = Book.objects.all()
for book in books:
    print(book.title, book.author.name)
```

Это пример проблемы "N+1 запросов". Сначала выполняется один запрос для получения всех книг, а затем для каждой книги
выполняется отдельный запрос для получения автора, что приводит к множеству запросов (N+1).

### Использование `select_related`

Метод `select_related` позволяет выполнять запросы с объединением (JOIN) таблиц, что значительно уменьшает количество
запросов к базе данных. Он используется для отношений "ForeignKey" и "OneToOne".

#### Пример использования `select_related`

```python
books = Book.objects.select_related('author').all()
for book in books:
    print(book.title, book.author.name)
```

В данном случае будет выполнен **один** SQL-запрос, использующий JOIN для получения данных о книгах и их авторах
одновременно.

#### Как это работает?

Когда вы используете `select_related`, Django выполняет SQL-запрос с использованием INNER JOIN или LEFT OUTER JOIN,
чтобы получить связанные объекты в рамках одного запроса. Это очень эффективно для отношений "один ко многим" и "один к
одному".

### Использование `prefetch_related`

Метод `prefetch_related` используется для оптимизации запросов, когда у вас есть отношение "многие ко многим" или "один
ко многим", и вы хотите избежать проблемы "N+1 запросов". В отличие от `select_related`, он выполняет отдельные запросы,
но затем обрабатывает их в Python, чтобы уменьшить общее количество запросов.

#### Пример использования `prefetch_related`

Предположим, у вас есть модели:

```python
class Publisher(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
```

Теперь, если вы хотите получить все книги и авторов для каждого из них:

```python
books = Book.objects.prefetch_related('authors').all()
for book in books:
    print(book.title)
    for author in book.authors.all():
        print(author.name)
```

Здесь `prefetch_related` выполнит два отдельных запроса: один для получения всех книг, а второй для получения всех
авторов, которые связаны с этими книгами. Django затем связывает авторов с книгами в Python, избегая проблемы "N+1
запросов".

#### Как это работает?

`prefetch_related` делает два (или более) отдельных запроса и затем соединяет результаты этих запросов в Python. Это
очень полезно для отношений "многие ко многим" или если вы хотите выполнить сложные фильтрации на связанном наборе
данных.

### Сравнение `select_related` и `prefetch_related`

- **`select_related`** используется для выполнения SQL JOIN и эффективен для отношений "ForeignKey" и "OneToOne". Все
  происходит на уровне базы данных.
- **`prefetch_related`** используется для отношений "многие ко многим" и "один ко многим". Он выполняет несколько
  запросов и объединяет результаты на уровне Python.

### Практические примеры

#### Пример с использованием обоих методов

Представьте, что у нас есть следующие модели:

```python
class Store(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    suppliers = models.ManyToManyField(Supplier)


class Supplier(models.Model):
    name = models.CharField(max_length=100)
```

Теперь, если нам нужно получить все продукты с их магазинами и поставщиками:

```python
products = Product.objects.select_related('store').prefetch_related('suppliers').all()
for product in products:
    print(product.name, product.store.name)
    for supplier in product.suppliers.all():
        print(supplier.name)
```

Этот пример сочетает оба подхода. Мы используем `select_related` для получения связанных магазинов с использованием JOIN
и `prefetch_related` для получения поставщиков, выполняя несколько запросов.

## Как управлять транзакциями?

В Django ORM управление транзакциями можно осуществлять с помощью встроенных инструментов, таких
как `atomic`, `transaction.on_commit`, а также с помощью ручного управления транзакциями через API транзакций.
Рассмотрим примеры для каждого из этих подходов.

### Управление транзакциями с использованием `atomic`

`atomic` — это контекстный менеджер или декоратор, который гарантирует, что все операции внутри блока будут выполнены в
одной транзакции. Если внутри блока возникает исключение, транзакция откатывается.

#### Пример с использованием контекстного менеджера:

```python
from django.db import transaction
from myapp.models import MyModel


def create_records():
    try:
        with transaction.atomic():
            obj1 = MyModel.objects.create(name="Object 1")
            obj2 = MyModel.objects.create(name="Object 2")
            # Если здесь возникнет исключение, то обе записи не будут добавлены
    except Exception as e:
        print(f"Transaction failed: {e}")
```

#### Пример с использованием декоратора:

```python
from django.db import transaction
from myapp.models import MyModel


@transaction.atomic
def create_records():
    obj1 = MyModel.objects.create(name="Object 1")
    obj2 = MyModel.objects.create(name="Object 2")
    # Если здесь возникнет исключение, то обе записи не будут добавлены
```

### Управление транзакциями с использованием `transaction.on_commit`

`on_commit` позволяет зарегистрировать функцию, которая будет выполнена только в случае успешного завершения транзакции.

#### Пример:

```python
from django.db import transaction
from myapp.models import MyModel


def notify_user():
    print("Transaction committed successfully!")


def create_record():
    with transaction.atomic():
        obj = MyModel.objects.create(name="Object 1")
        transaction.on_commit(notify_user)
        # notify_user будет вызвана только если транзакция завершится успешно
```

### Ручное управление транзакциями

Можно управлять транзакциями вручную, открывая и закрывая транзакции с помощью методов `transaction.commit()`
и `transaction.rollback()`.

#### Пример:

```python
from django.db import transaction
from myapp.models import MyModel


def create_records():
    try:
        transaction.set_autocommit(False)  # Отключаем автокоммит
        obj1 = MyModel.objects.create(name="Object 1")
        obj2 = MyModel.objects.create(name="Object 2")
        transaction.commit()  # Явно фиксируем транзакцию
    except Exception as e:
        transaction.rollback()  # Откатываем транзакцию в случае ошибки
        print(f"Transaction failed: {e}")
    finally:
        transaction.set_autocommit(True)  # Включаем автокоммит обратно
```

> Использование транзакций в Django ORM позволяет вам контролировать целостность данных, обеспечивая атомарность
> операций.
> Вы можете использовать контекстный менеджер или декоратор `atomic` для автоматического управления транзакциями, либо
> вручную управлять транзакциями для более точного контроля над процессом.