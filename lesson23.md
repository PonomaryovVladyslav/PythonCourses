# Лекция 23. Forms, ModelForms. User, Authentication.

![](https://img-9gag-fun.9cache.com/photo/aV3wWMd_460s.jpg)

## Что сегодня учим?

![mvc_forms.png](pictures/mvc_forms.png)

## HTML формы

`HTML форма` - это специальный тег, который "сообщает" браузеру, что данные из этого тега нужно сгруппировать и
подготовить
к отправке на сервер.

Принимает два параметра `action` и `method`.

`action` описывает, куда форма по результату должна обращаться (в нашем случае это будет `url`), если не указан явно, то
форма будет отправлена на тот же урл, на котором сейчас находится.

`method` отвечает за метод отправки, варианты - `get` и `post`. `get` будет использован по умолчанию, если не указан
явно.

Формы с методом `POST` используются для передачи данных, не подлежащих огласке, например, логин и пароль.
Формы с методом `GET` используются для общедоступной информации, например, строки поиска.

Внутри формы мы указываем нужное количество тегов `<input>` с нужными типами. Именно эти данные будут впоследствии
переданы
серверу.

[Ссылка на общее описание форм](https://www.w3schools.com/html/html_forms.asp)

#### Основные типы инпутов

**number** - ввод числа

**text** - ввод текста

**checkbox** - чекбокс (выбор нескольких элементов через галочки)

**radio** - радиобаттон (выбор только одного элемента из списка)

**button** - классическая кнопка (если в форме есть один такой элемент, но нет сабмита, браузер автоматически посчитает
его сабмитом)

**hidden** - скрытое поле, чаще всего нужно для целей безопасности или добавления информации и данных, не отображая их
(не отображается)

**submit** - отправка формы

Это далеко не все типы инпутов, которые могут быть.
[Ссылка на типы инпутов](https://www.w3schools.com/html/html_form_input_types.asp)

## GET форма

Создадим простейшую форму. Для этого создадим url, функцию для обработки и HTML страницу.

В urls.py

```python
...
from .views import form_view

...

...
path('form-url/', form_view, name='form-view'),
...
```

Во views.py

```python
def form_view(request):
    return render(request, 'form.html')
```

В form.html

```html
{% extends 'base.html' %}

{% block content %}
<form method="get" action="{% url 'form-view' %}">
    <label>
        <input type="text" name="my_name">
    </label>
    <button type="submit">Send name</button>
</form>
{% endblock %}
```

Обратите внимание, мы указали `GET` форму, `action` - урл на эту же страницу, который обрабатывается нашей же
функцией `form_view`.

В форме у нас один `input`, которому мы указали 2 атрибута `type` и `name`.

Атрибут `name` нам необходим для того, чтобы мы смогли обработать данные во view.

Также у нас есть кнопка `submit`, она необходима для того, чтобы отправить запрос на сервер.

При нажатии на кнопку формируется и отправляется request.

Примерно вот так будет выглядеть наша страница если зайти на адрес http://127.0.0.1:8000/form-url/:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson32/clean_get_form.png)

### request

Объект `request` мы принимаем первым параметром функции обработчика и его же передаём первым в
функцию `render`. Зачем он нужен и из чего он состоит?

#### Зачем нужен?

Чтобы обрабатывать любые пользовательские или служебные данные, которые были переданы.

#### Из чего состоит?

Состоит из переданных данных или файлов (если были переданы) и служебной информации (информации о
пользователе, методе запроса, о том, на какой url был запрос, из какого браузера, другой системной информации).

### Идемпотентность

![](http://risovach.ru/upload/2015/12/mem/kot-bezyshodnost_100253424_orig_.jpg)

HTTP-запрос идемпотентен тогда, когда клиенты могут делать один и тот
же вызов неоднократно при одном и том же результате на сервере. Другими словами, создание большого количества идентичных
запросов имеет такой же эффект, как и один запрос. Заметьте, что в то время, как идемпотентные операции производят один
и тот же результат на сервере, ответ сам по себе может не быть тем же самым (например, состояние ресурса может
измениться между запросами).

Методы GET, HEAD, OPTIONS и TRACE определены как безопасные. Это означает, что они предназначены только для получения
информации и не должны изменять состояние сервера. Они не должны иметь побочных эффектов, за исключением безобидных
эффектов таких как: логирование, кеширование, показ баннерной рекламы или увеличение веб-счетчика.

По определению, безопасные операции идемпотентны, так как они приводят к одному и тому же результату на сервере.
Безопасные методы реализованы как операции только для чтения. Однако безопасность не означает, что сервер должен
возвращать тот же самый результат каждый раз.

> Пока мы рассматриваем только GET и POST. GET - идемпотентен, POST - нет.

### Давайте отправим request

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson32/filled_get_form.png)

Что будет после нажатия кнопки `Send name`?

Будет сформирован `GET` (метод формы) запрос со всеми заполненными нами данными и отправлен на сервер.

Обратите внимание на новый url.

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson32/data_get_form.png)

`my_name` - это предварительно указанный атрибут `name` на нашей форме, а `Vlad` - значение, которое я передал в этот
инпут.

В случае `GET` запроса данные передаются явно, прям в url в виде ключ-значение. Если бы значений было больше одного,
они были бы соединены при помощи символа `&` (например, если бы я добавил к полю с указанным атрибутом `name` еще и поле
с атрибутом `age` и заполнил бы его значением 26, то url после запроса выглядел бы
так `/form-url/?my_name=Vlad&age=26`).
Никакой разницы между заполнением формы или записью этих данных руками прям в строке браузера для `GET` запроса нет.

### Обработка данных во view

Мы можем обработать данные во `view` при помощи переменной `request`. Данные из `GET` запроса будут находиться в
переменной `request.GET`

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson32/get_request_view.png)

Данные находятся в виде словаря, где ключами являются атрибуты `name` в каждом инпуте формы.

Эти данные можно использовать для любых целей, но чаще всего через `GET` передаются данные по фильтрации или
дополнительные параметры отображения. Например, когда вы добавляете фильтры в интернет магазине, пишете текст в поиске,
или когда на YouTube пересылаете ссылку с таймкодом, она тоже передаётся как `GET` параметр.

## POST запрос

Давайте заменим метод нашей формы с `GET` на `POST`:

В `form.html`:

```html
{% extends 'base.html' %}

{% block content %}
<form method="post" action="{% url 'form-view' %}">{# Тут я поменял метод #}
    <label>
        <input type="text" name="my_name">
    </label>
    <button type="submit">Send name</button>
</form>
{% endblock %}
```

Что произойдёт при отправке такого запроса?

Произойдёт примерно такая ошибка:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson32/csrf_failure.png)

