# Урок 43. Асинхронное программирование в Python. Корутины. Asyncio.

[/не отображается/]: # (![]&#40;https://www.meme-arsenal.com/memes/236bc16d8000fbe4d3cba00a5079436f.jpg&#41;)

## Итераторы

Во многих современных языках программирования используют такие сущности как итераторы. Основное их назначение – это
упрощение навигации по элементам объекта, который, как правило, представляет собой некоторую коллекцию (список, словарь
и т.п.). Язык Python в этом случае не исключение и в нем тоже есть поддержка итераторов. Итератор представляет собой
объект перечислитель, который для данного объекта выдает следующий элемент либо бросает исключение, если элементов
больше нет.

Основное место использования итераторов – это цикл `for`. Если вы перебираете элементы в некотором списке или символы в
строке с помощью цикла `for`, то фактически это означает, что при каждой итерации цикла происходит обращение к
итератору, содержащемуся в строке/списке с требованием выдать следующий элемент, если элементов в объекте больше нет,
то итератор генерирует исключение, обрабатываемое в рамках цикла `for` незаметно для пользователя.

Приведем несколько примеров, которые помогут лучше понять эту концепцию. Для начала выведем элементы произвольного
списка на экран.

```python
num_list = [1, 2, 3, 4, 5]
for i in num_list:
    print(i)
1
2
3
4
5
```

Как уже было сказано, объекты, элементы которых можно перебирать в цикле `for`, содержат в себе объект итератор, для
того, чтобы его получить, необходимо использовать функцию `iter()`, а для извлечения следующего элемента из итератора –
функцию `next()`.

```python
itr = iter(num_list)
print(next(itr))
1
print(next(itr))
2
print(next(itr))
3
print(next(itr))
4
print(next(itr))
5
print(next(itr))
# Traceback(most recent call last):
# File "<pyshell#12>", line1, in < module > print(next(itr))
# StopIteration
```

Как видно из приведенного выше примера, вызов функции `next(itr)` каждый раз возвращает следующий элемент из списка, а
когда эти элементы заканчиваются, генерируется исключение `StopIteration`.

### Последовательности и итерируемые объекты

По сути, вся разница между последовательностями и итерируемыми объектами (**Не итераторами**), заключается в том, что в
последовательностях элементы упорядочены.

Таким образом, последовательностями являются списки, кортежи и даже строки.

```python
numbers = [1, 2, 3, 4, 5]
letters = ('a', 'b', 'c')
characters = 'habristhebestsiteever'
numbers[1]
2
letters[2]
'c'
characters[11]
's'
characters[0:4]
'habr'
```

Итерируемые объекты же, напротив, не упорядочены, но, тем не менее, могут быть использованы там, где требуется итерация:
цикл `for`, выражения-генераторы, списковые включения (list comprehensions) — как примеры.

```python
# Can't be indexed
unordered_numbers = {1, 2, 3}
unordered_numbers[1]
# Traceback(most recent call last):
# File "<stdin>", line 1, in < module >
# TypeError: 'set' object is not subscriptable

users = {'males': 23, 'females': 32}
users[1]
# Traceback(most recent call last):
# File "<stdin>", line 1, in < module >
# KeyError: 1

# Can be used as sequence
[number ** 2 for number in unordered_numbers]
[1, 4, 9]

for user in users:
    print(user)

males
females
```

**Последовательность - всегда итерируемый объект, итерируемый объект не всегда последовательность.**

### Итераторы

Как мы могли убедиться, цикл `for` не использует индексы. Вместо этого он использует так называемые `итераторы`.

Итераторы — это такие штуки, которые, очевидно, можно итерировать :)
Получить итератор мы можем из любого итерируемого объекта.

Чтобы сделать это явно, нужно вызвать метод `iter()`:

```python
set_of_numbers = {1, 2, 3}
list_of_numbers = [1, 2, 3]
string_of_numbers = '123'
iter(set_of_numbers)
# < set_iterator object at 0x7fb192fa0480 >
iter(list_of_numbers)
# < list_iterator object at 0x7fb193030780 >
iter(string_of_numbers)
# < str_iterator object at 0x7fb19303d320 >
```

Чтобы получить следующий объект из итератора, нужно вызвать метод `next()`:

```python
iterator = iter('123')
next(iterator)
'1'
next(iterator)
'2'
next(iterator)
'3'
next(iterator)
# Traceback(most recent call last):
# File "<pyshell#12>", line1, in < module > print(next(itr))
# StopIteration
```

