# Урок 19. Декораторы. Декораторы с параметрами. Декораторы классов (staticmethod, classmethod, property)

![](https://tirinox.ru/wp-content/uploads/2019/10/risovach.ru_.jpg)

## Что такое декоратор

Итак, что же такое «декоратор»?

Функции в Python'e являются объектами

Для того чтобы понять, как работают декораторы, в первую очередь следует осознать, что в Python'е функции — это тоже 
объекты.

Давайте посмотрим, что из этого следует:

```python
def shout(word="Yes"):
    return word.capitalize()+"!"
 
print(shout())
# выведет: 'Yes!'
 
# Так как функция - это объект, вы можете связать её с переменной,
# как и любой другой объект
scream = shout
 
# Заметьте, что мы не используем скобок: мы НЕ вызываем функцию "shout",
# мы связываем её с переменной "scream". Это означает, что теперь мы
# можем вызывать "shout" через "scream":
 
print(scream())
# выведет: 'Yes!'

# Более того, это значит, что мы можем удалить "shout", и функция всё ещё
# будет доступна через переменную "scream"
 
del shout
try:
    print(shout())
except NameError, e:
    print (e)
    #выведет: "name 'shout' is not defined"
 
print (scream())
# выведет: 'Yes!'

```

Запомним этот факт, скоро мы к нему вернёмся, но кроме того стоит понимать, что функция в Python'e может быть 
определена… внутри другой функции!

```python
def talk():
    # Внутри определения функции "talk" мы можем определить другую...
    def whisper(word="yes"):
        return word.lower()+"..."
 
    # ... и сразу же её использовать!
    print (whisper())

# Теперь, КАЖДЫЙ РАЗ при вызове "talk" внутри неё определяется, а затем
# и вызывается функция "whisper".
talk()
# выведет: "yes..."
 
# Но вне функции "talk" НЕ существует никакой функции "whisper":
try:
    print whisper()
except NameError, e:
    print e
    #выведет : "name 'whisper' is not defined"
```

### Ссылки на функции

Теперь мы знаем, что функции являются полноправными объектами, а значит:

- могут быть связаны с переменной;
- могут быть определены одна внутри другой.

Что ж, а это значит, что одна функция может вернуть другую функцию!

Давайте посмотрим:

```python
def get_talk(type="shout"):
 
    # Мы определяем функции прямо здесь
    def shout(word="Yes"):
        return word.capitalize()+"!"
 
    def whisper(word="yes") :
        return word.lower()+"..."
 
    # Затем возвращаем необходимую
    if type == "shout":
        # Заметьте, что мы НЕ используем "()", нам нужно не вызвать функцию,
        # а вернуть объект функции
        return shout
    else:
        return whisper
 
# Как использовать это непонятное нечто?
# Возьмём функцию и свяжем её с переменной
talk = get_talk()
 
# Как мы можем видеть, теперь "talk" - объект "function":
print(talk)
# выведет: <function shout at 0xb7ea817c>
 
# Который можно вызывать, как и функцию, определённую "обычным образом":
print(talk())
 
# Если нам захочется, можно вызвать её напрямую из возвращаемого значения:
print(get_talk("whisper")())
# выведет: yes...

```
Подождите, раз мы можем возвращать функцию, значит, мы можем и передавать её другой функции как параметр:

```python
def do_something_before(func):
    print("Я делаю что-то ещё перед тем, как вызвать функцию, которую ты мне передал")
    print(func())
 
do_something_before(scream)

# выведет:
# Я делаю что-то ещё перед тем, как вызвать функцию, которую ты мне передал
# Yes!
```

Ну что, теперь у нас есть все необходимые знания для того, чтобы понять, как работают декораторы.

Как можно догадаться, декораторы — это просто своеобразные «обёртки», которые дают нам возможность делать 
что-либо до и после того, как декорируемая функция что-то сделает, не изменяя её.

Создадим свой декоратор «вручную»:

```python

# Декоратор - это функция, ожидающая ДРУГУЮ функцию в качестве параметра
def my_shiny_new_decorator(a_function_to_decorate):
    # Внутри себя декоратор определяет функцию-"обёртку".
    # Она будет (что бы вы думали?..) обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.

    def the_wrapper_around_the_original_function():
        # Поместим здесь код, который мы хотим запускать ДО вызова
        # оригинальной функции
        print("Я - код, который отработает до вызова функции")
 
        # ВЫЗОВЕМ саму декорируемую функцию
        a_function_to_decorate()

        # А здесь поместим код, который мы хотим запускать ПОСЛЕ вызова
        # оригинальной функции
        print("А я - код, срабатывающий после")

    # На данный момент функция "a_function_to_decorate" НЕ ВЫЗЫВАЛАСЬ НИ РАЗУ

    # Теперь, вернём функцию-обёртку, которая содержит в себе
    # декорируемую функцию, и код, который необходимо выполнить до и после.
    # Всё просто!
    return the_wrapper_around_the_original_function

# Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.
def a_stand_alone_function():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?..")
 
a_stand_alone_function()
# выведет: Я простая одинокая функция, ты ведь не посмеешь меня изменять?..
 
# Однако, чтобы изменить её поведение, мы можем декорировать её, то есть
# просто передать декоратору, который обернет исходную функцию в любой код,
# который нам потребуется, и вернёт новую, готовую к использованию функцию:
 
a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function_decorated()
#выведет:
# Я - код, который отработает до вызова функции
# Я простая одинокая функция, ты ведь не посмеешь меня изменять?..
# А я - код, срабатывающий после

# Наверное, теперь мы бы хотели, чтобы каждый раз, во время вызова a_stand_alone_function, вместо неё 
# вызывалась a_stand_alone_function_decorated. Нет ничего проще, просто перезапишем a_stand_alone_function 
# функцией, которую нам вернул my_shiny_new_decorator:
a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function()
# выведет:
# Я - код, который отработает до вызова функции
# Я простая одинокая функция, ты ведь не посмеешь меня изменять?..
# А я - код, срабатывающий после

```

Этот же синтаксис можно реализовать через @декораторы.:)

