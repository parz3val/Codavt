# More code for the FastAPI docs
# the main file got too crowded.

from typing import Optional
from fastapi import FastAPI, Query
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

# Post is used to handle the request bodies.
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()

    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def put_item(item_id: int, item: Item):
    # ** operator here is used to unpack the contents of item
    return {"item_id": item_id, **item.dict()}

@app.put("/items/{item_id}")
async def blip_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

""" @app.get("/items/")
async def read_items(q: Optional[str] = Query(None, max_length=50)):
    results = {"items": [
        {"item_id": "Foo"},
        {"item_id" : "Bar"}
    ]}
    if q:
        results.update({"q": q})
    return results
     """

# Above can also bee written as
@app.get("/items/")
async def read_items(q: str = Query(None, max_length=50)):
    results = {"items": [
        {"item_id": "Foo"},
        {"item_id" : "Bar"}
    ]}
    if q:
        results.update({"q": q})
    return results
    