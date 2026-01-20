# Лекция 18. Virtual env. Pip. Устанавливаемые модули. Pyenv.

### Оглавление курса

<details>
  <summary>Блок 1 — Python Basic (1–6)</summary>

  - [Лекция 1. Введение. Типизации. Переменные. Строки и числа. Булева алгебра. Ветвление](lesson01.md)
  - [Лекция 2. Обработка исключений. Списки, строки детальнее, срезы, циклы.](lesson02.md)
  - [Лекция 3. None. Range, list comprehension, sum, max, min, len, sorted, all, any. Работа с файлами](lesson03.md)
  - [Лекция 4. Хэш-таблицы. Set, frozenset. Dict. Tuple. Немного об импортах. Namedtuple, OrderedDict](lesson04.md)
  - [Лекция 5. Функции, типизация, lambda. Map, zip, filter.](lesson05.md)
  - [Лекция 6. Алгоритмы и структуры данных](lesson06.md)
</details>

<details>
  <summary>Блок 2 — Git (7–8)</summary>

  - [Лекция 7. Git. История системы контроля версий. Локальный репозиторий. Базовые команды управления репозиторием.](lesson07.md)
  - [Лекция 8. Git. Удаленный репозиторий. Remote, push, pull. GitHub, Bitbucket, GitLab, etc. Pull request.](lesson08.md)
</details>

<details>
  <summary>Блок 3 — Python Advanced (9–14)</summary>

  - [Лекция 9. Введение в ООП. Основные парадигмы ООП. Классы и объекты. Множественное наследование.](lesson09.md)
  - [Лекция 10. Magic methods. Итераторы и генераторы.](lesson10.md)
  - [Лекция 11. Imports. Standard library. PEP 8](lesson11.md)
  - [Лекция 12. Декораторы. Декораторы с параметрами. Декораторы классов (staticmethod, classmethod, property)](lesson12.md)
  - [Лекция 13. Тестирование](lesson13.md)
  - [Лекция 14. Проектирование. Паттерны. SOLID.](lesson14.md)
</details>

<details>
  <summary>Блок 4 — SQL (15–17)</summary>

  - [Лекция 15. СУБД. PostgreSQL. SQL. DDL. Пользователи. DCL. DML. Связи.](lesson15.md)
  - [Лекция 16. СУБД. DQL. SELECT. Индексы. Group by. Joins.](lesson16.md)
  - [Лекция 17. СУБД. Нормализация. Аномалии. Транзакции. ACID. TCL. Backup](lesson17.md)
</details>

- ▶ **Лекция 18. Virtual env. Pip. Устанавливаемые модули. Pyenv.**

<details>
  <summary>Блок 5 — Django (19–26)</summary>

  - [Лекция 19. Знакомство с Django](lesson19.md)
  - [Лекция 20. Templates. Static](lesson20.md)
  - [Лекция 21. Модели. Связи. Meta. Abstract, proxy.](lesson21.md)
  - [Лекция 22. Django ORM.](lesson22.md)
  - [Лекция 23. Forms, ModelForms. User, Authentication.](lesson23.md)
  - [Лекция 24. ClassBaseView](lesson24.md)
  - [Лекция 25. NoSQL. Куки, сессии, кеш](lesson25.md)
  - [Лекция 26. Логирование. Middleware. Signals. Messages. Manage commands](lesson26.md)
</details>

<details>
  <summary>Блок 6 — Django Rest Framework (27–30)</summary>

  - [Лекция 27. Что такое API. REST и RESTful. Django REST Framework.](lesson27.md)
  - [Лекция 28. @api_view, APIView, ViewSets, Pagination, Routers](lesson28.md)
  - [Лекция 29. REST-аутентификация. Авторизация. Permissions. Фильтрация.](lesson29.md)
  - [Лекция 30. Тестирование. Django, REST API.](lesson30.md)
</details>

<details>
  <summary>Блок 7 — Python async (31–33)</summary>

  - [Лекция 31. Celery. Multithreading. GIL. Multiprocessing](lesson31.md)
  - [Лекция 32. Asyncio. Aiohttp. Асинхронное программирование на практике.](lesson32.md)
  - [Лекция 33. Сокеты. Django Channels.](lesson33.md)
</details>

<details>
  <summary>Блок 8 — Deployment (34–35)</summary>

  - [Лекция 34. Linux. Все что нужно знать для деплоймента.](lesson34.md)
  - [Лекция 35. Deployment](lesson35.md)
</details>

- [Лекция 36. Методологии разработки. CI/CD. Монолит и микросервисы. Docker](lesson36.md)


![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLlWo64j4TGyFMYwBtv1W8eHaE4fXnaoZLDQ&s)

Виртуальное окружение (virtual environment) — это изолированная среда для выполнения Python, которая позволяет управлять
зависимостями проекта без влияния на системные пакеты Python. Это особенно важно для проектов, которые требуют различных
версий библиотек.

## Зачем это вообще нужно?

Когда вы работаете с различными устанавливаемыми модулями (а мы будем с ними работать), у вас возникает ситуация,
когда на одном компьютере есть больше чем один проект. И эти проекты вполне могут требовать совершенно разных
модулей или их версий. А это значит, что может сложиться ситуация, когда модули в одном проекте конфликтуют с
модулями в другом.

Например, один проект новый и требует новых версий зависимостей, а второй старый и требует старых. Но оба проекта
используют одни и те же пакеты. В этой ситуации вам и требуется изоляция проекта. Что и делается с помощью виртуального
окружения.

## Как работает виртуальное окружение?

