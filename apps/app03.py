from fastapi import APIRouter
from pydantic import BaseModel,Field,validator
from datetime import date
from typing import List,Union


app03 = APIRouter()

class Addr(BaseModel):
    province: str
    city:str




class User(BaseModel):
    name:str = "root"  # 设定name的默认值
    # family_name: str = Field(regex="^a")  # 支持正则表达式
    age:int = Field(default=0, gt=0, lt=100)  # 设定年龄范围 gt:greater than lt: less than
    birth: Union[date, None] = None
    friends:List[int]
    addr:Union[Addr,None] = None   # 可以内嵌一个类


#内嵌一个规则
    @validator("name")
    def name_must_alpha(cls,value):

        assert value.isalpha(), 'name must be a alpha'
        return value




@app03.post("/data")
def User_info(user:User):
    print(user,type(user))
    print(user.dict())

    return user