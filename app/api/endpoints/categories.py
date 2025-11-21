from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.database import get_db
from app.models.database_models import Category
from app.models.pydantic_models import CategoryCreate, CategoryResponse

router = APIRouter()

@router.get("/", response_model=List[CategoryResponse])
def get_categories(
    user_id: UUID,
    skip: int = 0, 
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Obtener categorías de un usuario"""
    categories = db.query(Category).filter(
        Category.user_id == user_id
    ).offset(skip).limit(limit).all()
    return categories

@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: UUID, db: Session = Depends(get_db)):
    """Obtener una categoría específica por ID"""
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    return category

@router.post("/", response_model=CategoryResponse)
def create_category(category: CategoryCreate, user_id: UUID, db: Session = Depends(get_db)):
    """Crear una nueva categoría para un usuario"""
    # Verificar si ya existe una categoría con el mismo nombre para este usuario
    existing_category = db.query(Category).filter(
        Category.user_id == user_id,
        Category.name == category.name
    ).first()
    
    if existing_category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category with this name already exists for this user"
        )
    
    db_category = Category(**category.dict(), user_id=user_id)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(
    category_id: UUID, 
    category_update: CategoryCreate, 
    db: Session = Depends(get_db)
):
    """Actualizar una categoría existente"""
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if not db_category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    
    for field, value in category_update.dict(exclude_unset=True).items():
        setattr(db_category, field, value)
    
    db.commit()
    db.refresh(db_category)
    return db_category

@router.delete("/{category_id}")
def delete_category(category_id: UUID, db: Session = Depends(get_db)):
    """Eliminar una categoría"""
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if not db_category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    
    db.delete(db_category)
    db.commit()
    return {"message": "Category deleted successfully"}