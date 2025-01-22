## *API Документация для веб-приложения персонализированного меню*

### *Пользователь:*

#### *1. Создание пользователя*

#### *Метод: POST *
#### *URL: /user *
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
  "preferences": [],
  "allergies": []
  "created_menus": []
}
```

**cURL:**
```
curl -X POST -H "Content-Type: application/json" -d '{"username":"anna", "is_admin":true,"password":"password12020"}' https://api.example.com/user/
```

### *2. Получение данных пользователя*

#### *GET /user/{user_id}*

**Описание:**  Получение данных о пользователе. Возвращает токен для авторизации, данные для аутентификации пользователя

**Заголовки:**
- ``Authorization: Bearer {ваш_токен}``

**Входные параметры:**  
Query:  
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

### *3. Обновление данных пользователя*

#### *PUT /user/{user_id}*
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

### *4. Удаление пользователя*

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
- `calorie_goal` (integer) - Цель по калориям
- `budget` (integer) - Еженедельная цель по бюджету

**Пример входных параметров:**
```json
{
{
  "budget": 2000,
  "dietary_preferences": ["vegetarian"], 
  "allergies": ["nuts", "dairy"]
}

}
```

**Код статусы ответа:**
- `201 Created` Успешное добавление
- `400 Bad Request` Ошибка в данных запроса
- `422 Unprocessable Entity` - Некорректный запрос (например, отсутствие обязательных параметров)

**Пример ответа:**
```json
{
  {
    "id": 1,
    "user_id": 1,
    "budget": 2000.0,
    "dietary_preferences": [
        "vegetarian"
    ],
    "allergies": [
        "dairy",
        "nuts"
    ],
    "created_at": "2025-01-21T21:54:48.346823"
}
}
```

**cURL:**
```
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {ваш_токен}" -d '{"budget":"2000", "dietaryPreferences": "vegetarian", allergies": ["nuts","dairy"]}' https://api.example.com/preferences/456
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
- `200 OK` - Успешный запрос, возвращается информация 
- `401 Unauthorized` - Ошибка авторизации, отсутствует или неверный токен
- `404 Not Found` - Предпочтения с указанным id не найден
- `422 Unprocessable Entity` - Некорректный запрос (например, отсутствие обязательных параметров)

**Пример ответа:**
```json
{
  {
    "id": 1,
    "user_id": 1,
    "budget": 2000.0,
    "dietary_preferences": [
        "vegetarian"
    ],
    "allergies": [
        "dairy",
        "nuts"
    ],
    "created_at": "2025-01-21T21:54:48.346823"
}
}
```

**cURL:** 
```
curl -X GET -H "Authorization: Bearer {ваш_токен}" https://api.example.com/preferences/456
```

### *3. Обновление предпочтений пользователя*

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
  "budget": "1500"
```

**Код статусы ответа:**
- `200 OK` - Успешный запрос, возвращается информация 
- `401 Unauthorized` - Ошибка авторизации, отсутствует или неверный токен
- `404 Not Found` - Предпочтения с указанным id не найден
- `422 Unprocessable Entity` - Некорректный запрос (например, отсутствие обязательных параметров)

**Пример ответа:**
```json
{
  {
    "id": 1,
    "user_id": 1,
    "budget": 1500.0,
    "dietary_preferences": [
        "vegetarian"
    ],
    "allergies": [
        "dairy",
        "nuts"
    ],
    "created_at": "2025-01-21T21:54:48.346823"
}
}
```

**cURL:** 
```
curl -X PUT -H "Content-Type: application/json" -H "Authorization: Bearer {ваш_токен}" -d '{"budget":"1500"}' https://api.example.com/preferences/456
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
- `204 No Content` - Успешное удаление 
- `401 Unauthorized` - Ошибка авторизации, отсутствует или неверный токен
- `404 Not Found` - Предпочтения с указанным id не найдена
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

### *1. Создание меню*

#### *POST/menu_recommendation*

**Описание:** Создание пользовательских предпочтений

**Заголовки:**
- ``Content-Type: application/json``
- ``Authorization: Bearer {ваш_токен}``

**Входные параметры:**  
Body:  
- `menu_items` (массив объектов) - Список рецептов

