# Урок 20. Тестирование

[/не отображается/]: # (![]&#40;https://pics.me.me/your-code-cant-fail-unit-tests-openim-if-you-dont-14499557.png&#41;)

## Общая информация

Тестирование - это огромная, нет **ОГРОМНАЯ** тема, настолько огромная, что порождает несколько отдельных видов 
сотрудников в IT индустрии.

### Автоматизированное и ручное тестирование

Хорошая новость в том, что вы, вероятно, уже создавали тесты, не осознавая этого. Помните, когда вы запускали приложение
и использовали его впервые? Вы проверяли функции и экспериментировали с ними? Это называется исследовательское
тестирование и является формой ручного тестирования.

Исследовательское тестирование — это форма тестирования, которая проводится без плана. В таком виде тестирования вы
просто изучаете приложение.

Чтобы получить полный набор ручных тестов, необходимо выполнить следующие шаги:
- составить список всех функций, которыми обладает ваше приложение;
- список различных типов входных данных, которые оно может принять;
- составить список всех ожидаемых результатов.

Теперь каждый раз, когда вы будете вносить изменения в свой код, вам нужно просмотреть каждый элемент в этом списке и
проверить его правильность.

Это не особо прикольно?

Вот где приходит на помощь **тест план**.

Тест план - это разделение вашего приложения на минимальные части и описание ожидаемой работы функционала каждой части,
порядка их выполнения, и ожидаемых результатов.

Если у вас есть тест план, вы можете каждый раз проходить по всем его пунктам и быть уверенным, что проверили всё. В
случае обновления приложения необходимо обновить и план.

### Модульные (unit) тесты против интеграционных тестов

Подумайте, как вы можете проверить свет в автомобиле. Вы должны включить фары (это будет называться один шаг теста (test
step)), далее нужно выйти из машины или попросить друга проверить, включены ли фары (это называется утверждение теста 
(test assertion)). 

Тестирование нескольких компонентов называется интеграционным тестированием (integration testing).
Основная проблема с интеграционным тестированием — это когда интеграционный тест не дает правильного результата. Иногда
очень трудно диагностировать проблему, не имея возможности определить, какая часть системы вышла из строя. Если фары не
включились, то, возможно, сломаны лампы или разряжен аккумулятор. А как насчет генератора? Или может быть сломан 
компьютер машины?

Если у вас модный современный автомобиль, он сообщит вам, когда ваши лампочки вышли из строя. Это делается с помощью
модульных тестов (unit test).

Как правило, юнит тест — это небольшой тест, который проверяет правильность работы отдельного компонента. Модульный
тест поможет вам выделить то, что сломано в вашем приложении, и быстро это исправить.

Вы только что рассмотрели два типа тестов:

1. Интеграционный тест, который проверяет, что компоненты в вашем приложении правильно работают друг с другом.
2. Модульный тест (unit test), который проверяет отдельный компонент в вашем приложении.

В Python вы можете написать как интеграционные, так и модульные тесты. Чтобы написать модульный тест для встроенной
функции `sum()`, вы должны сравнить выходные данные `sum()` с ожидаемыми выходными данными.

Например, чтобы проверить, что сумма чисел 1, 2, 3 равна 6, можно написать это:

```python
assert sum([1, 2, 3]) == 6, "Should be 6"
```

Ключевое слово `assert`, проверяет выражение на булево значение, если выражение равно `True`, то не сделает ничего, а
если `False`, то будет возбуждена ошибка, на этом и основано всё тестирование в Python.

В нашем примере значение истина, поэтому всё будет хорошо, но если заменить на:

```
assert sum([1, 1, 1]) == 6, "Should be 6"

Traceback(most recent call last):
File "<stdin>", line 1, in <module>
AssertionError: Should be 6
```

Естественно, вы можете обернуть `assert` в функцию или в метод, и всё это будет работать.

Если набор тестов является частью одного элемента, то такой набор называется **Test Case**, если взять как пример фару
автомобиля, то тест кейсом будет проверка, что лампочка целая, что провода функционируют, и что генератор работает. И
при этом во всех случаях необходимо убедиться, что машина заведена и что мы переключили тумблер для включения фар.

Тесты практически всегда пишут в виде тест кейсов, причём разделяя модульные и интеграционные.

Для запуска тестов используются так называемые `test runner` - это специальное приложение, которое умеет искать и
запускать тесты.

Их существует достаточно много, но основные всё-таки:

```
unittest
nose или nose2
pytest
```

`unittest` встроена в Python и не требует дополнительных установок, мы будем пользоваться именно им.

Остальные действуют по тем же принципам с немного другим синтаксисом.

Во встроенном в Python модуле `unittest` есть класс `TestCase`, все тесты должны быть описаны в его наследниках.

Вместо обычного `assert` юнит тест использует свои сразу заготовленные методы, вот некоторые из них:

```python
.assertEqual(a, b)  # a == b

.assertTrue(x)  # bool(x) is True

.assertFalse(x)  # bool(x) is False

.assertIs(a, b)  # a is b

.assertIsNone(x)  # x is None

.assertIn(a, b)  # a in b

.assertIsInstance(a, b)  # isinstance(a, b)
```

Каждый тестовый метод должен начинаться со слова `test`, иначе сборщик тестов его не увидит.

```python
import unittest


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")


if __name__ == '__main__':
    unittest.main()
```

Теперь если мы запустим файл, в котором это написано, мы увидим следующее:

```
$ python test_sum_unittest.py
.F
======================================================================
FAIL: test_sum_tuple (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_sum_unittest.py", line 9, in test_sum_tuple
    self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
AssertionError: Should be 6
----------------------------------------------------------------------
Ran 2 tests in 0.001s
FAILED (failures=1)
```