### Как работает `for`

Цикл `for` вызывает метод `iter()` и к полученному объекту применяет метод `next()`, пока не встретит
исключение `StopIteration`.

Это называется *протокол итерации*. На самом деле он применяется не только в цикле `for`, но и в генераторном выражении
и даже при распаковке и "звёздочке":

```python
coordinates = [1, 2, 3]
x, y, z = coordinates

numbers = [1, 2, 3, 4, 5]
a, b, *rest = numbers

print(rest)
[3, 4, 5]
```

В случае, если мы передаём в `iter()` итератор, то получаем тот же самый итератор:

```python
numbers = [1,2,3,4,5]
iter1 = iter(numbers)
iter2 = iter(iter1)
next(iter1)
# 1
next(iter2)
# 2
iter1 is iter2
# True
```

Подытожим.

`Итерируемый объект` — это что-то, что можно итерировать.

`Итератор` — это сущность, порождаемая функцией `iter`, с помощью которой происходит итерирование итерируемого объекта.

`Итератор` не имеет индексов и может быть использован только один раз.

### Итераторы повсюду

Мы уже видели много итераторов в Python. Я уже упоминал о том, что генераторы — это тоже итераторы. Многие встроенные
функции являются итераторами.

Так, например, `enumerate()`:

```python
numbers = [1,2,3]
enumerate_var = enumerate(numbers)
enumerate_var
# <enumerate object at 0x7ff975dfdd80>
next(enumerate_var)
# (0, 1)
```

А так же `zip()`:

```python
letters = ['a','b','c']
z = zip(letters, numbers)
z
# <zip object at 0x7ff975e00588>
next(z)
# ('a', 1)
```

И даже `open()`:

```python
f = open('foo.txt')
next(f)
# 'bar\n'
next(f)
# 'baz\n'
```

В Python очень много итераторов, и, как уже упоминалось выше, они откладывают выполнение работы до того момента, как мы
запрашиваем следующий элемент с помощью `next()`. Так называемое "ленивое" выполнение.

### Создание своих итераторов

Если нужно обойти элементы внутри объекта вашего собственного класса, необходимо построить свой итератор. Создадим
класс, объект которого будет итератором, выдающим определенное количество единиц, которое пользователь задает при
создании объекта. Такой класс будет содержать конструктор, принимающий на вход количество единиц и метод `__next__()`,
без него экземпляры данного класса не будут итераторами.

```python
class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        raise StopIteration


s_iter1 = SimpleIterator(3)
print(next(s_iter1))
print(next(s_iter1))
print(next(s_iter1))
print(next(s_iter1))
```

В нашем примере при четвертом вызове функции `next()` будет выброшено исключение `StopIteration`. Если мы хотим, чтобы с
данным объектом можно было работать в цикле `for`, то в класс `SimpleIterator` нужно добавить метод `__iter__()`,
который возвращает итератор, в данном случае этот метод должен возвращать `self`.

```python
class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        raise StopIteration


s_iter2 = SimpleIterator(5)
for i in s_iter2:
    print(i)
```

### Выражение итератора

Объект созданный при помощи list comprehension тоже является итератором.

```python
iterator = [i for i in range(10)]
```

## Генераторы

Генераторы — это тоже итераторы.

### Return VS Yield

Ключевое слово `return` — это финальная инструкция в функции. Она предоставляет способ для возвращения значения. При
возвращении весь локальный стек очищается. И новый вызов начнется с первой инструкции.

Ключевое слово `yield` же сохраняет состояние между вызовами. Выполнение продолжается с момента, где управление было
передано в вызывающую область, то есть, сразу после последней инструкции `yield`.

### Генератор vs. Функция

Дальше перечислены основные отличия между генератором и обычной функцией.

Генератор использует `yield` для отправления значения пользователю, а у функции для этого есть `return`;

- При использовании генератора может быть больше одного вызова `yield`;

- Вызов `yield` останавливает исполнение и возвращает итератор, а `return` всегда выполняется последним;

- Вызов метода `next()` приводит к выполнению функции генератора;

- Локальные переменные и состояния сохраняются между последовательными вызовами метода `next()`;

- Каждый дополнительный вызов `next()` вызывает исключение `StopIteration`, если нет следующих элементов для обработки.

