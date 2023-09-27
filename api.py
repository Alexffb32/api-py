from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Simulando um banco de dados simples em memória
db = []

# Modelo Pydantic para os dados que serão criados e atualizados
class Item(BaseModel):
    name: str
    description: str = None

# Rota para criar um novo item
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    db.append(item)
    return item

# Rota para recuperar todos os itens
@app.get("/items/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 10):
    return db[skip : skip + limit]

# Rota para recuperar um item pelo seu índice na lista
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id < 0 or item_id >= len(db):
        raise HTTPException(status_code=404, detail="Item not found")
    return db[item_id]

# Rota para atualizar um item pelo seu índice na lista
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    if item_id < 0 or item_id >= len(db):
        raise HTTPException(status_code=404, detail="Item not found")
    db[item_id] = item
    return item

# Rota para excluir um item pelo seu índice na lista
@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(db):
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = db.pop(item_id)
    return deleted_item

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