Один тест успешен, и один упал.

### Методы setUp и tearDown

Если добавить методы `setUp` и `tearDown`, то код из них будет исполняться перед каждым тестом и после каждого теста
соответственно.

```python
import unittest


class TestSum(unittest.TestCase):

    def setUp(self):
        self.my_num = 5

    def test_odd(self):
        self.assertTrue(self.my_num % 2, "Number is odd")

    def tearDown(self):
        self.my_num += 1


if __name__ == '__main__':
    unittest.main()
```

### Пропуск тестов

В пакете `unittest` есть декораторы `skip`, `skipIf` и `skipUnless`.

Необходимы для пропуска ненужных на данном этапе тестов.

```python
class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("Shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "Not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "Requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass
```

### Запуск и поиск тестов

Для запуска тестов можно использовать встроенную команду:

```
python -m unittest <file_name>
```

Указав имя файла или указав слово `discover`:

```
python -m unittest discover
```

Этот скрипт будет искать все тесты внутри всех файлов и папок в директории и запускать их.

## Mock

Мок - это фиктивные объекты. Очень часто мы попадаем в такие ситуации, когда в тесте мы не можем выполнить какое-либо
действие, например, HTTP запрос к стороннему сервису. В этом случае мы можем имитировать выполнение этого запроса, чтобы
не прерывать суть теста, тут нам и поможет `Mock`.

**Для версий Python 3.3 и старше, `Mock` является частью стандартной библиотеки, установка не требуется**

Для использования с версией ниже чем 3.3 необходимо установить пакет `Mock`:

```
pip install mock
```

Можно создать `Mock` объект и заменить им всё что угодно :)

```python
from unittest.mock import Mock
mock = Mock()
mock
<Mock id = '4561344720'>
```

Мы можем использовать фейковый объект в качестве аргумента или целиком заменяя сущность:

```python
# Pass mock as an argument to do_something()
do_something(mock)

# Patch the json library
json = mock
```

У фейкового объекта могут быть как атрибуты, так и методы:

```python
>> > mock.some_attribute
< Mock
name = 'mock.some_attribute'
id = '4394778696' >
>> > mock.do_something()
< Mock
name = 'mock.do_something()'
id = '4394778920' >
```

Есть достаточно много способов использовать `Mock`, очень хорошая 
статья [Тут](https://realpython.com/python-mock-library/)

Рассмотрим основные

### Контроль возвращаемого результата

Предположим, вам нужно убедиться, что ваш код в рабочие и в выходные дни ведёт себя по-разному, а код подразумевает
использование встроенной библиотеки `datetime`.

Для упрощения пока засунем все в один файл:

```python
from datetime import datetime


def is_weekday():
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return 0 <= today.weekday() < 5


# Test if today is a weekday
assert is_weekday()
```

Если мы запустим этот тест в воскресенье, то мы получим `exception`, что же с этим делать? Замокать... `Mock` объект 
может возвращать по вызову любой функции необходимое нам значение посредством заполнения `return_value`.

```python
import datetime
from unittest.mock import Mock

# Save a couple of test days
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

# Mock datetime to control today's date
datetime = Mock()


def is_weekday():
    today = datetime.datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return 0 <= today.weekday() < 5


# Mock .today() to return Tuesday
datetime.datetime.today.return_value = tuesday
# Test Tuesday is a weekday
assert is_weekday()
# Mock .today() to return Saturday
datetime.datetime.today.return_value = saturday
# Test Saturday is not a weekday
assert not is_weekday()
```

Если нам необходимо, чтобы после повторного вызова мы получали другие результаты, то нам поможет `side_effect`. Работает
также, как и `return_value`, только принимает перебираемый объект и с каждым вызовом возвращает следующее значение.

```python
>>> mock_poll = Mock(side_effect=[None, 'data'])
>>> mock_poll()
None
>>> mock_poll()
'data'
```

Или как в прошлом примере:

```python
import datetime
from unittest.mock import Mock

# Save a couple of test days
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

# Mock datetime to control today's date
datetime = Mock()


def is_weekday():
    today = datetime.datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return 0 <= today.weekday() < 5


# Mock .today() to return Tuesday first time and Saturday second time
datetime.datetime.today.side_effect = [tuesday, saturday]
assert is_weekday()
assert not is_weekday()
```

### Декоратор patch

Допустим, у нас есть класс, где мы имитируем какие-то длинные вычисления:

```python
import time


class Calculator:
    def sum(self, a, b):
        time.sleep(10)  # long running process
        return a + b
```

И тест к этой функции:

```python
from unittest import TestCase
from main import Calculator


class TestCalculator(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        answer = self.calc.sum(2, 4)
        self.assertEqual(answer, 6)
```

Этот тест будет идти 10 секунд, имитируя длительный процесс, но мы можем сымитировать выполнение этого метода.

```python
from unittest import TestCase
from unittest.mock import patch


class TestCalculator(TestCase):
    @patch('main.Calculator.sum', return_value=9)
    def test_sum(self, sum):
        self.assertEqual(sum(2, 3), 9)
```

или

```python
from unittest import TestCase
from unittest.mock import patch


class TestCalculator(TestCase):
    @patch('main.Calculator.sum')
    def test_sum(self, sum):
        sum.return_value = 9
        self.assertEqual(sum(2, 3), 9)
```

Пропатченные методы попадают в аргументы метода теста.


Практика:

Открываем модуль по ООП и покрываем всеми возможными тестами!!!