Разрушаем ореол таинственности вокруг декораторов.

Вот так можно было записать предыдущий пример, используя синтаксис декораторов:

```python
@my_shiny_new_decorator
def another_stand_alone_function():
    print("Оставь меня в покое")
 
another_stand_alone_function()
# выведет:
# Я - код, который отработает до вызова функции
# Оставь меня в покое
# А я - код, срабатывающий после
```

Да, всё действительно так просто! Декоратор — просто синтаксический сахар для конструкций вида:
```python
another_stand_alone_function = my_shiny_new_decorator(another_stand_alone_function)
```

Декораторы — это просто питоническая реализация паттерна проектирования «Декоратор». В Python включены некоторые 
классические паттерны проектирования, такие как рассматриваемые в этой статье декораторы, или привычные любому 
пайтонисту итераторы.

Конечно, можно вкладывать декораторы друг в друга, например так:

```python
def bread(func):
    def wrapper():
        print("</------\>")
        func()
        print("<\______/>")
    return wrapper
 
def ingredients(func):
    def wrapper():
        print("#tomatoes#")
        func()
        print("~lettuce~")
    return wrapper
 
def sandwich(food="--ham--"):
    print(food)
 
sandwich()
# выведет: --ham--
sandwich = bread(ingredients(sandwich))
sandwich()
# выведет:
# </------\>
# #tomatoes#
# --ham--
# ~lettuce~
# <\______/>
```
И используя синтаксис декораторов:

```python
@bread
@ingredients
def sandwich(food="--ham--"):
    print(food)
 
sandwich()
# выведет:
# </------\>
# #tomatoes#
# --ham--
# ~lettuce~
# <\______/>
```

Следует помнить о том, что порядок декорирования ВАЖЕН:

```python
@ingredients
@bread
def sandwich(food="--ham--"):
    print (food)
 
sandwich()
# выведет:
# #tomatoes#
# </------\>
# --ham--
# <\______/>
# ~lettuce~
```

