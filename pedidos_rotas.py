from fastapi import APIRouter
jason_fake = [
  {
    "id": 1,
    "nome": "Samuel 1",
    "email": "a1@a1",
    "fone": "111"
  },
  {
    "id": 2,
    "nome": "Samuel 2",
    "email": "a2@a2",
    "fone": "222"
  },
  {
    "id": 3,
    "nome": "Samuel 3",
    "email": "a3@a3",
    "fone": "333"
  },
  {
    "id": 6,
    "nome": "Samuel 14",
    "email": "a14@a14",
    "fone": "141414"
  },
  {
    "id": 5,
    "nome": "Samuel 15",
    "email": "a15@a15",
    "fone": "115115"
  },
  {
    "id": 10,
    "nome": "Samuel 5",
    "email": "a5@a5",
    "fone": "555"
  },
  {
    "id": 11,
    "nome": "Samuel 11",
    "email": "a11@a11",
    "fone": "111"
  },
  {
    "id": 50,
    "nome": "Samuel 50",
    "email": "a50@a11",
    "fone": "50"
  }
]

pedidos_roteador = APIRouter(prefix="/pedidos", tags=["pedidos"])

@pedidos_roteador.get("/")
async def pedidos():
    return {"mensagem": "Acessou rota de pedidos"}

@pedidos_roteador.get("/listar")
async def pedidos():
    return jason_fake

@pedidos_roteador.get("/pedido")
async def pedido(id: int):
    for i in jason_fake:
        if i["id"]==id:
            return i
    return {'msg': 'não encontrado'}