**Пример входных параметров:**
```json
{
  "menu_items": [
    {
      "id": 1,
      "name": "banana",
      "description": "A ripe banana",
      "ingredients": "Banana",
      "calories": 100,
      "tags": ["fruit", "snack"]
    },
    {
      "id": 2,
      "name": "sup",
      "description": "A vegetable soup",
      "ingredients": "Water, carrots, onions, spices",
      "calories": 150,
      "tags": ["vegetarian", "soup"]
    }
  ],
  "calories": 2000
}

```

**Код статусы ответа:**
- `201 Created` Успешное добавление
- `400 Bad Request` Ошибка в данных запроса
- `422 Unprocessable Entity` - Некорректный запрос (например, отсутствие обязательных параметров)

**Пример ответа:**
```json
{
    "id": 1,
    "user_id": 1,
    "generated_at": "2025-01-21T22:07:10.102070",
    "menu_items": [
        {
            "id": 1,
            "name": "banana",
            "description": "A ripe banana",
            "ingredients": "Banana",
            "calories": 100.0,
            "tags": [
                "snack",
                "fruit"
            ]
        },
        {
            "id": 2,
            "name": "sup",
            "description": "A vegetable soup",
            "ingredients": "Water, carrots, onions, spices",
            "calories": 150.0,
            "tags": [
                "soup",
                "vegetarian"
            ]
        }
    ],
    "calories": 2000.0
}
```

**cURL:**
```
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {ваш_токен}" -d '{menu_items": [{"id": 1, "name": "banana", "description": "A ripe banana", "ingredients": "Banana", "calories": 100.0,"tags": ["snack","fruit"]},{"id": 2,"name": "sup","description": "A vegetable soup","ingredients": "Water, carrots, onions, spices","calories": 150.0,"tags": [ "soup", "vegetarian"]}], "calories": 2000.0 }' https://api.example.com/preferences/456
```

### *2. Получение меню*

#### *GET /menu_recommendation/{menu_recommendation_id}*

**Описание:** Получение предпочтений пользователя

**Заголовки:**
- `Authorization: Bearer {ваш_токен}`

**Входные параметры:**  
Query:  
- `menu_recommendation_id` (intenger) - Идентификатор меню

**Пример входных параметров:**
```
/preferences_id/456
```

**Код статусы ответа:**
- `200 OK` - Успешный запрос, возвращается информация
- `401 Unauthorized` - Ошибка авторизации, отсутствует или неверный токен
- `404 Not Found` - Меню с указанным id не найден
- `422 Unprocessable Entity` - Некорректный запрос (например, отсутствие обязательных параметров)

**Пример ответа:**
```json
{
    "id": 1,
    "user_id": 1,
    "generated_at": "2025-01-21T22:07:10.102070",
    "menu_items": [
        {
            "id": 1,
            "name": "banana",
            "description": "A ripe banana",
            "ingredients": "Banana",
            "calories": 100.0,
            "tags": [
                "snack",
                "fruit"
            ]
        },
        {
            "id": 2,
            "name": "sup",
            "description": "A vegetable soup",
            "ingredients": "Water, carrots, onions, spices",
            "calories": 150.0,
            "tags": [
                "soup",
                "vegetarian"
            ]
        }
    ],
    "calories": 2000.0
}
```

**cURL:** 
```
curl -X GET -H "Authorization: Bearer {ваш_токен}" https://api.example.com/preferences/456
```

## *Тестирование*

### *Пользователь:*

