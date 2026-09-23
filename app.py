from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
servers = {
	1: {"id":1,"name":"web-app1","ip":"10.1.1.1"},
	2: {"id":2,"name":"web-app2","ip":"10.1.1.2"},
}

class NewServer(BaseModel):
	name: str 
	ip: str 
	env: str = "dev" 

@app.get("/")
async def root():
	return {" status " : "get ok"}

@app.get("/server")
async def list_ser():
	return list(servers.values())

@app.post("/server",status_code=201)
def creat_server(new_server:NewServer):	
	New_id=Max(server.key(), defailt=0) +1
	server = {
	"id": new_id,
	"name" :New_server.ip,
	"env": new_server.env ,
}

@app.post("/")
async def post():
	return {" status ":" post ok"}

@app.put("/")
async def put():
	return {"put is ok "}
