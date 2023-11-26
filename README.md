# Трекер привычек
Данный проект представляет собой **бэкэнд-часть SPA веб-приложения**, основной функционал которого построен на создании **привычек** и контроля за ними.

## Содержание
- [Технологии](#технологии)
- [Начало работы](#начало-работы)
- [Функциональные возможности](#функциональные-возможности)

## Технологии
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [DRF](https://www.django-rest-framework.org/)
- [Celery](https://docs.celeryq.dev/en/stable/)


## Начало работы
После клонирования проекта, рекомендуется:

Установить виртуальное окружение:
```sh
$ python3 -m vevn venv
```

Установить список зависимостей:
```sh
$ pip install -r requirements.txt
```

Отредактировать .env файл под себя:
```python
# Debug
DEBUG=True
...
```

Зависимости:
```python
django
psycopg2-binary
djangorestframework
djangorestframework-simplejwt
celery
django_celery_beat
redis
requests
django-cors-headers
coverage
python-dotenv
drf-yasg
ipython
```

## Функциональные возможности
1. **CRUD для привычек**: реализован механизм создания, чтения, обновления и удаления привычек. Пользователи могут добавлять новые привычки, просматривать существующие и удалять те, которые им больше не нужны.
2. **Создание пользователя**: имеются две команды:```python3 manage.py createuser``` и ```python3 manage.py createsuperuser```, а также соответствующие _эндпоинты_.
3. **Отложенные задачи**: подключен```celery```, который создает отложенные привычки по времени заданным при их создании.
4. **Интеграция с Telegram**: настроено получение```chat_id```пользователем, который запустил```bot`а```и выполнил команду```get_tg_chat_id```.\
По этому```tg_chat_id```и отправляется привычки принадлежащие текущему пользователю.
5. **Регистрация и верификация пользователей**: реализована регистрация пользователей через почту, а также механизм верификации для подтверждения почтового ящика.

### Сущности системы
**Привычка**: относится к текущему пользователю и может обладать статусом _полезной_, связывать себя с другой привычкой (если проходит валидацию) или обладать _вознаграждением_.\
Созданная привычка имеет такой макет (str)```я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]```.\
**Пользователь**: имеет **3** обязательных к заполнению поля: _email, password и tg_chat_id_.\

### Права доступа
* Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.
* Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.

### Валидаторы
* Исключен одновременный выбор связанной привычки и указания вознаграждения.
* Время выполнения привычки не больше 120 секунд.
* В связанные привычки могут попадать только привычки с признаком приятной привычки.
* У приятной привычки не может быть вознаграждения или связанной привычки.
* Нельзя выполнять привычку реже, чем 1 раз в 7 дней.

### Эндпоинты
* Регистрация
* Авторизация
* Список привычек текущего пользователя с пагинацией
* Список публичных привычек
* Создание привычки
* Редактирование привычки
* Удаление привычки