Это ошибка CSRF токена.

Чтобы понять, что это, нужно понимать разницу того, где используются разные запросы.

`GET` запросы - это запросы общедоступные и информационные: открыть страницу, отфильтровать данные и т. д.

`POST` запросы - это запросы с чувствительными данными: создание записей в базе, передача пароля, отправка денег со
счёта на счёт и т. д.

Так вот, если `GET` запрос отправить 5 раз подряд, то с точки зрения сервера ничего не изменится, вы просто 5 раз подряд
запросите одну и туже информацию.

Если изменить параметры, то тоже ничего страшного не произойдёт, просто запросятся другие данные.

А вот если повторить несколько раз или подделать данные в `POST` запросе, то можно совершить разные проблемные действия:
создание лишних записей в базе данных, перевод средств на счёт злоумышленников вместо ожидаемого и т. д.

Поэтому в Django изначально есть дополнительное требование к `POST` формам - это еще одно скрытое поле, заранее
сгенерированное сервером. Оно называется `CSRF токен`, где он проверяется и почему мы видим ошибку, мы разберём на
следующих занятиях.

Чтобы добавить нужный токен, используется специальный темплейт тег `{% csrf_token %}`. Его нужно добавить в
любом месте внутри тега `<form>`.

```html
{% extends 'base.html' %}

{% block content %}
<form method="post" action="{% url 'form-view' %}">
    {% csrf_token %}{# Тут я добавил темплейт тег #}
    <label>
        <input type="text" name="my_name">
    </label>
    {# А мог и тут #}
    <button type="submit">Send name</button>
    {# Или тут, не имеет значения #}
</form>
{% endblock %}
```

