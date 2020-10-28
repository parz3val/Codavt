from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: Optional[str] = None
    price: float
    is_offer: Optional[bool] = None

@app.get("/")
def read_root():
    return {"Hello" : "World"}

# FastAPI can type check and validate the
# existence of item_id in the request

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    # Automatically accepts the data as pyd from JSON obj
    # data is automatically returned as JSON from pyd
#return {"item_id": item_id, "q": q, item: Item}
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"Item name" : item.name, "item_id": item_id}