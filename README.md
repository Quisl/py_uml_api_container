Dockerhub: https://hub.docker.com/r/quisl/py_uml_api

Try this online: https://quisl.de/python-uml-generator/

Run this:

```bash
docker run quisl/py_uml_api
```

This container accepts python code via POST and returns a class diagram as png image. Created by Pyreverse.

It listens to... :8000/get_python_uml

and expects these POST variables in request body (application/x-www-form-urlencoded):

* pythoncode (sting) - Can be any Python3 code. Code must contain only standard libraries. (* REQUIRED)
* builtin (booleanl) - include builtin objects (default value: False)
* ancestor (boolean) - includes all ancestors of all classes in the project (default value: False)
* associated (boolean) - include objects of classes recursivly even if they are not part of the project (default value: False)


OPENAPI 3:
```openapi
{"openapi":"3.0.2","info":{"title":"FastAPI","version":"0.1.0"},"paths":{"/get_python_uml":{"post":{"summary":"Get Python Uml","operationId":"get_python_uml_get_python_uml_post","requestBody":{"content":{"application/x-www-form-urlencoded":{"schema":{"$ref":"#/components/schemas/Body_get_python_uml_get_python_uml_post"}}},"required":true},"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}}}},"components":{"schemas":{"Body_get_python_uml_get_python_uml_post":{"title":"Body_get_python_uml_get_python_uml_post","required":["pythoncode"],"type":"object","properties":{"pythoncode":{"title":"Pythoncode","type":"string"},"builtin":{"title":"Builtin","type":"boolean","default":false},"ancestor":{"title":"Ancestor","type":"boolean","default":false},"associated":{"title":"Associated","type":"boolean","default":false}}},"HTTPValidationError":{"title":"HTTPValidationError","type":"object","properties":{"detail":{"title":"Detail","type":"array","items":{"$ref":"#/components/schemas/ValidationError"}}}},"ValidationError":{"title":"ValidationError","required":["loc","msg","type"],"type":"object","properties":{"loc":{"title":"Location","type":"array","items":{"type":"string"}},"msg":{"title":"Message","type":"string"},"type":{"title":"Error Type","type":"string"}}}}}}
```
