from dataclasses import dataclass
from typing import List, Any
from datetime import datetime
from utils.serialization import from_int, from_float, from_list, from_str, to_class
from models.Recipe import Recipe  # Убедитесь, что путь правильный

@dataclass
class MenuRecommendation:
    id: int
    user_id: int
    generated_at: datetime
    menu_items: List[Recipe]  # Используем List вместо Set для объектов Recipe
    calories: float

    @staticmethod
    def from_dict(obj: Any) -> 'MenuRecommendation':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        user_id = from_int(obj.get("user_id"))
        generated_at = datetime.fromisoformat(from_str(obj.get("generated_at")))
        # Преобразуем элементы menu_items в объекты Recipe
        menu_items = from_list(Recipe.from_dict, obj.get("menu_items"))
        calories = from_float(obj.get("calories"))
        return MenuRecommendation(id, user_id, generated_at, menu_items, calories)

    def to_dict(self) -> dict:
        return {
            "id": from_int(self.id),
            "user_id": from_int(self.user_id),
            "generated_at": self.generated_at.isoformat(),
            # Преобразуем объекты Recipe обратно в словари
            "menu_items": [recipe.to_dict() for recipe in self.menu_items],
            "calories": from_float(self.calories),
        }


@dataclass
class NewMenuRecommendation:
    menu_items: List[Recipe]  # Используем List вместо Set
    calories: float

    @staticmethod
    def from_dict(obj: Any) -> 'NewMenuRecommendation':
        assert isinstance(obj, dict)
        # Преобразуем элементы menu_items в объекты Recipe
        menu_items = from_list(Recipe.from_dict, obj.get("menu_items"))
        calories = from_float(obj.get("calories"))
        return NewMenuRecommendation(menu_items, calories)

    def to_dict(self) -> dict:
        return {
            # Преобразуем объекты Recipe в словари
            "menu_items": [recipe.to_dict() for recipe in self.menu_items],
            "calories": from_float(self.calories),
        }
def new_menu_recommendation_from_dict(s: Any) -> NewMenuRecommendation:
    return NewMenuRecommendation.from_dict(s)


def new_menu_recommendation_to_dict(x: NewMenuRecommendation) -> Any:
    return to_class(NewMenuRecommendation, x)

@dataclass
class EditMenuRecommendation:
    menu_items: List[Recipe] | None = None  # Используем List вместо Set
    calories: float | None = None

    @staticmethod
    def from_dict(obj: Any) -> 'EditMenuRecommendation':
        assert isinstance(obj, dict)
        # Преобразуем элементы menu_items в объекты Recipe, если они присутствуют
        menu_items = from_list(Recipe.from_dict, obj.get("menu_items")) if obj.get("menu_items") else None
        calories = from_float(obj.get("calories")) if obj.get("calories") is not None else None
        return EditMenuRecommendation(menu_items, calories)

    def to_dict(self) -> dict:
        return {
            # Преобразуем объекты Recipe в словари, если menu_items не пусто
            "menu_items": [recipe.to_dict() for recipe in self.menu_items] if self.menu_items else None,
            "calories": from_float(self.calories) if self.calories is not None else None,
        }
def new_menu_recommendation_from_dict(s: Any) -> NewMenuRecommendation:
    return NewMenuRecommendation.from_dict(s)


def new_menu_recommendation_to_dict(x: NewMenuRecommendation) -> Any:
    return to_class(NewMenuRecommendation, x)



