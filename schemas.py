from pydantic import BaseModel


class UploadVideo(BaseModel):
    title: str
    descrip: str
    tags: str = None

