# Урок 37. Формы, реквест и авторизация.

![](http://memesmix.net/media/created/uuyoh3.jpg)

## HTML формы

Html форма, это специальный тег, который "сообщает" браузеру, что данные из этого тега нужно сгрупировать и подготовить к отправке на сервер.

Принимает два параметра `action` и `method`. `action` описывает, куда форма по результату должна обращаться, в нашем случае это будет `url`. `method` - отвечает за метод отправки, варианты это `get` и `post`. `get` будет использован по умолчанию если не указан явно. 

Пост формы используются для передачи данных не подлежащих огласке, например, логин и пароль. Гет формы, используются для обзедоступной информации, например строка поиска.

Внутри формы мы указываем нужное кол-во тегов <input> с нужными типами. Именно эти данные будут в последствии переданы серверу.

[Сслыка на общее описание форм](https://www.w3schools.com/html/html_forms.asp)

#### основные типы инпутов


**number** - ввод числа

**text** - ввод текста

**checkbox** - чекбокс (выбор нескольких элементов через галочки)

**radio** - радиобаттон (выбор только одного элемента из списка)

**button** - классическая кнопка (если в форме есть один такое элемент, но нет сабмита, браузер автоматически подсчитает его сабмитом)

**hidden** - скрытое поле, чаще всего нужно для целей безопасности или добавления информации и данным не отображая её (Не отображается)

**submit** - отправка формы

Это далеко не все типы инпутов, которые могут быть.
[Ссылка на типы инпутов](https://www.w3schools.com/html/html_form_input_types.asp)

Создадим простейшую форму:

```html
<form action="/your-form-url/" method="post">
    <label for="your_name">Your name: </label>
    <input id="your_name" type="text" name="your_name">
    <input type="submit" value="OK">
</form>
```

И создадим два урла и две вьюшки, один для отрисовки формы, второй для приёма данных (На самом деле, это чаще всего один урл с разной логикой, но пока так)

```python
def index(request):
    return render(request, 'index.html')


def get_name(request):
    return render(request, 'request.html')
```

Форму добавим на страницу `index.html`

Отрисовку реквеста в `request.html`

Файл `request.html`

```html
{% block content %}
   {{ request }}
{% endblock %}
```

Обработчиком в моём случае является метод `get_name` по урлу `/your-form-url/`

Если вы всё сделали правильно, то при открытии урла соответсвующего html c формой, вы удидите, что-то такое:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson37/simple_form.png)

А при попытке, засабмитить форму, такое

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson37/csrf.png)

Это сработала встроенная в джанго система защиты формы от кроссайтовго скриптинга.

Кому интересно что это читать [Тут](https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B6%D1%81%D0%B0%D0%B9%D1%82%D0%BE%D0%B2%D0%B0%D1%8F_%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D0%BB%D0%BA%D0%B0_%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D0%B0)

Как этого избежать. 

Для того, что бы бекенд мог нормально обрабатывать форму, нужно в каждую фому добавлять csrf токен.

Делается это при помощи, стандартного темплейт тега  `{% csrf_token %}`. Добавим его в нашу форму, и не забывайте добавлять его в каждую форму и методом пост.

Теперь html выглядит вот так.

```html
<form action="/your-form-url/" method="post">
    {% csrf_token %}
    <label for="your_name">Your name: </label>
    <input id="your_name" type="text" name="your_name">
    <input type="submit" value="OK">
</form>
```

Откроем страницу для обработки формы. и посмотрим в код страницы.

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson37/csrf_form.png)

Тег добавил нам специальное скрытое поле, со сгенерированным кодом. Почему он будет автоматичски обработан мы разберём в следующих занятиях.

Если теперь мы засабмитим форму, мы увидим, что всё отработало, и данные были отправленны.

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson37/request_html.png)

Но где-же наши данные?

давайте распечатаем в консоль, значения из переменной request.POST во вью

```python
def get_name(request):
    print(request.POST)
    return render(request, 'request.html')
```

Теперь, при сабмите формы, мы увидим в консоли:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson37/request_post.png)

Мы получим данные из формы, в виде словаря, причём ключами этого словаря, будут поля `name` в инпутах формы, если имя указанно не будет, данные потеряются.

### Джанго формы

Джанго предоставляет нам возможность гененрировать html формы из кода на python!

Что для этого нужно. Создадим в нашем приложении файл `forms.py`

