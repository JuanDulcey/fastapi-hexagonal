from fastapi import FastAPI
from infrastructure.postgres_user_repo import PostgresUserRepository
from application.user_service import UserService
from interfaces.user_controller import router

app = FastAPI()

# Creamos el repo y servicio una sola vez
repo = PostgresUserRepository()
service = UserService(repo)

# Registramos rutas
app.include_router(router)