Однако, все декораторы, которые мы до этого рассматривали не имели одного очень важного функционала — передачи 
аргументов декорируемой функции.

Что ж, исправим это недоразумение!

Передача («проброс») аргументов в декорируемую функцию.

Никакой чёрной магии, всё, что нам необходимо — собственно, передать аргументы дальше!

```python
def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2): # аргументы прибывают отсюда
        print ("Look what I've got:", arg1, arg2)
        function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments
 
# Теперь, когда мы вызываем функцию, которую возвращает декоратор,
# мы вызываем её "обёртку", передаём ей аргументы и уже в свою очередь
# она передаёт их декорируемой функции
 
@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print ("My name is", first_name, last_name)
 
print_full_name("Peter", "Wenkman")
# выведет:
# Look what I've got: Peter Wenkman
# My name is Peter Wenkman
```

### Декорирование методов

Один из важных фактов, которые следует понимать, заключается в том, что функции и методы в Python — это практически 
одно и то же за исключением того, что методы всегда ожидают первым параметром ссылку на сам объект (self). Это значит, 
что мы можем создавать декораторы для методов так же, как и для функций, просто не забывая про `self`.

```python
def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3 # действительно, дружелюбно - снизим возраст ещё сильней :-)
        return method_to_decorate(self, lie)
    return wrapper
 
 
class Lucy(object):
 
    def __init__(self):
        self.age = 32
 
    @method_friendly_decorator
    def say_your_age(self, lie):
        print("I'm {self.age + lie}. Do I look like it?")
 
l = Lucy()
l.say_your_age(-3)
# выведет: I'm 26. Do I look like it?
```

Конечно, если мы создаём максимально общий декоратор и хотим, чтобы его можно было применить к любой функции или методу,
то стоит воспользоваться тем, что `*args` распаковывает список `args`, а `**kwargs` распаковывает словарь `kwargs`:

```python
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # Данная "обёртка" принимает любые аргументы
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("Did they pass me anything?")
        print(args)
        print(kwargs)
        # Теперь мы распакуем *args и **kwargs
        # Если вы не слишком хорошо знакомы с распаковкой, можете прочесть следующую статью:
        # https://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
        function_to_decorate(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments
 
@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("Python is cool, no argument here.")
 
function_with_no_argument()
# выведет:
# Did they pass me anything?
# ()
# {}
# Python is cool, no argument here.
 
@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)
 
function_with_arguments(1,2,3)

# выведет:
# Did they pass me anything?
# (1, 2, 3)
# {}
# 1 2 3
 
@a_decorator_passing_arbitrary_arguments
def function_with_named_arguments(a, b, c, platypus="Why not?"):
    print("Do %s, %s and %s like platypuses? %s" % (a, b, c, platypus))
 
function_with_named_arguments("Bill", "Linus", "Steve", platypus="Definitely!")
# выведет:
# Did they pass me anything?
# ('Bill', 'Linus', 'Steve')
# {'platypus': 'Definitely!'}
# Do Bill, Linus and Steve like platypuses? Definitely!
 

class Mary(object):
    def __init__(self):
        self.age = 31
 
    @a_decorator_passing_arbitrary_arguments
    def say_your_age(self, lie=-3): # Теперь мы можем указать значение по умолчанию
        print(f"I'm {self.age + lie}. Do I look like it?")
 
m = Mary()
m.say_your_age()
# выведет:
# Did they pass me anything?
# (<__main__ .Mary object at 0xb7d303ac>,)
# {}
# I'm 28. Do I look like it?

```

### Вызов декоратора с различными аргументами

Отлично, с этим разобрались. Что вы теперь скажете о том, чтобы попробовать вызывать декораторы с различными 
аргументами?

Это не так просто, как кажется, поскольку декоратор должен принимать функцию в качестве аргумента, и мы не можем просто
так передать ему что-либо ещё.

Так что, перед тем как показать вам решение, я бы хотел освежить в памяти то, что мы уже знаем:

