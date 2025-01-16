from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    isAdmin = Column(Boolean, default=False)
    preferences = Column(String)
    allergies = Column(String)
    history = Column(String)

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    ingredients = Column(String)
    calories = Column(Float)
    tags = Column(String)

class UserPreferences(Base):
    __tablename__ = "user_preferences"
    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer)
    budget = Column(Float)
    dietaryPreferences = Column(String)
    allergies = Column(String)
    createdAt = Column(DateTime, default=datetime.utcnow)

class RequestLog(Base):
    __tablename__ = "request_logs"
    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
    action = Column(String)
    status = Column(String)
    responseTime = Column(Float)

class MenuRecommendation(Base):
    __tablename__ = "menu_recommendations"
    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer)
    generatedAt = Column(DateTime, default=datetime.utcnow)
    menuItems = Column(String)
    calories = Column(Float)
