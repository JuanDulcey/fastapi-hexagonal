from sqlalchemy.orm import Session
from domain.user import User
from domain.user_repository import UserRepository
from infrastructure.postgres_db import Base, engine, get_db, UserModel


class PostgresUserRepository(UserRepository):

    def create(self, user: User) -> User:
        db_user = UserModel(name=user.name, email=user.email)
        db = next(get_db())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        user.id = db_user.id
        return user

    def find_all(self):
        db = next(get_db())
        return db.query(UserModel).all()

    def find_by_id(self, user_id: int):
        db = next(get_db())
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            raise Exception("User not found")
        return user

    def update(self, user_id: int, user: User):
        db = next(get_db())
        db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not db_user:
            raise Exception("User not found")
        db_user.name = user.name
        db_user.email = user.email
        db.commit()
        db.refresh(db_user)
        return db_user

    def delete(self, user_id: int) -> bool:
        db = next(get_db())
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if user:
            db.delete(user)
            db.commit()
            return True
        return False