Что изменится с точки зрения `HTML`:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson32/csrf_html.png)

Появилось поле типа `hidden`. Это значит, что оно не будет отображаться, но эти данные все равно попадут на сервер. Это
часто используется, когда вам нужно передать данные, которые у вас уже есть при отрисовке, но их не видно явно.
Допустим,
если мы пишем комментарий к комментарию, то чтобы грамотно его создать, нам нужен `id` родителя, его обычно и передают
как `hidden` поле.

Теперь наш запрос отправится успешно.

Обратите внимание, что url не изменится!

Потому что данные отправленные через `POST` не должны быть общедоступны.

### Обработка во view

Обработать данные из `POST` запроса можно точно также, данные будут находиться в переменной `request.POST`, если это
просто данные, и в `request.FILES`, если были переданы файлы.

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson32/post_request_view.png)

Обратите внимание, что вместе с нашими данными был передан и `csrf` токен. Обычно при обработке данных он не нужен, но
данные были переданы, а значит они придут на сервер.

## Django Forms

Django предоставляет нам возможность генерировать `HTML` формы из кода на Python!

Что для этого нужно? Создадим в нашем приложении файл `forms.py`

Внутри этого файла укажем:

`forms.py`

```python
from django import forms


class MyForm(forms.Form):
    nickname = forms.CharField(label='My nickname', max_length=100)
    age = forms.IntegerField(label='My age')
```

Обработчик для урла заменим на:

Во views.py заменим нашу функцию на:

```python
from django.shortcuts import render

from .forms import MyForm


def form_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # some actions
            return render(request, 'form_was_valid.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MyForm()

    return render(request, 'form.html', {'form': form})
```

**Не забываем импортировать форму**

Изменим файл `form.html`:

```html
{% extends 'base.html' %}

{% block content %}
<form method="post" action="{% url 'form-view' %}">
    {% csrf_token %}
    {{ form }} {# Инпуты были заменены на переменную, в которой лежит объект класса Form #}
    <button type="submit">Send form</button>
</form>
{% endblock %}
```

и создадим файл `form_was_valid.html`:

```html
{% extends 'base.html' %}

{% block content %}
<div style="background-color: deeppink"> FORM WAS VALID</div>
<a href="{% url 'form-view' %}">To the form page</a>
{% endblock %}
```

Что именно мы сделали?

### Описание формы

В файле `forms.py` мы создали класс формы, в котором описали два атрибута `nickname` и `age`.

Они будут соответствовать двум инпутам, текстовому и числовому.

Естественно, типов существует гораздо больше.

Основные типы:

- `BooleanField` - булево значение

- `CharField` - текст

- `ChoiceField` - поле для выбора

- `DateTimeField` - дата/время

- `EmailField` - имейл

- `FileField` - файл

- `IntegerField` - целое число

- `MultipleChoiceField` - множественный выбор

