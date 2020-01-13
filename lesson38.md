# Урок 38. TemplateView, RedirectView, CreateView, UpdateView, DetailView, ListView, ModelForm 

![](http://memesmix.net/media/created/lm6uyu.jpg)

Теперь когда мы знаем, что любое отображение можно сделать при помощи классов, давайте познакомимся с использованием классов, для любых нужных нам задач.

## TemplateView

Дока [Тут](https://ccbv.co.uk/projects/Django/3.0/django.views.generic.base/TemplateView/)

TemplateView это класс который нужен для того, что бы отрендерить html страницу, без дополнительных действий.

Принимает следующие параметры:

content_type = None	

extra_context = None

http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

response_class = <class 'django.template.response.TemplateResponse'>

template_engine = None

template_name = None

content_type - тип контента, по умолчанию None, может быть разных типов например использоваться как файл (Подробнее [Тут](https://developer.mozilla.org/ru/docs/Web/HTTP/%D0%97%D0%B0%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BA%D0%B8/Content-Type)).
 
extra_content - None или словарь, всё что описанно в этом словаре, будет автоматически добавленно в контент.

http_method_names - список http методов

response_class - класс отвечающий за респонс, по умолчанию стандартный джанго темплейт класс

template_engine - "движок" темплейтов, по умолчанию береться из settings.py

template_name - имя шаблона который нужно отрендерить, единственный обязательный аттрибут в TemplateView

### Как пользоваться?

`views.py`
```python
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = 'index.html'
```
`urls.py`
```python
from .views import Index
urlpatterns = [
    path('', Index.as_view(), name='index'),
]
```

`templates/index.html`
```html
Some html code
```


###Важные методы

def get(self, request, *args, **kwargs) - отвечает за поведение гет запроса.
 
## RedirectView

Дока [тут](https://ccbv.co.uk/projects/Django/3.0/django.views.generic.base/RedirectView/)

RedirectView - класс отвечающий за перенаправление запроса

http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

pattern_name = None

permanent = False

query_string = False

url = None

pattern_name - имя урла на который вы хотите перенаправить запрос

url - сам урл куда вы хоттите перенаправить запрос. Работает только одно из двух. url выше по приоритету, чем pattern_name

query_string - булеан, хотите ли вы сохрание квери параметры при редиректе.

permanent - хотите ли вы следать редирект перманентным (подробности [тут](https://realpython.com/django-redirects/))

### Как пользоваться?
`views.py`
```python
from django.views.generic import RedirectView

class Redirect(RedirectView):
    pattern_name = 'index'
    query_string = True
```
`urls.py`
```python
from .views import Index
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('wrong/', Redirect.as_view(), name='wrong'),
]
```

###Важные методы

def get(self, request, *args, **kwargs) - отвечает за поведение гет запроса.

Все остальные методы будут ссылаться на гет.

## ModelForm

Дока [Тут](https://docs.djangoproject.com/en/2.2/topics/forms/modelforms/)

ModelForm - это тип формы который генерируется напрямую из модели. Используется для изменения поведения действий с моделями. Можно переопределть определенные действия с такими формами.

Синтаксис

`models.py`

```python
from django.db import models


TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
```

`forms.py`

```python
from django.forms import ModelForm


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']
```

Поле `fields` либо `exclude` являются обязательными

Такой вид форм, равнозначен с

`forms.py`

```python
from django import forms

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    title = forms.CharField(
        max_length=3,
        widget=forms.Select(choices=TITLE_CHOICES),
    )
    birth_date = forms.DateField(required=False)

class BookForm(forms.Form):
    name = forms.CharField(max_length=100)
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
```

Помимо стандартного метода `is_valid()` у моделформы существует так же встроенный метод `full_clean()`

Если первый отвечает за валидацию формы, то второй отвечает за валидацию для объекта модели.

Метод `save()` может принимать агрумент `commit`, по умолчанию `True`.

Если указать коммит как фолс, объект не будет сохранён в базу, будет только создан предварительный объект для создания, используется, когда нужно "дополнить" данные перед сохранением в базу.

```python
form = PartialAuthorForm(request.POST)
author = form.save(commit=False)
author.title = 'Mr'
author.save()
``` 

## CreateView

CreateView - класс отвечающий за создание объектов. 

Важные параметры.

fields = None

form_class = None

initial = {}

model = None

success_url = None

template_name = None

Если не определить моделформу, то такой класс сгенериует её автоматически из полей `fields` и `model`

fields - список полей из модели

model - модель

form_class - класс моделформы (Или указываем её или филдс и модель)

initial - указать предварительно подготовленные данные

success_url - урл на который нужно перейти в случае успеха

template_name - имя шаблона, который нужно отрендерить, в случае если это поле не указано, автоматически будет произведён поиск в (<app_name>/<model_name>_<template_name_suffix>.html)

Если вы не переопределяли `template_name_suffix` (по умолчанию `_form`), приложение называется `blog`, а модель `comment` то поиск будет произведён в `templates/blog/comment_form.html`

Добавляет в контекст переменную `form`

### Как пользоваться?

Если у вас есть модель Comment и урл '/comments'

`forms.py`

```python
class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'author', 'article']
```

`views.py`

```python
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreateForm
    success_url = '/comments'
```

`urls.py`

```python
from django.urls import include, path
from .views import CommentCreateView

urlpatterns = [
    path('comment_create/', CommentCreateView.as_view(), name='comment_create'),
]
```
###Важные методы

def get(self, request, *args, **kwargs) - отвечает за поведение гет запроса.

def post(self, request, *args, **kwargs) - отвечает за поведение пост и пут запросов.

def get_context_data(self, **kwargs) - отвечает за добавление контекста к реквесту.

def form_valid(self, form) - отвечает за поведение если форма валидна.

def form_invalid(self, form) - отвечает за поведение если форма не валидна.

def get_success_url(self) - определение урла после выполнения действия.

## UpdateView

UpdateView - класс отвечающий за обновление объектов. 

Теже поля что и у криэйт вью и новые.

У апдейт вью, обязательным параметром в урле, обязательно нужно передавать уникальный идентификатор.

Важные параметры.

pk_url_kwarg = 'pk'	

queryset = None	

slug_field = 'slug'	

slug_url_kwarg = 'slug'	

pk_url_kwarg - имя для уникального идентификатора, по умолчанию `pk`

queryset - кверисет которым можно ограничить объекты (например, убрать из возможности обновления деактивированные объекты)

slug_field - название аттрибута слага в модели.

slug_url_kwarg - филд для слага в урле, не обязательный, но если не указан pk джанго попытается найти объект по слагу

### Как пользоваться?

Если у вас есть модель Article и урл '/'

`views.py`

```python

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_update.html'
    success_url = '/'
    fields = ['name', 'text', 'author']
```

`urls.py`

```python
from django.urls import include, path
from .views import ArticleUpdateView

urlpatterns = [
    path('article_update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
]
```

Обратите внимание, в этот раз мы не использовали моделформу, она будет сгенерирована автоматически.

###Важные методы

Такие-же как и у криэйт вью и новые

def get_object(self, queryset=None) , метод отвечающий за получение объекта модели.

## DeleteView

DeleteView - класс отвечающий за удаление объектов. 

Работает по тому же принципу, что и апдейт вью, но не воспринимает форму.

### Как пользоваться?

Если у вас есть модель Article и урл '/'

`views.py`

```python
class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = '/'
```

`urls.py`

```python
from django.urls import include, path
from .views import ArticleDeleteView

urlpatterns = [
    path('article_delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
]
```

Обратите внимание, форма или даже филды не указанны вообще.

###Важные методы

Совпадают с апдейт вью.

## DetailView

DetailView - класс отвечающий за отображение одного объекта. 

Те же поля, что и у делит вью, так же не принимает форму, добавляет объект в контекст.

У дитейл вью, обязательным параметром в урле, обязательно нужно передавать уникальный идентификатор.

### Как пользоваться?

Если у вас есть модель Article и урл '/'

`views.py`

```python
class ArticleDetailView(DetailView):
    model = Article
```

`urls.py`

```python
from django.urls import include, path
from .views import ArticleDetailView

urlpatterns = [
    path('article_detail/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
]
```

При такой записи, обязательно должна существовать html (templates/app_name/article_detail.html)

###Важные методы

Совпадают с апдейт вью.

## ListView

ListView - класс отвечающий за отображение списка объектов. 

Те же поля, что и у дитейл вью, так же не принимает форму, добавляет список объектов и не только в контекст.

Важные поля.

allow_empty = True	, разрешить ли отображать пустой список

model = None	, модель

ordering = None	, ордеринг (правило сортировки)

page_kwarg = 'page'	(поле в квери параметре которое отвечает за-то какую страницу отобразить)

paginate_by = None	(нужно ли разбивать данные по страницам, если да, то по сколько именно, принимает число)

paginator_class = <class 'django.core.paginator.Paginator'>	, класс отвечающий за пагинацию

queryset = None , кверисет перебираемых объектов.

### Как пользоваться?

Если у вас есть модель Comment

`views.py`

```python
class CommentListView(ListView):
    model = Comment
    paginate_by = 10
    template_name = 'comments_list.html'
    queryset = Comment.objects.filter(parent__isnull=True)
```

`urls.py`

```python
from .views import CommentListView

urlpatterns = [
    path('comments/', CommentListView.as_view(), name='comments'),
]
```

###Важные методы

def get(self, request, *args, **kwargs) - отвечает за поведение гет запроса.

def get_ordering(self) - отвечает за ордеринг

def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True, **kwargs) - отвечает за объет пагинции

def paginate_queryset(self, queryset, page_size): пагинирует кверисет, если это необходимо.

def get_paginate_by(self, queryset): овечает за размер страницы при пагинации итд...


### Практика и еще раз практика!

# Домашнее задание:

1. Создать страницы просмотра, модификации, создания и удаления коментариев

2. Создать страницу где можно будет список коментариев, и возможность создавать коментарии, которые будут ответом на "корневые" (не имеющие родителя) коментарии.

