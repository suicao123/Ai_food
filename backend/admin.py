import os
import json
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db, FoodItem, Recipe
from auth import create_access_token, get_current_admin, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/api/admin", tags=["Admin"])

class RecipeCreate(BaseModel):
    food_item_id: int
    recipe_name: str
    ingredients: List[str]
    instructions: str

@router.post("/login")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    admin_username = os.getenv("ADMIN_USERNAME", "admin")
    admin_password = os.getenv("ADMIN_PASSWORD", "admin123")
    
    if form_data.username != admin_username or form_data.password != admin_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": admin_username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/foods")
def get_all_foods(db: Session = Depends(get_db), current_admin: str = Depends(get_current_admin)):
    foods = db.query(FoodItem).order_by(FoodItem.name).all()
    return [{"id": f.id, "name": f.name, "item_type": f.item_type} for f in foods]

@router.post("/recipes")
def add_new_recipe(recipe: RecipeCreate, db: Session = Depends(get_db), current_admin: str = Depends(get_current_admin)):
    food = db.query(FoodItem).filter(FoodItem.id == recipe.food_item_id).first()
    if not food:
        raise HTTPException(status_code=404, detail="FoodItem not found")
        
    new_recipe = Recipe(
        food_item_id=recipe.food_item_id,
        recipe_name=recipe.recipe_name,
        ingredients=json.dumps(recipe.ingredients, ensure_ascii=False),
        instructions=recipe.instructions
    )
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    
    return {"message": "Recipe added successfully", "recipe_id": new_recipe.id}
