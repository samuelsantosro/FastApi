from fastapi import APIRouter

autenticacao_roteador = APIRouter(prefix="/autenticacao", tags=["autenticacao"])

@autenticacao_roteador.get("/")
async def autenticacoes():
    return {"mensagem":"Acessou rota de autenticacoes"}