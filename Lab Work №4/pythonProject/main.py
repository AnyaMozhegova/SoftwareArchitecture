from datetime import datetime
from auth import create_access_token
from fastapi import FastAPI, HTTPException, Depends, File, UploadFile
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.responses import JSONResponse

from models.User import User, NewUser, EditUser
from models.User_preferences import UserPreferences, NewUserPreferences,EditUserPreferences
from models.Menu_recommendation import MenuRecommendation,NewMenuRecommendation,EditMenuRecommendation
from models.Recipe import Recipe

app = FastAPI()
bearer_scheme = HTTPBearer()

user_database = {}
user_preferences_database = {}
menu_recommendation_database = {}

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": f"Internal Server Error: {str(exc)}"},
    )
def find_user(token: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    # Find the user by token, and return the user object if found
    user = next((user for user in user_database.values() if user.token == token.credentials), None)
    if user is None:
        raise HTTPException(status_code=401, detail="Ошибка авторизации, отсутствует или неверный токен")
    return user



# User
@app.post("/user/", response_model=User, status_code=201)
async def create_user(new_user: NewUser):
    if new_user.username in [u.username for u in user_database.values()]:
        raise HTTPException(status_code=409, detail="Конфликт пользователь с таким именем уже существует")

    if not new_user.username or not new_user.is_admin or not new_user.password:
        raise HTTPException(status_code=422,
                            detail="Некорректный запрос (например, отсутствие обязательных параметров)")

    # Генерация ID
    user_id = len(user_database) + 1

    # Генерация токена с использованием Auth.py
    token = 'debsmahdb-asdbfasbfb-e9ueyfask-dasdasasd'

    # Создание нового пользователя
    user = User(
        id=user_id,
        token=token,  # Сгенерированный токен
        username=new_user.username,
        is_admin=new_user.is_admin,
        password=new_user.password,
        created_menus=set(),
        preferences=set()
    )

    # Сохранение в базу
    user_database[user_id] = user
    user = User(id=user_id,
                username=new_user.username,
                is_admin=new_user.is_admin,
                created_menus=[])

    user_database[user_id] = user

    return user


@app.get("/user/{user_id}", response_model=User, status_code=200)
async def read_user(user_id: int, our_user: bool = Depends(find_user)):
    if not our_user:
        raise HTTPException(status_code=401, detail="Ошибка авторизации, отсутствует или неверный токен")

    if user_id not in user_database:
        raise HTTPException(status_code=404, detail="Пользователь с указанным user_id не найден")

    if not user_id:
        raise HTTPException(status_code=422,
                            detail="Некорректный запрос (например, отсутствие обязательных параметров)")

    return user_database[user_id]


@app.put("/user/{user_id}", response_model=User, status_code=200)
async def create_user(user_id: int, edit_user: EditUser, our_user: bool = Depends(find_user)):
    if not our_user:
        raise HTTPException(status_code=401, detail="Ошибка авторизации, отсутствует или неверный токен")

    if user_id not in user_database:
        raise HTTPException(status_code=404, detail="Пользователь с указанным user_id не найден")

    if not user_id:
        raise HTTPException(status_code=422,
                            detail="Некорректный запрос (например, отсутствие обязательных параметров)")

    if edit_user.is_admin is not None:
        user_database[user_id].is_admin = edit_user.is_admin
    if edit_user.username is not None:
        user_database[user_id].username = edit_user.username
    if edit_user.password is not None:
        user_database[user_id].password = edit_user.password

    return user_database[user_id]


@app.delete("/user/{user_id}", response_model={}, status_code=204)
async def create_user(user_id: int, our_user: bool = Depends(find_user)):
    if not our_user:
        raise HTTPException(status_code=401, detail="Ошибка авторизации, отсутствует или неверный токен")

    if user_id not in user_database:
        raise HTTPException(status_code=404, detail="Пользователь с указанным user_id не найден")

    if not user_id:
        raise HTTPException(status_code=422,
                            detail="Некорректный запрос (например, отсутствие обязательных параметров)")


    user_database.pop(user_id)

    return {}


# UserPreferences
@app.post("/user_preferences/", response_model=UserPreferences, status_code=201)
async def create_user_preferences(new_preferences: NewUserPreferences, our_user: User = Depends(find_user)):
    if our_user is None:
        raise HTTPException(status_code=401, detail="Ошибка авторизации, отсутствует или неверный токен")

    # Получаем ID пользователя
    user_id = our_user.id

    user_preferences = UserPreferences(
        id=len(user_preferences_database) + 1,
        user_id=user_id,
        budget=new_preferences.budget,
        dietary_preferences=new_preferences.dietary_preferences,
        allergies=new_preferences.allergies,
        created_at=datetime.now(),
    )

    user_preferences_database[user_preferences.id] = user_preferences

    return user_preferences


@app.get("/user_preferences/{preference_id}", response_model=UserPreferences, status_code=200)
async def read_user_preferences(preference_id: int, our_user: bool = Depends(find_user)):
    if not our_user:
        raise HTTPException(status_code=401, detail="Ошибка авторизации, отсутствует или неверный токен")

    if preference_id not in user_preferences_database:
        raise HTTPException(status_code=404, detail="Предпочтения пользователя не найдены")

    return user_preferences_database[preference_id]


@app.put("/user_preferences/{preference_id}", response_model=UserPreferences, status_code=200)
async def update_user_preferences(preference_id: int, edit_preferences: EditUserPreferences, our_user: bool = Depends(find_user)):
    if not our_user:
        raise HTTPException(status_code=401, detail="Ошибка авторизации, отсутствует или неверный токен")

    if preference_id not in user_preferences_database:
        raise HTTPException(status_code=404, detail="Предпочтения пользователя не найдены")

    user_preferences = user_preferences_database[preference_id]

    if edit_preferences.budget is not None:
        user_preferences.budget = edit_preferences.budget
    if edit_preferences.dietary_preferences is not None:
        user_preferences.dietary_preferences = edit_preferences.dietary_preferences
    if edit_preferences.allergies is not None:
        user_preferences.allergies = edit_preferences.allergies

    return user_preferences


@app.delete("/user_preferences/{preference_id}", status_code=204)
async def delete_user_preferences(preference_id: int, our_user: bool = Depends(find_user)):
    if not our_user:
        raise HTTPException(status_code=401, detail="Ошибка авторизации, отсутствует или неверный токен")

    if preference_id not in user_preferences_database:
        raise HTTPException(status_code=404, detail="Предпочтения пользователя не найдены")

    user_preferences_database.pop(preference_id)
    return {}


# MenuRecommendation
@app.post("/menu_recommendation/", response_model=MenuRecommendation, status_code=201)
async def create_menu_recommendation(new_menu: NewMenuRecommendation, our_user: bool = Depends(find_user)):
    if not our_user:
        raise HTTPException(status_code=401, detail="Ошибка авторизации, отсутствует или неверный токен")

    menu_id = len(menu_recommendation_database) + 1
    user_id = next((u.id for u in user_database.values() if u.token == our_user.token), None)

    if not user_id:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    # Преобразуем меню и рецепты
    menu_items = [Recipe.from_dict(item) for item in new_menu.menu_items]

    menu = MenuRecommendation(
        id=menu_id,
        user_id=user_id,
        generated_at=datetime.now(),
        menu_items=menu_items,
        calories=new_menu.calories,
    )

    menu_recommendation_database[menu_id] = menu

    return menu



@app.get("/menu_recommendation/{menu_id}", response_model=MenuRecommendation, status_code=200)
async def read_menu_recommendation(menu_id: int, our_user: bool = Depends(find_user)):
    if not our_user:
        raise HTTPException(status_code=401, detail="Ошибка авторизации, отсутствует или неверный токен")

    if menu_id not in menu_recommendation_database:
        raise HTTPException(status_code=404, detail="Рекомендация меню не найдена")

    return menu_recommendation_database[menu_id]


@app.put("/menu_recommendation/{menu_id}", response_model=MenuRecommendation, status_code=200)
async def update_menu_recommendation(menu_id: int, edit_menu: EditMenuRecommendation, our_user: bool = Depends(find_user)):
    if not our_user:
        raise HTTPException(status_code=401, detail="Ошибка авторизации, отсутствует или неверный токен")

    if menu_id not in menu_recommendation_database:
        raise HTTPException(status_code=404, detail="Рекомендация меню не найдена")

    menu = menu_recommendation_database[menu_id]

    if edit_menu.menu_items is not None:
        menu.menu_items = edit_menu.menu_items
    if edit_menu.calories is not None:
        menu.calories = edit_menu.calories

    return menu


@app.delete("/menu_recommendation/{menu_id}", status_code=204)
async def delete_menu_recommendation(menu_id: int, our_user: bool = Depends(find_user)):
    if not our_user:
        raise HTTPException(status_code=401, detail="Ошибка авторизации, отсутствует или неверный токен")

    if menu_id not in menu_recommendation_database:
        raise HTTPException(status_code=404, detail="Рекомендация меню не найдена")

    menu_recommendation_database.pop(menu_id)
    return {}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
