from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, conint, constr

app = FastAPI()
# Creación de la instancia principal de la aplicación FastAPI

class Item(BaseModel):     
    # Modelo de datos que valida los parámetros enviados en el método POST.

    nome: constr(min_length=3, max_length=100) 
     # Nombre: valida la longitud entre 3 y 100 caracteres.
  
    idade: conint(ge=18, le=120) 
    # Edad: acepta valores entre 18 y 120.
    
    email: EmailStr  
    # EmailStr: valida el formato del correo electrónico (ejemplo@dominio.com).
   
    telefone: constr(min_length=10, max_length=15)  
    # Teléfono: longitud entre 10 y 15 caracteres.
   
    endereco: constr(min_length=5)  
    # Dirección: mínimo de 5 caracteres.
   
    cidade: constr(min_length=3, max_length=100)  
    # Ciudad: longitud entre 3 y 100 caracteres.


@app.get("/")
def read_root() -> dict:
    return {"message": "API funcionando!"}
#    Devuelve un mensaje simple para verificar que la API está funcionando. 
   
@app.post("/criar-item/")
def create_item(item: Item) -> dict:
        # Recibe un objeto Item y retorna un diccionario.

    return {
        "nome": item.nome, 
        # Nombre proporcionado.

        "idade": item.idade,
        # Edad proporcionada.

        "email": item.email,
        # Email proporcionado.

        "telefone": item.telefone,
        # Teléfono proporcionado.

        "endereco": item.endereco,
        # Dirección proporcionada.
        
        "cidade": item.cidade
        # Ciudad proporcionada.
    }

