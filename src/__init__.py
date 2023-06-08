from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import os

from .routers.router import router
import json

tags = [
    {
        "name": "ping",
        "description": "pong"
    },
    {
        "name": "utils",
        "description": "Utilities"
    }
]

app = FastAPI(openapi_tags=tags)

app.include_router(router=router)

def custom_openapi_func ():
    if (app.openapi_schema):
        return app.openapi_schema
    app.openapi_schema =  get_openapi(
        title="ping API",
        version="0.1.0",
        routes=app.routes,
        description="This is a simple API to test the ping functionality",
        tags=tags,
    )
    return app.openapi_schema

app.openapi = custom_openapi_func

# write data to file
if not os.path.isdir("./dist"): os.mkdir("./dist")
with open("./dist/openapi.json", "w") as f:
    openapi_schema = app.openapi()
    f.write(json.dumps(openapi_schema))
    f.close()