Дальше пример функции генератора с несколькими `yield`.

```python
def testGen():
    x = 2
    print('Первый yield')
    yield x

    x *= 1
    print('Второй yield')
    yield x

    x *= 1
    print('Последний yield')
    yield x


# Вызов генератора
iter = testGen()

# Вызов первого yield
next(iter)

# Вызов второго yield
next(iter)

# Вызов последнего yield
next(iter)
```

Вывод:

```
Первый yield
Второй yield
Последний yield
```

Генераторы тоже реализуют протокол итератора:

Если генератор встречает `return`, то в этот момент генерируется исключение `StopIteration`

Если функция завершается без `return`, то после последней строки вызывается `return` без параметров, что и
вызовет `StopIteration` в следующем примере:

```python
>>> def custom_range(number):
...     index = 0 
...     while index < number:
...         yield index
...         index += 1
... 
>>> range_of_four = custom_range(4)
>>> next(range_of_four)
0
>>> next(range_of_four)
1
>>> next(range_of_four)
2
>>> next(range_of_four)
3
>>> next(range_of_four)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

### Когда использовать генератор?

Есть много ситуаций, когда генератор оказывается полезным. Вот некоторые из них:

- Генераторы помогают обрабатывать большие объемы данных. Они позволяют производить так называемые ленивые вычисления.

- Подобным образом происходит потоковая обработка. Генераторы можно устанавливать друг за другом и использовать их как
  Unix-каналы.

- Генераторы позволяют настроить одновременное исполнение.

- Они часто используются для чтения крупных файлов. Это делает код чище и компактнее, разделяя процесс на более мелкие
  сущности.

- Генераторы особенно полезны для веб-скрапинга и увеличения эффективности поиска. Они позволяют получить одну страницу,
  выполнить какую-то операцию и двигаться к следующей. Этот подход куда эффективнее, чем получение всех страниц сразу и
  использование отдельного цикла для их обработки.

### Зачем использовать генераторы?

Генераторы предоставляют разные преимущества для программистов и расширяют особенности, которые проявляются во время
выполнения.

#### Удобные для программистов

Генератор кажется сложной концепцией, но его легко использовать в программах. Это хорошая альтернатива итераторам.

Рассмотрим следующий пример реализации арифметической прогрессии с помощью класса итератора.

Создание арифметической прогрессии с помощью класса итератора:

```python
class AP:
    def __init__(self, a1, d, size):
        self.ele = a1
        self.diff = d
        self.len = size
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.len:
            raise StopIteration
        elif self.count == 0:
            self.count += 1
            return self.ele
        else:
            self.count += 1
            self.ele += self.diff
            return self.ele


for ele in AP(1, 2, 10):
    print(ele)
```

Ту же логику куда проще написать с помощью генератора.

Генерация арифметической прогрессии с помощью функции генератора:

```python
def ap(a1, d, size):
    count = 1
    while count <= size:
        yield a1
        a1 += d
        count += 1


for ele in ap(1, 2, 10):
    print(ele)
```

#### Экономия памяти

Есть использовать обычную функцию для возвращения списка, то она сформирует целую последовательность в памяти перед
отправлением. Это приведет к использованию большого количества памяти, что неэффективно.

Генератор же использует намного меньше памяти за счет обработки одного элемента за раз.

#### Обработка больших данных

Генераторы полезны при обработке особенно больших объемов данных, например, Big Data. Они работают как бесконечный поток
данных.

Такие объемы нельзя хранить в памяти. Но генератор, выдающий по одному элементы за раз, представляет собой этот
бесконечный поток.

Следующий код теоретически может выдать все простые числа.

Найдем все простые числа с помощью генератора:

```python
def find_prime():
    num = 1
    while True:
        if num > 1:
            for i in range(2, num):
                if not num % i:
                    break
            else:
                yield num
        num += 1


for ele in find_prime():
    print(ele)
```

#### Последовательность генераторов

С помощью генераторов можно создать последовательность разных операций. Это более чистый способ разделения обязанностей
между всеми компонентами и последующей интеграции их для получения нужного результата.

Цепочка нескольких операций с использованием pipeline генератора:

```python
def find_prime():
    num = 1
    while num < 100:
        if num > 1:
            for i in range(2, num):
                if not num % i:
                    break
            else:
                yield num
        num += 1


def find_even_prime(seq):
    for num in seq:
        if not num % 2:
            yield num


