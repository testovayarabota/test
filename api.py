from schemas import UploadVideo, GetVideo, User
from fastapi import FastAPI, UploadFile, APIRouter, Form, File
from typing import List
from models import Video
import shutil

video_router = APIRouter()

@video_router.post("/")
async def root(title: str = Form(...), descrip: str = Form(...), file: UploadFile = File(...)):
    info = UploadVideo(title=title, descrip=descrip)
    with open(f'{file.filename}', 'wb') as buffer:
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

@video_router.get("/video", response_model=GetVideo)
async def video_get():
    video = {'title' :'title', 'descrip':'des'}
    user = {'id':25, 'name': 'Name'}
    return GetVideo(user=user, video = video)


@video_router.post("/video")
async def create_video(video: Video):
    await video.save()
    return video
