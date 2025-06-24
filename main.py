#venv\Scripts\activate
#alembic revision --autogenerate -m "Geracao Inicial"
#alembic upgrade head
#pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography] python-dotenv python-multipart

#uvicorn main:app --reload

from fastapi import FastAPI

app = FastAPI()

from autenticacao_rotas import autenticacao_roteador
from pedidos_rotas import pedidos_roteador

app.include_router(autenticacao_roteador)
app.include_router(pedidos_roteador)