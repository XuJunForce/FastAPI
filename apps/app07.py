from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from typing import Union,List

app07 = APIRouter()

class UserIn(BaseModel):
    name:str
    password:str
    email:EmailStr


class UserOut(BaseModel):
    name:str
    email:EmailStr


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float =10.5
    tags: List[str] = []


items={
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 32.1},
    "baz": {"name": "Baz", "description": None, "price": 50.88, "tax": 10.5, "tags": []}
}


@app07.post("/UserRespond", response_model=UserOut)
async def reg(user:UserIn):
    return user


# 返回值中 排除那些未设置的值 即使他有默认值
@app07.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def Item(id:str):
    return items[id]
