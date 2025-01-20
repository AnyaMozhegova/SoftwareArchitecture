## *API Документация для веб-приложения персонализированного меню*

### *Пользователь:*

#### *1. Создание пользователя*

#### *POST/user*

**Описание:** Регистрация (создание) пользователя. Возвращает токен для авторизации, данные для аутентификации пользователя

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
  "is_admin": true,
  "preferences": ""
  "allergies": ""
  "history": ""
}
```

**cURL:**
```
curl -X POST -H "Content-Type: application/json" -d '{"username":"anna", "is_admin":true,"password":"password12020"}' https://api.example.com/user/
```

### *2. Получение данных пользователя*

#### *POST /user/{user_id}*

**Описание:**  Получение данных о пользователе. Возвращает токен для авторизации, данные для аутентификации пользователя

**Заголовки:**
- ``Content-Type: application/json``

**Входные параметры:**  
Body:  
- `user_id` (intenger) - Идентификатор пользователя

**Пример входных параметров:**
```json
{  /user/123
}
```

**Код статусы ответа:**
- `200 OK` Успешная авторизация
- `401 Unauthorized`  Неверные учетные данные
- `404 Not Found` - Пользователь с указанным user_id не найден
- `422 Unprocessable Entity` - Некорректный запрос (например, отсутствие обязательных параметров)


**Пример ответа:**
```json
{
  "token": "debsmahdb-asdbfasbfb-e9ueyfask-dasdasasd",
  "user_id": 123,
  "username": "anna",
  "is_admin": true,
  "preferences": ""
  "allergies": ""
  "history": ""
}
```

**cURL:**
```
curl -X GET -H "Authorization: Bearer {ваш_токен}" https://api.example.com/user/123

```
### *3. Обновление юзера*
**Описание:** Обновление данных пользователя. Возвращает токен для авторизации, данные для аутентификации пользователя (обновлённые) 

**Заголовки:**
- `Content-Type: application/json`
- `Authorization: Bearer {ваш_токен}`

**Входные параметры:**  
Query: 

- `user_id` (integer) - Идентификатор пользователя

Body:  
- `username` (string) - Имя пользователя
- `password` (string) - Пароль пользователя
- `is_admin` (boll) - Является ли пользователь администратором


**Пример входных параметров:**
```
/user/123
```
```json
{
  "username": "anna",
  "is_admin": true,
  "password": "password12020"
}
```

**Код статусы ответа:**
- `200 OK` - Успешное обновление данных пользователя
- `401 Unauthorized` - Ошибка авторизации, отсутствует или неверный токен
- `404 Not Found` - Пользователь с указанным user_id не найден
- `422 Unprocessable Entity` - Некорректный запрос (например, отсутствие обязательных параметров)

**Пример ответа:**
```json
{
   "token": "debsmahdb-asdbfasbfb-e9ueyfask-dasdasasd",
   "user_id": 123,
   "username": "anna",
   "is_admin": true,
   "preferences": ""
   "allergies": ""
   "history": ""
}
```

**cURL:** 
```
curl -X PUT -H "Content-Type: application/json" -H "Authorization: Bearer {ваш_токен}" -d '{"username":"anna","is_admin": true,"password":"new_password12020"}' https://api.example.com/user/123
```

### *4. Удаление юзера*
#### *DELETE /user/{user_id}*

**Описание:** Удаление пользователя. Смотрим на код статусы.

**Заголовки:**
- `Authorization: Bearer {ваш_токен}`

**Входные параметры:**  
Query:  
- `user_id` (integer) - Идентификатор пользователя

**Пример входных параметров:**
```
/user/123
```

**Код статусы ответа:**
- `204 No Content` - Успешное удаление пользователя
- `401 Unauthorized` - Ошибка авторизации, отсутствует или неверный токен
- `404 Not Found` - Пользователь с указанным user_id не найден
- `422 Unprocessable Entity` - Некорректный запрос (например, отсутствие обязательных параметров)

**Пример ответа:**
```json
{}
```

**cURL:** 
```
curl -X DELETE -H "Authorization: Bearer {ваш_токен}" https://api.example.com/user/123
```

### *Предпочтения:*

### *1. Настройка предпочтений пользователя*

#### *POST/preferences*

**Описание:** Создание пользовательских предпочтений

**Заголовки:**
- ``Content-Type: application/json``
- ``Authorization: Bearer {ваш_токен}``

**Входные параметры:**  
Body:  
- `dietaryPreferences` (string) - Тип диеты (например, "vegan", "gluten-free")
- `allergies` (array) - Список аллергенов
- `calorie_goal` (integer) - Цель по калориям
- `budget` (integer) - Еженедельная цель по бюджету

**Пример входных параметров:**
```json
{
  "budget": "2000",
  "dietaryPreferences":"vegetarian"
  "calorie_goal": "2000"
  "allergies": ["nuts", "dairy"]
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
  "preferences_id": 456,
  "user_id": "123",
  "budget": "2000",
  "dietaryPreferences":"vegetarian"
  "calorie_goal": "2000"
  "allergies": ["nuts", "dairy"]
}
```

**cURL:**
```
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {ваш_токен}" -d '{"budget":"2000", "dietaryPreferences": "vegetarian", "calorie_goal": "2000", allergies": ["nuts","dairy"]}' https://api.example.com/preferences/456
```

### *2. Получение предпочтений пользователя*

#### *GET /preferences/{preferences_id}*

**Описание:** Получение предпочтений пользователя

**Заголовки:**
- `Authorization: Bearer {ваш_токен}`

**Входные параметры:**  
Query:  
- `preferences_id` (intenger) - Идентификатор предпочтений

**Пример входных параметров:**
```
/preferences_id/456
```

**Код статусы ответа:**
- `200 OK` - Успешный запрос, возвращается информация о маршруте
- `401 Unauthorized` - Ошибка авторизации, отсутствует или неверный токен
- `404 Not Found` - Маршрут с указанным route_id не найден
- `422 Unprocessable Entity` - Некорректный запрос (например, отсутствие обязательных параметров)

**Пример ответа:**
```json
{
  "preferences_id": 456,
  "user_id": "123",
  "budget": "2000",
  "dietaryPreferences":"vegetarian"
  "calorie_goal": "2000"
  "allergies": ["nuts", "dairy"]
}
```

**cURL:** 
```
curl -X GET -H "Authorization: Bearer {ваш_токен}" https://api.example.com/preferences/456
```

### *3. Получение предпочтений пользователя*

#### *PUT /preferences/{preferences_id}*

**Описание:** Обновление пользовательских предпочтений

**Заголовки:**
- `Authorization: Bearer {ваш_токен}`

**Входные параметры:**  
Query:  
- `preferences_id` (intenger) - Идентификатор предпочтений
- `Authorization: Bearer {ваш_токен}`

**Пример входных параметров:**
```
  "budget": "2000",
  "dietaryPreferences":"vegetarian"
  "calorie_goal": "2000"
  "allergies": ["nuts", "dairy"]