Внутри этого файла укажем.

`forms.py`

```python
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
```

Обработчик для урла заменим на:

`views.py`

```python
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'index.html', {'form': form})
```

html с формой на:

```html
<form action="/your-form-url/" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit">
</form>
```

Что именно мы сделали. 

В файле `forms.py` мы создали класс формы. в котором описали одно поле **your_name**

Текстового типа, с указанным лейблом и максимальной длинной, так же как и у моделей у форм существует больше кол-во типов полей

Основые типы:

BooleanField - булеан

CharField - текст

ChoiceField - поле для выбора

DateTimeField - дата время

EmailField - имейл

FileField - файл

IntegerField - целое число

MultipleChoiceField - множественный выбор

И многие другие, почитать про них нужно [тут](https://docs.djangoproject.com/en/2.2/ref/forms/fields/#built-in-field-classes)

У полей формы есть такое понятие как виджет, он отвечает за то, как именно будет отображаться конкретный филд, например, для текста базово это текстовое поле, а для даты и времени, это встроенный пикер (выпадающее окно с календарём и часами) итд.

Виджет можно указать отличающийся от стандартного.

Прочитать про виджеты нужно [тут](https://docs.djangoproject.com/en/2.2/ref/forms/widgets/#built-in-widgets).

К каждому полю, мы можем указать дополнительные аттрибуты

required - является ли поле обязательным

label - лейбл, приписка к инпуту

label_suffix - символ между лейблом и инпутом

initial - значение по умолчанию

widget - читай выше

help_text - подскасзка к инпуту

error_messages - переписать сдарнтые тексты для ошибок типов полей

validators - дополенительные проверки поля

localize - информация о переводе формы на другие языки

disabled - сделать поле не активным (без возможности изменения)

В обработчике, указываем разное поведение для разных типов запросов.

В реквесте хранится информация о типе запроса. В данном случае, если запрос пришел по методу POST, то мы в переменной form инициализируем класс формы, передав в неё данные из запроса. Далее проверяем данные на "правильность" и если всё хорошо, то переходим на другую страницу, это стандартная логика, для, допустим, формы востановления пароля, если все данные введены правильно (при помощи стандартного метода is_valid, отображаем другую страницу, если нет, подсвечиваем ошибки.

Если метод запроса, не POST, чаще всего это GET, инциализируем пустой класс формы и передаём его в html.

В таком случае, если форма была заполнена правильно, мы это проверили, и выполнили дальнейшую интересующую нас логику, если не правильно, то джанго за нас отобразит все поля с ошибками.

Если запрос не был запросом с данными, просто отображаем нашу форму, как обычную переменную в шаблоне, при помощи `{{ form }}`.

**После применения метода `is_valid` у объекта формы, появляется аттрибут `cleaned_data` который хранит все данные в виде словаря, если форма валидна, и аттрибут `errors` если данные не валидны.**

### Отображение формы в шаблоне.

У объекта формы есть стандартные поля и методы, которые мы можем указывать в шаблоне, например.

{{ form.as_table }} - рендер в виде таблицы, через <tr> теги

{{ form.as_p }} рендер каждого поля через <p> теги

{{ form.as_ul }} рендер в виде списка через <li> теги


Так-же, можно рендерить форму не целиком, а например, по отдельным филдам, при помощи стандартного обращения через точку, например `{{ form.name }}`

У каждого поля есть аттрибут `errors` который хранит информацию об ошибках по этому полю, если они были обнаружены. `{{ form.my_field.errors }}`

Если в запустить форму через for в итерируемом объекте будут поля.

```html
{% for field in form %}
    <div class="fieldWrapper">
        {{ field.errors }}
        {{ field.label_tag }} {{ field }}
        {% if field.help_text %}
        <p class="help">{{ field.help_text|safe }}</p>
        {% endif %}
    </div>
{% endfor %}
```

И многие другие атрибуты и методы, подробно можно прочитать [тут](https://docs.djangoproject.com/en/3.0/topics/forms/#working-with-form-templates)

## Капелька практики

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4NaUeUrcabAUeF6LAMR4FdHZxmPWPA73dbqOm51051b2AyeUstQ&s)

Напишите форму, в которой можно указать имя, пол, возраст и уровень владения английским (выпадающим списком), если введенные данные это парень старше 20-и (включительно) и уровнем английского B2 выше, или девушка старше 22-ух и уровнем выше чем B1 то перейти на страницу где будет написано, что вы нам подходите, и что не подходит соответсвенно.

# Переходим к CCBV

Описывать действия при помощи методов конечно же можно, но более комплексным и готовым решением является использование встроенных классов

Все основные существующие классы описаны [Тут](https://ccbv.co.uk/)

Мы будем рассматривать часть этих классов на занятии, еще часть на самостоятельное изучение.

Начнём с класса `FormView`

Если открыть вот [эту](https://ccbv.co.uk/projects/Django/2.2/django.views.generic.edit/FormView/) ссылку, то можно увидеть все встроенные системы этого класса и все зависимости.

Но, как этим пользоваться?

`views.py`

Если заменить код во вью на вот такой0

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

В любой стандартной Class-base view есть метод `dispatch` который отвечает за обработку запросов, если он не переопределен, то изначально, он выполняет действия по запросу, описанные в методе, с таким же названием как и у http метода.

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

**Любой метод можно переписать!** Лучше практикой считается переписывание только тех методов которые вам нужны, с вызовом супера, для этого метода (Но бывают случаи, когда логика требует другого, и это тоже нормально)

Практика:

Переписываем прошлый пример, при помощи класс бейз вью.

# Система авторизации

### Логин

Для того, что бы пользователь мог авторизоваться на сайте, нам нужны его входные данные и стандартные методы `authenticate, login`

Как это работает. Если вы не дополняли сеттинги, то джанго автоматически использует стандартного юзера, и стандартную систему авторизации.

Метод `authenticate` принимает, имя пользователя и пароль, и если находит совпадение то возвращает объект пользователя(модели), если не находит, то возвращает `None`.

Метод `login` принимает, реквест, и объект модели пользователя.

По этому стандартным способом, для авторизации является примерно такой код:

```python
from django.contrib.auth import authenticate, login

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...
```


### Logout

Для вывода пользователя из системы, используется метод `logout` который принимает только реквест.

```python
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirect to a success page.
```

### Проверка на то, что пользователь уже зашел в систему

В реквесте всегда есть поле `user`, у которого всегда есть аттрибут `is_authenticated` проверяя его, мы можем определять является ли пользователь авторизированным

```python
request.user.is_authenticated
```

### Закрыть страницу от не залогиненего пользователя

Для того, что бы не предоставлять доступ, для не залогиненых пользователей, существует два способа, для функцифонально описанных вью это декоратор `@login_required`

```python
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    ...
```

Он так-же может принимать ссылку, на страницу логина, и автоматически отправлять на эту страницу, для не залогиненного пользователя.

```python
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def my_view(request):
    ...
```

Для такой же проверки для класс бейз вью используется LoginRequiredMixin. Почитать [Тут](http://ccbv.co.uk/projects/Django/2.2/django.contrib.auth.mixins/LoginRequiredMixin/)

Для этого наследуемся от него тоже.

Например вот так

```python
from .forms import MyForm
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin


class MyFormView(FormView, LoginRequiredMixin):
    template_name = 'index.html'
    http_method_names = ['get', 'post']
    form_class = MyForm
    success_url = '/'
    login_url = '/login/'
```

Теперь нельзя попась на страницу обрабатываемую этим классом, если пользователь не залогинен. В случае если он не залогинен, он будет перекинут на страницу указанную в атрибуте `login_url`.

Практика:

Пишем страницу логина и логаута

# Домашнее задание:

Прочитать все ссылки из лекции!!! Буду спрашивать.

1. Переписать страницы логина и логаута на класс бейз вью, подсказка [Тут](https://ccbv.co.uk/projects/Django/2.2/django.contrib.auth.views/LoginView/)

2. Написать страницу с гет формой, для поиска по тексту ваших коментариев, отобразить все найденные частичные совпадение, без учёта регистра.

3. Написать базовую страницу регистрации. (для назначения пароля используйте метод `set_password()`)

3.1 Страница для изменения пароля.  Подсказка  [Тут](https://ccbv.co.uk/projects/Django/2.2/django.contrib.auth.views/PasswordChangeView/)

4. Написать страницу добавления коментария (форма и пост запрос). Без вложенности, и возможности коментировать коментарий. (Пока)

5. Изменить поиск по коментариям, добавить галочку, что бы искать только по своим коментариям (отображать только для залогиненных пользователей))