![](https://www.dataquest.io/wp-content/uploads/2022/01/python-virtual-envs1.webp)

См. определение выше; ниже — как оно устроено и из каких компонентов состоит.

### Основные концепции и компоненты

1. **Изоляция**: Виртуальное окружение изолирует зависимости проекта, что предотвращает конфликты между пакетами,
   используемыми в разных проектах.
2. **Копия интерпретатора Python**: Виртуальное окружение содержит копию интерпретатора Python и минимальный набор
   необходимых стандартных библиотек.
3. **Собственная директория для пакетов**: Все установленные пакеты и зависимости хранятся в отдельной директории, что
   обеспечивает независимость от глобальных пакетов.

### Что происходит при создании

При создании виртуального окружения происходит следующее:

1. **Создание директорий**: Создаются директории для хранения копий интерпретатора Python и пакетов.
2. **Копирование интерпретатора**: Копируется или создается ссылка на интерпретатор Python, используемый для создания
   окружения.
3. **Установка необходимых файлов**: Создаются и устанавливаются необходимые файлы и скрипты для управления окружением,
   такие как `activate`, `deactivate`, и конфигурационные файлы.

> Это же вкратце.
> - Когда вы устанавливаете python на компьютер, вы устанавливаете сам язык, его зависимости и стандартную
    > библиотеку.
> - Если вы начнете устанавливать пакеты прям туда, то вы установите модули сразу для всех проектов.
> - Виртуальное окружение — это, по сути, создание папки с копией всего, что устанавливается вместе с Python. И теперь,
    когда у нас есть копия, мы можем делать с ней всё что угодно. Она никак не повлияет ни на оригинал, ни на другие
    копии.
> - После создания виртуальное окружение необходимо активировать (об этом дальше)

### Структура виртуального окружения

Структура типичного виртуального окружения выглядит следующим образом (внутри той папки, которую вы создадите):

```
myenv/ (это название, тут могло быть все что угодно)
├── bin/ (Scripts/ на Windows)
│   ├── activate
│   ├── python
│   └── ...
├── lib/ (Lib/ на Windows)
│   └── pythonX.X/
│       └── site-packages/
├── include/
└── pyvenv.cfg
```

- **bin/Scripts**: Содержит скрипты для активации/деактивации окружения и сам интерпретатор Python.
- **lib/Lib**: Содержит установленные пакеты и зависимости.
- **include**: Содержит файлы заголовков C, если они требуются для пакетов.
- **pyvenv.cfg**: Конфигурационный файл, содержащий информацию о виртуальном окружении.

### Создание виртуального окружения

#### Windows

Для создания виртуального окружения на Windows, выполните следующие шаги:

1. Установите Python, если он ещё не установлен.
2. Откройте командную строку (Command Prompt) или PowerShell.
3. Выполните команду:
    ```bash
    python -m venv myenv
    ```
   Здесь `myenv` — это имя вашего виртуального окружения.

#### macOS и Linux

Для создания виртуального окружения на macOS и Linux, выполните следующие шаги:

1. Установите Python, если он ещё не установлен.
2. Откройте терминал.
3. Выполните команду:
    ```bash
    python3 -m venv myenv
    ```
   Здесь `myenv` — это имя вашего виртуального окружения.

> Обратите внимание!
> В данной команде `venv` — это название модуля, который нужно запустить, а `myenv` — название виртуального окружения,
> которое нужно создать.

> Команда в этой ситуации использует **относительный путь**. Это значит, что вам нужно быть осторожным и проверять,
> в какой папке вы в данный момент находитесь. Либо использовать **абсолютный путь**.

### Активация виртуального окружения

При активации виртуального окружения происходит изменение переменных окружения:

1. **Изменение `PATH`**: Путь к исполняемым файлам виртуального окружения добавляется в начало переменной `PATH`. Это
   обеспечивает приоритет использования интерпретатора и скриптов из виртуального окружения.
2. **Установка переменных окружения**: Устанавливаются специфические переменные окружения, такие как `VIRTUAL_ENV`,
   указывающая на путь к активному виртуальному окружению.

Пример активации на разных операционных системах:

- **Windows (cmd)**: `myenv\\Scripts\\activate.bat`
- **Windows (PowerShell)**: `.\\myenv\\Scripts\\Activate.ps1`
- **macOS и Linux (bash/zsh)**: `source myenv/bin/activate`
> Подсказка (PowerShell): при необходимости разрешите выполнение скриптов:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

#### Рекомендации по структуре проекта

- Создавайте окружение прямо в корне проекта и называйте его `.venv`.
- Добавьте его в `.gitignore`, чтобы не коммитить окружение:

```gitignore
.venv/
```

- Примеры создания и активации:

```bash
python3 -m venv .venv           # macOS/Linux
source .venv/bin/activate       # macOS/Linux
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

> Как только вы активируете своё виртуальное окружение, в консоли тут же появится об этом отметка (скрин ниже). Теперь
> все ваши действия, связанные с Python, будут затрагивать только это виртуальное окружение. А значит, вы можете с ним
> делать всё что угодно.

![](https://miro.medium.com/v2/resize:fit:1400/0*EZpE6Kb4wKI3ih88.png)

> Пример из Git bash консоли, на Windows, но в стиле linux.

```shell
(myvenv)
```

Вот эта надпись перед началом строки и говорит нам о том, что виртуальное окружение подключено.

### Работа в виртуальном окружении

После активации виртуального окружения все команды `python` и `pip` будут использоваться из активного окружения. Это
позволяет устанавливать и управлять пакетами, не затрагивая глобальные установки.

### Деактивация виртуального окружения

Для деактивации виртуального окружения и возврата к глобальной среде Python, используется команда:

```bash
deactivate
```

Эта команда восстанавливает первоначальные значения переменных окружения, такие как `PATH`.

> Виртуальные окружения в Python являются мощным инструментом для управления зависимостями и обеспечения изоляции
> проектов. Они просты в использовании и эффективно решают проблемы совместимости и конфликтов пакетов, делая разработку
> более удобной и безопасной.

### Удаление виртуального окружения

Для удаления виртуального окружения просто удалите его папку:

```bash
rm -rf myenv  # для macOS и Linux
rmdir /s /q myenv  # для Windows
```

### Сравнение виртуальных окружений и Docker

![](https://www.meme-arsenal.com/memes/c69830fc6e8ed01171ad3167fe4405ef.jpg)

#### Что такое Docker?

Docker — это платформа для контейнеризации, которая позволяет разработчикам упаковывать приложения и их зависимости в
контейнеры. Контейнеры обеспечивают изоляцию, подобную виртуальным машинам, но более легковесны и эффективны. Они
содержат все необходимое для запуска приложения: код, библиотеки, зависимости и настройки. В отличие от виртуальных
окружений Python, которые изолируют только пакеты Python, Docker обеспечивает полную изоляцию на уровне операционной
системы, позволяя запускать любые приложения и среды независимо от хоста. Docker более универсален, поддерживает любые
языки и стеки технологий, тогда как виртуальные окружения Python удобны для управления зависимостями и изоляцией
исключительно Python-проектов.

> Docker работает с любыми языками программирования и базами данных.
> И в целом является более мощным инструментом для изоляции.

#### Виртуальное окружение

- **Изоляция**: Обеспечивает изоляцию библиотек и пакетов Python.
- **Использование**: Легко создать и использовать для небольших проектов.
- **Производительность**: Низкие накладные расходы на систему.
- **Ограничения**: Изоляция ограничена только Python-зависимостями.

#### Docker

- **Изоляция**: Полная изоляция на уровне операционной системы, включая все зависимости и системные библиотеки.
- **Использование**: Более сложен в настройке, но обеспечивает высокий уровень изоляции и воспроизводимости.
- **Производительность**: Больше накладных расходов по сравнению с виртуальными окружениями Python.
- **Применение**: Подходит для комплексных проектов, требующих определенной версии ОС или нескольких языков
  программирования.

Виртуальные окружения Python и Docker служат для различных целей и решают разные задачи. Виртуальные окружения удобны
для управления зависимостями Python-проектов, в то время как Docker предоставляет более универсальное решение для
изоляции и развертывания приложений. Выбор между ними зависит от конкретных потребностей вашего проекта.

> В рамках нашего курса нам будет достаточно `virtual env`. Но вы всегда можете изучить `docker` самостоятельно, лишними
> эти знания точно не окажутся, а возможно даже пригодятся на собеседованиях.

## Pip и его аналоги

![](https://i.redd.it/99y476u8o3751.jpg)

`pip` (от англ. `Python Installs Packages`) – это основной инструмент для управления пакетами в Python. С его помощью
можно устанавливать, обновлять и удалять библиотеки и другие зависимости. pip широко используется благодаря своей
простоте и удобству.

`pip` идёт в комплекте с `python`. Если вы уже установили `python`, это значит, что `pip` у вас уже установлен и вы можете
им свободно пользоваться.

> Если установить пакет без включенного виртуального окружения. То он установится прямо в основной
> установленный `python`.
> Следите за этим и устанавливайте пакеты только при включенном виртуальном окружении.

### Основные функции pip

#### Установка пакетов

Для установки пакета используется команда:

```bash
python -m pip install имя_пакета
```

Например, чтобы установить библиотеку requests, выполните:

```bash
python -m pip install requests
```

#### Установка пакетов конкретной версии

Достаточно часто нам нужно поставить пакет какой-то определенной версии, а не самый последний.
Для этого нужно сделать так:

```bash
python -m pip install имя_пакета==x.x
```

где `x.x` — это номер версии.

Например, чтобы установить библиотеку requests, выполните:

```bash
pip install requests==2.16
```

или

```bash
pip install requests==2.16.2
```

- **Ограничители версий (рекомендуется для приложений):**

```bash
python -m pip install "requests>=2.31,<3"
python -m pip install "requests~=2.31"
```


#### Обновление пакетов

Чтобы обновить пакет до последней версии, используется команда:

```bash
python -m pip install --upgrade имя_пакета
```

Например, чтобы обновить библиотеку numpy:

```bash
python -m pip install --upgrade numpy
```

#### Удаление пакетов

Для удаления пакета используется команда:

```bash
python -m pip uninstall имя_пакета
```

Например, чтобы удалить библиотеку pandas:

```bash
python -m pip uninstall pandas
```

#### Список установленных пакетов

Для просмотра списка установленных пакетов используется команда:

```bash
python -m pip list
```

#### Поиск пакетов и просмотр версий

- Ищите пакеты и читайте документацию на PyPI: https://pypi.org
- Посмотреть доступные версии пакета из pip:

```bash
python -m pip index versions имя_пакета
```

#### Замораживание и восстановление зависимостей

> Это сверх важная штука, мы будем это делать. И даже больше, с этого занятия ПР без `requirements.txt` рассматриваться
> не будет

pip позволяет замораживать (фиксировать) зависимости проекта в файл `requirements.txt`, что удобно для развертывания
приложения на других системах:

```bash
python -m pip freeze > requirements.txt
```

Для установки зависимостей из файла `requirements.txt` используется команда:

```bash
python -m pip install -r requirements.txt
```
> Примечание: `pip freeze` фиксирует ТЕКУЩИЕ версии всех установленных пакетов. В приложениях полезно хранить строгие версии в `requirements.txt`,
> а в документации/учебных проектах — показывать диапазоны версий (см. примеры с ">=,<" и "~=").


## Как работает pip

pip работает с репозиторием пакетов Python Package Index (PyPI), откуда загружает и устанавливает пакеты. Когда вы
устанавливаете пакет, pip выполняет следующие шаги:

1. **Поиск пакета**: pip отправляет запрос в PyPI для поиска указанного пакета.
2. **Загрузка пакета**: pip загружает пакет и его зависимости.
3. **Установка пакета**: pip устанавливает пакет в вашу систему, включая все необходимые зависимости.

> На момент написания лекции в [PyPI](https://pypi.org/) находилось `559249` пакетов, доступных к установке

pip также поддерживает установку пакетов из различных источников, таких как:

- Локальные файлы (`pip install ./some-package`)
- Архивы (`pip install some-package.tar.gz`)
- Репозитории версионного контроля (например, Git) (`pip install git+https://github.com/username/repo.git`)

## Настройка pip

pip можно настраивать через файл конфигурации `pip.conf` (Linux и macOS) или `pip.ini` (Windows). Вот пример файла
конфигурации:

```ini
[global]
timeout = 60
index-url = https://pypi.org/simple
trusted-host = pypi.org
```

Этот файл можно разместить в одном из следующих мест:

- `/etc/pip.conf` (глобально для всех пользователей)
- `~/.pip/pip.conf` (для текущего пользователя)
- в папке проекта под именем `pip.conf` или `pip.ini`

## pyproject.toml — современный стандарт

`pyproject.toml` — это современный стандартный файл конфигурации Python-проектов (PEP 517, 518, 621).
Он заменяет устаревшие `setup.py`, `setup.cfg` и частично `requirements.txt`.

### Зачем нужен pyproject.toml?

1. **Единый файл конфигурации** — зависимости, метаданные проекта, настройки инструментов (pytest, black, ruff) в одном месте
2. **Стандартизация** — все современные инструменты (pip, poetry, uv, hatch) понимают этот формат
3. **Декларативность** — описываете ЧТО нужно, а не КАК это сделать (в отличие от setup.py)

### Пример pyproject.toml

```toml
[project]
name = "my-project"
version = "1.0.0"
description = "Описание проекта"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "requests>=2.31",
    "django>=5.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "ruff>=0.1",
]

[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.ruff]
line-length = 100
```

### Установка зависимостей из pyproject.toml

```bash
# Установить проект с зависимостями
python -m pip install .

# Установить с dev-зависимостями
python -m pip install ".[dev]"

# Или через uv (быстрее)
uv pip install .
uv pip install ".[dev]"
```

### requirements.txt vs pyproject.toml

| Аспект                 | requirements.txt   | pyproject.toml           |
|------------------------|--------------------|--------------------------|
| Формат                 | Простой список     | TOML (структурированный) |
| Метаданные проекта     | Нет                | Да                       |
| Настройки инструментов | Нет                | Да                       |
| Группы зависимостей    | Несколько файлов   | В одном файле            |
| Lock-файл              | Нет (сам является) | Отдельный файл           |

> **Рекомендация:** Для новых проектов используйте `pyproject.toml`. Для простых скриптов и обучения
> `requirements.txt` по-прежнему удобен.

## Аналоги pip

Кроме pip, существуют и другие системы управления пакетами для Python:

1. **uv** ⭐ — самый современный и быстрый инструмент (2026). Написан на Rust, работает в 10-100 раз быстрее pip.
   Заменяет pip, venv, pyenv, poetry — всё в одном. Подробнее см. раздел "UV — современный менеджер пакетов" ниже.

   ```bash
   uv pip install имя_пакета
   uv add имя_пакета  # для проектов с pyproject.toml
   ```

2. **poetry** — популярный инструмент для управления зависимостями и упаковки проектов. Использует `pyproject.toml`
   и создаёт lock-файлы для воспроизводимых сборок.

   ```bash
   poetry add имя_пакета
   ```

3. **pip-tools** — набор утилит для работы с requirements. `pip-compile` создаёт lock-файл из `requirements.in`,
   `pip-sync` синхронизирует окружение с lock-файлом.

   ```bash
   pip-compile requirements.in  # создаёт requirements.txt с точными версиями
   pip-sync requirements.txt    # устанавливает ровно то, что в файле
   ```

4. **conda** — инструмент для управления пакетами и окружениями, используемый в Anaconda и Miniconda. Поддерживает пакеты
   не только для Python, но и для других языков и системных библиотек. Популярен в Data Science.

   ```bash
   conda install имя_пакета
   ```

5. **pipenv** — инструмент, объединяющий pip и virtualenv. Был популярен в 2018-2020, сейчас уступает poetry и uv.

   ```bash
   pipenv install имя_пакета
   ```

> **Что выбрать?**
> - Для обучения и простых проектов: `pip` + `venv` + `requirements.txt`
> - Для production-проектов: `uv` или `poetry` с lock-файлами
> - Для Data Science: `conda`

## Устанавливаемые модули

Существует невероятно огромное количество различных устанавливаемых пакетов, которыми мы можем (и будем) пользоваться.

Если попытаться найти самые популярные пакеты для установки `python`, то вы найдете:

- `NumPy`: Библиотека для работы с массивами и матрицами, а также для выполнения математических операций над ними.
- `Pandas`: Библиотека для удобной работы с данными, обеспечивающая средства для их манипуляции и анализа.
- `Requests`: Библиотека для простого и удобного выполнения HTTP-запросов.
- `Matplotlib`: Библиотека для создания статических, анимированных и интерактивных визуализаций данных.
- `SciPy`: Библиотека для научных и технических вычислений, которая включает модули для оптимизации, линейной алгебры,
  интеграции и других задач.
- `TensorFlow`: Платформа для машинного обучения и искусственного интеллекта, разработанная для построения и обучения
  моделей.
- `Scikit-Learn`: Библиотека для машинного обучения, предоставляющая простые и эффективные инструменты для анализа и
  моделирования данных.
- `Flask`: Легковесный веб-фреймворк для создания веб-приложений на Python.
- `Django`: Высокоуровневый веб-фреймворк, предназначенный для быстрого создания безопасных и масштабируемых
  веб-приложений.
- `PyTorch`: Библиотека для машинного обучения, известная своей гибкостью и динамическими вычислительными графами.

Итого, 4 пакета для работы с данными(`DS/Big data`), 3 пакета для машинного обучения (`ML`), 2 веб-фреймворка (`web`) и
одна библиотека `requests`

Инструменты для DS/ML мы разбирать не будем. Веб-фреймворк будем изучать весь остаток курса. Что же такое `requests`?

### requests

Этот пакет нужен, чтобы отправлять HTTP-запросы. Технически внутри Python уже есть всё необходимое для отправки
таких запросов. Но в этой библиотеке всё описано просто невероятно удобно и элегантно.

Библиотека `requests` для Python используется для выполнения HTTP-запросов. Она предоставляет простой и интуитивно
понятный API для взаимодействия с веб-сервисами. Вот краткий обзор с примерами использования:

#### Установка

Установить библиотеку можно так, чтобы точно использовать нужный интерпретатор:

```bash
python -m pip install requests
```

#### Выполнение GET-запроса

GET-запрос используется для получения данных с сервера.

```python
import requests

response = requests.get('https://api.example.com/data')
print(response.status_code)  # Статус ответа, например, 200
print(response.text)  # Тело ответа в виде текста
print(response.json())  # Тело ответа, преобразованное в JSON (если применимо)
```

#### Передача параметров в GET-запросе

Можно передавать параметры запроса в URL с помощью параметра `params`.

```python
params = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://api.example.com/data', params=params)
print(response.url)  # Полный URL запроса
```

#### Выполнение POST-запроса

POST-запрос используется для отправки данных на сервер.

```python
data = {'username': 'testuser', 'password': 'testpass'}
response = requests.post('https://api.example.com/login', data=data)
print(response.status_code)  # Статус ответа
print(response.json())  # Тело ответа, преобразованное в JSON (если применимо)
```

#### Отправка JSON данных в POST-запросе

Можно отправлять данные в формате JSON, указав параметр `json`.

```python
json_data = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://api.example.com/data', json=json_data)
print(response.json())  # Тело ответа в виде JSON
```

#### Обработка заголовков ответа

Можно получать и обрабатывать заголовки ответа.

```python
response = requests.get('https://api.example.com/data')
print(response.headers)  # Все заголовки ответа
print(response.headers['Content-Type'])  # Определенный заголовок
```

#### Добавление заголовков в запрос

Можно добавлять свои заголовки в запрос с помощью параметра `headers`.

```python
headers = {'Authorization': 'Bearer YOUR_TOKEN'}
response = requests.get('https://api.example.com/protected', headers=headers)
print(response.status_code)
```

#### Обработка ошибок

Библиотека `requests` предоставляет удобные методы для обработки ошибок.

```python
try:
    response = requests.get('https://api.example.com/data')
    response.raise_for_status()  # Возбудит исключение для кодов ответа 4xx/5xx
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except requests.exceptions.RequestException as err:
    print(f"Error occurred: {err}")
```

### httpx — современная альтернатива requests

`httpx` — это современная HTTP-библиотека, которая поддерживает как синхронные, так и асинхронные запросы.
API очень похож на `requests`, но с дополнительными возможностями.

#### Установка

```bash
python -m pip install httpx
```

#### Синхронное использование (как requests)

```python
import httpx

# Практически идентично requests
response = httpx.get('https://api.example.com/data')
print(response.status_code)
print(response.json())

# POST-запрос
response = httpx.post('https://api.example.com/login', json={'user': 'test'})
```

#### Асинхронное использование

```python
import httpx
import asyncio

async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.example.com/data')
        return response.json()

# Запуск
data = asyncio.run(fetch_data())
```

#### Когда использовать httpx вместо requests?

- Нужна поддержка async/await
- Нужен HTTP/2
- Работаете с современным async-фреймворком (FastAPI, Starlette)
- Хотите единый API для sync и async кода

> **Совет:** Для обучения и простых скриптов `requests` по-прежнему отличный выбор.
> Для production-проектов с async — выбирайте `httpx`.

## Просто полезные пакеты

### `more_itertools`

```bash
python -m pip install more_itertools
```

`more_itertools` — это библиотека, предоставляющая дополнительные инструменты для работы с итераторами и
последовательностями, расширяя возможности стандартного модуля `itertools`.

#### Примеры использования:

- **chunked**: Разделяет последовательность на подсписки фиксированной длины.
  ```python
  from more_itertools import chunked

  data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  chunks = list(chunked(data, 3))
  print(chunks)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  ```

- **collapse**: Развертывает вложенные итераторы в один плоский итератор.
  ```python
  from more_itertools import collapse

  nested = [[1, 2, [3, 4]], [5, 6], 7]
  flat = list(collapse(nested))
  print(flat)  # [1, 2, 3, 4, 5, 6, 7]
  ```

### `python-dateutil` (модуль импортируется как `dateutil`)

```bash
python -m pip install python-dateutil
```

`dateutil` — мощная библиотека для работы с датами и временем. Она предоставляет
инструменты для анализа, обработки и вычисления дат.

#### Примеры использования:

- **парсинг строк даты**:
  ```python
  from dateutil import parser

  date_str = "2023-07-14 12:34:56"
  date = parser.parse(date_str)
  print(date)  # 2023-07-14 12:34:56
  ```

- **релятивные дельты**: Позволяют выполнять операции с датами, такие как добавление месяцев или дней.
  ```python
  from datetime import datetime
  from dateutil.relativedelta import relativedelta

  now = datetime.now()
  one_year_later = now + relativedelta(years=1)
  print(one_year_later)  # Дата ровно через год от текущей даты
  ```

### `openpyxl`

```bash
python -m pip install openpyxl
```

`openpyxl` — это библиотека для чтения и записи файлов Excel (формата .xlsx).

#### Примеры использования:

- **Создание нового файла Excel и запись данных**:
  ```python
  from openpyxl import Workbook

  wb = Workbook()
  ws = wb.active

  ws['A1'] = 'Hello'
  ws['B1'] = 'World'

  wb.save("example.xlsx")
  ```

- **Чтение данных из файла Excel**:
  ```python
  from openpyxl import load_workbook

  wb = load_workbook("example.xlsx")
  ws = wb.active

  print(ws['A1'].value)  # Hello
  print(ws['B1'].value)  # World
  ```

### `pytest`

```bash
python -m pip install pytest
```

`pytest` — популярная библиотека для написания тестов в Python. Она поддерживает простое написание тестов, фикстуры,
параметризацию тестов и многое другое.

#### Примеры использования:

- **Простой тест**:
  ```python
  def test_sum():
      assert sum([1, 2, 3]) == 6, "Should be 6"
  ```

- **Использование фикстур**:
  ```python
  import pytest

  @pytest.fixture
  def sample_list():
      return [1, 2, 3]

  def test_sum(sample_list):
      assert sum(sample_list) == 6, "Should be 6"
  ```

- **Параметризация тестов**:
  ```python
  @pytest.mark.parametrize("input,expected", [
      ([1, 2, 3], 6),
      ([1, 1, 1], 3),
      ([1, -1, 1], 1),
  ])
  def test_sum(input, expected):
      assert sum(input) == expected
  ```

## Пакеты часто используемые в web

### BeautifulSoup

BeautifulSoup — это библиотека для парсинга HTML- и XML-документов. Она создаёт дерево разбора из страниц, что позволяет
легко извлекать данные из HTML- и XML-документов.

**Установка**:

```bash
python -m pip install beautifulsoup4
```

**Пример использования**:

```python
from bs4 import BeautifulSoup

html_doc = """
<html>
 <head><title>The Dormouse's story</title></head>
 <body>
  <p class="title"><b>The Dormouse's story</b></p>
  <p class="story">Once upon a time there were three little sisters; and their names were
   <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
   <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
   <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
   and they lived at the bottom of a well.</p>
 </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.title.string)
# Output: The Dormouse's story

print(soup.find_all('a'))
# Output: [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

for link in soup.find_all('a'):
    print(link.get('href'))
# Output:
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie
```

### Pillow

Pillow — это библиотека для работы с изображениями на Python. Она позволяет открывать, изменять, создавать и сохранять
различные форматы изображений.

**Установка**:

```bash
python -m pip install pillow
```

**Пример использования**:

```python
from PIL import Image

# Открыть изображение
image = Image.open('example.jpg')

# Показать изображение
image.show()

# Изменить размер изображения
resized_image = image.resize((200, 200))
resized_image.save('resized_example.jpg')

# Применить фильтр
from PIL import ImageFilter

filtered_image = image.filter(ImageFilter.BLUR)
filtered_image.save('blurred_example.jpg')
```

### Scrapy

Scrapy — это фреймворк для веб-скрейпинга, который позволяет извлекать данные из веб-сайтов и обрабатывать
их. Scrapy поддерживает различные методы обхода и парсинга веб-страниц.

**Установка**:

```bash
python -m pip install scrapy
```

**Пример использования**:

```python
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

# Чтобы запустить паука, сохраните этот код в файл quotes_spider.py и выполните команду:
# scrapy runspider quotes_spider.py -o quotes.json
```

### psycopg

`psycopg` — современная библиотека (v3) для работы с PostgreSQL в Python; `psycopg2` — классическая версия.
Обе позволяют выполнять запросы, управлять транзакциями и эффективно взаимодействовать с PostgreSQL.
Для простоты в примерах ниже показан `psycopg2`.

### Установка

Для установки (выберите подходящий вариант):

- Вариант A (v3, psycopg):
```bash
python -m pip install "psycopg[binary]"
```
- Вариант B (v2, psycopg2):
```bash
python -m pip install psycopg2-binary
```
> Примечание: для `psycopg` (v3) импорт и API отличаются: `import psycopg` и `psycopg.connect(...)`. Примеры ниже используют `psycopg2`.


### Примеры использования:

#### Подключение к базе данных

```python
import psycopg2

conn = psycopg2.connect(
    dbname="yourdbname",
    user="yourusername",
    password="yourpassword",
    host="yourhost",
    port="yourport"
)
```

#### Создание курсора и выполнение запросов

```python
cur = conn.cursor()
cur.execute("SELECT version();")
db_version = cur.fetchone()
print(db_version)
```

#### Создание таблицы

```python
create_table_query = '''
CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    salary NUMERIC
);
'''
cur.execute(create_table_query)
conn.commit()
```

#### Вставка данных в таблицу

```python
insert_query = '''
INSERT INTO employees (name, salary) VALUES (%s, %s);
'''
cur.execute(insert_query, ('John Doe', 50000))
conn.commit()
```

#### Чтение данных из таблицы

```python
select_query = '''
SELECT * FROM employees;
'''
cur.execute(select_query)
rows = cur.fetchall()
for row in rows:
    print(row)
```

#### Обновление данных

```python
update_query = '''
UPDATE employees SET salary = %s WHERE name = %s;
'''
cur.execute(update_query, (55000, 'John Doe'))
conn.commit()
```

#### Удаление данных

```python
delete_query = '''
DELETE FROM employees WHERE name = %s;
'''
cur.execute(delete_query, ('John Doe',))
conn.commit()
```

#### Закрытие курсора и соединения

```python
cur.close()
conn.close()
```

### Использование контекстных менеджеров

`psycopg2` поддерживает использование контекстных менеджеров для автоматического закрытия соединений и курсоров:

```python
import psycopg2

with psycopg2.connect(
        dbname="yourdbname",
        user="yourusername",
        password="yourpassword",
        host="yourhost",
        port="yourport"
) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        print(db_version)
```

### Обработка исключений

При работе с базами данных важно обрабатывать возможные исключения:

```python
import psycopg2
from psycopg2 import OperationalError, errorcodes, errors

try:
    conn = psycopg2.connect(
        dbname="yourdbname",
        user="yourusername",
        password="yourpassword",
        host="yourhost",
        port="yourport"
    )
    cur = conn.cursor()
    cur.execute("SELECT version();")
    db_version = cur.fetchone()
    print(db_version)
except OperationalError as e:
    print(f"The error '{e}' occurred")
finally:
    if conn:
        cur.close()
        conn.close()
```

Эти примеры показывают основные операции, которые можно выполнять с помощью `psycopg2` для взаимодействия с базой данных
PostgreSQL.

> По сути, этот случайный набор инструментов демонстрирует практически бесконечный функционал для работы с Python.

## Pyenv

`pyenv` — это утилита для управления версиями Python, которая позволяет пользователям легко переключаться между разными
версиями Python. Это особенно полезно для разработчиков, которые работают над проектами, требующими различных версий
Python, или для тех, кто хочет протестировать свои проекты на нескольких версиях.

### Основные возможности `pyenv`

1. **Установка различных версий Python:**
    - `pyenv` позволяет установить любую версию Python, начиная с самых ранних версий до самых последних релизов,
      включая версии Anaconda и PyPy.

2. **Переключение между версиями Python:**
    - Легко переключаться между установленными версиями Python для различных проектов.

3. **Глобальные и локальные версии Python:**
    - `pyenv` поддерживает установку глобальной версии Python, которая будет использоваться по умолчанию, и локальных
      версий для конкретных проектов.

4. **Поддержка виртуальных окружений:**
    - В сочетании с `pyenv-virtualenv` можно управлять виртуальными окружениями Python, что делает разработку еще более
      гибкой.

### Установка `pyenv`

#### На macOS и Linux:

Для установки `pyenv` на macOS и Linux выполните следующие команды:

```bash
curl https://pyenv.run | bash
```

Далее добавьте следующие строки в ваш профиль оболочки (например, `.bashrc` или `.zshrc`):

```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

После этого перезапустите терминал или выполните `source ~/.bashrc` (или соответствующую команду для вашей оболочки).

#### На Windows:

Для Windows рекомендуется использовать `pyenv-win`, который является портом `pyenv` для Windows. Установка
осуществляется через команду:

```bash
pip install pyenv-win --target %USERPROFILE%\.pyenv
```

Далее добавьте следующие пути в переменную окружения PATH:

```
setx PATH "%PATH%;%USERPROFILE%\.pyenv\pyenv-win\bin"
setx PATH "%PATH%;%USERPROFILE%\.pyenv\pyenv-win\shims"
```

### Основные команды `pyenv`

1. **Установка Python:**

   ```bash
   pyenv install 3.12.0
   ```

   Эта команда установит Python версии 3.12.0.

2. **Просмотр доступных версий для установки:**

   ```bash
   pyenv install --list
   ```

3. **Установка глобальной версии Python:**

   ```bash
   pyenv global 3.12.0
   ```

   Эта версия будет использоваться по умолчанию.

4. **Установка локальной версии Python:**

   Внутри каталога проекта выполните:

   ```bash
   pyenv local 3.11.0
   ```

   Эта версия будет использоваться только внутри данного проекта.

5. **Переключение между версиями Python:**

   ```bash
   pyenv shell 3.13.0
   ```

   Эта команда переключит версию Python только для текущей сессии оболочки.

### Примеры использования

#### Пример 1: Установка и переключение между версиями

Установим две версии Python и переключимся между ними.

```bash
# Установка версий Python
pyenv install 3.11.0
pyenv install 3.12.0

# Установка глобальной версии Python
pyenv global 3.12.0

# Проверка текущей версии Python
python --version
# Output: Python 3.12.0

# Переключение на другую версию Python
pyenv shell 3.11.0

# Проверка текущей версии Python
python --version
# Output: Python 3.11.0
```

#### Пример 2: Локальная версия для проекта

Создадим проект и установим для него локальную версию Python.

```bash
# Создание нового проекта
mkdir my_project
cd my_project

# Установка локальной версии Python для проекта
pyenv local 3.12.0

# Проверка текущей версии Python
python --version
# Output: Python 3.12.0
```

## UV — современный менеджер пакетов

![](https://github.com/astral-sh/uv/raw/main/docs/assets/logo-letter.svg)

`uv` — это сверхбыстрый менеджер пакетов и проектов для Python, написанный на Rust.
Разработан компанией Astral (создатели линтера Ruff). Выпущен в 2024 году и быстро стал
стандартом де-факто для современной Python-разработки.

### Почему UV?

1. **Скорость** — в 10-100 раз быстрее pip (установка Django за 0.5 сек вместо 10 сек)
2. **Всё в одном** — заменяет pip, venv, pyenv, pip-tools, poetry
3. **Совместимость** — работает с существующими `requirements.txt` и `pyproject.toml`
4. **Lock-файлы** — автоматическое создание `uv.lock` для воспроизводимых сборок
5. **Управление Python** — установка любых версий Python без pyenv

### Установка UV

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Или через pip (если уже есть Python)
pip install uv
```

### Основные команды UV

#### Управление виртуальными окружениями

```bash
# Создать виртуальное окружение
uv venv

# Создать с конкретной версией Python
uv venv --python 3.12

# Активация (как обычно)
source .venv/bin/activate  # macOS/Linux
.\.venv\Scripts\Activate.ps1  # Windows
```

#### Установка пакетов (режим совместимости с pip)

```bash
# Установить пакет
uv pip install requests

# Установить из requirements.txt
uv pip install -r requirements.txt

# Заморозить зависимости
uv pip freeze > requirements.txt
```

#### Управление проектом (современный подход)

```bash
# Инициализировать новый проект
uv init my_project
cd my_project

# Добавить зависимость (обновляет pyproject.toml и uv.lock)
uv add requests
uv add django>=5.0

# Добавить dev-зависимость
uv add --dev pytest ruff

# Удалить зависимость
uv remove requests

# Синхронизировать окружение с lock-файлом
uv sync

# Запустить скрипт в окружении проекта
uv run python main.py
uv run pytest
```

#### Управление версиями Python

```bash
# Посмотреть доступные версии
uv python list

# Установить конкретную версию
uv python install 3.12
uv python install 3.11 3.13

# Закрепить версию для проекта
uv python pin 3.12
```

### Пример: создание проекта с UV

```bash
# Создаём проект
uv init my_web_app
cd my_web_app

# Устанавливаем Python 3.12
uv python install 3.12
uv python pin 3.12

# Добавляем зависимости
uv add django
uv add requests
uv add --dev pytest

# Запускаем
uv run python -c "import django; print(django.VERSION)"
```

После этих команд у вас будет:
- `pyproject.toml` — конфигурация проекта
- `uv.lock` — lock-файл с точными версиями
- `.python-version` — закреплённая версия Python
- `.venv/` — виртуальное окружение

### UV vs другие инструменты

| Возможность           | pip + venv     | poetry    | uv           |
|-----------------------|----------------|-----------|--------------|
| Скорость              | Медленно       | Средне    | Очень быстро |
| Виртуальные окружения | venv отдельно  | Встроено  | Встроено     |
| Lock-файлы            | Нет            | Да        | Да           |
| Управление Python     | pyenv отдельно | Нет       | Встроено     |
| pyproject.toml        | Частично       | Да        | Да           |
| Совместимость с pip   | —              | Частичная | Полная       |

> **Рекомендация:** Для новых проектов используйте `uv`. Для обучения можно начать с `pip + venv`,
> а затем перейти на `uv` — команды очень похожи.

---

## Практика на занятии

### Задание 1. Настройка окружения

1. Создайте виртуальное окружение для проекта
2. Активируйте его
3. Установите пакеты: `requests`, `python-dateutil`
4. Создайте `requirements.txt`
5. Деактивируйте окружение

### Задание 2. Работа с requests

Напишите скрипт, который:

```python
import requests

def get_random_joke() -> dict:
    """Получает случайную шутку с API."""
    # Используйте: https://official-joke-api.appspot.com/random_joke
    pass

def get_weather(city: str) -> dict:
    """Получает погоду для города (используйте любой бесплатный API)."""
    pass

if __name__ == "__main__":
    joke = get_random_joke()
    print(f"{joke['setup']} — {joke['punchline']}")
```

---

## Домашняя работа

### Задание 1. Виртуальное окружение и зависимости

1. Создайте новый проект с виртуальным окружением
2. Установите `psycopg2-binary` и `python-dotenv`
3. Создайте `requirements.txt` с точными версиями
4. Добавьте `.venv/` в `.gitignore`

### Задание 2. Миграция на базу данных

Для вашего модуля из первого блока курса:
1. Замените хранение данных в файлах на PostgreSQL
2. Используйте `psycopg2` для подключения
3. Создайте необходимые таблицы
4. Реализуйте CRUD-операции

### Задание 3. HTTP-клиент

Напишите модуль для работы с публичным API:

```python
import requests

class APIClient:
    """Клиент для работы с JSONPlaceholder API."""

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_users(self) -> list:
        """Получает список пользователей."""
        pass

    def get_user(self, user_id: int) -> dict:
        """Получает пользователя по ID."""
        pass

    def get_user_posts(self, user_id: int) -> list:
        """Получает посты пользователя."""
        pass

    def create_post(self, user_id: int, title: str, body: str) -> dict:
        """Создаёт новый пост (POST-запрос)."""
        pass
```

### Задание 4. ⭐ Попробуйте UV

1. Установите `uv`
2. Создайте новый проект: `uv init uv_test`
3. Добавьте зависимости: `uv add requests httpx`
4. Сравните скорость установки с pip
5. Изучите созданные файлы (`pyproject.toml`, `uv.lock`)

> На этом месте мы наконец-то готовы переходить к материалу, ради которого всё и затевалось.

---

[← Лекция 17: СУБД. Нормализация. Аномалии. Транзакции. ACID. TCL. Backup](lesson17.md) | [Лекция 19: Знакомство с Django →](lesson19.md)
