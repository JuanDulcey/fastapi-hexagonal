from fastapi import APIRouter, HTTPException, Depends
from application.user_service import UserService
from domain.user import User

router = APIRouter()

# Dependencia
def get_user_service() -> UserService:
    from main import service
    return service

@router.post("/users", response_model=User)
def create_user(user: User, service: UserService = Depends(get_user_service)):
    return service.create_user(user)

@router.get("/users", response_model=list[User])
def get_users(service: UserService = Depends(get_user_service)):
    return service.get_all_users()

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    try:
        return service.get_user_by_id(user_id)
    except:
        raise HTTPException(status_code=404, detail="User not found")

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User, service: UserService = Depends(get_user_service)):
    try:
        return service.update_user(user_id, user)
    except:
        raise HTTPException(status_code=404, detail="User not found")

@router.delete("/users/{user_id}")
def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    if service.delete_user(user_id):
        return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
