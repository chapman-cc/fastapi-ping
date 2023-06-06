from fastapi import APIRouter

router = APIRouter()

@router.post("/hello-world",tags=["utils"])
def hello_world():
    return {"message": "Hello World"}

@router.get("/ping", tags=["ping"])
def ping():
    return {"message": "pong"}