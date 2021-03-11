# Урок 33. ModelForm, ClassBaseView

![](http://memesmix.net/media/created/lm6uyu.jpg)

## ModelForm

Дока [Тут](https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/)

ModelForm - это тип формы который генерируется напрямую из модели. Это очень мощный инструмент работы с моделями.

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

### Валидация

Помимо стандартного метода `is_valid()` у моделформы существует так же встроенный метод `full_clean()`

Если первый отвечает за валидацию формы, то второй отвечает за валидацию для объекта модели.

### Метод save() у формы

Метод save в ModelForm объекте выполняет по сути два действия, получает объект модели основываясь на переданных данных,
и вызывает метод `save`, но уже для модели.

Метод `save()` может принимать аргумент `commit`, по умолчанию `True`. Если указать `commit` как False, метод `save`
модели не будет вызван (объект не будет сохранён в базу), будет только создан предварительный объект модели,
используется, когда нужно "дополнить" данные перед сохранением в базу. Очень часто используется! Например добавление
пользователя из request.

```python
form = PartialAuthorForm(request.POST)
author = form.save(commit=False)
author.title = 'Mr'
author.save()
``` 

### Передача объекта

Такая форма может принимать не только данные, но и целый объект из базы:

```python
from myapp.models import Article
from myapp.forms import ArticleForm

# Create a form instance from POST data.
f = ArticleForm(request.POST)

# Save a new Article object from the form's data.
new_article = f.save()

# Create a form to edit an existing Article, but use
# POST data to populate the form.
a = Article.objects.get(pk=1)
f = ArticleForm(request.POST, instance=a)
f.save()
```

Так как мы можем не только создавать новый инстанс, но и обновлять существующий.

# Class Base View

С этого момента мы переходим на использование `view` основанных исключительно на классах.

Все основные существующие классы описаны [Тут](https://ccbv.co.uk/)

## Class View

Основой всех классов используемых во `view` является класс `View`, методы этого класса используются всеми остальными
классами.

Основные аттрибуты:

```http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']```

Атрибут который нужен, что бы определить какие виды запросов будут доступны для запросов.

Основные функции:

`as_view` - метод который всегда вызывается что-бы использовать класс в `urls.py`, внутри вызывает методы `setup`
и `dispatch`

`setup` - метод, который добавляет `request` в `self`, благодаря чему `request` будет доступен в абсолютно любом методе
всех наших `view` классов

`http_method_not_allowed` - метод, который генерирует ошибку запроса (не могу обработать, например, POST запрос.

`dispatch` - метод отвечающий за вызов обработчика при запросе.

```python
def dispatch(self, request, *args, **kwargs):
    # Try to dispatch to the right method; if a method doesn't exist,
    # defer to the error handler. Also defer to the error handler if the      
    # request method isn't on the approved list.
    if request.method.lower() in self.http_method_names:  # Если запрос находится в списке разрешенных то заходим.
        handler = getattr(self, request.method.lower(),
                          self.http_method_not_allowed)  # Пытаемся из self получить аттрибут или метод совпадающий названием с методом запроса (POST - post, GET - get), если не получается, то вернуть метод http_method_not_allowed
    else:
        handler = self.http_method_not_allowed  # Вернуть метод http_method_not_allowed
    return handler(request, *args,
                   **kwargs)  # Вызвать метод который мы получили ранее, если удалось, то, например, get(), или post(), если нет, то http_method_not_allowed()
```

Как это работает?

Если наследоваться от этого класса, то мы можем описать функцию `get` и/или `post` что бы описать что необходимо делать
при запросе методами `GET` или `POST`

И можем описать какие вообще запросы мы ожидаем принимать в аттрибуте `http_method_names`

Например:

Во `views.py`

```python
from django.views import View
from django.shortcuts import render


class MyView(View):
    http_method_names = ['get', ]

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
```

В `urls.py`:

```python
...
path('some-url/', MyView.as_view(), name='some-name')
...
```

Чем такая конструкция лучше, чем обычная функция? Тем, что обычная функция обязана принимать любой запрос и дальше
только при помощи `if` разделять разные запросы.

Такой класс, будет принимать только запросы описанных методов, отклоняя все остальные, и каждый запрос будет написан в
отдельном методе, что сильно улучшает читабельность кода.

## Class TemplateView

Класс необходимый для рендера html файлов

Основные атрибуты:

```python
template_name = None  # Имя html файла который нужно рендерить
extra_content = None  # Словарь с контентом
```

Основные методы:

Описан метод `get`

```python
def get(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)
    return self.render_to_response(context)
```

`get_context_data` - Метод возвращающий данные которые будут добавлены в контекст

Как этим пользоваться?

```python
from django.views.generic.base import TemplateView

from articles.models import Article


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context
```

Мы описали класс, который будет рендерить файл `home.html`, в контексте которого будет переменная `latest_articles` в
которой будет коллекция из объектов модели.

То же самое можно было сделать через `extra_context`:

```python
from django.views.generic.base import TemplateView

from articles.models import Article


class HomePageView(TemplateView):
    template_name = "home.html"
    extra_context = {"latest_articles": Article.objects.all()[:5]}
```

## Class RedirectView

Класс необходимый, что бы перенаправлять запросы с одного url на другой.

Основные атрибуты:

```python 
query_string = False # сохранить ли квери параметры (то что в строке браузера после ?) при редиректе
url = None # Урл на который надо перейти
pattern_name = None # Имя урла, на который надо перейти
```

Основные методы:

Описаны все HTTP методы, и все они ссылаются на `get`, например `delete`:

```python
def delete(self, request, *args, **kwargs):
    return self.get(request, *args, **kwargs)
```

Метод `get_redirect_url` отвечает за то, что бы получить url на который надо перейти

Как пользоваться

```python
class ArticleRedirectView(RedirectView):
    query_string = True
    pattern_name = 'article-detail'
```

## Class DetailView

Класс, который необходим для того что бы сделать страницу для просмотра одного объекта.

Ему необходимо передать `pk` либо `slug` и это позволит отобразить один объект (статью, товар итд.)

Как этим пользоваться?

Например:

Во views.py

```python
from django.views.generic.detail import DetailView

from articles.models import Article


class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()  # Просто добавляем текущее время к контексту
        return context
```

В urls.py:

```python
from django.urls import path

from article.views import ArticleDetailView

urlpatterns = [
    path('<pk:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]
```

Этого уже достаточно что бы отрисовать страницу деталей объекта. Если `template_name` не указан явно, то Django, будет
пытаться отобразить `templates/app_name/model_detail.html` где `app_name` - название приложения, `model` - название
модели, `detail` - константа.

В контекст будет передана переменная `object`. Методы `post`, `put` итд. не определены.

Важные параметры.

```python
pk_url_kwarg = 'pk'  # Как переменная называется в urls.py, например `<int:my_id>`
queryset = None  # если указан, то возможность ограничить доступ только для части объектов (например, убрать из возможности обновления деактивированные объекты).
template_name = None  # указать имя шаблона.
model = None  # класс модели, если не указан queryset, сгенерирует queryset из модели.
```

Важные методы:

`get_queryset` - переопределить queryset

`get_context_data` - тоже что и у TemplateView

`get_object` - определяет логику получения объекта

## Class ListView

Класс, необходимый для отображения списка объектов.

Добавляет в контекст список объектов и информацию о пагинации.

Как пользоваться?

```python
class CommentListView(ListView):
    paginate_by = 10
    template_name = 'comments_list.html'
    queryset = Comment.objects.filter(parent__isnull=True)
```

### Пагинация

Очень часто наше приложение хранит большое кол-во данных, и при отображении нам не нужно показывать прям всё (допустим у
нас блог на 1000000000 статей), для выдачи данных порциями, это и называется пагинация, или разбиение на страницы.

Когда вы листаете ленту, на самом деле, вы подгружаете всё новые и новые страницы, просто при помощи JSa это сделано
так, что вы этого не замечаете.

За это отвечает параметр:

```python
paginate_by = None  # можно указать сколько должно быть объектов на одной странице 
```

В шаблон будут переданы как список объектов, так и данные по пагинации

```python
context = {
    'paginator': paginator,  # объект класса пагинации, хранит все подробности, которые только могут быть.
    'page_obj': page,
    # информация о текущей странице, какая это страница, сколько всего страниц, урл на следующую и предыдущую страницу
    'is_paginated': is_paginated,
    # были ли данные вообще пагинированы, возможно у вас 10 объектов на страницу, а их всего 5, тогда нет смысла в пагинации
    'object_list': queryset  # Сам кверисет с объектами
}
```

Важные параметры, такие же как у DetailView, и еще новые

```python
allow_empty = True  # разрешить ли отображение пустого списка
ordering = None  # явно указать ордеринг
```

Всё еще описан только метод `get`. Методы `post`, `put` итд не разрешены.

Важные методы:

`get_queryset` - переопределить queryset

`get_context_data` - тоже что и у TemplateView

`get_paginator` - определяет логику получения класса пагинатора

`get_paginate_by` - определяет логику получения значение paginate_by

`get_ordering` - определяет логику получения ордеринга

`get_allow_empty` - определяет логику получения переменной allow_empty

## Class FormView

Не все классы предназначены только для чтения данных.

FormView класс необходимый для обработки формы.

Как пользоваться?

В forms.py

```python
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
```

Во views.py

```python
from myapp.forms import ContactForm
from django.views.generic.edit import FormView


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
```

В contact.html:

```python
< form
method = "post" > { % csrf_token %}
{{form.as_p}}
< input
type = "submit"
value = "Send message" >
< / form >
```

Важные параметры:

Такие же, как у TemplateView и еще свои

```python
form_class = None  # сам класс формы
success_url = None  # На какую страницу перейти если форма была валидна
initial = {}  # Словарь с базовыми значениями формы
```

Важные методы:

Тут наконец определён метод `post`:

```python
def post(self, request, *args, **kwargs):
    """
    Handle POST requests: instantiate a form instance with the passed
    POST variables and then check if it's valid.
    """
    form = self.get_form()
    if form.is_valid():
        return self.form_valid(form)
    else:
        return self.form_invalid(form)
```

Так же все методы из TemplateView

`get_context_data` - дополнительно добавляет переменную `form` в темплейт

`get_form` - получить объект формы

`get_form_class` - получить класс формы

`form_valid` - Что делать если форма валидна

`form_invalid` - Что делать если форма не валидна

`get_success_url` - Переопределить генерацию урла на который будет совершен переход если форма валидна


## Class CreateView

Класс для создания объектов.

Как этим пользоваться?

Во views.py

```python
from django.views.generic.edit import CreateView
from myapp.models import Author

class AuthorCreate(CreateView):
    template_name = 'author_create.html'
    model = Author
    fields = ['name']
```

В author_create.html

```html
<form method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save">
</form>
```


# Переходим к CCBV

Описывать действия при помощи методов конечно же можно, но более комплексным и готовым решением является использование
встроенных классов

Мы будем рассматривать часть этих классов на занятии, еще часть на самостоятельное изучение.

Начнём с класса `FormView`

Если открыть вот [эту](https://ccbv.co.uk/projects/Django/2.2/django.views.generic.edit/FormView/) ссылку, то можно
увидеть все встроенные системы этого класса и все зависимости.

Но, как этим пользоваться?

`views.py`

Если заменить код во вью на вот такой:

```python
from .forms import MyForm
from django.views.generic import FormView


class MyFormView(FormView):
    template_name = 'index.html'
    http_method_names = ['get', 'post']
    form_class = MyForm
    success_url = '/'
```

И переписать урл на

```python
path('', MyFormView.as_view()),
```

Этого будет уже достаточно, для отрисовки и обработки формы

В любой стандартной Class-base view есть метод `dispatch` который отвечает за обработку запросов, если он не
переопределен, то изначально, он выполняет действия по запросу, описанные в методе, с таким же названием, как и у http
метода.

```python
class MyFormView(FormView):
    template_name = 'index.html'
    http_method_names = ['get', 'post']
    form_class = MyForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        print('GET REQUEST')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('POST REQUEST')
        return super().post(request, *args, **kwargs)
```

**Любой метод можно переписать!** Лучше практикой считается переписывание только тех методов которые вам нужны, с
вызовом супера, для этого метода (Но бывают случаи, когда логика требует другого, и это тоже нормально)

Теперь когда мы знаем, что любое отображение можно сделать при помощи классов, давайте познакомимся с использованием
классов, для любых нужных нам задач.

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

content_type - тип контента, по умолчанию None, может быть разных типов например использоваться как файл (
Подробнее [Тут](https://developer.mozilla.org/ru/docs/Web/HTTP/%D0%97%D0%B0%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BA%D0%B8/Content-Type))

extra_content - None или словарь, всё что описано в этом словаре, будет автоматически добавлено в контент.

http_method_names - список http методов

response_class - класс отвечающий за респонс, по умолчанию стандартный джанго темплейт класс

template_engine - "движок" темплейтов, по умолчанию берется из settings.py

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

### Важные методы

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

url - сам урл куда вы хотите перенаправить запрос. Работает только одно из двух. url выше по приоритету, чем
pattern_name

query_string - булеан, хотите ли вы сохранение квери параметры при редиректе.

permanent - хотите ли вы сделать редирект перманентным (подробности [тут](https://realpython.com/django-redirects/))

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

### Важные методы

def get(self, request, *args, **kwargs) - отвечает за поведение гет запроса.

Все остальные методы будут ссылаться на гет.

## CreateView

CreateView - класс отвечающий за создание объектов.

Важные параметры.

fields = None

form_class = None

initial = {}

model = None

success_url = None

template_name = None

Если не определить моделформу, то такой класс сгенерирует её автоматически из полей `fields` и `model`

fields - список полей из модели

model - модель

form_class - класс моделформы (Или указываем её, или филдс и модель)

initial - указать предварительно подготовленные данные

success_url - урл на который нужно перейти в случае успеха

template_name - имя шаблона, который нужно отрендерить, в случае если это поле не указано, автоматически будет
произведён поиск в (<app_name>/<model_name>_<template_name_suffix>.html)

Если вы не переопределяли `template_name_suffix` (по умолчанию `_form`), приложение называется `blog`, а
модель `comment` то поиск будет произведён в `templates/blog/comment_form.html`

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

### Важные методы

def get(self, request, *args, **kwargs) - отвечает за поведение гет запроса.

def post(self, request, *args, **kwargs) - отвечает за поведение пост и пут запросов.

def get_context_data(self, **kwargs) - отвечает за добавление контекста к реквесту.

def form_valid(self, form) - отвечает за поведение если форма валидна.

def form_invalid(self, form) - отвечает за поведение если форма не валидна.

def get_success_url(self) - определение урла после выполнения действия.

## UpdateView

UpdateView - класс отвечающий за обновление объектов.

Те же поля что и у криэйт вью и новые.

У апдейт вью, обязательным параметром в урле, обязательно нужно передавать уникальный идентификатор.

Важные параметры.

pk_url_kwarg = 'pk'

queryset = None

slug_field = 'slug'

slug_url_kwarg = 'slug'

pk_url_kwarg - имя для уникального идентификатора, по умолчанию `pk`

queryset - кверисет которым можно ограничить объекты (например, убрать из возможности обновления деактивированные
объекты)

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

### Важные методы

Такие-же как и у криэйт вью и новые

def get_object(self, queryset=None), метод отвечающий за получение объекта модели.

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

### Важные методы

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

### Важные методы

Совпадают с апдейт вью.

## ListView

ListView - класс отвечающий за отображение списка объектов.

Те же поля, что и у дитейл вью, так же не принимает форму, добавляет список объектов и не только в контекст.

Важные поля.

allow_empty = True, разрешить ли отображать пустой список

model = None , модель

ordering = None, ордеринг (правило сортировки)

page_kwarg = 'page' (поле в квери параметре которое отвечает за-то какую страницу отобразить)

paginate_by = None (нужно ли разбивать данные по страницам, если да, то по сколько именно, принимает число)

paginator_class = <class 'django.core.paginator.Paginator'>    , класс отвечающий за пагинацию

queryset = None, кверисет перебираемых объектов.

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

### Важные методы

def get(self, request, *args, **kwargs) - отвечает за поведение гет запроса.

def get_ordering(self) - отвечает за ордеринг

def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True, **kwargs) - отвечает за объет
пагинции

def paginate_queryset(self, queryset, page_size): пагинирует кверисет, если это необходимо.

def get_paginate_by(self, queryset): отвечает за размер страницы при пагинации итд...

### Практика и еще раз практика!

# Выдача задания на модуль!

## Задание должно быть выполнено через Class Base View!!

Для такой же проверки для класс бейз вью используется LoginRequiredMixin.
Почитать [Тут](http://ccbv.co.uk/projects/Django/2.2/django.contrib.auth.mixins/LoginRequiredMixin/)

Для этого наследуемся от него тоже.

Например вот так

```python
from .forms import MyForm
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin


class MyFormView(LoginRequiredMixin, FormView):
    template_name = 'index.html'
    http_method_names = ['get', 'post']
    form_class = MyForm
    success_url = '/'
    login_url = '/login/'
```

Теперь нельзя попасть на страницу обрабатываемую этим классом, если пользователь не залогинен. В случае если он не
залогинен, он будет перекинут на страницу указанную в атрибуте `login_url`.
