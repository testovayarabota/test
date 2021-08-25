from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

class UploadVideo(BaseModel):
    title: str
    descrip: str
    tags: str = None


class GetVideo(BaseModel):
    user: User
    video: UploadVideo