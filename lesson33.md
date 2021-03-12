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

[Дока](https://ccbv.co.uk/projects/Django/3.1/django.views.generic.base/View/)

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

[Дока](https://ccbv.co.uk/projects/Django/3.1/django.views.generic.base/TemplateView/)

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

[Дока](https://ccbv.co.uk/projects/Django/3.1/django.views.generic.base/RedirectView/)

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

[Дока](https://ccbv.co.uk/projects/Django/3.1/django.views.generic.detail/DetailView/)

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

[Дока](https://ccbv.co.uk/projects/Django/3.1/django.views.generic.list/ListView/)

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

[Дока](https://docs.djangoproject.com/en/3.1/topics/pagination/)

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

[Дока](https://ccbv.co.uk/projects/Django/3.1/django.views.generic.edit/FormView/)

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

```html

<form method="post"> {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Send message">
</form>
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

[Дока](https://ccbv.co.uk/projects/Django/3.1/django.views.generic.edit/CreateView/)

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

В класс нужно передать либо ModelForm, либо модель и поля, что бы класс сам сгенерировал такую форму.

Метод `get` откроет страницу, на которой будет переменая `form`, как и другие view, к которым добавляется форма.

Метод `post` выполнит те же действия, что и FormView, но в случае валидности формы, предварительно
выполнит `form.save()`

Важные параметры:

Такие же, как у FormView и еще свои

```python
form_class = None  # Должен принимать ModelForm
model = None  # Можно указать модель вместо формы, что бы сгенерировать её на ходу
fields = None  # Поля модели, если не указана форма
```

Важные методы:

Все методы из FormView, но дополненные под создание объкта:

`post` - предварительно добавит классу атрибут `self.object = None`

`form_valid` - дополнительно выполнит такую строку `self.object = form.save()`

# Class UpdateView

[Дока](https://ccbv.co.uk/projects/Django/3.1/django.views.generic.edit/UpdateView/)

Класс для обновления объекта, как пользоваться:

Во views.py:

```python
from django.views.generic.edit import UpdateView
from myapp.models import Author


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']
    template_name_suffix = '_update_form'
```

в myapp/author_update_form.html:

```html

<form method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Update">
</form>
```

Методы и атрибуты почти полностью совпадают с CreateView, только UpdateView, перед действиями вызывает
метод `get_object`, для получения нужного объекта, и url должен принимать `pk` для определения этого объекта

## Class DeleteView

[Дока](https://ccbv.co.uk/projects/Django/3.1/django.views.generic.edit/DeleteView/)

Класс для удаления обхектов.

Как пользоваться?

Во views.py:

```python
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from myapp.models import Author


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')
```

В html:

```html

<form method="post">{% csrf_token %}
    <p>Are you sure you want to delete "{{ object }}"?</p>
    <input type="submit" value="Confirm">
</form>
```

Не принимает форму! Принимает модель или кверисет, и обязательно url должен принимать идентификатор, для определения
объекта

## Class LoginView

Класс реализующий логику логина.

Основан на FormView, если форма не была заменена, то по умолчанию
использует `django.contrib.auth.forms.AuthenticationForm`, эта форма содержит два поля, `username` и `password`,
проверяет, что данные валидны, и в случае если данные валидны и пользователь активен, добавляет пользователя в объект
формы.

Так же в LoginView переписан метод form_valid:

```python
def form_valid(self, form):
    """Security check complete. Log the user in."""
    auth_login(self.request, form.get_user())
    return HttpResponseRedirect(self.get_success_url())
```

Если форма валидна, то провести авторизацию.

## Class LogougView

Класс для логаута.

У LogoutView, переписан метод `dispatch`, так что каким бы методом вы не обратились к классу, вы всё равно будете
разлогинены.

## Регистрация

По сути регистрация, это CreateView со своими особенностями (пароль хешируется), поэтому для регистрации используют
просто CreateView, и существует заранее описанная форма UserCreationForm

```python
class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"),
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
                                widget=forms.PasswordInput,
                                help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
```

Принимает `username` и два раза пароль, проверяет, что бы пароли были одинаковые, и при сохранении записывает пароль в
хешированном виде.

## LoginRequiredMixin

Если необходимо закрыть доступ для не залогиненых юзеров от какого либо из классов, то используют `LoginRequiredMixin`,

При наследовании его необходимо указать перед основным классом. Например:

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

Добавляет в класс аттрибут `login_url` который определяет куда нужно перейти, если пользователь пытается получить
доступ, но он не авторизирован.

## Живой пример

Допустим нам нужен сайт, на котором можно зарегистрироваться, залогинится, разлогинится и написать заметку, если ты
залогинен. Заметки должны отображаться списком, последняя созданная, отображается первой. Все пользователи видят все
заметки, возле тех которые создал текущий пользователь, должна быть кнопка удалить.

Как это сделать?

Разработка всегда начинается с описания моделей, нам нужно две сущности, юзер и заметка.

Мы не будем изменять юзера, нам подходит стандартный.

Создадим модель заметки:

В models.py:

```python
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Note(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    class Meta:
        ordering = ['-created_at', ]
```

Не забываем про миграции, и про добавление приложения в settings.py

Создадим необходимые шаблоны: `base`, `index`, `login`, `register`. Пока пустые, заполним чуть позже.

Создадим view. Для базовой страницы на которой отображается список заметок, лучше всего подходит ListView, для логина, и
логаута, существующие классы, для регистрации CreateView.

Для логина и регистрации воспользуемся готовой формой.

Базовую страницу и логаут закроем от не залогиненых пользователей.

Получается как-то так:

Во views.py

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, CreateView

from app.models import Note


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'index.html'
    login_url = 'login/'


class Login(LoginView):
    success_url = '/'
    template_name = 'login.html'


class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = '/'


class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = 'login/'
```

В urls.py проекта добавим через инклюд urls.py приложения

В app/urls.py:

```python
from django.urls import path
from .views import NoteListView, Login, Logout, Register

urlpatterns = [
    path('', NoteListView.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
]

```

И заполним html файлы

base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Base</title>
</head>
<body>
<div>
    {% block content %}
    {% endblock %}
</div>
</body>
</html>
```

index.html

```html
{% extends 'base.html' %}

{% block content %}
<div>
    <a href="{% url 'logout' %}">Logout</a>
</div>
{% endblock %}
```

login.html

```html
{% extends 'base.html' %}

{% block content %}
<span>Wanna register? <a href="{% url 'register' %}">Sign Up</a></span>

<form method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Login">
</form>
{% endblock %}
```

register

```html
{% extends 'base.html' %}

{% block content %}
<span>Already has account? <a href="{% url 'login' %}">Login</a></span>

<form method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Register">
</form>
{% endblock %}
```

Структура для логина, логаута, и регистрации готова.

Добавим отображение списка заметок:

в index.html:

```html
{% extends 'base.html' %}

{% block content %}
<div>
    <a href="{% url 'logout' %}">Logout</a>
</div>

<div>
    {% for obj in object_list %}
    <div>
        {{ obj.text }} from {{ obj.author.username }}
    </div>
    {% endfor %}
</div>
{% endblock %}
```

Но как добавить создание заметок?

Нам нужна форма для создания заметок, и CreateView

В forms.py

```python
from django.forms import ModelForm

from app.models import Note


class NoteCreateForm(ModelForm):
    class Meta:
        model = Note
        fields = ('text',)
```

В полях только текст, потому что время создания будет заполняться автоматически, айди тоже, а юзера мы будем брать из
реквеста.

Будем ли мы отображать отдельную страницу для создания? Нет, значит отдельный хтмл файл нам не нужен, а раз мы не будем
отображать страницу, то и метод `get` нам не нужен. Оставим только post.

Создадим CreateView:

В views.py

```python
class NoteCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login/'
    http_method_names = ['post']
    form_class = NoteCreateForm
    success_url = '/'
```

B выведем урл под этот класс:

В urls.py

```python
from django.urls import path
from .views import NoteListView, Login, Logout, Register, NoteCreateView

urlpatterns = [
    path('', NoteListView.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
    path('note/create/', NoteCreateView.as_view(), name='note-create'),
]
```

Достаточно ли этого, что бы создавать заметки? Нет, потому что мы никуда не вывели форму для создания заметок. Давайте
выведем её на нашу основную страницу.

Во views.py изменим класс `NoteListView`, добавив аттрибут `extra_context = {'create_form': NoteCreateForm()}`

```python
class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'index.html'
    login_url = 'login/'
    extra_context = {'create_form': NoteCreateForm()}
```

Теперь мы можем вывести форму в шаблоне, изменим `index.html`

```html
{% extends 'base.html' %}

{% block content %}
<div>
    <a href="{% url 'logout' %}">Logout</a>
</div>

<div>
    {% for obj in object_list %}
    <div>
        {{ obj.text }} from {{ obj.author.username }}
    </div>
    {% endfor %}
</div>
<form method="post" action="{% url 'note-create' %}">
    {% csrf_token %}
    {{ create_form }}
    <input type="submit" value="Create">
</form>
{% endblock %}
```

Достаточно ли этого? Нет. Наша заметка должна хранить в себе пользователя, а мы нигде его не добавляем. при попытке
вызвать `save()` мы получим ошибку, не могу сохранить без юзера.

Что будем делать? Переписывать логику `form_valid`, мы знаем, что метод `save()` для CreateView вызывается там.

Что бы добавить пользователя, будем использовать `commit=False` для ModelForm, а пользователя возьмем из реквеста.

Перепишем класс NoteCreateView:

Во views.py:

```python
class NoteCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login/'
    http_method_names = ['post']
    form_class = NoteCreateForm
    success_url = '/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form=form)
```

Обратите внимание после успеха, мы попадаем обратно на `/` (success_url) где мы сразу же увидим новую заметку.

Создание готово.

Как добавим удаление? Создадим новую DeleteView, она даже не требует форму.

Во views.py

```python
class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = '/'
```

Не забываем добавить url

В urls.py:

```python
from django.urls import path
from .views import NoteListView, Login, Logout, Register, NoteCreateView, NoteDeleteView

urlpatterns = [
    path('', NoteListView.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
    path('note/create/', NoteCreateView.as_view(), name='note-create'),
    path('note/delete/<int:pk>/', NoteDeleteView.as_view(), name='note-delete'),
]
```

И добавляем форму, для удаления в шаблон.

В index.html:

```html
{% extends 'base.html' %}

{% block content %}
<div>
    <a href="{% url 'logout' %}">Logout</a>
</div>

<div>
    {% for obj in object_list %}
    <div>
        {{ obj.text }} from {{ obj.author.username }}
        <form method="post" action="{% url 'note-delete' obj.pk %}">
            {% csrf_token %}
            <input type="submit" value="Delete">
        </form>
    </div>
    {% endfor %}
</div>
<form method="post" action="{% url 'note-create' %}">
    {% csrf_token %}
    {{ create_form }}
    <input type="submit" value="Create">
</form>
{% endblock %}
```

Это уже будет работать. Но нам же нужно, что бы кнопка удалять была только у своих заметок. Ок добавим `if`.

```html
{% extends 'base.html' %}

{% block content %}
<div>
    <a href="{% url 'logout' %}">Logout</a>
</div>

<div>
    {% for obj in object_list %}
    <div>
        {{ obj.text }} from {{ obj.author.username }}
        {% if obj.author == request.user %}
        <form method="post" action="{% url 'note-delete' obj.pk %}">
            {% csrf_token %}
            <input type="submit" value="Delete">
        </form>
        {% endif %}
    </div>
    {% endfor %}
</div>
<form method="post" action="{% url 'note-create' %}">
    {% csrf_token %}
    {{ create_form }}
    <input type="submit" value="Create">
</form>
{% endblock %}
```

Осталась маленькая деталь, сейчас мы отображаем все существующие заметки, а что если их будет миллион? это не
рационально, давайте добавим пагинацию.

ListView уже передаёт все необходимые данные, нам нужно только добавить размер страницы, и добавить отображение по
страницам в шаблоне.

Во views.py изменим NoteListView

```python
class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'index.html'
    login_url = 'login/'
    extra_context = {'create_form': NoteCreateForm()}
    paginate_by = 5
```

А в index.html:

```html
{% extends 'base.html' %}

{% block content %}
    <div>
        <a href="{% url 'logout' %}">Logout</a>
    </div>

    <div>
        {% for obj in page_obj %} {# обратите внимание я заменил объект #}
            <div>
                {{ obj.text }} from {{ obj.author.username }}
                {% if obj.author == request.user %}
                    <form method="post" action="{% url 'note-delete' obj.pk %}">
                        {% csrf_token %}
                        <input type="submit" value="Delete">
                    </form>
                {% endif %}
            </div>
        {% endfor %}
        <div class="pagination">
    <span class="step-links">
        {% if page_obj.has_previous %}
            <a href="?page=1">&laquo; first</a>
            <a href="?page={{ page_obj.previous_page_number }}">previous</a>
        {% endif %}

        <span class="current">
            Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
        </span>

        {% if page_obj.has_next %}
            <a href="?page={{ page_obj.next_page_number }}">next</a>
            <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
        {% endif %}
    </span>
        </div>
    </div>
    <form method="post" action="{% url 'note-create' %}">
        {% csrf_token %}
        {{ create_form }}
        <input type="submit" value="Create">
    </form>
{% endblock %}


```

Профит! Всё работает. Переходим к заданию на модуль. Все задания должны быть выполнены через Class Based View.