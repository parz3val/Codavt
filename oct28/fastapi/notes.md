## Quick Guide

1. Import FastAPI

` from fastapi import FastAPI`

2. create a FastAPI "instance"
` app = FastAPI() `

3. Create a path operation

` /items/foo` 
Operation here refers to one of the HTTP methods.
- POST
- GET
- PUT 
- DELETE

Exotic ones

- OPTIONS
- HEAD
- PATCH
- TRACE

All the path operations are executed with the path operation decorator.

For example:
The @app.get("/") tells FastAPI that the function is in charge of handling requests that go:
- the path "/"
- using a get operation

>> More decorator ops for the FastAPI
- @app.post()
- @app.put()
- @app.delete()
- @app.options()
- @app.head()
- @app.patch()
- @app.trace()

4. Define the path operation function
Operation function provides functionalities for our API endpoints. In the given function.

- path is "/"
- operation is `get`
- functions : is the func below the "decorator" 
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "This is root"}
```
This fucntion is called by FastAPI whenever it receives a request to the given path/URL using a a GET operation.
In this case, this is an `async` function.