```python
# Декораторы - это просто функции
def my_decorator(func):
    print("I'm an ordinary function")
    def wrapper():
        print("I'm a function returned by the decorator.")
        func()
    return wrapper
 
# Так что мы можем вызывать её, не используя "@"-синтаксис:
 
def lazy_function():
    print("zzzzzzzz")
 
decorated_function = my_decorator(lazy_function)
# выведет: I'm an ordinary function.
 
# Данный код выводит "I'm an ordinary function", потому что это ровно то, что мы сделали:
# вызвали функцию. Ничего сверхъестественного.
 
@my_decorator
def lazy_function():
    print("zzzzzzzz")
 
# выведет: I'm an ordinary function.


```
Как мы видим, это два аналогичных действия. Когда мы пишем `@my_decorator` — мы просто говорим интерпретатору «вызвать 
функцию под названием `my_decorator`». Это важный момент, потому что данное название может как привести нас напрямую к
декоратору… так и нет!
Давайте сделаем нечто страшное!:)

```python
def decorator_maker():
    print("I make decorators!\n" 
          "I will be called only once when you ask me to create a decorator for you.")

    def my_decorator(func):
        print("I'm a decorator!\n" 
              "I will be called only once: at the moment of decorating the function.")

        def wrapped():
            print("I'm the wrapper around the function being decorated.\n"
                  "I will be called every time you call the decorated function.\n"
                  "I return the result of the decorated function.")
            return func()

        print("I return the decorated function.")

        return wrapped

    print("I return the decorator.")
    return my_decorator


# Давайте теперь создадим декоратор. Это всего лишь ещё один вызов функции
new_decorator = decorator_maker()

# выведет:
# I make decorators!
# I will be called only once when you ask me to create a decorator for you.
# I return the decorator.

# Теперь декорируем функцию
def decorated_function():
    print("I'm the decorated function.")


decorated_function = new_decorator(decorated_function)
# выведет:
# I'm a decorator!
# I will be called only once: at the moment of decorating the function.
# I return the decorated function.


# Теперь наконец вызовем функцию:
decorated_function()
# выведет:
# I'm the wrapper around the function being decorated.
# I will be called every time you call the decorated function.
# I'm the decorated function.

```

Длинно? Длинно. Перепишем данный код без использования промежуточных переменных:

```python
def decorated_function():
    print("I'm the decorated function")
decorated_function = decorator_maker()(decorated_function)
# выведет:
# I make decorators!
# I will be called only once when you ask me to create a decorator for you.
# I return the decorator.
# I'm a decorator!
# I will be called only once: at the moment of decorating the function.
# I return the decorated function.
 
# Наконец:
decorated_function()
# выведет:
# I'm the wrapper around the function being decorated.
# I will be called every time you call the decorated function.
# I return the result of the decorated function.
# I'm the decorated function.
```

А теперь ещё раз, ещё короче:

```python
@decorator_maker()
def decorated_function():
    print("I am the decorated function.")

# выведет:
# I make decorators!
# I will be called only once when you ask me to create a decorator for you.
# I return the decorator.
# I'm a decorator!
# I will be called only once: at the moment of decorating the function.
# I return the decorated function.
 
# И снова:
decorated_function()
# выведет:
# I'm the wrapper around the function being decorated.
# I will be called every time you call the decorated function.
# I return the result of the decorated function.
# I'm the decorated function.
```

Вы заметили, что мы вызвали функцию, после знака "@"?:)

Вернёмся, наконец, к аргументам декораторов, ведь если мы используем функцию, чтобы создавать декораторы «на лету», мы 
можем передавать ей любые аргументы, верно?