И многие другие, почитать про них нужно [тут](https://docs.djangoproject.com/en/stable/ref/forms/fields/#built-in-field-classes)

#### Виджет

У полей формы есть такое понятие как виджет. Он отвечает за то, как именно будет отображаться конкретное поле, например,
для текста - это текстовое поле, а для даты и времени - это встроенный пикер (выпадающее окно с календарём и часами)
и т. д.

Виджет можно указать отличающийся от стандартного.

Прочитать про виджеты нужно [тут](https://docs.djangoproject.com/en/stable/ref/forms/widgets/#built-in-widgets).

Каждому полю мы можем указать дополнительные атрибуты:

`required` - является ли поле обязательным

`label`- лейбл, подпись к инпуту

`label_suffix` - символ между `label` и инпутом

`initial` - значение по умолчанию

`widget` - читай выше

`help_text` - подсказка к инпуту

`error_messages` - переписать стандартные тексты для ошибок типов полей

`validators` - дополнительные проверки поля

`localize` - информация о переводе формы на другие языки

`disabled` - сделать поле не активным (без возможности изменения)

### Описание view

В переменной `request` хранится информация о том, какой именно тип запроса к нам пришел, а это значит, что простым if мы
можем разграничить логику, которая будет обрабатывать разные типы запросов.

Если мы просто открываем страницу в браузере, то на самом деле мы посылаем обыкновенный `GET` запрос.

Взглянем на код. При `GET` запросе мы не попадаем в первое условие, переменной `form` назначаем объект класса `MyForm`
без каких-либо данных, и после этого рендерим страницу, передав на страницу пустой объект класса формы.

При рендере объекта класса формы в шаблоне этот объект преобразуется в набор инпутов с уже указанными
атрибутами `name`

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson32/django_form_get.png)

Если мы заполним данные и нажмём на кнопку `Send form`, то мы отправим по этому же url запрос, но уже типа `POST` с
заполненными данными.

Посмотрим в код еще раз, мы попадём в первый if и переменной `form` назначим объект класса `MyForm`, но предварительно
передав туда данные через `request.POST`.

А значит на этом этапе у нас есть объект с данными, переданными нам от клиента.

> Данные, которые мы получили из реквеста, всегда нужно валидировать (проверять).

## Валидация формы

[Тут](https://docs.djangoproject.com/en/stable/ref/forms/validation/) вся дока по валидации.

За валидацию данных в форме отвечает встроенный метод `is_valid()` который применяется к объекту класса формы.

Этот метод возвращает нам булево значение: `True`, если данные валидны, `False`, если нет.

После вызова этого метода у переменной, к которой он был вызван (в нашем случае переменная `form`), появляются
дополнительные атрибуты.

Если форма валидна, то появляется дополнительный атрибут `cleaned_data` - это словарь, в котором хранятся все
данные, присланные нам пользователем (например, логин и пароль).

Если форма не валидна, то появляется дополнительный атрибут `errors`, который хранит в себе информацию об ошибках
конкретных полей или общих ошибках.

Этот атрибут сразу хранит информацию о том, как отображать эти ошибки в шаблоне, если они существуют.

### Валидность

Что же такое валидность?

Валидность - это соответствие заданным критериям. Например, если мы ожидаем в поле возраста получить числовой тип, а
пользователь отправляет текст, то данные не валидны.

Некоторые распространённые виды валидаций можно указать как атрибут поля формы, например, максимальную длину для
строки, максимальное и минимальное значение для числа.

#### clean_`field`()

Если мы вызываем метод `is_valid()`, мы проверяем все описанные валидации. Но где они описаны, и можем ли мы добавить
свои?

Описаны они в классе формы, и да, мы можем добавить свои.

Все базовые валидации были описаны при создании полей.

Но допустим, что мы считаем, что для нашей формы валидным является только чётный возраст, как нам это проверить?

Для проверки конкретного поля в форме класса нужно указать метод, который будет начинаться со слова `clean_` и после
этого название поля, которое мы валидируем.

Все данные будут лежать в атрибуте `self.cleaned_data`.

Если значение валидно, то метод должен возвращать значение этого атрибута.

Если значение не валидно, то метод должен возбуждать ошибку `ValidationError` с описанием ошибки, которая позже будет
отображаться в `html`.

В forms.py:

```python
from django import forms
from django.core.exceptions import ValidationError


class MyForm(forms.Form):
    nickname = forms.CharField(label='My nickname', max_length=100)
    age = forms.IntegerField(label='My age')

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age % 2:
            raise ValidationError('Age should be even.')
        return age
```

#### clean()

А что делать если нужно проверить соответствие данных между собой? Например, что пользователь не использовал свой
возраст, как часть своего никнейма?

Для этого мы можем использовать метод `clean()`, в котором можем выполнить все необходимые нам проверки.

Для выполнения всех базовых проверок обычно используется `super()`.

В forms.py

```python
from django import forms
from django.core.exceptions import ValidationError


class MyForm(forms.Form):
    nickname = forms.CharField(label='My nickname', max_length=100)
    age = forms.IntegerField(label='My age')

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age % 2:
            raise ValidationError('Age should be even.')
        return age

    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data.get('age')
        nickname = cleaned_data.get('nickname')
        if str(age) in nickname:
            raise ValidationError('Age can\'t be in nickname')
        return cleaned_data
```

Если при проверке у вас может быть больше одной ошибки, то `raise` вам не подходит.

#### add_error

Для этого может использоваться метод класса формы `add_error()`. Он принимает два параметра: название поля, к которому
относится ошибка (может быть None, если ошибка не относится к какому-либо полю), и сообщение, например, неправильные
имя пользователя и/или пароль.

В forms.py

```python
from django import forms
from django.core.exceptions import ValidationError


class MyForm(forms.Form):
    nickname = forms.CharField(label='My nickname', max_length=100)
    age = forms.IntegerField(label='My age')

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age % 2:
            raise ValidationError('Age should be even')
        return age

    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data.get('age')
        nickname = cleaned_data.get('nickname')
        if str(age) in nickname:
            self.add_error('age', 'Age can\'t be in nickname')
        self.add_error(None, 'This form is always incorrect')
```

### Отображение формы в шаблоне

Итак, если наша форма была валидна, то мы отрендерили вообще другую страницу, но если всё-таки была не валидна, то мы
отрендерим форму, у которой есть атрибут `errors`, ошибки сразу же будут отрисованы.

Также у нас есть способы по-разному отрисовывать формы:

У объекта формы есть стандартные поля и методы, которые мы можем указывать в шаблоне, например:

`{{ form.as_table }}` - рендер в виде таблицы, через теги <tr>

`{{ form.as_p }}` - рендер каждого поля через теги <p>

`{{ form.as_ul }}` - рендер в виде списка через теги <li>

Также можно рендерить форму не целиком, а, например, по отдельным полям, при помощи стандартного обращения через
точку: `{{ form.name }}`.

У каждого поля есть атрибут `errors`, который хранит информацию об ошибках по этому полю, если они были
обнаружены: `{{ form.my_field.errors }}`.

Если запустить форму через `for` в итерируемом объекте будут поля.

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

И многие другие атрибуты и методы, подробно можно прочитать [тут](https://docs.djangoproject.com/en/stable/topics/forms/#working-with-form-templates)

### Про отправку файлов

Нужно в шаблоне добавить атрибут `enctype="multipart/form-data"` к тегу `<form>`, чтобы форма могла отправлять файлы:

```html
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
</form>
```

### Про отображение медиа файлов

Если вы хотите впоследствии отображать медиафайлы (например, аватар пользователя), необходимо использовать следующий синтаксис

```html
<img src="{{ user.profile.avatar.url }}" alt="Avatar">
```

Здесь `avatar.url` возвращает полный путь к файлу, который был загружен.

## ModelForm

Дока [Тут](https://docs.djangoproject.com/en/stable/topics/forms/modelforms/)

ModelForm - это тип формы, который генерируется напрямую из модели. Это очень мощный инструмент работы с моделями.

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

Поле `fields` или поле `exclude` являются обязательными.

Такой вид форм эквивалентен обычной форме с объявлением всех полей:

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

Помимо стандартного метода `is_valid()` у ModelForm существует также встроенный метод `full_clean()`

Если первый отвечает за валидацию формы, то второй отвечает за валидацию для объекта модели.

### Метод save() у формы

Метод `save()` в ModelForm объекте выполняет по сути два действия: получает объект модели, основываясь на переданных
данных, и вызывает метод `save()`, но уже для модели.

Метод `save()` может принимать аргумент `commit`, по умолчанию - `True`. Если указать `commit=False`, метод `save()`
модели не будет вызван (объект не будет сохранён в базу), будет только создан предварительный объект модели. Такой
подход используется, когда нужно "дополнить" данные перед сохранением в базу. Очень часто используется! Например,
добавление пользователя из `request`.

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

По аналогии, мы можем не только создавать новый объект, но и обновлять существующий.

## Модель User

### Стандартная модель пользователя в Django

По умолчанию Django предоставляет модель пользователя, которая определена в модуле `django.contrib.auth`. Эта модель
называется `User` и она уже содержит большинство необходимых полей для работы с пользователями:

- **Username**: уникальное имя пользователя.
- **Password**: хэшированный пароль.
- **Email**: электронная почта (необязательное поле).
- **First name и Last name**: имя и фамилия.
- **is_active**: флаг, который указывает, активен ли пользователь.
- **is_staff**: флаг, который определяет, является ли пользователь частью административного персонала.
- **is_superuser**: флаг, который определяет, является ли пользователь суперпользователем (администратором с полными
  правами).
- **last_login**: время последнего входа.
- **date_joined**: дата регистрации.

Эти поля покрывают базовые потребности большинства приложений. Django также предоставляет систему аутентификации,
включающую в себя:

- Вход в систему и выход из нее.
- Восстановление пароля.
- Регистрацию нового пользователя.
- Поддержку групп и разрешений.

### Про пароли

В современном мире безопасность данных становится всё более актуальной задачей, особенно когда речь идёт о хранении
паролей пользователей. Одним из основных способов обеспечения безопасности паролей является их хеширование и
использование соли. В этой лекции мы рассмотрим, как хранятся пароли, зачем нужно хеширование и что такое соль.

#### Зачем хранить пароли безопасно?

Когда пользователь регистрируется на сайте, он создаёт уникальный пароль для доступа к своей учётной записи. Если пароли
будут храниться в базе данных в открытом виде (plaintext), то при взломе базы данных злоумышленник получит доступ ко
всем паролям пользователей. Это ставит под угрозу не только одну систему, но и другие учётные записи, поскольку многие
пользователи склонны использовать один и тот же пароль на разных сервисах.

#### Хеширование паролей

**Хеширование** — это процесс преобразования строки данных (например, пароля) в фиксированную длину строку, которая
является уникальной для каждого исходного набора данных. Важной особенностью хеширования является то, что этот процесс
необратим: невозможно получить исходный пароль из его хеша.

Самый простой способ защитить пароли — это хранить их в виде хешей. Например, если пользователь вводит пароль "
password123", и он проходит через хеш-функцию, то результатом будет хеш, например, "ef92b778ba2231b9e28d9d...". При
каждом входе в систему пароль пользователя хешируется, и этот хеш сравнивается с хешем, хранящимся в базе данных.

**Примеры хеш-функций**:

- MD5 (считается устаревшим и небезопасным)
- SHA-1 (тоже устаревший и небезопасный)
- SHA-256
- bcrypt, scrypt, Argon2 (предназначены специально для хеширования паролей)

#### Зачем нужна соль?

Несмотря на то, что хеширование защищает пароли, оно не полностью защищает от атак по словарю и атак с помощью радужных
таблиц. Радужные таблицы представляют собой предварительно вычисленные таблицы паролей и их хешей. Если злоумышленник
знает хеш, он может легко найти исходный пароль, если этот пароль слабый или популярный.

**Соль** — это случайная строка, которая добавляется к паролю перед его хешированием. Например, если пользовательский
пароль — "password123", и к нему добавляется соль "xyz123", результатом будет хеш от "password123xyz123". Таким образом,
даже если два пользователя используют одинаковые пароли, их хеши будут разными благодаря уникальным солям.

Соль должна быть уникальной для каждого пользователя и храниться в базе данных вместе с хешем пароля. При проверке
пароля система извлекает соль, добавляет её к введённому паролю, и затем сравнивает полученный хеш с хешем, хранящимся в
базе данных.

**Пример**:

- Пароль: "password123"
- Соль: "xyz123"
- Хеш: "a1b2c3d4..."

> Все эти действия django делает за нас. Но мы должны помнить об этом, потому что иначе мы не сможем нормально
> пользоваться встроенными методами.

### Методы юзера

```python
get_username()  # получить юзернейм

get_full_name()  # получить имя и фамилию через пробел

set_password(raw_password)  # установить хешированный пароль

check_password(raw_password)  # проверить пароль на правильность

set_unusable_password()  # сделать пароль непригодным для аутентификации

email_user(subject, message, from_email=None, **kwargs)  # отправить пользователю имейл
```

Например:

```python
u = User.objects.get(username='blabla')
u.check_password('some_cool_password')  # True
```

> Пароль хеширован, мы не можем сравнить его напрямую

И другие методы, отвечающие за доступы, группы и т. д.

### Базовый менеджер юзера

Содержит дополнительные методы

`create_user(username, email=None, password=None, **extra_fields)`

`create_superuser(username, email, password, **extra_fields)`

`create_user()` отличается от `create()` тем, что `create_user()` правильно задаст пароль через `set_password()`

### Когда и зачем нужно создавать кастомную модель пользователя

Однако стандартная модель `User` может не удовлетворять всем требованиям конкретного проекта. Например, вам может
понадобиться:

- Добавить дополнительные поля (например, номер телефона, дата рождения, аватар).
- Изменить логику аутентификации (например, использовать email вместо username).
- Подключить несколько моделей пользователей для разных типов пользователей (например, клиенты и поставщики услуг).

В таких случаях Django позволяет создать кастомную модель пользователя. Это лучше сделать на ранних этапах разработки
проекта, так как изменение модели пользователя в уже работающем приложении может вызвать сложности.

### Создание кастомной модели пользователя

Чтобы создать свою модель пользователя, выполните следующие шаги:

Для использования модели пользователя, которую нам нужно расширить (а это нужно почти всегда), используется наследование
от базового абстрактного юзера.

Выглядит примерно так:

```python
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    birth_date = models.DateField()
    avatar = models.ImageField(blank=True, null=True)
```

Чтобы Django оценивала эту модель как пользователя в `settings.py` нужно в любом месте указать:

```python
AUTH_USER_MODEL = 'myapp.User'
```

Где `myapp` - название приложения, `User` - название модели.

Юзер `обязательно` должен быть описан до первой миграции!! Иначе Django автоматически будет использовать базового
встроенного юзера, и использовать сразу несколько юзеров у вас не получится. Так как по дефолту, если этой переменной
нет, то Django считает, что там указана ссылка на базового юзера, и создаёт таблицу юзера, основываясь на базовом
юзере, поменять такую таблицу нельзя.

Все возможные подробности про модель юзера [тут](https://docs.djangoproject.com/en/stable/ref/contrib/auth/#django.contrib.auth.models.User)

### Пример более детальной кастомизации

Вместо использования стандартной модели `User`, вы можете создать свою модель, унаследовав ее от `AbstractBaseUser`
и `PermissionsMixin`. Это позволит вам кастомизировать поля и методы, сохраняя при этом функциональность, связанную с
аутентификацией и авторизацией.

Пример кастомной модели пользователя:

```python
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
```

> Создание кастомной модели пользователя может потребовать дополнительных усилий, но оно того стоит, если вам нужно
> больше
> гибкости и контроля над поведением пользователей в вашем приложении.

## Логин

На самом деле логин состоит из нескольких частей, давайте их рассмотрим.

### Аутентификация, идентификация, авторизация

Аутентификация - процесс проверки подлинности доступа.

Например, проверить логин и пароль на соответствие.

Если говорить о бытовом примере, то когда вы проходите на любую проходную, например, заходя в университет, вы должны
предъявить студенческий. То, что он у вас есть и есть процесс аутентификации.

Идентификация - процесс определения конкретного лица.

Например, получить конкретного пользователя из базы.

В примере с университетом, если охранник возьмет ваш студенческий и прочитает, как вас зовут и из какой вы группы, это и
будет идентификация.

Авторизация - процесс предоставления доступа.

Охранник вас пропустит.

### Как это работает?

Чтобы пользователь мог авторизоваться на сайте, нам нужны его входные данные и стандартные методы `authenticate, login`

Метод `authenticate` отвечает сразу за два процесса: аутентификацию и идентификацию. Он принимает имя пользователя и
пароль, и если находит совпадение, то возвращает объект пользователя(модели), если не находит, то возвращает `None`.

Если нам вернулся объект юзера, значит, аутентификация пройдена, и пользователь идентифицирован.

Метод `login` принимает реквест и объект модели пользователя и отвечает за процесс авторизации, после этого действия
во всех следующих запросах в переменной `request` будет храниться наш текущий пользователь.

Поэтому стандартным способом авторизации является примерно такой код:

В forms.py

```python
from django.contrib.auth import authenticate
from django import forms
from django.utils.translation import gettext as _



class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError("Incorrect username/password")
```

в view.py

```python
from .forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect



def my_login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AuthenticationForm(request.POST)
        # check validity:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # some actions
            login(request, form.user)
            return redirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
```

### Logout

Для вывода пользователя из системы используется метод `logout`, который принимает только реквест.

```python
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    # Redirect to a success page.
```

### Проверка на то, что пользователь уже зашел в систему

В реквесте всегда есть поле `user`, у которого всегда есть атрибут `is_authenticated`; проверяя его, мы можем
определять, аутентифицирован ли пользователь.

```python
request.user.is_authenticated
```

## Управление доступом

В этой лекции мы рассмотрим два часто используемых декоратора: `login_required` и `user_passes_test`.

### Декоратор `login_required`

Декоратор `login_required` используется для ограничения доступа к представлениям для неавторизованных пользователей.
Если пользователь не авторизован, он будет перенаправлен на страницу входа в систему.

#### Пример использования

Предположим, у нас есть представление, которое отображает профиль пользователя:

```python
from django.shortcuts import render


def profile_view(request):
    return render(request, 'profile.html')
```

Это представление доступно для всех пользователей, независимо от того, авторизованы они или нет. Чтобы ограничить доступ
только для авторизованных пользователей, мы можем использовать декоратор `login_required`:

```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def profile_view(request):
    return render(request, 'profile.html')
```

Теперь, если неавторизованный пользователь попытается получить доступ к этому представлению, он будет перенаправлен на
страницу входа.

### Настройка URL перенаправления

По умолчанию, декоратор `login_required` перенаправляет пользователей на URL, указанный в настройке `LOGIN_URL`. Вы
можете настроить его следующим образом в файле `settings.py`:

```python
LOGIN_URL = '/login/'
```

Если вы хотите использовать другой URL для конкретного представления, вы можете указать его прямо в декораторе:

```python
@login_required(login_url='/custom-login/')
def profile_view(request):
    return render(request, 'profile.html')
```

### Декоратор `user_passes_test`

Декоратор `user_passes_test` предоставляет более гибкий способ управления доступом к представлениям, позволяя проверять
различные условия. Он принимает функцию, которая проверяет условия, и только если эта функция возвращает `True`, доступ
к представлению будет разрешен.

#### Пример использования

Рассмотрим пример, когда только пользователи, имеющие адрес электронной почты на определенном домене, могут получить
доступ к представлению:

```python
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


def email_check(user):
    return user.email.endswith('@example.com')


@user_passes_test(email_check)
def special_view(request):
    return render(request, 'special.html')
```

В этом примере функция `email_check` проверяет, заканчивается ли адрес электронной почты пользователя на '@example.com'.
Если это так, пользователь получит доступ к представлению `special_view`.

#### Перенаправление при отказе в доступе

Если проверка не пройдена, пользователь будет перенаправлен на страницу входа по умолчанию. Однако вы можете указать
другую страницу для перенаправления, используя параметр `login_url`:

```python
@user_passes_test(email_check, login_url='/no-access/')
def special_view(request):
    return render(request, 'special.html')
```

#### Комбинирование с `login_required`

Часто `user_passes_test` используется в комбинации с `login_required`, чтобы сначала убедиться, что пользователь
авторизован, а затем проверить дополнительные условия:

```python
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
@user_passes_test(email_check)
def special_view(request):
    return render(request, 'special.html')
```
