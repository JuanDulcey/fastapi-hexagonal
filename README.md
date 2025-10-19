# 🧩 FastAPI Hexagonal Architecture Example

Este proyecto es un backend desarrollado en **Python con FastAPI**, aplicando los principios de **Arquitectura Hexagonal (Ports & Adapters)**. Está conectado a una base de datos **PostgreSQL** y permite la gestión de usuarios mediante un CRUD completo.

---

## 📐 Objetivo del Proyecto

El propósito principal de este repositorio es servir como base para:
✅ Aprender arquitectura hexagonal aplicada en Python  
✅ Implementar dominios desacoplados  
✅ Aplicar buenas prácticas para QA y CI/CD  
✅ Trabajar con ramas `feature`, `develop`, `master/main`  
✅ Prepararse para escalar hacia microservicios o DDD  

---

## 🏗️ Arquitectura Hexagonal aplicada

domain/
├─ user.py # Entidad User
├─ user_repository.py # Puerto (interface repository)
application/
├─ user_service.py # Caso de uso (lógica de aplicación)
infrastructure/
├─ postgres_user_repo.py # Adaptador a PostgreSQL
├─ postgres_db.py # Config DB
interfaces/
├─ user_controller.py # Adaptador REST (FastAPI)
main.py # Punto de entrada


✅ Dominio independiente  
✅ Aplicación orquesta casos de uso  
✅ Infraestructura es reemplazable  
✅ Interfaces permiten interacción (REST, CLI, etc.)

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Descripción |
|-----------|------------|
| Python 3.11+ | Lenguaje principal |
| FastAPI | Framework backend |
| PostgreSQL | Base de datos relacional |
| SQLAlchemy | ORM |
| Uvicorn | Servidor ASGI |
| Pydantic | Validación de datos |
| Git Flow | Estrategia de ramas |
| Arquitectura Hexagonal | Patrón de diseño |

---

## 📦 Requisitos previos

| Requisito | Versión mínima |
|-----------|---------------|
| Python | 3.11 |
| PostgreSQL | 14+ |
| Git | Última versión |
| Pycharm / VS Code (opcional) | Recomendado |

---

## 🚀 Instalación y configuración

```bash
# 1️⃣ Clonar repo
git clone https://github.com/tu_usuario/fastapi-hexagonal.git
cd fastapi-hexagonal

# 2️⃣ Crear entorno virtual
python -m venv .venv
source .venv/Scripts/activate  # En Windows PowerShell

# 3️⃣ Instalar dependencias
pip install -r requirements.txt

# 🗄️ Configuración de base de datos (PostgreSQL)
Crea una base de datos en PostgreSQL y edita postgres_db.py:
DATABASE_URL = "postgresql://usuario:password@localhost:5432/mi_basedatos"

# ▶️ Ejecutar el proyecto
uvicorn main:app --reload

📍 Accede a la documentación automática:
➡️ http://localhost:8000/docs

➡️ http://localhost:8000/redoc

