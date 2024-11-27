from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, conint, constr, Field

app = FastAPI()

class Item(BaseModel):
    nome: constr(min_length=3, max_length=100)  
    idade: conint(ge=18, le=120) 
    email: EmailStr  
    telefone: constr(min_length=10, max_length=15)  
    endereco: constr(min_length=5)  
    cidade: constr(min_length=3, max_length=100)  


@app.get("/")
def read_root():
    return {"message": "API funcionando!"}


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
