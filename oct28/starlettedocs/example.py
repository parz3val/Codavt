# Tutorial for the Starlete
from starlette.applications import Starlette as st
from starlette.responses import PlainTextResponse
from starlette.routing import Route, Mount, WebSocketRoute
from starlette.staticfiles import StaticFiles

def homepage(request):
    return PlainTextResponse('Hello, World!')

def user_me(request):
    username = "John O"
    return PlainTextResponse('Hello, {0}', username)
routes = (
    Route("/",homepage),

)

def startup():
    print("Ready to go")

app = st(debug = True, routes = routes, on_startup = [startup])




