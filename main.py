from fastapi import FastAPI, UploadFile, File
from typing import List
import shutil

app = FastAPI()


@app.post("/")
async def root(file: UploadFile = File(...)):
    with open('test.mp4', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"file_name": file.filename}



@app.post("/img")
async def up_img(files: List[UploadFile] = File(...)):
    for img in files:
        with open(f'{img.filename}', 'wb') as buffer:
            shutil.copyfileobj(img.file, buffer)
    return {"file_name": "GOOOD"}
