# app/api/endpoints/__init__.py
from .users import router as users_router
from .tasks import router as tasks_router
from .categories import router as categories_router
from .recommendations import router as recommendations_router
from .energy_logs import router as energy_logs_router
from .task_history import router as task_history_router

__all__ = [
    "users_router",
    "tasks_router", 
    "categories_router",
    "recommendations_router",
    "energy_logs_router",
    "task_history_router"
]