a_pipeline = find_even_prime(find_prime())

for a_ele in a_pipeline:
    print(a_ele)
```

В примере выше связаны две функции. Первая находит все простые числа от 1 до 100, а вторая — выбирает четные.

#### yield from

Есть специальная конструкция `yield from`, она нужна для:

```python
# Обычный yield
def numbers_range(n):
    for i in range(n):
        yield i


# yield from
def numbers_range(n):
    yield from range(n)
```

`yield from` принимает в качестве параметра итератор.

Напоминаю, генератор - это тоже итератор.

А значит `yield from` может принимать другой генератор:

```python
def subgenerator():
    yield 'World'


def generator():
    yield 'Hello,'
    yield from subgenerator()  # Запрашиваем значение из функции subgenerator()
    yield '!'


for i in generator():
    print(i, end=' ')
```

```
# Вывод
Hello, World !
```

Это важнейшее свойство мы и будем использовать далее.

### Генераторные выражения и особенности генераторов

В случае использования выражения-генератора мы не храним значения, а значит, что мы можем использовать его только 1 раз:

```python
gen = (x for x in range(0, 100 * 10000))
100 in gen
True
100 in gen
False
```

## Корутины

![](https://habrastorage.org/webt/zy/vb/px/zyvbpxrx43dnun4q8wcegtqwnn0.png)

А теперь о том, ради чего это, собственно, затевалось. Оказывается, генератор может не только возвращать значения, но и
принимать их на вход.

О стандарте можно почитать тут [PEP 342](https://www.python.org/dev/peps/pep-0342/).

Предлагаю сразу начать с примера. Напишем простую реализацию генератора, который может складывать два аргумента, хранить
историю результатов и выводить историю.

```python
def calc():
    history = []
    while True:
        x = yield
        if x == 'h':
            print(history)
            continue
        print(x)
        history.append(x)


c = calc()

next(c)  # Необходимая инициация. Можно написать c.send(None)
c.send(1)  # Выведет 1
c.send(100)  # Выведет 100
c.send(666)  # Выведет 666
c.send('h')  # Выведет [1, 100, 666]
c.close()  # Закрываем генератор, данные сотрутся, генератор необходимо будет создавать заново.
```

Пример с передачей более чем одного параметра

```python
def calc():
    history = []
    while True:
        x, y = (yield)
        if x == 'h':
            print(history)
            continue
        result = x + y
        print(result)
        history.append(result)


c = calc()

next(c)  # Необходимая инициация. Можно написать c.send(None)
c.send((1, 2))  # Выведет 3
c.send((100, 30))  # Выведет 130
c.send((666, 0))  # Выведет 666
c.send(('h', 0))  # Выведет [3, 130, 666]
c.close()  # Закрываем генератор, данные сотрутся, генератор необходимо будет создавать заново.
```

### send, throw, close

В Python 2.5 добавили в генераторы возможность отправлять данные и `exception`.

- `send` - передача данных в корутину. `send(None)` - равносильно `next`.

- `throw` - передача исключения в корутину. Например, `GeneratorExit` для выхода из корутины.

- `close` - для "закрытия" корутины и очистки локальной памяти корутины.

### Корутина как декоратор

Т.е. мы создали генератор, проинициализировали его и подаём ему входные данные. В свою очередь он эти данные
обрабатывает и сохраняет своё состояние между вызовами до тех пор, пока мы его не закрыли. После каждого вызова
генератор возвращает управление туда, откуда его вызвали. Это важнейшее свойство генераторов мы и будем использовать.

Теперь, когда мы разобрались с общим принципом работы, давайте теперь избавим себя от необходимости каждый раз руками
инициализировать генератор. Решим это типичным для Python образом, с помощью декоратора.

```python
def coroutine(f):
    def wrap(*args, **kwargs):
        gen = f(*args, **kwargs)
        gen.send(None)
        return gen

    return wrap


@coroutine
def calc():
    history = []
    while True:
        x, y = (yield)
        if x == 'h':
            print(history)
            continue
        result = x + y
        print(result)
        history.append(result)
```

## Asyncio

![](http://risovach.ru/upload/2020/10/mem/internet_253267592_orig_.jpg)

Начиная с Python 3.4, существует новый модуль `asyncio`, который вводит `API` для обобщенного асинхронного 
программирования. Мы можем использовать корутины с этим модулем для простого и понятного выполнения асинхронного кода. 
Мы можем использовать корутины вместе с модулем `asyncio` для простого выполнения асинхронных операций. Пример из 
официальной документации:

```python
import asyncio
import datetime
import random


