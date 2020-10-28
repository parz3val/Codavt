from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()

@app.get("/")
def root():
    return { "Messsage" : "This is root"}

# path parameters
# stuff inside curcly braces is the variables.
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
#providing type hinting is helpful for fast api dbv

@app.get("/items/{item_id}/{item_name}")
async def new_item(item_id: int, item_name: str):
    return {"item_id:": item_id, "item_name": item_name}

## Order matters
@app.get("/users/me")
async def read_user_me():
    return {"User ID: " : "The current user"}

@app.get("users/{user_id}")
async def read_user(user_id: str):
    return {"User ID: " : user_id}

## Predefined values
class ModelName(str, Enum):
    alexnet = "alexnet"
    harris = "harris"
    mister = "mister"

@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning"}
    
    if model_name.value == "harris":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message" : "Have some residuals"}

# Path parameters containing paths
# Let's say we have a path operation with path `/files/{file_path}`
# But we need file path itself to contain a path like `/home/johndoe/myfile.jpg`
# So, the url for the file would be: `files/home/johdoe/myfile.txt`

## Path converter
# Using an option directly from Starlette we can declare path
# paratemer containing path using a URL like:
# `/files/{file_path: path}`

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"File Path: " : file_path}


fake_items_db = [{"items_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/stuffs/")
async def read_stuff(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

# Optional parameters
@app.get("/stuffs/{stuff_id}")
async def get_stuff(item_id : str, q : Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}

    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"Description": "I already like FastAPI more."}
        )
    return item