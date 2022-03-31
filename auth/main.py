import json
from typing import Optional
from fastapi import Body, FastAPI
from starlette.requests import Request
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

origins = [
    "http://auth_server_py:8000",
    "http://0.0.0.0:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    name: str
    key: str


@app.post('/auth')
async def auth(request: Request):
    data = await request.form()
    key = data.get('key')
    if key == 'supersecret':
        return Response(status_code=200)
    return Response(status_code=403)
