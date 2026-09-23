from fastapi import FastAPI
from pydantic import BaseModel

app11 = FastAPI()

serv = {
    1: {"id": 1, "name": "web-app1", "ip": "10.1.1.1"},
    2: {"id": 2, "name": "web-app2", "ip": "10.1.1.2"},
}


class NewSer(BaseModel):
    name: str
    ip: str
    env: str = "dev"


@app11.get("/")
async def root():
    return {"status": "get ok"}


@app11.get("/server")
async def list_ser():
    return list(serv.values())


@app11.post("/server", status_code=201)
def creat_server(new_server: NewSer):
    new_id = max(serv.keys(), default=0) + 1

    server = {
        "id": new_id,
        "name": new_server.name,
        "ip": new_server.ip,
        "env": new_server.env,
    }

    serv[new_id] = server

    return server


@app11.post("/")
async def post():
    return {"status": "post ok"}


@app11.put("/")
async def put():
    return {"status": "put is ok"}
