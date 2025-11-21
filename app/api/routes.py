# app/api/routes.py
from fastapi import APIRouter
from app.api.endpoints import (
    users_router, 
    tasks_router, 
    categories_router,
    recommendations_router,
    energy_logs_router,
    task_history_router
)

api_router = APIRouter()

api_router.include_router(users_router, prefix="/users", tags=["users"])
api_router.include_router(tasks_router, prefix="/tasks", tags=["tasks"])
api_router.include_router(categories_router, prefix="/categories", tags=["categories"])
api_router.include_router(recommendations_router, prefix="/recommendations", tags=["recommendations"])
api_router.include_router(energy_logs_router, prefix="/energy-logs", tags=["energy-logs"])
api_router.include_router(task_history_router, prefix="/task-history", tags=["task-history"])