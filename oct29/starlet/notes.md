## More notes from the starlette docs

### Performance 
Because starlette offers both tooling and framework features, speed is relative but still very fast. For the high throughout loads make sure to use:
- ujson and UJSONResponse
- Run using `Gunicorn` using the `uvicorn` worker class
- Use one or two workers per CPU core. 
- Disable access logging


