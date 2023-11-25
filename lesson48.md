# Урок 48. Amazon RDS. S3 bucket. IAM. Route 53. HTTPS.

![](https://lumecloud.com/wp-content/uploads/2017/10/Lume_BraceYourselves-AWS-meme.jpg)

## Сервисы Amazon

Amazon - это не только инстансы, это огромная, нет **ОГРОМНАЯ** экосистема из очень большого количества различных 
сервисов, которые мы можем использовать для своих нужд, там есть почти всё :) даже генераторы нейросетей.

Нас на данном этапе интересует несколько сервисов:

- **RDS** (*Relational Database Service*) - сервис по использованию SQL баз данных, которые будут находиться на Amazon. 
  Зачем это нужно? Во-первых, это надёжно. Мы уверены, что БД находится в облаке, мы за неё платим и Amazon гарантирует
  её сохранность. В случае хранения БД на инстансе, БД в случае чего удалится вместе с инстансом. Во-вторых, в случае
  микросервисной архитектуры микросервисы физически могут находиться на совершенно разных машинах, а требуется
  использовать одну и ту же БД. Облачная БД - лучший для этого выбор. В-третьих, при использовании Amazon RDS не
  требуется настраивать систему резервных копий, она уже предоставлена экосистемой Amazon в несколько кликов.

- **S3 Bucket** - это просто хранилище для файлов. Используется для адекватного хранения статики и медиа. Преимущества 
  очень похожи на RDS. Во-первых, мы не потеряем данные статики и медиа в случае "переезда" на новый сервер. Во-вторых,
  пользовательские медиа могут занимать огромные объемы данных (например, видеофайлы). В случае хранения их на 
  выделенном сервере мы упираемся в размер сервера (чем больше, тем дороже), а расширять сервер только для "картинок и 
  видео" не очень разумно. Стоимость S3 Bucket гораздо меньше и удобнее для этих целей. В-третьих, безопасность, когда 
  вы складываете статику и медиа у себя, доступ к ним есть у всех пользователей. Кто угодно может открыть наш JS 
  почитать, это не очень безопасно, вдруг у нас там дыры. :) С медиа всё еще хуже, это пользовательские данные, а мы
  выставляем их на всеобщее обозрение. Это не очень правильно. При использовании S3 Bucket мы можем настроить
  безопасность, создать пользователя в сервисе IAM (о неё дальше). Django из коробки умеет добавлять безопасный токен
  при использовании Amazon.

- **IAM** - сервис для настроек безопасности. Всё на самом деле просто, там можно создать юзеров и группы юзеров, и 
  раздать им права на любые сервисы Amazon. Допустим, одна группа может только настраивать RDS и смотреть на EC2, а 
  другая обладает полными правами. В нашем случае мы будем создавать пользователя с правами на чтение S3 Bucket и 
  использовать его credentials для статики и медиа.

- **Route 53** - сервис для настройки DNS и регистрации доменов, будем использовать его для того, чтобы купить домен и
  преобразовать наш IP в нормальный URL.

## RDS

Мы будем использовать PostgreSQL.

При создании БД вам будет предложено создать мастер пароль для пользователя `postgres`, его надо запомнить :)

После создания базы данных нужно открыть подробности и раздел `Connectivity & security`:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson48/rds-settings.png)

После чего мы можем открыть PostgreSQL консоль из консоли нашего инстанса:

```psql --host=<DB instance endpoint> --port=<port> --username=<master username> --password```

Создаём пользователя и базу, мы это уже умеем делать.

Допустим, у нас опять user - `myuser`, password - `mypass`, db - `mydb`;

Как подключить RDS к приложению? Добавляем URL в переменные окружения, и база будет подключена.

Не забываем провести миграции, мы подключили новую базу!

## IAM

Для использования S3 Bucket нам необходим специальный юзер, которого мы можем создать в IAM

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson48/IAM-accesslevel.png)

Выбираем `Programmatic access` наш пользователь не будет заходить в настройки, только генерировать токен.

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson48/IAM-permissions.png)

Добавляем пользователю полные права на S3 Bucket.

Обязательно сохраняем ключи от пользователя.

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson48/IAM-creeds.png)

Никогда, нет, **НИКОГДА** не выкладываем эти ключи на git (в `settings.py` или где-либо еще). Amazon мониторит 
абсолютно весь интернет. :) И если ваши ключи окажутся в открытом репозитории, пользователь будет мгновенно 
заблокирован, а владельцу аккаунта напишут об этом письмо и позвонят, чтобы предупредить.

## S3 Bucket

Создадим новый S3 Bucket в регионе `us-east-1`, с ним самая простая настройка.

С полностью закрытым доступом к файлам.

Для использования S3 в нашем проекте нужно доставить Python модули:

```pip install django-storages boto3```

Если вы будете использовать S3 и локально, то можно установить пакеты и локально, но чаще всего для локальных тестов
внешние сервисы не используются.

Для использования нужно добавить `storages` в `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...,
    'storages',
]
```

после чего достаточно добавить настройки:

