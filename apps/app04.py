from fastapi import APIRouter, Form

app04 = APIRouter()


@app04.post("/reg")
def reg(username: str = Form(), password: str = Form()):
    print(f"username:{username}, password:{password}")
    return username
