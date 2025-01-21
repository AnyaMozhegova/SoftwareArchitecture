from dataclasses import dataclass
from typing import Set, Any
from models.Menu_recommendation import MenuRecommendation
from models.User_preferences import UserPreferences
from utils.serialization import from_int, from_str, from_bool, from_set, to_class


@dataclass
class User:
    id: int
    token: str
    username: str
    is_admin: bool
    password: str
    created_menus: Set[MenuRecommendation]
    preferences: Set[UserPreferences]  # Связь с UserPreferences (множество предпочтений)

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        token = from_str(obj.get("token"))
        username = from_str(obj.get("username"))
        password = from_str(obj.get("password"))
        is_admin = from_bool(obj.get("is_admin"))
        created_menus = from_set(MenuRecommendation.from_dict, obj.get("created_menus"))
        preferences = from_set(UserPreferences.from_dict, obj.get("preferences", []))  # Чтение предпочтений
        return User(id, token, username, is_admin, password, created_menus, preferences)

    def to_dict(self) -> dict:
        return {
            "id": from_int(self.id),
            "token": from_str(self.token),
            "username": from_str(self.username),
            "password": from_str(self.password),
            "is_admin": from_bool(self.is_admin),
            "created_menus": [menu.to_dict() for menu in self.created_menus],
            "preferences": [preference.to_dict() for preference in self.preferences],  # Сериализация предпочтений
        }

def user_from_dict(s: Any) -> User:
    return User.from_dict(s)


def user_to_dict(x: User) -> Any:
    return to_class(User, x)

@dataclass
class NewUser:
    username: str
    is_admin: bool
    password: str | None = None  # токен будет сгенерирован позже
    created_menus: Set[MenuRecommendation] | None = None  # Можно передать меню, если нужно
    preferences: Set[UserPreferences] | None = None  # Можно передать предпочтения, если нужно

    @staticmethod
    def from_dict(obj: Any) -> 'NewUser':
        assert isinstance(obj, dict)
        # id и token можно не передавать, они будут генерироваться при создании
        id = from_int(obj.get("id", 0))  # по умолчанию id будет 0, если не передан
        token = from_str(obj.get("token", ""))
        username = from_str(obj.get("username"))
        is_admin = from_bool(obj.get("is_admin"))
        password = from_str(obj.get("password"))
        created_menus = from_set(MenuRecommendation.from_dict, obj.get("created_menus", []))
        preferences = from_set(UserPreferences.from_dict, obj.get("preferences", []))
        return NewUser(id, token, username, is_admin, password, created_menus, preferences)

    def to_dict(self) -> dict:
        return {
            "id": from_int(self.id) if self.id else None,  # id может быть None
            "token": from_str(self.token) if self.token else None,  # токен может быть None
            "username": from_str(self.username),
            "is_admin": from_bool(self.is_admin),
            "password": from_str(self.password) if self.password else None,
            "created_menus": [menu.to_dict() for menu in self.created_menus] if self.created_menus else [],
            "preferences": [preference.to_dict() for preference in self.preferences] if self.preferences else [],
        }

def new_user_from_dict(s: Any) -> NewUser:
    return NewUser.from_dict(s)

def new_user_to_dict(x: NewUser) -> Any:
    return to_class(NewUser, x)

@dataclass
class EditUser:
    username: str | None = None
    is_admin: bool | None = None
    password: str | None = None
    created_menus: Set[MenuRecommendation] | None = None
    preferences: Set[UserPreferences] | None = None

    @staticmethod
    def from_dict(obj: Any) -> 'EditUser':
        assert isinstance(obj, dict)
        username = from_str(obj.get("username"))
        is_admin = from_bool(obj.get("is_admin"))
        password = from_str(obj.get("password"))
        created_menus = from_set(MenuRecommendation.from_dict, obj.get("created_menus", []))
        preferences = from_set(UserPreferences.from_dict, obj.get("preferences", []))
        return EditUser(username, is_admin, password, created_menus, preferences)

    def to_dict(self) -> dict:
        result = {}
        if self.username is not None:
            result["username"] = from_str(self.username)
        if self.is_admin is not None:
            result["is_admin"] = from_bool(self.is_admin)
        if self.password is not None:
            result["password"] = from_str(self.password)
        if self.created_menus is not None:
            result["created_menus"] = [menu.to_dict() for menu in self.created_menus]
        if self.preferences is not None:
            result["preferences"] = [preference.to_dict() for preference in self.preferences]
        return result

def edit_user_from_dict(s: Any) -> EditUser:
    return EditUser.from_dict(s)

def edit_user_to_dict(x: EditUser) -> Any:
    return to_class(EditUser, x)
