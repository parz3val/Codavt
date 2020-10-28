## Fast API

- Web framework for building APIs

- Used to build web apis with the type annotated code.

### Depenedencies
1. Pydantic - For the type annotations.
2. Univorn - ASGI Server // Can also use Django or Flask

``` 
uvicorn main:app --reload  
// --reload, reloads the page automatically on the content change.
```

### Important features
1. Editor Support - Type Checking, Completion
2. Data validation - automatic and clear errors; validation for deeply nested JSON objects.
3. Conversion of input data from the protocol to Py data and types including
- JSON
- Path parms and args
- Query and parms
- Cookies
- Headeres
- Forms
- Files
4. Conversion of ouput data from pyd to JSON
5. Open API Specification `https://github.com/OAI/OpenAPI-Specification`
6. Better JSON Schema `http://json-schema.org/`
7. Static Typing `https://fastapi.tiangolo.com/python-types/`