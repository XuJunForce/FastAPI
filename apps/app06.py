from fastapi import APIRouter,Request

app06 = APIRouter()

@app06.post("/item")
async def items(request:Request):
    return{
        "URL":request.url,
        "客户端代理":request.headers.get("user-agent"),
        "客户端IP":request.client.host
    }



