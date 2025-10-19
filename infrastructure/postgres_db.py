from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker



# Tener encuenta que esta URL debe crear la bd
# Usuario crear nombre_bd=fastapi_hexagonal_db, usuario=postgres, y password="con la de seguridad pgadmin"
#postgresql://usuario:contraseña@localhost:5432/nombre_bd
DATABASE_URL = "postgresql://postgres:1981@localhost:5432/fastapi_hexagonal_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)


Base.metadata.create_all(bind=engine)
