from fastapi import APIRouter
from typing import Union,Optional
app02 = APIRouter()

@app02.get("/jobs/{kd}")
async def get_jobs(kd,xl:Union[str,None]=None,gj:Optional[str] = None):

    # 基于参数的数据库查询


    return {
        "kd":kd,
        "xl":xl,
        "gj":gj
    }