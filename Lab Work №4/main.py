from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.models import Base, Recipe, UserPreferences, RequestLog, MenuRecommendation
from app.database import engine, get_db
from app.auth import auth_router
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Include the auth router
app.include_router(auth_router)

# Pydantic models
class AddRecipe(BaseModel):
    name: str
    description: str
    ingredients: str
    calories: float
    tags: str

class UpdatePreferences(BaseModel):
    budget: Optional[float]
    dietaryPreferences: Optional[str]
    allergies: Optional[str]

# Routes
@app.post("/api/v1/recipes")
def add_recipe(recipe: AddRecipe, db: Session = Depends(get_db)):
    new_recipe = Recipe(**recipe.dict())
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return {"message": "Recipe added successfully", "recipe_id": new_recipe.id}

@app.get("/api/v1/menu/recommendations")
def get_menu_recommendations(userId: int, db: Session = Depends(get_db)):
    recommendations = db.query(MenuRecommendation).filter(MenuRecommendation.userId == userId).all()
    return {"recommendations": recommendations}

@app.get("/api/v1/logs")
def get_request_logs(userId: int, db: Session = Depends(get_db)):
    logs = db.query(RequestLog).filter(RequestLog.userId == userId).all()
    return {"logs": logs}

@app.put("/api/v1/users/preferences")
def update_user_preferences(userId: int, preferences: UpdatePreferences, db: Session = Depends(get_db)):
    db_preferences = db.query(UserPreferences).filter(UserPreferences.userId == userId).first()
    if not db_preferences:
        db_preferences = UserPreferences(userId=userId, **preferences.dict(exclude_unset=True))
    else:
        for key, value in preferences.dict(exclude_unset=True).items():
            setattr(db_preferences, key, value)
    db.add(db_preferences)
    db.commit()
    db.refresh(db_preferences)
    return {"message": "Preferences updated successfully"}

# Initialize database
Base.metadata.create_all(bind=engine)