```python
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
 
    print("Я создаю декораторы! И я получил следующие аргументы:", decorator_arg1, decorator_arg2)
 
    def my_decorator(func):
        print("Я - декоратор. И ты всё же смог передать мне эти аргументы:", decorator_arg1, decorator_arg2)
 
        # Не перепутайте аргументы декораторов с аргументами функций!
        def wrapped(function_arg1, function_arg2) :
            print ("Я - обёртка вокруг декорируемой функции.\n"
                  "И я имею доступ ко всем аргументам: \n"
                  "\t- и декоратора: {0} {1}\n"
                  "\t- и функции: {2} {3}\n"
                  "Теперь я могу передать нужные аргументы дальше"
                  .format(decorator_arg1, decorator_arg2,
                          function_arg1, function_arg2))
            return func(function_arg1, function_arg2)
 
        return wrapped
 
    return my_decorator
 
@decorator_maker_with_arguments("Леонард", "Шелдон")
def decorated_function_with_arguments(function_arg1, function_arg2):
    print ("Я - декорируемая функция и я знаю только о своих аргументах: {0}"
           " {1}".format(function_arg1, function_arg2))
 
decorated_function_with_arguments("Раджеш", "Говард")
# выведет:
# Я создаю декораторы! И я получил следующие аргументы: Леонард Шелдон
# Я - декоратор. И ты всё же смог передать мне эти аргументы: Леонард Шелдон
# Я - обёртка вокруг декорируемой функции.
# И я имею доступ ко всем аргументам: 
#   - и декоратора: Леонард Шелдон
#   - и функции: Раджеш Говард
# Теперь я могу передать нужные аргументы дальше
# Я - декорируемая функция и я знаю только о своих аргументах: Раджеш Говард
```

Вот он, искомый декоратор, которому можно передавать произвольные аргументы.

Безусловно, аргументами могут быть любые переменные:
```python
c1 = "Пенни"
c2 = "Лесли"
 
@decorator_maker_with_arguments("Леонард", c1)
def decorated_function_with_arguments(function_arg1, function_arg2):
    print ("Я - декорируемая функция и я знаю только о своих аргументах: {0}"
           " {1}".format(function_arg1, function_arg2))
 
decorated_function_with_arguments(c2, "Говард")
# выведет:
# Я создаю декораторы! И я получил следующие аргументы: Леонард Пенни
# Я - декоратор. И ты всё же смог передать мне эти аргументы: Леонард Пенни
# Я - обёртка вокруг декорируемой функции.
# И я имею доступ ко всем аргументам: 
#   - и декоратора: Леонард Пенни
#   - и функции: Лесли Говард
# Теперь я могу передать нужные аргументы дальше
# Я - декорируемая функция и я знаю только о своих аргументах: Лесли Говард
```

Таким образом, мы можем передавать декоратору любые аргументы, как обычной функции. Мы можем использовать и распаковку 
через `*args` и `**kwargs` в случае необходимости.

Но необходимо всегда держать в голове, что декоратор вызывается ровно один раз. Ровно в момент, когда Python 
импортирует Ваш скрипт. После этого мы уже не можем никак изменить аргументы, с которыми он был вызван.

Когда мы пишем `import x` все функции из `x` декорируются сразу же, и мы уже не сможем ничего изменить.

Немного практики: напишем декоратор, декорирующий декоратор.

Вот вам бонус :) Это небольшая хитрость позволит вам превратить любой обычный декоратор в декоратор, принимающий 
аргументы.

Изначально, чтобы получить декоратор, принимающий аргументы, мы создали его с помощью другой функции.

Мы обернули наш декоратор.

Есть ли у нас что-нибудь, чем можно обернуть функцию?

Точно, декораторы!

Давайте же немного развлечёмся и напишем декоратор для декораторов:

```python
def decorator_with_args(decorator_to_enhance):
    """
    Эта функция задумывается КАК декоратор и ДЛЯ декораторов.
    Она должна декорировать другую функцию, которая должна быть декоратором.
    Лучше выпейте чашку кофе.
    Она даёт возможность любому декоратору принимать произвольные аргументы,
    избавляя Вас от головной боли о том, как же это делается, каждый раз, когда этот функционал необходим.
    """
 
    # Мы используем тот же трюк, который мы использовали для передачи аргументов:
    def decorator_maker(*args, **kwargs):
 
        # создадим на лету декоратор, который принимает как аргумент только 
        # функцию, но сохраняет все аргументы, переданные своему "создателю"
        def decorator_wrapper(func):
 
            # Мы возвращаем то, что вернёт нам изначальный декоратор, который, в свою очередь
            # ПРОСТО ФУНКЦИЯ (возвращающая функцию).
            # Единственная ловушка в том, что этот декоратор должен быть именно такого
            # decorator(func, *args, **kwargs)
            # вида, иначе ничего не сработает
            return decorator_to_enhance(func, *args, **kwargs)
 
        return decorator_wrapper
 
    return decorator_maker
```
Это может быть использовано так:

```python
# Мы создаём функцию, которую будем использовать как декоратор и декорируем её :-)
# Не стоит забывать, что она должна иметь вид "decorator(func, *args, **kwargs)"

@decorator_with_args
def decorated_decorator(func, *args, **kwargs):
    def wrapper(function_arg1, function_arg2):
        print("Мне тут передали...:", args, kwargs)
        return func(function_arg1, function_arg2)
    return wrapper
 
# Теперь декорируем любую нужную функцию нашим новеньким, ещё блестящим декоратором:
 
@decorated_decorator(42, 404, 1024)
def decorated_function(function_arg1, function_arg2):
    print ("Привет,", function_arg1, function_arg2)
 
decorated_function("Вселенная и", "всё прочее")
# выведет:
# Мне тут передали...: (42, 404, 1024) {}
# Привет, Вселенная и всё прочее
 
# Уфффффф!
```

Рекомендации для работы с декораторами

Декораторы несколько замедляют вызов функции, не забывайте об этом.

Вы не можете «раздекорировать» функцию. Безусловно, существуют трюки, позволяющие создать декоратор, который можно 
отсоединить от функции, но это плохая практика. Правильней будет запомнить, что если функция декорирована — это не 
отменить.

Декораторы оборачивают функции, что может затруднить отладку.

Как можно использовать декораторы? Зачем же нужны декораторы? Как их можно использовать?

Декораторы могут быть использованы для расширения возможностей функций из сторонних библиотек (код которых мы не можем
изменять) или для упрощения отладки (мы не хотим изменять код, который ещё не устоялся).

Так же полезно использовать декораторы для расширения различных функций одним и тем же кодом, без повторного его 
переписывания каждый раз, например:

```python
def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло
    выполнение декорируемой функции.
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print(func.__name__, time.clock() - t)
        return res

    return wrapper


def logging(func):
    """
    Декоратор, логирующий работу кода.
    (хорошо, он просто выводит вызовы, но тут могло быть и логирование!)
    """

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(func.__name__, args, kwargs)
        return res

    return wrapper


def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.
    """

    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print("{0} была вызвана: {1}x".format(func.__name__, wrapper.count))
        return res

    wrapper.count = 0
    return wrapper


@benchmark
@logging
@counter
def reverse_string(string):
    return str(reversed(string))


print(reverse_string("А роза упала на лапу Азора"))
print(reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni,"
                     "a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam,"
                     "a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!"))

# выведет:
# reverse_string ('А роза упала на лапу Азора',) {}
# wrapper 0.0
# reverse_string была вызвана: 1x
# арозА упал ан алапу азор А
# reverse_string ('A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!',) {}
# wrapper 0.0
# reverse_string была вызвана: 2x
# !amanaP :lanac a ,noep a ,stah eros ,raj a ,hsac ,oloR a ,tur a ,mapS ,snip ,eperc a ,)lemac a ro( niaga gab ananab a ,gat a ,nat a ,gab ananab a ,gag a ,inoracam ,elacrep ,epins ,spam ,arutaroloc a ,shajar ,soreh ,atsap ,eonac a ,nalp a ,nam A
```

Таким образом, декораторы можно применить к любой функции, расширив её функционал и не переписывая ни строчки кода!

