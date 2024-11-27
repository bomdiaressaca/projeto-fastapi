from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, conint, constr, Field

# Criação da aplicação FastAPI
app = FastAPI()

# Definindo o modelo de dados para o POST com Pydantic e validações
class Item(BaseModel):
    nome: constr(min_length=3, max_length=100)  # Nome com mínimo de 3 e máximo de 100 caracteres
    idade: conint(ge=18, le=120)  # Idade entre 18 e 120
    email: EmailStr  # Validar que o campo é um email válido
    telefone: constr(min_length=10, max_length=15)  # Telefone com comprimento entre 10 e 15 caracteres
    endereco: constr(min_length=5)  # Endereço com no mínimo 5 caracteres
    cidade: constr(min_length=3, max_length=100)  # Cidade com nome entre 3 e 100 caracteres

# Método GET
@app.get("/")
def read_root():
    return {"message": "API funcionando!"}

# Método POST
@app.post("/criar-item/")
def create_item(item: Item):
    return {
        "nome": item.nome,
        "idade": item.idade,
        "email": item.email,
        "telefone": item.telefone,
        "endereco": item.endereco,
        "cidade": item.cidade
    }
