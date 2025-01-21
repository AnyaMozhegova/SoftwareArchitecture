from dataclasses import dataclass
from typing import Set, Any
from datetime import datetime
from utils.serialization import from_int, from_float, from_set, from_str, to_class


@dataclass
class UserPreferences:
    id: int
    user_id: int  # Идентификатор пользователя, с которым связаны предпочтения
    budget: float
    dietary_preferences: Set[str]
    allergies: Set[str]
    created_at: datetime

    @staticmethod
    def from_dict(obj: Any) -> 'UserPreferences':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        user_id = from_int(obj.get("user_id"))
        budget = from_float(obj.get("budget"))
        dietary_preferences = from_set(from_str, obj.get("dietary_preferences"))
        allergies = from_set(from_str, obj.get("allergies"))
        created_at = datetime.fromisoformat(from_str(obj.get("created_at")))
        return UserPreferences(id, user_id, budget, dietary_preferences, allergies, created_at)

    def to_dict(self) -> dict:
        return {
            "id": from_int(self.id),
            "user_id": from_int(self.user_id),
            "budget": from_float(self.budget),
            "dietary_preferences": list(self.dietary_preferences),
            "allergies": list(self.allergies),
            "created_at": self.created_at.isoformat(),
        }


@dataclass
class NewUserPreferences:
    budget: float
    dietary_preferences: Set[str]
    allergies: Set[str]

    @staticmethod
    def from_dict(obj: Any) -> 'NewUserPreferences':
        assert isinstance(obj, dict)
        budget = from_float(obj.get("budget"))
        dietary_preferences = from_set(from_str, obj.get("dietary_preferences"))
        allergies = from_set(from_str, obj.get("allergies"))
        return NewUserPreferences(budget, dietary_preferences, allergies)

    def to_dict(self) -> dict:
        return {
            "budget": from_float(self.budget),
            "dietary_preferences": list(self.dietary_preferences),
            "allergies": list(self.allergies),
        }


def new_user_preferences_from_dict(s: Any) -> NewUserPreferences:
    return NewUserPreferences.from_dict(s)


def new_user_preferences_to_dict(x: NewUserPreferences) -> Any:
    return to_class(NewUserPreferences, x)


@dataclass
class EditUserPreferences:
    budget: float | None = None
    dietary_preferences: Set[str] | None = None
    allergies: Set[str] | None = None

    @staticmethod
    def from_dict(obj: Any) -> 'EditUserPreferences':
        assert isinstance(obj, dict)
        budget = from_float(obj.get("budget"))
        dietary_preferences = from_set(from_str, obj.get("dietary_preferences"))
        allergies = from_set(from_str, obj.get("allergies"))
        return EditUserPreferences(budget, dietary_preferences, allergies)

    def to_dict(self) -> dict:
        return {
            "budget": from_float(self.budget) if self.budget is not None else None,
            "dietary_preferences": list(self.dietary_preferences) if self.dietary_preferences else None,
            "allergies": list(self.allergies) if self.allergies else None,
        }


def edit_user_preferences_from_dict(s: Any) -> EditUserPreferences:
    return EditUserPreferences.from_dict(s)


def edit_user_preferences_to_dict(x: EditUserPreferences) -> Any:
    return to_class(EditUserPreferences, x)
