from typing import Optional

from fastapi import FastAPI, APIRouter

from app.routes.send_email import send_email_router
from app.routes.hello_world import hello_world_router

app = FastAPI()


app.include_router(send_email_router, prefix="/send_email")
app.include_router(hello_world_router, prefix="/hello_world")