```

**Код статусы ответа:**
- `200 OK` - Успешный запрос, возвращается информация о маршруте
- `401 Unauthorized` - Ошибка авторизации, отсутствует или неверный токен
- `404 Not Found` - Маршрут с указанным route_id не найден
- `422 Unprocessable Entity` - Некорректный запрос (например, отсутствие обязательных параметров)

**Пример ответа:**
```json
{
  "preferences_id": 456,
  "user_id": "123",
  "budget": "2000",
  "dietaryPreferences":"vegetarian"
  "calorie_goal": "2000"
  "allergies": ["nuts", "dairy"]
}
```

**cURL:** 
```
curl -X PUT -H "Content-Type: application/json" -H "Authorization: Bearer {ваш_токен}" -d '{"budget":"2000", "dietaryPreferences": "vegetarian", "calorie_goal": "2000", allergies": ["nuts","dairy"]}' https://api.example.com/preferences/456
```

### *4. Удаление предпочтений пользователя*

#### *DELETE /preferences/{preferences_id}*

**Описание:** Удаление пользовательских предпочтений

**Заголовки:**
- `Authorization: Bearer {ваш_токен}`

**Входные параметры:**  
Query:  
- `preferences_id` (integer) - Идентификатор предпочтений

**Пример входных параметров:**
```
/preferences_id/456
```

**Код статусы ответа:**
- `204 No Content` - Успешное удаление точки интереса
- `401 Unauthorized` - Ошибка авторизации, отсутствует или неверный токен
- `404 Not Found` - Точка интереса с указанным point_id не найдена
- `422 Unprocessable Entity` - Некорректный запрос (например, отсутствие обязательных параметров)

**Пример ответа:**
```json
{}
```

**cURL:** 
```
curl -X DELETE -H "Authorization: Bearer {ваш_токен}" https://api.example.com/preferences/456
```


### *Меню:*


### *1. Получение меню*

#### *GET /menus/{menu_id}*

**Описание:** Получение меню

**Заголовки:**
- ``Content-Type: application/json``

**Входные параметры:**  
Body:  



**Пример входных параметров:**
```json
{
 /menus/789 
}
```

**Код статусы ответа:**
- `200 OK` - Успешный запрос, возвращается информация о точке интереса
- `401 Unauthorized` - Ошибка авторизации, отсутствует или неверный токен
- `404 Not Found` - Точка интереса с указанным point_id не найдена
- `422 Unprocessable Entity` - Некорректный запрос (например, отсутствие обязательных параметров)

**Пример ответа:**
```json
{
  "menu_id": 456,
  "user_id": "123",
  "menuItems": ["nuts", "dairy"],
  "calories": "2000"
}
```
cURL:
```
curl -X GET -H "Authorization: Bearer {ваш_токен}" https://api.example.com/menus/789
```
Рецепты:

### * 1. Получение рецепта*

#### *GET  recipe/{recipe_id}*
**Описание:** Получение меню

**Заголовки:**
- ``Content-Type: application/json``

**Входные параметры:**  
Body:  
- 


**Пример входных параметров:**
```json
{
 /recipe/789 
}
```

**Код статусы ответа:**
- `200 OK` - Успешный запрос, возвращается информация о точке интереса
- `401 Unauthorized` - Ошибка авторизации, отсутствует или неверный токен
- `404 Not Found` - Точка интереса с указанным point_id не найдена
- `422 Unprocessable Entity` - Некорректный запрос (например, отсутствие обязательных параметров)

**Пример ответа:**
```json
{
 
}
```
cURL:
```
curl -X GET -H "Authorization: Bearer {ваш_токен}" https://api.example.com/menus/789
```
