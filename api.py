from schemas import UploadVideo
from fastapi import FastAPI, UploadFile, APIRouter, Form, File
from typing import List
import shutil

video_router = APIRouter()

@video_router.post("/")
async def root(title: str = Form(...), descrip: str = Form(...), file: UploadFile = File(...)):
    info = UploadVideo(title=title, descrip=descrip)
    with open('test.mp4', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"file_name": file.filename, "info": info}



@video_router.post("/img")
async def up_img(files: List[UploadFile] = File(...)):
    for img in files:
        with open(f'{img.filename}', 'wb') as buffer:
            shutil.copyfileobj(img.file, buffer)
    return {"file_name": "GOOOD"}


@video_router.get("/info")
async def info_get():
    title = 'title'
    desc = 'Descrip'
    return UploadVideo(title=title, descrip=desc)