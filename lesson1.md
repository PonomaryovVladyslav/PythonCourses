# Лекция 1. Введение. Переменные. Строки и числа

## Что такое программирование?

Программирование — это процесс создания инструкций, которые позволяют компьютеру выполнять определенные задачи. Эти
инструкции называются программами. Программы могут решать широкий спектр задач, от простых вычислений до управления
сложными системами и автоматизации процессов. Программирование требует логического мышления и умения решать проблемы.

По сути программирование состоит из двух частей. Это алгоритмы и структуры данных.

Алгоритмы — это четкие последовательности действий, которые описывают, как решить конкретную задачу. Они являются
основой программирования, так как позволяют разработчикам точно указать, что должно быть сделано для достижения цели.
Примеры алгоритмов включают сортировку данных, поиск значений и выполнение математических вычислений.

Структуры данных — это способы организации и хранения данных для эффективного доступа и модификации. Они включают
массивы, списки, стеки, очереди, деревья и хеш-таблицы. Понимание алгоритмов и структур данных является ключевым для
написания эффективных и оптимизированных программ.

Если говорить простым языком, алгоритмы это как делать, а структуры данных это с чем делать.

![](https://miro.medium.com/v2/resize:fit:439/1*ZYyXvhYDGvELzYoXYpPLMg.png)

## Python

![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/640px-Python-logo-notext.svg.png)

Python — это высокоуровневый язык программирования, который отличается простотой и читаемостью синтаксиса. Его легко
изучить, что делает его популярным среди начинающих программистов, а также профессионалов. Python поддерживает несколько
парадигм программирования, включая процедурное, объектно-ориентированное и функциональное программирование.

История Python начинается в конце 1980-х годов. Язык был создан Гвидо ван Россумом в Центре математики и информатики (
CWI) в Нидерландах. Ван Россум начал работу над Python в декабре 1989 года, а первая версия была выпущена в феврале 1991
года. Название "Python" происходит не от змеи, а от британского комедийного шоу "Monty Python’s Flying Circus", которое
ван Россум очень любил.

Основные этапы развития Python:

- Python 1.0 (январь 1994): Включал основные возможности, такие как обработка исключений, функции и модули.
- Python 2.0 (октябрь 2000): Представил новые возможности, включая сборку мусора и поддержку Unicode.
- Python 3.0 (декабрь 2008): Внес изменения, которые не были обратно совместимы с предыдущими версиями, с целью сделать
  язык более понятным и легким в использовании.

Python активно развивается и поддерживается сообществом разработчиков по всему миру. Последние версии языка включают
множество улучшений и новых возможностей, что делает его мощным инструментом для решения самых разнообразных задач.

В современном мире активно используется python 3+, но на некоторых старых проектах можно встретить и версии 2+

## Где можно применять язык Python?

Python — это высокоуровневый язык программирования, известный своей простотой и читаемостью. Он широко используется в
различных областях, таких как:

1. **Веб-разработка:** Создание серверной логики для веб-приложений (Django, Flask).
2. **Научные исследования и анализ данных:** Инструменты для работы с большими данными, машинное обучение (NumPy,
   Pandas, TensorFlow, scikit-learn).
3. **Автоматизация и скриптинг:** Автоматизация рутинных задач (Selenium, BeautifulSoup).
4. **Разработка игр:** Создание простых игр и графических приложений (Pygame).
5. **Встроенные системы:** Программирование микроконтроллеров (MicroPython).
6. **Образование:** Простой синтаксис делает Python отличным выбором для обучения программированию.

Первые три являются основными сферами применения языка, как раз с первой мы и будем знакомиться глубже

## Установка Python на Windows

![](https://i.redd.it/i0auas97taz61.jpg)

Для операционной системы Windows необходимо скачать и установить Python с официального сайта. Перейдите
по [ссылке](https://www.python.org/downloads/) и загрузите последнюю версию Python. Убедитесь, что во время установки вы
отметили опцию "Add Python to PATH".

## Как запустить консоль

![](https://i.ytimg.com/vi/1uvr7CJazqE/maxresdefault.jpg)

Для запуска Python в различных операционных системах:

1. **Windows:**
    - Откройте "Пуск" (либо кнопки Win + R) и введите "cmd" или "Командная строка".
    - Нажмите Enter для открытия командной строки.

2. **Linux:**
    - Откройте терминал. Обычно это можно сделать с помощью сочетания клавиш `Ctrl + Alt + T` или через меню приложений.

3. **macOS:**
    - Откройте "Finder" и перейдите в "Программы" -> "Утилиты".
    - Откройте "Терминал".

## Что вообще использовать для написания кода? Какие программы?

В первую очередь такие программы называются IDE или редакторы кода. Хотя чисто технически можно использовать хоть word,
хоть блокнот, разница только в вашем личном удобстве.

Редактор кода — это специализированная программа, предназначенная для написания и редактирования кода. Он предоставляет
функции, которые упрощают процесс программирования, такие как подсветка синтаксиса, автодополнение, отладка и многое
другое.

### 1. Visual Studio Code (VS Code)

![VS Code](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/512px-Visual_Studio_Code_1.35_icon.svg.png?20210804221519)

**Visual Studio Code** — это бесплатный, открытый и кроссплатформенный редактор кода, разработанный Microsoft. Он
поддерживает множество языков программирования, включая Python, и предлагает богатый набор функций:

- **Подсветка синтаксиса и автодополнение:** VS Code поддерживает подсветку синтаксиса и автодополнение для Python.
- **Отладка:** Встроенная отладка позволяет легко находить и исправлять ошибки.
- **Расширения:** Существует множество расширений, которые можно установить для улучшения функциональности редактора.
- **Интеграция с Git:** Удобные инструменты для работы с системой контроля версий Git.

### 2. PyCharm

![PyCharm](https://intellij-support.jetbrains.com/hc/user_images/5l0fLOoDkFwpjU_ZKu7Ofg.png)

**PyCharm** — это интегрированная среда разработки (IDE) для Python, разработанная JetBrains. PyCharm доступен в двух
версиях: Community (бесплатная) и Professional (платная с дополнительными функциями).

- **Умное автодополнение кода:** PyCharm предлагает мощное автодополнение кода и анализ кода в реальном времени.
- **Отладка и тестирование:** Встроенные инструменты для отладки и тестирования кода.
- **Поддержка веб-разработки:** Версия Professional поддерживает разработку веб-приложений с использованием Django,
  Flask и других фреймворков.
- **Интеграция с VCS:** Поддержка различных систем контроля версий, включая Git, Mercurial и другие.

### 3. Sublime Text

![Sublime Text](https://www.sublimehq.com/images/sublime_text.png)

**Sublime Text** — это легкий и быстрый текстовый редактор, который поддерживает различные языки программирования,
включая Python.

- **Подсветка синтаксиса и автодополнение:** Sublime Text поддерживает подсветку синтаксиса и автодополнение для Python.
- **Пакетный менеджер:** С помощью пакетного менеджера Package Control можно легко установить дополнительные пакеты и
  плагины.
- **Мини-карта:** Удобная навигация по коду с помощью мини-карты, отображающей весь файл.

### 4. Jupyter Notebook

![Jupyter Notebook](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/1767px-Jupyter_logo.svg.png)

**Jupyter Notebook** — это веб-приложение, которое позволяет создавать и делиться документами, содержащими живой код,
уравнения, визуализации и текстовые пояснения. Оно широко используется в науке о данных, исследовательской и
образовательной деятельности.

- **Интерактивные блокноты:** Возможность выполнения кода по ячейкам, что упрощает тестирование и отладку.
- **Визуализация данных:** Поддержка встроенных библиотек для визуализации данных, таких как Matplotlib и Seaborn.
- **Поддержка нескольких языков:** Помимо Python, Jupyter Notebook поддерживает другие языки программирования через
  ядра (kernels).

## Что же выбрать?

На самом деле это далеко не все редакторы кода которые существуют.

Для задач нашего курса хорошо подходят VsCode или PyCharm.

Я лично использую PyCharm.

Но нужно обратить внимание, версия которая позволит нам нормально изучать вторую половину курса с использованием PyCharm
**платная**, ну или надо искать пиратку :) VsCode бесплатный, так что выбор за вами

## Наконец к коду! Переменные

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVTw0XbQfbys-OwqVRM5wrPt-0CPwIZSZsqw&s)

Переменная — это именованная область памяти, которая используется для хранения данных, которые могут изменяться во время
выполнения программы. В Python переменные создаются присваиванием значения идентификатору:

```python
x = 5
name = "Alice"
```

В этих примерах `x` и `name` это имена переменных, а 5 и "Alice" это их значения

Имена переменных могут содержать маленькие и большие буквы латинского алфавита, цифры и символ `_`

Имя переменной не может начинаться с цифры и не может быть из списка ключевых слов, мы будем все их разбирать в рамках
этого курса

Технически вы можете использовать большие буквы для имени переменной, но не стоит этого делать, это не соответствует
общепринятым правилам. Дальше по курсу я расскажу когда можно и нужно использовать большие буквы.

## Использование функции `print`

![](https://imgb.ifunny.co/images/797eea0107b32bed63dd37959289419e5ed25ef3cef42df6af1f6e5e4e6668ef_1.jpg)

Функция `print` — это встроенная функция Python, которая используется для вывода текста и данных на экран. Она может
принимать один или несколько аргументов и выводить их в стандартный поток вывода (обычно это консоль или терминал).

Создание переменной это хорошо, но нам для обучения будет необходимо еще и смотреть что находится в переменных, самый
простой способ это попросить python распечатать значение переменной через функцию `print`

1. **Вывод строки:**

   ```python
   print("Hello, World!")
   ```

2. **Вывод чисел:**

   ```python
   age = 30
   print(age)
   ```

3. **Вывод нескольких значений:**

   ```python
   name = "Alice"
   age = 30
   print("Name:", name, "Age:", age)
   ```

Как вы видите из примеров, можно выводить как переменные так и просто сразу данные, через запятую можно указать
несколько значений для вывода, у этой функции гораздо больше параметров, но пока что нам достаточно и этих.

## Способы запуска Python кода

Как же нам запустить наш код?

Существует несколько способов запуска кода на Python. Вот основные из них:

1. **Интерактивная оболочка (REPL):** Позволяет вводить команды и видеть результат их выполнения сразу же. Чтобы
   запустить REPL, просто введите `python` или `python3` в командной строке и нажмите энтер.

   ```shell
   $ python3
   Python 3.9.1 (default, Dec  8 2020, 07:51:42)
   [Clang 12.0.0 (clang-1200.0.32.27)] on darwin
   Type "help", "copyright", "credits" or "license" for more information.
   >>>
   ```

   Если вы видите нечто похожее на мой пример, значит все хорошо и вы смогли запустить интрепретатор.
   Тут можно писать код и он будет мгновенно исполняться после каждой строчки. Иногда нам будет нужен этот инструмент,
   но все таки не часто.


2. **Скрипт:** Python-программы обычно пишутся в текстовом файле с расширением `.py` и запускаются с помощью
   интерпретатора Python.

   Гораздо чаще мы будем сохранять код в файлах с расширением `.py` и запускать файл целиком (Такие файлы называются
   скриптами)

   ```shell
   $ python my_script.py
   ```

## Типы данных

Любое изучение программирования начинается с типов данных.

### Виды типизаций

Типизация определяет, как язык программирования работает с типами данных и как они используются в программах.

#### Слабая (не строгая) / Сильная (строгая) типизации

- Слабая (не строгая) типизация: Язык слабо типизирован, если он позволяет выполнять операции между различными типами
  данных без явного приведения типов. Пример: JavaScript.

- Сильная (строгая) типизация: Язык сильно типизирован, если он требует явного приведения типов для выполнения операций
  между различными типами данных. Пример: Python.

При слабой типизации сложить число и строку можно, при сильной нельзя.

#### Статическая / Динамическая типизации

Статическая типизация: В статически типизированных языках типы переменных определяются во время компиляции и не могут
изменяться. Пример: Java, C++.

Динамическая типизация: В динамически типизированных языках типы переменных могут изменяться во время выполнения
программы. Пример: Python, JavaScript.

При статической типизации нужно четко указывать тип данных переменной, при динамической будет использована утиная
типизация, и переменная может изменить свой тип во врем исполнения.

Python является языком с сильной, динамической типизацией.

### Утиная типизация

![](https://python-school.ru/wp-content/uploads/2022/01/Untitled-8-360x203.png)

В питоне используется так называемая утиная типизация. Если что-то выглядит как утка, плавает как утка и крякает как
утка, то это, скорее всего, утка :)

Пока что мы не будем вникать в детали и рассмотрим только два очень простых типа. Строки и числа.

### Строка (String)

Строка — это последовательность символов, используемая для представления текста. В Python строки заключаются в одинарные
или двойные кавычки:

Если у вас что-то обернуто в кавычки (неважно одинарные или двойные, главное с обеих сторон одинаковые), то это строка.

```python
greeting = "Hello, World!"
```

Строки поддерживают множество операций, таких как конкатенация (сложение), извлечение подстрок и методы для работы с
текстом:

Пока что нас будет интересовать всего одна вещь, конкатенация строк

```python
greeting = "Hello, World!"
name = "Alice"
full_greeting = greeting + " " + name
print(full_greeting)  # Вывод: Hello, World! Alice
```

### Число (Number)

Числа в Python могут быть целыми (int) или вещественными (float):

```python
age = 30  # Целое число
height = 1.75  # Вещественное число
```

Python поддерживает стандартные арифметические операции, такие как сложение, вычитание, умножение и деление, деление
нацело, остаток от деления, возведение в степень:

```python
var = 25

sum = var + 10
print(sum)  # Вывод: 35

difference = var - 5
print(difference)  # Вывод: 20

mul = var * 2
print(mul)  # Вывод: 50

div = var / 2
print(div)  # Вывод: 12.5

full_div = var // 2
print(full_div)  # Вывод: 12

reminder = var % 20
print(reminder)  # Вывод: 5

power = var ** 2
print(power)  # Вывод: 625

```

## Порядок выполнения операций

Python выполняет операции в соответствии с приоритетом операторов (как в математике):

1. Скобки `()`
2. Возведение в степень `**`
3. Умножение и деление `*`, `/`, `//`, `%`
4. Сложение и вычитание `+`, `-`

Пример:

```python
result = 2 + 3 * 4  # Результат: 14, так как сначала выполняется умножение
result_with_parentheses = (2 + 3) * 4  # Результат: 20, так как сначала выполняется выражение в скобках
```

## Операции между разными типами данных

В Python нельзя выполнять арифметические операции между строками и числами напрямую. Попытка сделать это приведет к
ошибке:

```python
age = 30
name = "Alice"

# Это вызовет ошибку
message = name + age
```

Для выполнения подобных операций необходимо явно преобразовать тип данных:

```python
age = 30
name = "Alice"
message = name + str(age)
print(message)  # Вывод: Alice30
```

Для преобразования чего угодно в строку используется метод `str`, а для преобразования в число методы `float` и `int`

## Что такое метод `input`?

Метод `input` в Python используется для получения ввода от пользователя. Он позволяет программе принимать данные от
пользователя во время выполнения, что делает её более интерактивной.

### Основное использование

Метод `input` принимает необязательный аргумент, который является строкой, и выводит его в качестве подсказки для
пользователя. После этого программа приостанавливается и ожидает, пока пользователь введет данные и нажмет Enter.
Введенные пользователем данные возвращаются в виде строки.

Пример:

```python
name = input("Введите ваше имя: ")
print("Привет, " + name + "!")
```

Когда вы запустите этот код, программа выведет сообщение "Введите ваше имя: ". После того, как вы введете свое имя и
нажмете Enter, программа продолжит выполнение и выведет приветственное сообщение с вашим именем.

### Преобразование типов данных

По умолчанию, метод input возвращает данные в виде строки. Если вам нужно работать с числовыми значениями или другими
типами данных, вы должны преобразовать введенные данные.

Пример:

```python
age = input("Введите ваш возраст: ")
age = int(age)
print("Через 10 лет вам будет " + str(age + 10) + " лет.")
```

В этом примере введенное значение преобразуется в целое число с помощью функции **int()**, чтобы с ним можно было
выполнять
арифметические операции. Обратите внимание, что результат арифметической операции снова преобразуется в строку для
вывода.

### Примеры использования

Получение числового ввода от пользователя:

```python
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
sum = num1 + num2
print("Сумма: " + str(sum))
```

Получение строкового ввода и работа с ним:

```python
city = input("Введите название вашего города: ")
print("Вы живете в " + city + ".")
```

## Практические задания

0. Запустите 
    ```python
    print("Hello, world!")
    ```
   С этого начинается изучение любого языка программирования, это традиция
1. Создайте переменные `a` и `b`, присвойте им значения 10 и 20 соответственно. Выполните сложение, вычитание, умножение
   и деление этих переменных и выведите результаты.
2. Создайте переменную `text` со значением "Python". Умножьте эту строку на 3 и выведите результат.
3. Создайте переменную `name` со значением вашего имени и переменную `age` с вашим возрастом. Создайте строку, которая
   будет содержать сообщение вида "Меня зовут [имя], мне [возраст] лет." и выведите ее.
4. Напишите программу, которая считает выражение `(5 + 3) * 2 ** 2` и выводит результат.
5. Попробуйте сложить строку и число без приведения типов и исправьте ошибку, используя явное преобразование типов.
6. Сделать задачи 1, 2, 3 при помощи **input**