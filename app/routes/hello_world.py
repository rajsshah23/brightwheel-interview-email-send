from fastapi import APIRouter


hello_world_router: APIRouter = APIRouter()


@hello_world_router.get("/")
def hello_world():
    return {"Hello": "World"}
