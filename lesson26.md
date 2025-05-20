# Лекция 26. Middleware. Signals. Messages. Manage commands

## Введение

Когда вы обрабатываете HTTP-запросы в Django, вы взаимодействуете с мощным механизмом — **middleware**, сигналами и
системой сообщений. Эти три слоя делают веб-приложения гибкими, расширяемыми и отзывчивыми.

---

## 🧩 Middleware

![](https://memegenerator.net/img/instances/81631865.jpg)

📚 [Официальная документация](https://docs.djangoproject.com/en/5.2/topics/http/middleware/)

### Что это?

Мы с вами рассмотрели основные этапы того, какие этапы должен пройти request на всём пути нашей request-response
системы,
но на самом деле каждый request проходит кучу дополнительных обработок, таких как middleware, причём каждый request
делает это дважды, при "входе" и при "выходе".

**Middleware** — это фреймворк обработки запросов и ответов. Каждый HTTP-запрос проходит через цепочку middleware "
вперёд" к view и "обратно" — к пользователю. Это похоже на слоёный пирог: каждый слой может что-то сделать с запросом
или ответом.

```plaintext
Request ↓
 ┌─────────────────────────────────────────────────────────┐
 │ SecurityMiddleware                                      │
 │ SessionMiddleware                                       │
 │ CommonMiddleware                                        │
 │ CsrfViewMiddleware                                      │
 │ AuthenticationMiddleware                                │
 │ YOUR CUSTOM MIDDLEWARE                                  │
 │ MessageMiddleware                                       │
 │ Clickjacking Protection (XFrameOptionsMiddleware)       │
 └─────────────────────────────────────────────────────────┘
                    View →
         ← Response (тот же путь обратно)
```

---

### Пример структуры в `settings.py`

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'main.middleware.CheckUserStatus',  # ваш кастомный
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

---

### Как написать свой middleware?

#### ✅ Вариант 1: Функциональный

```python
def simple_middleware(get_response):
    def middleware(request):
        print("Before view")
        response = get_response(request)
        print("After view")
        return response

    return middleware
```

#### ✅ Вариант 2: Классовый (рекомендуется)

```python
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Before view")
        response = self.get_response(request)
        print("After view")
        return response
```

Добавьте middleware в `settings.py`.

---

### 💡 Совет

Порядок **имеет значение**! Если вы добавили middleware, работающий с `request.user`, он должен быть **после**
`AuthenticationMiddleware`.

---

### 🔧 MiddlewareMixin

Для совместимости с устаревшими API:

```python
from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ...

    def process_response(self, request, response):
        ...
```

---

## 📡 Signals (Сигналы)

📚 [Signals](https://docs.djangoproject.com/en/5.2/topics/signals/)

### Что это?

Сигналы — способ уведомить части вашего приложения о том, что «что-то произошло» — например, сохранение объекта. Это
помогает **разделить ответственность** и **не писать логику в моделях или view напрямую**.

---

### Часто используемые сигналы:

| Сигнал                                 | Когда вызывается            |
|----------------------------------------|-----------------------------|
| `pre_save` / `post_save`               | До/после сохранения объекта |
| `pre_delete` / `post_delete`           | До/после удаления объекта   |
| `m2m_changed`                          | Изменения в ManyToMany      |
| `request_started` / `request_finished` | Начало/конец запроса        |

---

### Использование с декоратором

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import Order


@receiver(post_save, sender=Order)
def after_order_save(sender, instance, created, **kwargs):
    if created:
        send_email_to_manager(instance)
```

---

### Ручной сигнал

```python
from django.dispatch import Signal

pizza_done = Signal()

pizza_done.send(sender=None, toppings=["pepperoni"], size="large")
```

---

### ⚠️ Потенциальные проблемы

- **Скрытая логика**: сигналы вызываются "в фоне", усложняя отладку.
- **Неявные зависимости**: сложно понять, кто слушает сигнал.
- **Ошибки в сигналах → падает всё**.

Используйте **осознанно и выборочно**, особенно в больших проектах.

---

### 📁 Где регистрировать сигналы?

Обычно сигналы регистрируются в отдельном модуле `signals.py` внутри вашего приложения, а затем подключаются в
`apps.py`.

#### Пример структуры:

```
myapp/
├── apps.py
├── models.py
├── signals.py
```

#### signals.py:

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order


@receiver(post_save, sender=Order)
def notify_manager(sender, instance, created, **kwargs):
    if created:
        print(f"New order created: {instance.id}")
```

#### apps.py:

```python
from django.apps import AppConfig


class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        import myapp.signals
```

📌 Метод `ready()` вызывается при старте Django, и именно там следует **импортировать** модуль с сигналами, чтобы они
были зарегистрированы. Не подключайте сигналы в `models.py` или `__init__.py` — это может привести к проблемам с
импортами.

---

### ℹ️ Что такое `apps.py`?

Файл `apps.py` содержит класс-настройку вашего приложения и используется Django для конфигурации.

#### Пример базовой конфигурации:

```python
from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
```

### Что можно делать в `apps.py`?

- Регистрировать сигналы
- Выполнять инициализацию сторонних библиотек
- Проверять зависимости
- Настраивать логгеры
- Создавать фоновые задачи или cron-хуки (например, через Celery beat)

📌 Только не загружайте `ready()` тяжёлыми действиями — он вызывается при **каждом запуске** процесса Django.

---

## ✉️ Messages (Flash-сообщения)

📚 [Документация](https://docs.djangoproject.com/en/5.2/ref/contrib/messages/)

Сообщения позволяют показать одноразовое уведомление пользователю после запроса. Пример — «Вы успешно
зарегистрировались».

---

### Включение

Убедитесь, что:

- `'django.contrib.messages'` в `INSTALLED_APPS`
- `'django.contrib.messages.middleware.MessageMiddleware'` в `MIDDLEWARE`
- `django.contrib.messages.context_processors.messages` в `TEMPLATES -> OPTIONS -> context_processors`

---

### Как использовать

```python
from django.contrib import messages


def my_view(request):
    messages.success(request, "Профиль обновлён!")
    return redirect("profile")
```

---

### Уровни сообщений

```python
messages.debug(request, "Отладка")
messages.info(request, "Информация")
messages.success(request, "Успех!")
messages.warning(request, "Предупреждение")
messages.error(request, "Ошибка")
```

---

### Отображение в шаблоне

```html
{% if messages %}
<ul class="messages">
    {% for message in messages %}
    <li class="{{ message.tags }}">{{ message }}</li>
    {% endfor %}
</ul>
{% endif %}
```

---

### Использование с CBV (Class-Based Views)

```python
from django.contrib.messages.views import SuccessMessageMixin


class MyView(SuccessMessageMixin, CreateView):
    success_message = "Объект успешно создан!"
```

---

### 💡 Практические кейсы

| Сценарий                    | Пример сообщения   |
|-----------------------------|--------------------|
| Успешная регистрация        | `messages.success` |
| Ошибка заполнения формы     | `messages.error`   |
| Предупреждение о балансе    | `messages.warning` |
| Отображение отладочной info | `messages.debug`   |

---

## 🧪 Повторим и закрепим

✅ Middleware — это **обработчик запроса и ответа**, может быть функцией или классом  
✅ Signals позволяют **реагировать на действия** модели без изменения её кода  
✅ Messages — это **одноразовые уведомления**, удобно использовать после redirect'ов  
✅ Не забывайте включать нужные middleware и context_processors  
✅ Middleware работают в **двух направлениях**: запрос и ответ

---

## Manage-команды и настройки.

Manage-команды в рамках Django - это возможность запустить скрипт из консоли для выполнения абсолютно различных
действий.

Существует три способа запуска manage-команды:

```
django-admin <command> [options]
python manage.py <command> [options]
python -m django <command> [options]
```

В случае запуска через `django-admin` вы можете указать, какой файл настроек использовать при помощи опции `--settings`.

Если вы запускаете команду через `manage.py` (самый распространенный способ), файл настроек будет выбран в соответствии
с самим файлом `manage.py` (Напоминаю структуру, информация о файле настроек для Django проекта находится именно в
файле `manage.py`).

Мы использовали некоторые команды, но давайте посмотрим подробнее.

## Доступные команды.

![](https://www.meme-arsenal.com/memes/d4d5ed953c6b783bc97f142cb8e89d4d.jpg)

| Категория                            | Команда            | Описание                                             | Пример использования                                |
|--------------------------------------|--------------------|------------------------------------------------------|-----------------------------------------------------|
| 🏗 **Создание проекта и приложений** | `startproject`     | Создает новый Django-проект                          | `django-admin startproject mysite`                  |
|                                      | `startapp`         | Создает новое Django-приложение                      | `python manage.py startapp blog`                    |
| 🔄 **Миграции и работа с БД**        | `makemigrations`   | Генерирует файлы миграций на основе моделей          | `python manage.py makemigrations users`             |
|                                      | `migrate`          | Применяет миграции к базе данных                     | `python manage.py migrate`                          |
|                                      | `showmigrations`   | Показывает все миграции и их статус                  | `python manage.py showmigrations`                   |
|                                      | `sqlmigrate`       | Показывает SQL-код конкретной миграции               | `python manage.py sqlmigrate users 0001`            |
|                                      | `squashmigrations` | Объединяет несколько миграций в одну                 | `python manage.py squashmigrations users 0001 0005` |
|                                      | `flush`            | Удаляет все данные из базы (сохраняя структуру)      | `python manage.py flush`                            |
|                                      | `sqlflush`         | Показывает SQL-код, который будет выполнен при flush | `python manage.py sqlflush`                         |
|                                      | `sqlsequencereset` | Сброс последовательностей (id)                       | `python manage.py sqlsequencereset users`           |
|                                      | `inspectdb`        | Генерирует модели на основе существующей БД          | `python manage.py inspectdb > models.py`            |
| 🧪 **Тестирование**                  | `test`             | Запускает unit-тесты                                 | `python manage.py test`                             |
| 🧠 **Управление пользователями**     | `createsuperuser`  | Создание суперпользователя                           | `python manage.py createsuperuser`                  |
|                                      | `changepassword`   | Изменение пароля пользователя                        | `python manage.py changepassword admin`             |
| 🌐 **Сервер и консоль**              | `runserver`        | Запускает локальный сервер разработки                | `python manage.py runserver 8080`                   |
|                                      | `shell`            | Открывает Django shell                               | `python manage.py shell`                            |
|                                      | `dbshell`          | Открывает shell для БД (например, `psql`)            | `python manage.py dbshell`                          |
| 🗃 **Работа с данными (фикстуры)**   | `dumpdata`         | Экспорт данных в JSON (фикстуры)                     | `python manage.py dumpdata > data.json`             |
|                                      | `loaddata`         | Импорт данных из JSON-файла                          | `python manage.py loaddata data.json`               |
| 📖 **Работа с переводами**           | `makemessages`     | Поиск строк для перевода (создает `.po`)             | `python manage.py makemessages -l ru`               |
|                                      | `compilemessages`  | Компиляция `.po` в `.mo` для использования           | `python manage.py compilemessages`                  |
| 📦 **Кэш и сессии**                  | `createcachetable` | Создает таблицу в БД для хранения кэша               | `python manage.py createcachetable`                 |
|                                      | `clearsessions`    | Удаляет устаревшие сессии из БД                      | `python manage.py clearsessions`                    |
| 🔧 **Отладка и администрирование**   | `check`            | Проверка проекта на ошибки конфигурации              | `python manage.py check`                            |
|                                      | `diffsettings`     | Сравнение текущих и дефолтных настроек               | `python manage.py diffsettings`                     |
|                                      | `sendtestemail`    | Отправка тестового письма (если email настроен)      | `python manage.py sendtestemail user@example.com`   |
| 📜 **Пользовательские команды**      | (имя команды)      | Кастомная команда в `management/commands/`           | `python manage.py close_orders`                     |

Как создавать проект и приложения вы в целом научились, давайте посмотрим на новые команды, или как можно не стандартно
использовать старые.

## 🔄 **Миграции и работа с БД**   

### makemigrations

Уже известная вам команда, которая создаёт файлы миграций, и может принимать имя приложения, чтобы создать только для
конкретного приложения.

Может принимать важный параметр `--empty`, при этом флаге создастся пустая миграция, никак не привязанная к моделям.
Выглядеть будет примерно вот так:

```python
# Generated by Django 3.0.7 on 2020-10-29 11:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('storages', '0003_auto_20201029_1352'),
    ]

    operations = [
    ]
```

Тут указано приложение, для которого миграция будет применена, и прошлая миграция, с которой текущая миграция будет
связана.

Зачем это вообще надо?

Мы можем в операции добавить любые интересующие нас действия, например, выполнения кода на Python.

Для этого нужно добавить класс `RunPython` из пакета `migrations`, который будет принимать два метода, первый будет
выполнен в случае выполнения миграции, второй - в случае отката миграции.

```python
# Generated by Django 3.0.7 on 2020-10-29 11:59

from django.db import migrations


def some_forward_action(apps, schema_editor):
    Team = apps.get_model('storages', 'Team')
    Team.objects.create(name='B2B')
    Team.objects.create(name='CX')
    Team.objects.create(name='SFA')


def some_backward_action(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('storages', '0003_auto_20201029_1352'),
    ]

    operations = [
        migrations.RunPython(some_forward_action, some_backward_action)
    ]
```

Такие миграции называются **Data Migrations**.

Чаще всего для того, чтобы занести какие-либо данные в базу данных на этапе миграции, например, создать заведомо
известные объекты, как в моём примере, или для установки вычисляемого значения по умолчанию.

Для обратной миграции чаще всего действия не требуются (хоть и далеко не всегда), поэтому чаще всего обратная миграция
записывается в виде лямбды `lambda x, y: None`

Типовая Data Migration:

```python
# Generated by Django 3.0.7 on 2020-10-29 11:59

from django.db import migrations


def some_forward_action(apps, schema_editor):
    Team = apps.get_model('storages', 'Team')  # Приложение и модель
    Team.objects.create(name='B2B')
    Team.objects.create(name='CX')
    Team.objects.create(name='SFA')


class Migration(migrations.Migration):
    dependencies = [
        ('storages', '0003_auto_20201029_1352'),
    ]

    operations = [
        migrations.RunPython(some_forward_action, lambda x, y: None)
    ]
```

### migrate

Уже известная вам команда для применения миграции

Команда migrate применяется для выполнения миграций и синхронизации состояния базы данных с текущими моделями проекта.

```
python manage.py migrate [app_label] [migration_name]
```

- app_label — имя приложения, миграции которого необходимо применить.

- migration_name — имя конкретной миграции (обычно достаточно первых четырёх цифр из имени миграции).

Если не указать параметры, команда применит **все миграции для всех приложений**.

#### Пример: откат миграции

Допустим, вы уже применили миграции до `0008`, но обнаружили ошибку в `0006`. Вы можете откатить состояние базы данных
до миграции `0005`:

```bash
python manage.py migrate my_app 0005
```

> ⚠️ Это приведёт к откату всех миграций после 0005 и, скорее всего, приведёт к потере данных, связанных с удаляемыми
> моделями и полями.

#### Флаг `--fake`

Флаг `--fake` позволяет пометить миграцию как выполненную, **не внося реальные изменения** в базу данных:

```bash
python manage.py migrate my_app 0005 --fake
```

Этот приём используется в ситуациях, когда база данных уже была подготовлена вручную или через внешнюю систему (например
переносите проект с другого фреймворка на джанго), и вы хотите синхронизировать Django с её текущим состоянием.

#### Откат до нуля

Если вместо номера миграции указать `zero`, можно откатить **все миграции** для указанного приложения:

```bash
python manage.py migrate my_app zero
```

> 🔥 **Важно:** Откат миграций удалит таблицы и данные. Сделайте резервную копию!


### showmigrations

Также уже известная вам команда, которая отобразит список миграций и их состояние (применена или нет).


### `sqlmigrate`

Команда `sqlmigrate` позволяет **посмотреть SQL-код**, который будет сгенерирован и выполнен при применении определённой миграции. Это особенно полезно, если вы хотите:

- понять, какие **структурные изменения** будут внесены в базу;
- провести **аудит миграций** перед деплоем;
- получить SQL-запросы для ручного применения или изучения.

```bash
python manage.py sqlmigrate <app_label> <migration_name>
```

- `app_label` — имя приложения, например `users`;
- `migration_name` — имя миграции **без префикса `0XXX_`**, достаточно просто `0001` или `initial`.

#### Пример:

```bash
python manage.py sqlmigrate users 0001
```

Вывод будет содержать SQL-запросы, необходимые для создания таблиц и индексов, например:

```sql
CREATE TABLE "users_user" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "username" varchar(150) NOT NULL UNIQUE,
    "email" varchar(254) NOT NULL
);
```

> 🔍 **Совет:** Используйте `sqlmigrate`, чтобы убедиться, что миграции не создают неожиданных изменений, особенно если вы вносите правки вручную или используете `RunSQL`.

### squashmigrations

Команда `squashmigrations` используется для объединения нескольких последовательных миграций в одну, чтобы упростить структуру миграций и улучшить читаемость проекта.

Это особенно полезно после активной разработки, когда в приложении накопилось множество миграций, добавляющих поля, изменяющих типы или удаляющих элементы в одной и той же модели.

#### Синтаксис

```bash
python manage.py squashmigrations <app_label> <start_migration> <end_migration>
```

#### Пример

Допустим, в приложении `myapp` имеются миграции `0004`, `0005`, `0006` и `0007`, каждая из которых добавляет или изменяет поля в одной модели. Чтобы объединить их в одну миграцию, выполните:

```bash
python manage.py squashmigrations myapp 0004 0007
```

Это создаст новую миграцию, содержащую совокупность всех изменений между `0004` и `0007`, и заменит старые миграции.

:::tip
Squash-команды следует выполнять **только после того**, как все предыдущие миграции были применены на всех окружениях, иначе возможны проблемы с синхронизацией структуры базы данных.
:::

#### Когда применять squashmigrations

- После нескольких итераций разработки модели, когда накопилось много миграций.
- Перед выпуском в продакшн, чтобы упростить аудит миграций.
- Для улучшения производительности применения миграций при CI/CD.

#### Примечание

Squash не удаляет старые миграции автоматически — вы можете проверить и при необходимости удалить их вручную после тестирования новой объединённой миграции.


### flush

Команда `flush` очищает базу данных от всех данных пользователя, сбрасывая содержимое всех таблиц, **но не отменяя миграций и не удаляя структуру базы**.

Это значит, что после выполнения команды:

- Все таблицы останутся на месте.
- Все миграции будут считаться применёнными.
- Будут удалены все данные, включая созданных пользователей, записи моделей и данные сессий.
- Значения автоинкрементных полей (`id`) будут сброшены (если это поддерживает СУБД).

```bash
python manage.py flush
```

После выполнения вы получите предупреждение с подтверждением:

```bash
You have requested a flush of the database.
This will IRREVERSIBLY DESTROY all data in the database.
Are you sure you want to do this?
```

#### Применение:

- Для быстрого сброса данных при локальной разработке.
- При подготовке к демонстрации, когда нужна «чистая» база.
- Для очистки базы перед загрузкой фикстур:

```bash
python manage.py flush
python manage.py loaddata initial_data.json
```

> ⚠️ **Важно**: не используйте `flush` в продакшене — она удалит все данные и их восстановление будет невозможно без резервной копии.

### sqlflush

Команда `sqlflush` выводит SQL-инструкции, которые будут выполнены при вызове команды [`flush`](#flush).

Это полезно, если вы хотите:

- Предварительно увидеть, какие SQL-команды будут применены;
- Понять, какие таблицы будут очищены;
- Использовать SQL напрямую (например, для предварительного анализа или отладки).

#### Синтаксис

```
python manage.py sqlflush
```

#### Пример использования

```bash
$ python manage.py sqlflush
BEGIN;
DELETE FROM "myapp_modelname";
DELETE FROM "auth_user";
DELETE FROM "django_session";
...
COMMIT;
```

#### Примечания

- Команда **не выполняет очистку базы данных**, она **только печатает SQL**, который бы использовался.
- Учитывает текущую конфигурацию базы данных и зарегистрированные модели.


### sqlsequencereset

Команда `sqlsequencereset` используется для сброса последовательностей автогенерации идентификаторов (например, `id`) в базе данных. Это важно, когда вы вручную очищаете таблицы и хотите, чтобы следующая вставка начиналась с `id = 1`.

```bash
python manage.py sqlsequencereset <app_label>
```

- `<app_label>` — имя приложения Django, для которого нужно сбросить последовательности.

Например:

```bash
python manage.py sqlsequencereset blog
```

Эта команда не вносит изменений в базу напрямую, а просто **печатает SQL-код**, который необходимо выполнить для сброса последовательностей. Это особенно полезно при ручной очистке таблиц с помощью `flush` или `truncate`.

#### Почему это нужно?

Когда вы удаляете все записи из таблицы вручную (например, через `DELETE FROM`), следующий `id` по умолчанию не будет начинаться с 1, так как значение хранится в последовательности (sequence). `sqlsequencereset` позволяет сбросить эти sequence-объекты, чтобы обеспечить консистентность ID.

⚠️ **Важно:**  
Не применяйте сброс последовательностей на продуктивной базе с пользовательскими данными. Это может привести к конфликтам ключей.

#### Пример вывода:

```sql
SELECT setval(pg_get_serial_sequence('"myapp_mymodel"', 'id'), COALESCE(MAX("id"), 1), max("id") IS NOT null) FROM "myapp_mymodel";
```

Этот SQL-запрос устанавливает значение последовательности `id` в зависимости от текущих данных в таблице.

### inspectdb

Команда `inspectdb` используется для генерации моделей Django на основе уже существующей базы данных.

Это особенно полезно, если вы начинаете работать над проектом с существующей схемой базы данных, которая ранее не использовалась с Django. Вместо того чтобы вручную описывать модели, вы можете сгенерировать их автоматически.

```bash
python manage.py inspectdb
```

Вывод будет содержать Python-код с определениями моделей, которые можно скопировать в файл `models.py` соответствующего приложения.

#### Пример использования

Предположим, у вас есть существующая база данных с таблицами `users` и `orders`. Выполнив команду:

```bash
python manage.py inspectdb > myapp/models.py
```

Вы получите файл `models.py` с автосгенерированными моделями:

```python
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    email = models.EmailField()

    class Meta:
        managed = False
        db_table = 'users'
```

#### Параметры

- `--database`: имя подключения к базе данных, если используется не дефолтное (`default`).
- `--include-partial`: добавляет частично поддерживаемые поля.
- `--table`: позволяет указать конкретные таблицы для генерации моделей.

Пример для одной таблицы:

```bash
python manage.py inspectdb --table users
```

#### Обратите внимание

- Генерируемые модели будут иметь `managed = False`, что означает, что Django не будет пытаться мигрировать эти таблицы.
- После генерации моделей их часто нужно вручную отредактировать: переименовать поля, добавить связи, ограничения и т. д.
- Это хороший старт, но не замена полноценного проектирования моделей вручную.

#### Когда использовать?

- При переносе существующего проекта (например, с PHP или Java) на Django.
- При необходимости подключиться к сторонней базе и использовать Django ORM без миграций.
- Для быстрого создания моделей для репорта или анализа на основе чужой БД.

🧠 **Управление пользователями**

### changepassword

Команда для смены пароля конкретному пользователю.

```manage.py changepassword ringo```

### createsuperuser

Команда для создания пользователя со всеми правами.


## 🌐 **Сервер и консоль**

### shell

Команда `shell` запускает интерактивную Python-консоль с уже настроенной Django-средой. Это означает, что вам не нужно вручную импортировать модели, настройки и другие компоненты проекта — всё уже доступно.

Примеры использования:
```bash
python manage.py shell
```

Полезно для:
- Ручного тестирования функций и моделей
- Временного взаимодействия с ORM
- Быстрого импорта и анализа данных

---

### dbshell

Команда `dbshell` открывает интерактивную консоль для работы с базой данных, указанной в настройках `DATABASES`.

Например, если вы используете PostgreSQL, будет открыт `psql`, если SQLite — обычная SQLite-консоль и т.д.

Примеры:
```bash
python manage.py dbshell
```

Полезно для:
- Прямого выполнения SQL-запросов
- Быстрого анализа или модификации данных на низком уровне
- Отладки проблем с миграциями и схемой

> Убедитесь, что нужный клиент базы данных установлен в системе (например, `psql` для PostgreSQL, `mysql` для MySQL).

---

### runserver

Команда `runserver` запускает встроенный отладочный сервер Django.

Пример:
```bash
python manage.py runserver
```

Можно указать IP и порт:
```bash
python manage.py runserver 0.0.0.0:8000
```

По умолчанию используется порт `8000` и адрес `127.0.0.1`.

Полезно для:
- Разработки и локального тестирования приложения
- Быстрой демонстрации функциональности

> ⚠️ **Важно:** `runserver` не предназначен для продакшена. На боевых серверах используйте WSGI-серверы, такие как Gunicorn, uWSGI, Daphne и т. п.

## 🗃 **Работа с данными (фикстуры)**

### dumpdata

Команда `dumpdata` используется для создания резервной копии данных из базы данных в виде JSON-файла (или в другом формате, если указать).

Это особенно полезно для:

- создания фикстур (fixtures), которые можно использовать для загрузки данных в тестовую или начальную среду;
- резервного копирования состояния отдельных приложений или моделей;
- миграции данных между проектами.

#### Синтаксис

```bash
python manage.py dumpdata [app_label.ModelName] [--indent N] [--output filename.json]
```

#### Примеры использования

- Сохранить все данные из базы:
  ```bash
  python manage.py dumpdata > all_data.json
  ```

- Сохранить данные только из приложения `blog`:
  ```bash
  python manage.py dumpdata blog > blog_data.json
  ```

- Сохранить данные из конкретной модели `Author`:
  ```bash
  python manage.py dumpdata blog.Author > authors.json
  ```

- Сохранять с отступами (удобнее для чтения):
  ```bash
  python manage.py dumpdata blog.Author --indent 2 > authors.json
  ```

- С указанием имени файла напрямую:
  ```bash
  python manage.py dumpdata blog --output blog_data.json
  ```

#### Подсказка

Вы можете комбинировать команды с `--exclude`:
```bash
python manage.py dumpdata --exclude auth.permission --exclude contenttypes > data.json
```

---

### loaddata

Команда `loaddata` загружает данные из JSON-файла (или другого формата фикстур) обратно в базу данных.

Это особенно полезно для:

- восстановления состояния базы из резервной копии;
- начального наполнения базы данных (например, при запуске нового окружения);
- использования в тестах.

#### Синтаксис

```bash
python manage.py loaddata filename.json
```

#### Примеры использования

- Загрузка полного дампа:
  ```bash
  python manage.py loaddata all_data.json
  ```

- Загрузка дампа только моделей `Author`:
  ```bash
  python manage.py loaddata authors.json
  ```

- Загрузка нескольких файлов:
  ```bash
  python manage.py loaddata file1.json file2.json
  ```

#### Подсказка

Фикстуры можно хранить в директориях `fixtures/` в каждом приложении — Django их найдёт автоматически.

---

> **Важно:** При загрузке данных из JSON-файла все `id`, указанные в файле, будут использоваться как есть. Убедитесь, что данные не конфликтуют с уже существующими.

## 📖 **Работа с переводами**

# Команды `makemessages` и `compilemessages` в Django

В Django команды `makemessages` и `compilemessages` используются для организации и управления локализацией (переводом интерфейса на разные языки).

## Команда `makemessages`

Команда `makemessages` используется для создания или обновления файлов перевода (`.po`), которые содержат строки, подлежащие переводу.

### Синтаксис

```bash
python manage.py makemessages -l <locale> [опции]
```

### Основные параметры

- `-l, --locale` — язык перевода (например, `fr`, `pt_BR`, `uk`).
- `--ignore` — шаблон файлов, которые нужно игнорировать.
- `--extension` — расширения файлов, где следует искать переводы (по умолчанию `.html`, `.txt`, `.py`).
- `--domain` — можно указать `djangojs` для перевода JS-файлов.

### Пример

```bash
python manage.py makemessages -l uk
```

Этот вызов создаст (или обновит) файл перевода `uk/LC_MESSAGES/django.po`.

### Где использовать `makemessages`

- В проектах с мультиязычным интерфейсом.
- При локализации текстов, сообщений и шаблонов.
- В любых Django-приложениях, где используется `gettext`, `ugettext`, либо шаблонные теги `{% trans "..." %}`.

### Пример строки перевода

В `views.py`:

```python
from django.utils.translation import gettext as _

def my_view(request):
    output = _("Welcome to my site.")
    return HttpResponse(output)
```

В `.po` файле:

```po
msgid "Welcome to my site."
msgstr "Ласкаво просимо на мій сайт."
```

---

## Команда `compilemessages`

После редактирования `.po` файлов необходимо скомпилировать их в `.mo` файлы, которые используются Django во время выполнения.

### Синтаксис

```bash
python manage.py compilemessages [опции]
```

### Пример

```bash
python manage.py compilemessages
```

Эта команда пройдёт по всем подкаталогам и скомпилирует `.po` файлы в `.mo` файлы.

### Когда использовать `compilemessages`

- После каждого изменения или добавления новых переводов.
- Перед сборкой и деплоем проекта, если используется мультиязычность.

---

## Итоговый сценарий работы с переводами

```bash
# Обнаружение строк для перевода
python manage.py makemessages -l fr

# Перевод строк вручную в файле locale/fr/LC_MESSAGES/django.po

# Компиляция перевода
python manage.py compilemessages
```

> **Важно:** Убедитесь, что в `settings.py` указана настройка `LOCALE_PATHS`, чтобы Django знал, где искать переводы:
>
> ```python
> LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]
> ```
## Написание собственных manage-команд в Django

В Django вы можете создавать собственные команды для `manage.py`, как и встроенные команды (`migrate`, `runserver`, `makemigrations` и т.д.). Это полезно для автоматизации задач: отчёты, массовые изменения в базе, уведомления и др.

### Пример: автоматическое закрытие заказов в пиццерии

Предположим, у нас есть проект пиццерии, и мы хотим, чтобы каждый день в 18:00 система проверяла заказы, которые остались в статусе "открыт", переводила их в статус "manual" и отправляла уведомление владельцу заведения.

### Шаг 1: структура проекта

Создаём команду `close_orders` внутри приложения `orders`:

```
orders/
├── __init__.py
├── models.py
├── management/
│   └── commands/
│       └── close_orders.py
├── tests.py
└── views.py
```

> Папки `management` и `commands` должны быть именно с такими названиями.

### Шаг 2: Реализация команды

```python
from django.core.management.base import BaseCommand
from orders.models import Order
from orders.utils import send_email  # примерная утилита отправки писем

class Command(BaseCommand):
    help = "Close orders which weren't closed manually"

    def handle(self, *args, **options):
        orders = Order.objects.filter(status="opened")
        if orders.exists():
            orders.update(status="manual")
            send_email(
                subject="Unclosed orders",
                message=f"You have {orders.count()} unclosed orders marked as 'manual'.",
                to="owner@example.com"
            )
            self.stdout.write(self.style.SUCCESS("Successfully closed open orders."))
        else:
            self.stdout.write("No open orders to close.")
```

### Шаг 3: Запуск команды

Запустить команду можно вручную:

```bash
python manage.py close_orders
```

### Шаг 4: Автоматизация через CRON (Linux)

Добавьте в расписание `cron` выполнение этой команды каждый день в 18:00:

```cron
0 18 * * 1-5 /usr/bin/python3 /path/to/project/manage.py close_orders
```

> Убедитесь, что активировано правильное виртуальное окружение, или используйте путь до интерпретатора прямо из него.

---

Создание кастомных `manage.py` команд — мощный способ автоматизировать задачи и расширить функциональность вашего проекта.