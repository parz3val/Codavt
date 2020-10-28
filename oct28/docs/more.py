# More code for the FastAPI docs
# the main file got too crowded.

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Multiple path and query parameters

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}

    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"Description" : "This is nice, fastapi."}
        )
    return item

# Required, optional and default parameters in one.
@app.get("/items/{items_id}")
async def user_item(item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit":limit}
    return item

## Request body
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float 
    tax: Optional[float] = None

@app.post("/items/")
async def create_item(item: Item):
    return item
