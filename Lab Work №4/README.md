## *API Документация для веб-приложения персонализированного меню*

### *1. Регистрация пользователя*

#### *POST /user/register*

**Описание:** Регистрация нового пользователя

**Заголовки:**
- ``Content-Type: application/json``

**Входные параметры:**  
Body:  
- `username` (string) - Имя пользователя
- `password` (string) - Пароль пользователя
- `is_admin` (boll) - Является ли пользователь администратором

**Пример входных параметров:**
```json
{
  "username": "anna",
  "is_admin": true,
  "password": "password12020"
}
```

**Код статусы ответа:**
- `201 Created` Успешная регистрация
- `400 Bad Request` Ошибка в данных запроса
- `409 Conflict` - Конфликт пользователь с таким именем уже существует
- `422 Unprocessable Entity` - Некорректный запрос (например, отсутствие обязательных параметров)

**Пример ответа:**
```json
{
  "token": "debsmahdb-asdbfasbfb-e9ueyfask-dasdasasd",
  "user_id": 123,
  "username": "anna",
  "is_tourist": true,
  "preferences": ""
  "allergies": ""
  "history": ""
}
```

**cURL:**
```
curl -X POST -H "Content-Type: application/json" -d '{"username":"anna","password":"password12020"}' https://api.example.com/api/v1/users/register

```
### *2. Авторизация пользователя*

#### *POST /user/login*

**Описание:** Авторизация пользователя и получение JWT-токена

**Заголовки:**
- ``Content-Type: application/json``

**Входные параметры:**  
Body:  
- `username` (string) - Имя пользователя
- `password` (string) - Пароль пользователя


**Пример входных параметров:**
```json
{  "username": "anna",
  "password": "password12020"
  
}
```

**Код статусы ответа:**
- `200 OK` Успешная авторизация
- `401 Unauthorized`  Неверные учетные данные


**Пример ответа:**
```json
{
  "token": "abc1234def5678ghi90",
}
```

**cURL:**
```
curl -X POST -H "Content-Type: application/json" -d '{"username":"anna","password":"password12020"}' https://api.example.com/api/v1/users/login

```
### *3. Получение списка рецептов*

#### *GET /api/v1/recipes*

**Описание:** Получение списка рецептов с учетом пользовательских предпочтений и ограничений

**Заголовки:**
- ``Content-Type: application/json``

**Входные параметры:**  
Body:  
- `diet` (string): Тип диеты (например, "vegetarian").
- `allergies` (array): Список аллергенов.
- `page` (integer): Номер страницы (по умолчанию 1).
- `limit` (integer): Количество рецептов на странице (по умолчанию 10).

**Пример входных параметров:**
```json
{  "username": "anna",
  "password": "password12020"
  
}
```

**Код статусы ответа:**
- `200 OK` Успешный запрос


**Пример ответа:**
```json
{
  {
  "recipes": [
    {
      "id": "1",
      "name": "Vegetarian Pasta",
      "ingredients": ["pasta", "tomato sauce", "vegetables"],
      "instructions": "Boil pasta. Add sauce. Mix vegetables."
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 5
  }
}

}
```
### *4. Настройка предпочтений пользователя*

#### *POST  users/preferences*

**Описание:** Установка или обновление пользовательских предпочтений

**Заголовки:**
- ``Content-Type: application/json``
- ``Authorization: Bearer <token>``
  
**Входные параметры:**  
Body:  
- `diet` (string) - Тип диеты (например, "vegan", "gluten-free")
- `allergies` (array) - Список аллергенов
- `calorie_goal` (integer) - Ежедневная цель по калориям

**Пример входных параметров:**
```json
{ 
  "diet": "vegetarian",
  "allergies": ["nuts", "dairy"],
  "calorie_goal": 2000

}
```

**Код статусы ответа:**
- `200 OK` Успешный запрос
- `400 Bad Request` - Ошибка в данных запроса


**Пример ответа:**
```json
{
  "message": "Preferences updated successfully"

}

```
**cURL:**
```
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer abc1234def5678ghi90" -d '{"diet":"vegetarian","allergies":["nuts","dairy"],"calorie_goal":2000}' https://api.example.com/api/v1/users/preferences

```
### * 5. Получение списка администраторов*

