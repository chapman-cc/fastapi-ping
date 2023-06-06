from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from .routers.router import router

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

def openapi_func ():
    if (app.openapi_schema):
        return app.openapi_schema
    app.openapi_schema =  get_openapi(
        title="ping API",
        version="0.1.0",
        description="This is a simple API to test the ping functionality",
        routes=app.routes,
        tags=tags,
        openapi_version="3.0.0",
)

app.openapi = openapi_func

@app.get("/echo", tags=["utils"])
def echo():
    return {"message": "Yean I can read you"}
