
# Job Portal

Основная функциональность:
- Авторизация и аутентификация пользователей
- Добавление, удаление и изменение вакансий
- Добавление, удаление и изменение организаций
- Restful API используя Django REST Framework
- API документация используя swagger


## API

#### Все вакансии

```http
  GET /api/jobs
```


#### Информация об одной вакансии

```http
  GET /api/jobs/<int:job_id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Нужен ID запрашиваемой вакансии |



#### Все организации

```http
  GET /api/organizations
```


#### Информация об одной организации

```http
  GET /api/organizations/<int:organization_id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Нужен ID запрашиваемой организации |

...
## Run Locally

Склонируйте проект

```bash
  git clone https://github.com/narmatov-asylbek/job-project
```

Перейдите в директорию


Создайте виртуальное окружение

```bash
  python3 -m venv env
```
Активируйте виртуальное окружение

```bash
  source env/bin/activate
```
Установите все необходимое

```bash
  pip3 install -r requirements.py
```

Сделайте миграции

```bash
  ./manage.py migrate
```

Запустите сервер

```bash
  ./manage.py runserver
```
  
