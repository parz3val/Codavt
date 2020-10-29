# Starlette : Getting Started and Takeaways

- Async framework for python. 
- Bare metal
- Apparently fast

## Some features
- websocket support
- graphql support
- in process background tasks
- startup and shutdown events.
- test client on `requests`
- Session and cookie support
- 100% test coverage
- type annotated
- no hard dependencies

## Hello World

```python
from starlette.applications import Starlette 
from starlette.responses import JSONResponse
from starlette.routing import Route 

async def homepage(request):
    return JSONResponse({"Hello": "World"})

app = Starlette(debug = True, routes = [
    Route('/',homepage),
])

```

## Dependencies
- `requests` - only required for the `TestClient`
- `aiofiles` - required if you want to use `FileResponse` or `Static Files`
- `jinja2` - required for the `Jinja2Templates`
- `python-multipart` - Required for the `request.form()` support
- `itsdangerours` - Required for `SessionMiddleware` support
- `pyyaml` - Required for the `SchemaGenerator` support.
- `graphene` - Required for the `GRaphQLApp` support.
- `ujson` - Required for the `UJSONResponse` -- it makes the json parsing and dumping super snappy.

**Starlette is designed to be ussed either as a complete framework or as an ASGI toolkit. You can use any of its componenets independently.**

>>Note: 
Looks very similar to Laravel and Node.