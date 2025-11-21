from pydantic import BaseModel, EmailStr, validator
from typing import Optional, Dict, Any
from datetime import datetime, date
from uuid import UUID

# User schemas (ya existentes)
class UserBase(BaseModel):
    email: EmailStr
    name: str
    preferences: Optional[Dict[str, Any]] = None
    energy_level: Optional[str] = 'medium'

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: UUID
    created_at: datetime
    last_login: Optional[datetime]
    is_active: bool
    
    class Config:
        from_attributes = True

# Task schemas (ya existentes)
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    urgency: Optional[str] = None
    impact: Optional[str] = None
    estimated_duration: Optional[int] = None
    deadline: Optional[datetime] = None
    category_id: Optional[UUID] = None
    energy_required: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: UUID
    user_id: UUID
    priority_score: Optional[int] = None
    priority_level: Optional[str] = None
    completion_probability: Optional[float] = None
    status: str = 'pending'
    created_at: datetime
    updated_at: datetime
    completed_at: Optional[datetime] = None
    actual_duration: Optional[int] = None
    
    class Config:
        from_attributes = True

# Category schemas (ya existentes)
class CategoryBase(BaseModel):
    name: str
    color: Optional[str] = '#007bff'
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: UUID
    user_id: UUID
    created_at: datetime
    
    class Config:
        from_attributes = True

# Recommendation schemas (ya existentes)
class DailyRecommendationBase(BaseModel):
    task_id: UUID
    recommendation_reason: str
    confidence_score: Optional[float] = None

class DailyRecommendationCreate(DailyRecommendationBase):
    recommendation_date: date

class DailyRecommendationResponse(DailyRecommendationBase):
    id: UUID
    user_id: UUID
    status: str = 'pending'
    was_completed: Optional[bool] = None
    completed_on_time: Optional[bool] = None
    created_at: datetime
    
    class Config:
        from_attributes = True

# Energy Log schemas (nuevos)
class EnergyLogBase(BaseModel):
    energy_level: str
    notes: Optional[str] = None
    task_id: Optional[UUID] = None

class EnergyLogCreate(EnergyLogBase):
    pass

class EnergyLogResponse(EnergyLogBase):
    id: UUID
    user_id: UUID
    logged_at: datetime
    
    class Config:
        from_attributes = True

# Task History schemas (nuevos)
class TaskHistoryBase(BaseModel):
    change_type: str
    old_values: Optional[Dict[str, Any]] = None
    new_values: Optional[Dict[str, Any]] = None
    change_description: Optional[str] = None

class TaskHistoryResponse(TaskHistoryBase):
    id: UUID
    task_id: UUID
    user_id: UUID
    created_at: datetime
    
    class Config:
        from_attributes = True