#### *POST  admins/*

**Описание:**  Получение списка всех администраторов

**Заголовки:**
- ``Authorization: Bearer <token>``
  

**Код статусы ответа:**
- `200 OK` Успешный запрос
- `400 Bad Request` - Ошибка в данных запроса


**Пример ответа:**
```json
{
{
  "admins": [
    {
      "id": 1,
      "username": "admin1",
      "email": "admin1@example.com"
    },
    {
      "id": 2,
      "username": "admin2",
      "email": "admin2@example.com"
    }
  ]
}


}

```
**cURL:**
```
curl -X GET -H "Authorization: Bearer admin12345token" https://api.example.com/api/v1/admins

```
### * 6. Генерация меню на неделю *

#### *POST  menu/generate*

**Описание:**  Генерация персонального меню на неделю на основе пользовательских предпочтений

**Заголовки:**
- ``Content-Type: application/json``
- ``Authorization: Bearer <token>``

**Входные параметры:**  
Body:  
- `diet` (string) - Тип диеты (например, "vegan", "gluten-free")
- `allergies` (array) - Список аллергенов
- `calorie_goal` (integer) - Ежедневная цель по калориям
- `budget` (integer) - Максимальный бюджет на неделю

**Пример входных параметров:**
```json
{ 
  "diet": "vegetarian",
  "allergies": ["nuts", "dairy"],
  "calorie_goal": 2000
  "budget": 2000
}
```


**Код статусы ответа:**
- `200 OK` Успешный запрос
- `400 Bad Request` - Ошибка в данных запроса


**Пример ответа:**
```json
{
  "menu": [
    {
      "day": "Monday",
      "meals": [
        {
          "name": "Oatmeal with Fruits",
          "calories": 350,
          "ingredients": ["oats", "milk", "banana"]
        },
        {
          "name": "Vegetable Soup",
          "calories": 250,
          "ingredients": ["carrot", "celery", "potato"]
        }
      ]
    }
  ]
}


```
**cURL:**
```
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer abc1234def5678ghi90" -d '{"budget":5000}' https://api.example.com/api/v1/menu/generate

```
### * 7. Удаление учетной записи пользователя *

#### *DELETE   users/{user_id}*

**Описание:**  Удаление учетной записи текущего пользователя

**Заголовки:**
- ``Authorization: Bearer <token>``

**Входные параметры:**  

Query::  
- `id` (integer) - Идентификатор юзера


**Пример входных параметров:**
```json
{ 
  /users/9
}
```


**Код статусы ответа:**
- `204 No Content` - Успешное удаление материала
- `401 Unauthorized` - Ошибка авторизации, отсутствует или неверный токен
- `404 Not Found` - Юзер с указанным user_id не найден
- `422 Unprocessable Entity` - Некорректный запрос (например, отсутствие обязательных параметров)


**Пример ответа:**
```json
{
}
```
**cURL:**
```
curl -X DELETE -H "Authorization: Bearer abc1234def5678ghi90" https://api.example.com/api/v1/users/profile

```
### * 8. Обновление профиля пользователя *

#### *PUT    users/{user_id}*

**Описание:** Обновление данных профиля пользователя

**Заголовки:**
- ``Content-Type: application/json``
- ``Authorization: Bearer <token>``

**Входные параметры:**  

Body:  
- `username` (string, опционально) - Новое имя пользователя
- `password` (string, опционально) - Новая электронная почта


**Пример входных параметров:**
```json

  {
  "username": "new_username",
  "password": "new_password",
 
}

```


**Код статусы ответа:**
- `200 OK` Успешный запрос
- `400 Bad Request` - Ошибка в данных запроса
- `401 Unauthorized` - Ошибка авторизации, отсутствует или неверный токен



**Пример ответа:**
```json
{
  "message": "Profile updated successfully"
}

```
**cURL:**
```
curl -X PUT -H "Content-Type: application/json" -H "Authorization: Bearer abc1234def5678ghi90" -d '{"username":"new_username","email":"new_email@example.com","calorie_goal":1800}' https://api.example.com/api/v1/users/profile

```