```python
# Optional
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
# Required
AWS_STORAGE_BUCKET_NAME = 'BUCKET_NAME'
AWS_S3_REGION_NAME = 'REGION_NAME'  # e.g. us-east-2
AWS_ACCESS_KEY_ID = 'xxxxxxxxxxxxxxxxxxxx'
AWS_SECRET_ACCESS_KEY = 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
# НЕ ВПИСЫВАЙТЕ САМИ КЛЮЧИ, ТОЛЬКО os.environ.get('SOME_KEY')

# Tell the staticfiles app to use S3Boto3 storage when writing the collected static files (when
# you run `collectstatic`).
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```

Этого достаточно, чтобы команда `collectstatic` собирала всю статику в S3 Bucket от Amazon, а template tag `static`
генерировал URL с параметрами безопасности, получить такую статику просто так нельзя.

`AWS_S3_OBJECT_PARAMETERS` - необязательный параметр, чтобы указать настройки объектов, параметров довольно много.

Но при такой настройке вся статика будет просто сложена в S3 Bucket, как на свалке, куда же мы поместим медиа?

Чтобы сложить статику и медиа в один S3 Bucket, нужно создать новые классы для storages, где указать папки для хранения
разных типов данных.

Создадим файл `custom_storages.py` на одном уровне с `settings.py`.

```python
# custom_storages.py
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

А в `settings.py` укажем:

```python
# settings.py
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
```

Этого полностью достаточно, чтобы команда `collectstatic` собрала всё статику в папку `static` на S3 Bucket, а любые
загруженные пользователями файлы - в папку `media`.

Добавляем все необходимые переменные окружения, запускаем `collectstatic`, убеждаемся, что всё собрано правильно, и
статика работает, так же можем попробовать загрузить что-либо и убедиться, что медиа грузится правильно (если такой
функционал заложен в проект).

При таком подходе Nginx не обрабатывает статику и медиа, а значит, что эти строки можно не вносить (или удалить из
конфига).

## Route 53

Route 53 - это сервис, где вы можете зарегистрировать домен, и привязать его к вашему IP адресу, чтобы использовать URL,
а не IP.

Я заранее купил домен `a-level-test.com` :) Поэтому, если я открою вкладку `Hosted zones`, то увижу:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson48/hosted-zones.png)

Создам новую запись в `hosted zone`:

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson48/route53-record.png)

В поле `value` я указал IP, который выдал мне Amazon к моему инстансу.

В `settings.py` в `ALLOWED_HOSTS` нужно добавить новый URL.

```python
...
DEBUG = False
ALLOWED_HOSTS = ['a-level-test.com']
...
```

Пулим новый код, перезапускаем gunicorn:

```sudo systemctl restart gunicorn```

После этого мне нужно обновить Nginx и поменять там `server_name`;

```
server {
    listen 80;
    server_name a-level-test.com;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/deployment/r/gunicorn.sock;
    }
}
```

Перезапускаем Nginx:

```sudo service nginx restart```

Открываем URL, убеждаемся, что всё работает и статика не потерялась.

## HTTPS. Certbot

Наше соединение работает, но при этом абсолютно не защищено. Почему мы не сделали его безопасным раньше? Всё просто,
сертификат для включения `https` привязывается к URL, а не к IP адресу.

Сделать это можно очень просто и в практически автоматическом режиме.

Для начала необходимо доставить на сервер некоторые модули:

```sudo apt install certbot python3-certbot-nginx```

И выполнить команду:

```sudo certbot --nginx -d a-level-test.com```

После параметра `-d` указывается `server_name` из Nginx;

Certbot спросит у вас почту, если это первый запуск, попросит принять условия и указать, редиректить небезопасное
соединение в безопасное или нет, всё зависит от ваших условий.

Он автоматически заменит и перезапустит конфигурацию Nginx:

```
server {
    server_name a-level-test.com;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/deployment/r/gunicorn.sock;
    }

    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/a-level-test.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/a-level-test.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}
server {
    if ($host = a-level-test.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    listen 80;
    server_name a-level-test.com;
    return 404; # managed by Certbot


}
```

### Открыть на Amazon 443 порт

Не забываем открыть порт номер 443 для нашего инстанса.

![](https://djangoalevel.s3.eu-central-1.amazonaws.com/lesson48/https-setting.png)

Всё, пробуем открыть сайт и видим, что он теперь безопасен.

### Автообновление сертификата

Сертификаты *Let’s Encrypt* действительны только в течение 90 дней. Это сделано для стимулирования пользователей к
автоматизации процесса обновления сертификатов. Установленный нами пакет `certbot` выполняет это автоматически, добавляя
таймер `systemd`, который будет запускаться два раза в день и автоматически продлевать все сертификаты, истекающие
менее, чем через 30 дней.

Чтобы протестировать процесс обновления, можно сделать запуск «вхолостую» с помощью `certbot`:

```sudo certbot renew --dry-run```

Если ошибок нет, все нормально. Certbot будет продлевать ваши сертификаты, когда это потребуется, и перезагружать Nginx
для активации изменений. Если процесс автоматического обновления когда-нибудь не выполнится, то *Let’s Encrypt*
отправит сообщение на указанный вами адрес электронной почты с предупреждением о том, что срок действия сертификата 
подходит к концу.
