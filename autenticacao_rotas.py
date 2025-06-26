from fastapi import APIRouter
from modelos import Usuario, db
from sqlalchemy.orm import sessionmaker

autenticacao_roteador = APIRouter(prefix="/autenticacao", tags=["autenticacao"])

@autenticacao_roteador.get("/")
async def autenticacoes():
    return {"mensagem":"Acessou rota de autenticacoes"}

@autenticacao_roteador.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str):
    Session = sessionmaker(bind=db)
    session = Session()
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
        return {"mensagem":"Ja existe usuário com esse e-mail"}
    else:
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem":"Usuário cadastrado com sucesso"}
