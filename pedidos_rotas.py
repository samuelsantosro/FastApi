from fastapi import APIRouter

pedidos_roteador = APIRouter(prefix="/pedidos", tags=["pedidos"])

@pedidos_roteador.get("/")
async def pedidos():
    return {"mensagem":"Acessou rota de pedidos"}