#### *POST*
![image](https://github.com/user-attachments/assets/84a272cb-03ca-4dfe-886d-1b0fc64ff438)
![image](https://github.com/user-attachments/assets/e1746cc4-71b4-4ef5-9c91-12a1099be924)
![image](https://github.com/user-attachments/assets/679f07e8-ae7e-43d2-8009-97840a9d0ef7)
![image](https://github.com/user-attachments/assets/568b7e22-95b4-457f-a097-577ac1780a57)
![image](https://github.com/user-attachments/assets/6e13217a-ebf3-4cf5-9c18-32b5c5af59ea)
![image](https://github.com/user-attachments/assets/d4f5bc19-735c-4666-ae7b-7346ec997415)
#### *GET*
![image](https://github.com/user-attachments/assets/02a262e9-6b59-44f4-b531-2254d3b413b9)
![image](https://github.com/user-attachments/assets/0d456e1e-5a87-4a2d-9da0-0233023b2a23)
![image](https://github.com/user-attachments/assets/9026163e-bd95-4003-98f6-13cd7152069b)
![image](https://github.com/user-attachments/assets/34d69bc9-7ea6-43c2-8558-9281f914eaff)
#### *PUT*
![image](https://github.com/user-attachments/assets/da2acace-90ae-4d3f-afe4-9c3467f11ff5)
![image](https://github.com/user-attachments/assets/5774f489-3670-40e4-9e25-75ea16df76aa)
![image](https://github.com/user-attachments/assets/2e162124-40f3-4302-ad97-aca74ee2f787)
![image](https://github.com/user-attachments/assets/49d3f06a-b557-4170-a867-97b654840fe5)
#### *DELETE*
![image](https://github.com/user-attachments/assets/c988f51a-c07e-4af1-ab40-a31d5118d38c)
![image](https://github.com/user-attachments/assets/b8eee3a7-1bb7-4e74-9e20-2bcf8f0b46cf)
![image](https://github.com/user-attachments/assets/cd4b8fae-07a6-4c08-a27c-59b9b7759c8d)
![image](https://github.com/user-attachments/assets/af943a7c-c8be-4eb6-8aba-ce5e247a3fe1)

### *Предпочтения:*

#### *POST*
![image](https://github.com/user-attachments/assets/55cfe4c6-6dc5-4e86-a0b0-566944a03c83)
![image](https://github.com/user-attachments/assets/afb3b07d-a1e7-4efd-bb2d-a8e256719bad)
![image](https://github.com/user-attachments/assets/f3ae332b-c761-467b-802c-7518d794a57b)
![image](https://github.com/user-attachments/assets/01861141-6edc-4c87-9c8b-595594c46a53)
#### *GET*
![image](https://github.com/user-attachments/assets/57d93d6d-f949-4bbc-bc58-85804614f457)
![image](https://github.com/user-attachments/assets/a381a8cf-81d3-4181-8b9a-d7c24369e24a)
![image](https://github.com/user-attachments/assets/021f978f-cac5-465b-8060-1252685e61af)
![image](https://github.com/user-attachments/assets/d43167da-c0dc-4609-8525-c72f383a10e5)
#### *PUT*
![image](https://github.com/user-attachments/assets/9cba36d8-352a-41be-ba4e-5b639ea14bdd)
![image](https://github.com/user-attachments/assets/63f881cb-3f25-44b5-9179-caa4d735450d)
![image](https://github.com/user-attachments/assets/8fdf4e44-8a14-49d7-98aa-5a6e9f59138e)
![image](https://github.com/user-attachments/assets/5f4947bb-fefe-4b79-af35-d49fb863d89d)
#### *DELETE*
![image](https://github.com/user-attachments/assets/55acd402-3b63-489c-8106-7a5d66343092)
![image](https://github.com/user-attachments/assets/20625009-3a6f-496b-8f21-d72a83689372)
![image](https://github.com/user-attachments/assets/6bc7ec1c-8cb4-453e-af8c-29eef68781ed)
![image](https://github.com/user-attachments/assets/35b83e53-2044-4ad7-bf34-2fd109b709b0)

### *Меню:*

#### *POST*
![image](https://github.com/user-attachments/assets/49a211d1-8d75-4d23-80b2-5d5a1e34f26d)
![image](https://github.com/user-attachments/assets/4bf51bab-fdc2-45ba-9c28-6885ce0b39c3)
![image](https://github.com/user-attachments/assets/8e6067a3-070b-4908-b588-e62cdc8edff5)
![image](https://github.com/user-attachments/assets/d63a590d-ffb6-476a-b4ae-3491297db3ae)
![image](https://github.com/user-attachments/assets/1de9213e-296e-4cfc-bdfc-f9b7d7055af5)
#### *GET*
![image](https://github.com/user-attachments/assets/c169c473-3b4d-4b1e-bed3-790638b6fe04)
![image](https://github.com/user-attachments/assets/394f0696-fed9-4201-9965-732dea13802e)
![image](https://github.com/user-attachments/assets/d5378b89-fb01-4ca4-be12-b489e82fafc7)
![image](https://github.com/user-attachments/assets/6049d945-0c03-4ddd-b714-41540bea5d63)
![image](https://github.com/user-attachments/assets/0d3724c3-5802-42b9-aeac-c0ce34b67237)