@asyncio.coroutine
def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print(f"Loop: {num} Time: {datetime.datetime.now()}")
        if (loop.time() + 1.0) >= end_time:
            break
        yield from asyncio.sleep(random.randint(0, 5))


loop = asyncio.get_event_loop()

asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))

loop.run_forever()
```

Мы создали функцию `display_date(num, loop)`, которая принимает два аргумента, первый - номер, а второй - цикл событий, 
после чего наша корутина печатает текущее время. После чего используется ключевое слово `yield from` для ожидания 
результата выполнения `asyncio.sleep`, которая является корутиной, выполняющейся через указанное количество 
секунд (пауза выполнения), мы в своем коде передаем в эту функцию случайное количество секунд. После чего мы используем
`asyncio.ensure_future` для планирования выполнения корутины в цикле событий. После чего мы указываем, что цикл событий
должен работать бесконечно долго.

Если мы посмотрим на вывод программы, то увидим, что две функции выполняются одновременно. Когда мы используем 
`yield from`, цикл обработки событий знает, что он будет какое-то время занят, поэтому он приостанавливает
выполнение функции и запускает другую. Таким образом, две функции работают одновременно (но не параллельно, поскольку
цикл обработки событий является однопоточным).

Стоит отметить, что `yield from` – это синтаксический сахар для `for x in asyncio.sleep(random.randint(0, 5)): yield x` 
– который делает код чище и проще.

**Этот декоратор был удалён в Python 3.8**

### Встроенные корутины

![](https://raw.githubusercontent.com/kblok/kblok.github.io/master/img/deeper-async/bob-loves-async.jpg)

Помните, мы все еще используем функции на основе генератора? В Python 3.5 мы получили новые встроенные корутины, которые
используют синтаксис `async / await`. Предыдущая функция может быть написана так:

```python
import asyncio
import datetime
import random


async def display_date(num, loop):
    end_time = loop.time() + 10.0
    while True:
        print(f"Loop: {num} Time: {datetime.datetime.now()}")
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(random.randint(0, 5))


loop = asyncio.get_event_loop()

asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))

loop.run_forever()
```

Фактически изменены были только строки 6 и 12, для определения встроенной корутины определение функции помечается
ключевым словом `async`, а вместо `yield from` используется `await`.

### Корутины на генераторах и встроенные корутины

Функционально нет никакой разницы между корутинами на генераторах и встроенными корутинами кроме различия в синтаксисе.
Кроме того, не допускается смешивания их синтаксисов. То есть нельзя использовать `await` внутри корутин на генераторах 
или `yield` / `yeild from` внутри встроенных корутин.

Несмотря на различия, мы можем организовывать взаимодействия между ними. Нам просто нужно добавить декоратор
`@types.coroutine` к старым генераторам. Тогда мы можем использовать старый генератор из встроенных корутин и наоборот.

Пример для Python 3.6:

```python
import asyncio
import datetime
import random
import types


@types.coroutine
def my_sleep_func():
    yield from asyncio.sleep(random.randint(0, 5))


async def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print(f"Loop: {num} Time: {datetime.datetime.now()}")
        if (loop.time() + 1.0) >= end_time:
            break
        await my_sleep_func()


loop = asyncio.get_event_loop()

asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))

loop.run_forever()

# Output:
# Loop: 1 Time: 2023-08-14 16:26:35.231695
# Loop: 2 Time: 2023-08-14 16:26:35.231792
# Loop: 2 Time: 2023-08-14 16:26:37.233039
# Loop: 2 Time: 2023-08-14 16:26:38.234310
# Loop: 1 Time: 2023-08-14 16:26:40.232999
# Loop: 1 Time: 2023-08-14 16:26:40.233097
# ...
```

## Asyncio. Loop, run, create_task, gather, etc.

### loop

`loop` - один набор событий, до версии Python 3.7 любые корутины запускались исключительно внутри `loop`

Давайте рассмотрим пример, где отдельная корутина вычисляет факториал последовательно (сначала 2, потом 3, потом 4 и т.
д.) и делает паузу на одну секунду перед следующим вычислением:

```python
import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")


