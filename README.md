# 🏠 House Price Prediction & CRUD API with FastAPI

A combined machine learning + CRUD microservice built with FastAPI, backed by PostgreSQL (Docker). The API exposes endpoints to:

- Predict house prices (based on features like area, bedrooms, parking)
- Perform CRUD operations on house records stored in the database

This repo contains two main modules:

- fastapi-ml — modules related to training, saving and serving the ML model
- fastapi-crud — CRUD endpoints + persistence logic

## 📦 Tech Stack

| Component                   | Purpose                                     |
| --------------------------- | ------------------------------------------- |
| **Python 3.9+**             | Core language                               |
| **FastAPI**                 | Web framework for building APIs             |
| **Uvicorn**                 | ASGI server to run the FastAPI app          |
| **scikit-learn**            | ML model training, preprocessing            |
| **joblib**                  | Serialize / load trained model              |
| **PostgreSQL**              | Relational database for data persistence    |
| **Docker & Docker Compose** | Containerization and database orchestration |

## 🚀 Getting Started

### Prerequisites
- Docker & Docker Compose installed
- Python 3.9+ environment (for running the API locally)
- (Optional) poetry or pip to manage Python dependencies

### Setup Steps

1. Clone the repository
```python
git clone https://github.com/schonsnatan/Machine-Learning-and-Crud-with-FastAPI.git
cd Machine-Learning-and-Crud-with-FastAPI
```

2. Launch PostgreSQL via Docker Compose
The docker-compose.yml includes:

```yaml
version: '3.8'
services:
  db:
    image: postgres:latest
    restart: always
    environment:
      POSTGRES_DB: mydatabase
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```
- Run:
```bash
docker-compose up -d
```

- This sets up a Postgres container on localhost:5432.

3. Initialize the database schema / sample data

- Use your preferred client (e.g. pgAdmin, psql) to connect:

```yaml
host: localhost
port: 5432
database: mydatabase
user: myuser
password: mypassword
```

- Insert sample data or seed as needed.

4. Install Python dependencies

- Using poetry:

```bash
poetry install
poetry shell
```

- Or with pip (after creating a virtualenv):
```bash
pip install -r requirements.txt
```

5. Run the FastAPI app

- From the project root:

```bash
uvicorn fastapi-crud.main:app --reload
```

- This starts your API server (default on http://127.0.0.1:8000).

## 🧭 API Documentation & Endpoints

Once the server is running, you get:

- Swagger UI — http://127.0.0.1:8000/docs
- ReDoc — http://127.0.0.1:8000/redoc

These include interactive docs where you can try out endpoints, see request/response schemas, etc.

### Key Endpoints (examples)

Here are the main API endpoints available in this project:

- POST /users/: Create a new user.
- GET /users/: Retrieve a list of users.
- GET /users/{user_id}: Retrieve a specific user by ID.
- PUT /users/{user_id}: Update a user's information.
- DELETE /users/{user_id}: Delete a user.

- POST /predict/ — Submit features to get a price prediction

[Add other endpoints related to your machine learning model or other resources]