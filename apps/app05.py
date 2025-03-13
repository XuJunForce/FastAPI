from fastapi import APIRouter, File,UploadFile
from typing import List
import os
app05 = APIRouter()


# @app05.post("/file")
# async def upload_file(file: bytes = File()):
#     with open("H:\fastapi_learn\content.txt","wb") as buffer:
#         content = file.read()
#         buffer.write(content)
#     return {
#         "file": len(file)
#     }



app05 = APIRouter()

# 确保保存路径存在
SAVE_DIR = r"H:\fastapi_learn"  # 使用原始字符串避免转义问题
os.makedirs(SAVE_DIR, exist_ok=True)  # 自动创建目录


@app05.post("/file")
async def upload_file(file: bytes = File()):
    save_path = os.path.join(SAVE_DIR, "content.txt")

    # 直接写入 bytes 内容（无需调用 read()）
    with open(save_path, "wb") as buffer:
        buffer.write(file)  # file 本身就是 bytes

    return {"file": len(file)}

@app05.post("/files")
async def upload_files(files:List[bytes] = File()):
    for f in files:
        print(len(f))

    return len(files)


@app05.post("/UploadFile")
async def Upload_UploadFiles(file:UploadFile):
    os.makedirs("imgs", exist_ok=True)
    path = os.path.join("imgs", file.filename)


    # 文件保存
    with open(path, "wb") as f:
        for line in file.file:
            f.write(line)

    return {
        "file":file.filename
    }

@app05.post("/UploadFiles")
async def UploadFiles(files:List[UploadFile]):
    return {
        "name":[file.filename for file in files]
    }