loop = asyncio.get_event_loop()
loop.run_until_complete(factorial('A', 4))
```

Обратите внимание, этот код будет работать на Python 3.6+

### run

То же самое для Python 3.7+ будет выглядеть так:

```python
import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")


asyncio.run(factorial('A', 4))  # Добавлено в 3.7

# Output:
# Task A: Compute factorial(2)...
# Task A: Compute factorial(3)...
# Task A: Compute factorial(4)...
# Task A: factorial(4) = 24
```

### create_tasks

Рассмотрим код, в котором основная корутина запускает две других.

```python
import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"Started at {time.strftime('%X')}")

    await say_after(1, 'hello,')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())

# Output:
# Started at 16:28:52
# hello,
# world
# finished at 16:28:55
```

Обязаны ли мы задавать параметры там же, где и запускаем корутину? Нет, мы можем сделать это через `create_task`

```python
async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello,'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Подождите, пока обе задачи не будут выполнены (должно пройти около 2 секунд.)
    await task1
    await task2
```

Попытка запустить асинхронный метод синхронно не приведёт ни к чему, это просто не будет работать.

```python
import asyncio


async def nested():
    return 42


async def main():
    # Ничего не произойдет, если мы просто вызовем "nested()".
    # Объект корутины создан, но не await,
    # так что *не будет работать вообще*.
    nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".


asyncio.run(main())
```

### gather

Что если нам необходимо запустить асинхронно несколько одинаковых задач с разными параметрами? Нам поможет `gather`.

Вернёмся к коду с факториалами:

```python
import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")


async def main():
    # Запланировать дерево вызовов *конкурентно*:
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )


asyncio.run(main())

# Ожидаемый вывод:
#
#     Task A: Compute factorial(2)...
#     Task B: Compute factorial(2)...
#     Task C: Compute factorial(2)...
#     Task A: factorial(2) = 2
#     Task B: Compute factorial(3)...
#     Task C: Compute factorial(3)...
#     Task B: factorial(3) = 6
#     Task C: Compute factorial(4)...
#     Task C: factorial(4) = 24
```

Обратите внимание, если вам необходимо вернуть значения, вы свободно можете использовать `return`, где это необходимо.

```python
import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():
    # Запланировать дерево вызовов *конкурентно*:
    res = await asyncio.gather(
        factorial("A", 4),
        factorial("B", 3),
        factorial("C", 2),
    )
    print(res)


asyncio.run(main())

```

Вы можете быть уверены в том, что в переменную `res` результаты придут именно в том порядке, в котором вы их запросили, 
в примере результат всегда будет [24, 6, 2], никакой неожиданности.

Это далеко не все методы и подробности корутин, за всеми деталями
в [доку](https://docs.python.org/3/library/asyncio.html)

## Aiohttp.

Как мы помним, одно из основных преимуществ использования асинхронности - это возможность отправки параллельных HTTP
запросов, не дожидаясь результатов других. К сожалению, при использовании корутин вместе с классическим `requests`
запросы будут выполнены синхронно, т. к. сами запросы не являются `awaitable` объектами, и результат будет таким же, как
если бы вы использовали обычный `sleep`, а не асинхронными, соседние корутины будут ждать остальные. Чтобы такого не 
было, существует специальный пакет `aiohttp`, его необходимо устанавливать через `pip`:

```pip install aiohttp```

После чего необходимо создать асинхронный клиент, и можно выполнять запросы.

```python
import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://httpbin.org/#/HTTP_Methods/get_get') as resp:
            print(resp.status)
            print(await resp.text())


asyncio.run(main())

# Output:
# 200
# <!DOCTYPE html>
# <html lang="en">
# 
# <head>
#     <meta charset="UTF-8">
#     <title>httpbin.org</title>
#     <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700|Source+Code+Pro:300,600|Titillium+Web:400,600,700"
#         rel="stylesheet">
# ...
```

Объединив знания, можно приступать к практике и сделать те же задачи, что и на прошлом занятии, но теперь при помощи
корутин.

Практика/Домашка:

1. Написать функцию, которая будет делать запросы на `https://google.com`, `https://amazon.com`, `https://microsoft.com`.
   Оценить время выполнения.

- 1.1 сделать по 5 запросов на каждый сайт, получить время.

2. Написать функцию, которая возводит числа 2, 3 и 5, в 1000000 степень. Оценить время выполнения, сделать выводы.
