from fastapi import FastAPI,Query,File,UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import pandas as pd

app=FastAPI()

class Employee(BaseModel):
    id : int
    name : str
    # description : Optional[str] = None
    # price : float
    # tax : float | None = None
    age : int
    position : str | None = None

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

@app.post("/employee")
async def postCall(employee : Employee):
    return employee

@app.post("/emp")
async def fileUpload(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_excel(contents)
        # print(df)
        await seperate_raw_df(df)
        return JSONResponse(content={"Message":"File received",
                                     "data":df.to_json(orient="records")
                                    # "data":pd.json_normalize(df.to_dict()).to_json(orient="records")
                                     })
        
    except Exception as e:
        return JSONResponse(content={"Message":e.__str__()})


async def seperate_raw_df(df : pd.DataFrame):
    df_new = df
    df = df["awbBodyRaw"]
    # df_normalize = pd.json_normalize(df.to_dict(orient="records"))
    df.to_csv('normalize',index=True)
    # print(df.columns)

    