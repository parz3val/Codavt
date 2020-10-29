## Simple example program using starlette for the application class demo.
from starlette.authentication import (
    AuthenticationBackend, AuthenticationError, SimpleUser, UnauthenticatedUser,
    AuthCredentials
)
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route, Mount, WebSocketRoute
from starlette.staticfiles import StaticFiles
import uvicorn
from starlette.authentication import requires
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
import base64
import binascii



""" 
def root(request):
    return PlainTextResponse('Hell, World')

def user_me(request):
    username = "Harris"
    return PlainTextResponse('Hello, %s!' % username)

def user(request):
    username = request.path_params['username']
    return PlainTextResponse('Hello, %s!' % username)

async def websocket_endpoint(websocket):
    await websocket.accept()
    await websocket.send_text('Hello, websocket!')
    await websocket.close()

def startup():
    print("Let's go")

routes = [
        Route('/',root),
        Route('/user/me',user_me),
        Route('/user/{username}', user),
        WebSocketRoute('/ws', websocket_endpoint),
            ] """

class BasicAPIAuth(AuthenticationBackend):
    async def authenticate(self, request):
        if "Authorization" not in request.headers:
            return
        auth = request.headers["Authorization"]

        try:
            scheme, credentials = auth.split()
            if scheme.lower() != 'basic':
                return
            decoded = base64.b64decode(credentials).decode("ascii")
        except (ValueError, UnicodeDecodeError, binascii.Error) as exc:
            raise AuthenticationError('Invalid creds:  {0}', exc)

        username, _, password = decoded.partition(":")
        if username.lower() == "harris" and password.lower() == "1234":
            return AuthCredentials(["authenticated"]),SimpleUser(username)
    
middleware = [
    Middleware(AuthenticationMiddleware),
]

app = Starlette(debug = True, middleware=middleware)

@app.route("/")
async def homepage(request):
    return PlainTextResponse("Hello World")

@requires('authenticated')
@app.route("/user/{user}")
async def userpage(request):
    await BasicAPIAuth().authenticate(request)
    user = request.path_params['user']
    return PlainTextResponse("Hello Mr. {0}",user)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

