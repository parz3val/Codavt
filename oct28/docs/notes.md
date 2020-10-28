# FastAPI User Guide Code : Short Bites

## Path conversion

We can convert the path directly from the option of startlete in the FastAPI using the `path` option like:

`/files/{file_path:path}`

>> Note:
If we need parameter to contain `/home/johndoe/myfile.txt` with a leading slash `/`. In that casee, the URL would be : `/files//home/johndoe/myfile.txt`, with a a double slash `//` in between home and files.

Takeaways:

- Editor support, error checks, completions.
- Data parsing.
- Data Validation
- API annotation and automatic documentation

## Query Parameters

When we declare any other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.

For instance, in the given get function, any parameters that are not part of the path parms will be treated as query parms by FastAPI.

```python
fake_items_db = [{"items_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/stuffs/")
async def read_stuff(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]
```

Here, when the variables are provided they are read as str by the python which are then parsed by FastAPI against the type hint that we provide in thee function.

## Defaults

In the above example, we can pass the query as:
`https://localhost/items/` or `https://localhost/items/?skip=0&limit=10`, as both of them are samee because we provided the defaults for our parms.

## Optional parameters

The same way, we can declare optional query parameters, by setting thie default to None, we can create optional parameters by settign their defaults to none.

```python
from typing import Optional
from fastapi import FastAPI as Fa
app = Fa()

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item id" : item_id, "q" : q}
    return {"item_id": item_id}
```

Here, the parameter q will be optional and will be None by default.

>> Note: 
Keep in mind that FastAPI is smart enough to notice tht the path parameter `item_id` is a path parameter and `q` is not, it's a querey parameter.
FastAPI will know that `q` is optional parm because of the `=None`. 
The Optional in Optional[str] is not used by FastAPI (FastAPI will only use the str part), but the Optional[str] will let your editor help you finding errors in your code. We can alsso use `ENUM` the same way as with Path Parameters. 

>> We can use all kinds of parameters in the same function.

## Request Body

When we send data from a client to our API, it is packaged in a request body. When server sends data back to our client, it is packaged up in a response body. 

An API almost always has to send a response body. But don't necessarily need to send request bodiess all the time.

**To declare a request body, we use Pydantic models with all their power and benefits. :)**

>> Note:
To send data, use one of : POST (the most common), PUT, DELETE, or PATCH.
Sending a body with a `GET` reequest has an undefined behavior in the specs, nevertheless, it is supported by FastAPI, only for very complex/extreme use cases.
As it is discouraged, the interactive docs with Swagger UI won't show the documentation body when using `GET`, and proxies in the middle might not support it.




