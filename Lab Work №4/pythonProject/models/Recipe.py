from dataclasses import dataclass
from typing import Set, Any
from utils.serialization import from_int, from_str, from_float, from_set


@dataclass
class Recipe:
    id: int
    name: str
    description: str
    ingredients: str
    calories: float
    tags: Set[str]

    @staticmethod
    def from_dict(obj: Any) -> 'Recipe':
        if isinstance(obj, Recipe):
            obj = obj.to_dict()  # Convert Recipe instance to dictionary
        if not isinstance(obj, dict):
            raise ValueError(f"Expected dict, got {type(obj)}. Received object: {obj}")

        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        description = from_str(obj.get("description"))
        ingredients = from_str(obj.get("ingredients"))
        calories = from_float(obj.get("calories"))
        tags = from_set(from_str, obj.get("tags"))

        return Recipe(id, name, description, ingredients, calories, tags)

    def to_dict(self) -> dict:
        return {
            "id": from_int(self.id),
            "name": from_str(self.name),
            "description": from_str(self.description),
            "ingredients": from_str(self.ingredients),
            "calories": from_float(self.calories),
            "tags": list(self.tags),
        }