```python
import httplib
 
@benchmark
@logging
@counter
def get_random_futurama_quote():
    conn = httplib.HTTPConnection("slashdot.org:80")
    conn.request("HEAD", "/index.html")
    for key, value in conn.getresponse().getheaders():
        if key.startswith("x-b") or key.startswith("x-f"):
            return value
    return "Эх, нет... не могу!"
 
print (get_random_futurama_quote())
print (get_random_futurama_quote())
 
# outputs:
# get_random_futurama_quote () {}
# wrapper 0.02
# get_random_futurama_quote была вызвана: 1x
# The laws of science be a harsh mistress.
# get_random_futurama_quote () {}
# wrapper 0.01
# get_random_futurama_quote была вызвана: 2x
# Curse you, merciful Poseidon!
```

## Декораторы классов

Согласно модели данных Python, язык предлагает три вида методов: статические, класса и экземпляра класса. Давайте 
посмотрим, что же происходит за кулисами каждого из видов методов. Понимание принципов их работы поможет в создании 
красивого и эффективного кода. Начнём с самого простого примера, в котором демонстрируются все три вида методов.

```python
class ToyClass:
    def instancemethod(self):
        return 'instance method called', self
    
    @classmethod
    def classmethod(cls):
        return 'class method called', cls
    @staticmethod
    def staticmethod():
        return 'static method called'
```

### Методы экземпляра класса

Не будем рассматривать подробно, т. к. это любой уже знакомый нам обычный метод класса.

Это наиболее часто используемый вид методов. Методы экземпляра класса принимают объект класса как первый аргумент, 
который принято называть `self` и который указывает на сам экземпляр. Количество параметров метода не ограничено.

Используя параметр `self`, мы можем менять состояние объекта и обращаться к другим его методам и параметрам. К тому же,
используя атрибут `self.__class__`, мы получаем доступ к атрибутам класса и возможности менять состояние самого класса. 
То есть методы экземпляров класса позволяют менять как состояние определённого объекта, так и класса.

Встроенный пример метода экземпляра — `str.upper()`:

```python
>>> "welcome".upper()   # <- вызывается на строковых данных
'WELCOME'
```

### Методы класса

Методы класса принимают класс в качестве параметра, который принято обозначать как `cls`. Он указывает на класс 
ToyClass, а не на объект этого класса. При декларации методов этого вида используется декоратор `classmethod`.

Методы класса привязаны к самому классу, а не его экземпляру. Они могут менять состояние класса, что отразится на всех 
объектах этого класса, но не могут менять конкретный объект.

Встроенный пример метода класса — `dict.fromkeys()` — возвращает новый словарь с переданными элементами в качестве 
ключей.
```python
dict.fromkeys('AEIOU')  # <- вызывается при помощи класса dict
{'A': None, 'E': None, 'I': None, 'O': None, 'U': None}
```

### Статические методы

Статические методы декларируются при помощи декоратора `staticmethod`. Им не нужен определённый первый аргумент (ни 
`self`, ни `cls`).

Их можно воспринимать как методы, которые “не знают, к какому классу относятся”.

Таким образом, статические методы прикреплены к классу лишь для удобства и не могут менять состояние ни класса, ни его
экземпляра.

С теорией достаточно. Давайте разберёмся с работой методов, создав объект нашего класса и вызвав поочерёдно каждый из 
методов: `instancemethod`, `classmethod` и `staticmethod`.
```python
>>> obj = ToyClass()
>>> obj.instancemethod()
('instance method called', ToyClass instance at 0x10f47e7a0>)
>>> ToyClass.instancemethod(obj)
('instance method called', ToyClass instance at 0x10f47e7a0>)
```
Пример выше подтверждает то, что метод `instancemethod` имеет доступ к объекту класса ToyClass через аргумент `self`.

Теперь давайте вызовем метод класса:
```python
>>> obj.classmethod()
('class method called', <class  ToyClass at 0x10f453a10>)
```
Мы видим, что метод класса `classmethod()` имеет доступ к самому классу ToyClass, но не к его конкретному экземпляру 
объекта. Запомните, в Python всё является объектом. Класс тоже объект, который мы можем передать функции в качестве 
аргумента.

