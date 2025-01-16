## *API Документация для веб-приложения персонализированного меню*

### * Регистрация пользователя*

#### *POST /user/*

**Описание:** Регистрация нового пользователя

**Заголовки:**
- ``Content-Type: application/json``

**Входные параметры:**  
Body:  
- `username` (строка) - Имя пользователя
- `password` (строка) - Пароль пользователя
- `is_admain` (булевое) - Является ли пользователь администратором

**Пример входных параметров:**
```json
{
  "username": "anna",
  "is_tourist": true,
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
