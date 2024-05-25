from fastapi import FastAPI,Query
from pydantic import BaseModel

app=FastAPI()

@app.get("/")
async def get():
    return "Hello World!!"

@app.get("/hello/{name}")
async def getWithParam(name)->str:
    return name

@app.get("/user/{userid}")
async def get_user(userid:int):
    return f"userid {userid}"

@app.get("/query/{name}")
async def queryParams(name,id:int | None=0):
    return f"{id} {name}"