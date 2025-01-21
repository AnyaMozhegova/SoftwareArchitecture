import hashlib
from typing import Dict

# Функция для создания токена (например, используя SHA256 для примера)
def create_access_token(data: Dict) -> str:
    token = hashlib.sha256(str(data).encode()).hexdigest()
    return token

# Вспомогательная функция для проверки данных пользователя
def verify_user(username: str, password: str, users_db: list) -> dict:
    user_db = next((user for user in users_db if user['username'] == username), None)
    if user_db and user_db['password'] == password:
        return user_db
    return None
