from fastapi import APIRouter

app01 = APIRouter()


@app01.get("/user/{id}")
def get_user(num: int):
    # id = 1
    print("id", num)
    return {
        "user_id": num
    }
