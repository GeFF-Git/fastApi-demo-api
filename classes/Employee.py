from pydantic import BaseModel
from typing import Optional
class Employee(BaseModel):
    id : int
    name : str
    # description : Optional[str] = None
    # price : float
    # tax : float | None = None
    age : int
    position : str | None = None