Заметьте, что `self` и `cls` — не обязательные названия, и эти параметры можно называть иначе.
```python
def instancemethod(self, ...)
def classmethod(cls, ...)
```
-------то же самое, что и----------
```python
def instancemethod(my_object, ...)
def classmethod(my_class, ...)
```
Это лишь общепринятые обозначения, которым следуют все. Тем не менее они должны находиться первыми в списке параметров.

Вызовем статический метод:
```python
>>> obj.staticmethod()
static method called
```
Да, это может вас удивить, но статические методы можно вызывать через объект класса. Вызов через точку нужен лишь для 
удобства. На самом же деле, в случае статического метода никакие аргументы (`self` или `cls`) методу не передаются.

То есть статические методы не могут получить доступ к параметрам класса или объекта. Они работают только с теми данными,
которые им передаются в качестве аргументов.

Теперь давайте вызовем те же самые методы, но на самом классе.
```python
>>> ToyClass.classmethod()
('class method called', <class ToyClass at 0x10f453a10>)
>>> ToyClass.staticmethod()
'static method called'
>>> ToyClass.instancemethod()
TypeError: unbound method instancemethod() 
must be called with ToyClass instance as 
first argument (got nothing instead)
```
Метод класса и статический метод работают как нужно. Однако вызов метода экземпляра класса выдаёт `TypeError`, так как 
метод не может получить на вход экземпляр класса.

Теперь, когда вы знаете разницу между тремя видами методов, давайте рассмотрим реальный пример для понимания того, 
когда и какой метод стоит использовать.
```python
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)
    
    @staticmethod
    def is_adult(age):
        return age > 18

person1 = Person('Sarah', 25)
person2 = Person.from_birth_year('Roark', 1994)
>>> person1.name, person1.age
Sarah 25
>>> person2.name, person2.age
Roark 24
>>> Person.is_adult(25)
True
```
#### Когда использовать каждый из методов?

Выбор того, какой из методов использовать, может показаться достаточно сложным. Тем не менее, с опытом этот выбор 
делать гораздо проще.

Чаще всего метод класса используется тогда, когда нужен генерирующий метод, возвращающий объект класса. Как видим, 
метод класса `from_birth_year` используется для создания объекта класса `Person` по году рождения, а не возрасту.

Статические методы в основном используются как вспомогательные функции и работают с данными, которые им передаются.

## @property (Свойство)

Конвертация метода класса в атрибуты только для чтения;

Один из самых простых способов использования `property` - это использовать его в качестве декоратора метода. Это 
позволит вам превратить метод класса в атрибут класса.

Давайте взглянем на простой пример:

```python
class Person(object):
    """"""
    def __init__(self, first_name, last_name):
        """Конструктор"""
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def full_name(self):
        """
        Возвращаем полное имя
        """
        return f"{self.first_name} {self.last_name}"
```
В данном коде мы создали два класса атрибута, или свойств: `self.first_name` и `self.last_name`.

Далее мы создали метод `full_name`, который содержит декоратор `@property`. Это позволяет нам использовать следующий 
код в сессии интерпретатора:

```python
person = Person("Mike", "Driscoll")

print(person.full_name) # Mike Driscoll
print(person.first_name) # Mike

person.full_name = "Jackalope"
Traceback (most recent call last):
    File "<string>", line 1, in <fragment>
AttributeError: can't set attribute
```

Как вы видите, в результате превращения метода в свойство мы можем получить к нему доступ при помощи обычной точечной 
нотации. Однако, если мы попытаемся настроить свойство на что-то другое, мы получим ошибку `AttributeError`. 
Единственный способ изменить свойство `full_name` - сделать это косвенно:
```python
Python
person.first_name = "Dan"
print(person.full_name) # Dan Driscoll
```

## Вывод

В Python включены такие декораторы как `@property`, `@staticmethod` и т. д.

В Django декораторы используются для управления кешированием, контроля за правами доступа и определения обработчиков 
адресов. В Twisted — для создания поддельных асинхронных inline-вызовов.

Декораторы открывают широчайший простор для экспериментов!
