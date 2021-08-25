from collections import defaultdict
from typing import Optional
import databases
from fastapi.datastructures import Default
import ormar
from ormar.fields.model_fields import DateTime
from db import metadata, database
import datetime 


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database

class User(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    username: str = ormar.String(max_length=100)


class Video(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=100)
    descrip: str = ormar.String(max_length=500)
    file: str = ormar.String(max_length=500)
    create_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    user: Optional[User] = ormar.ForeignKey(User)
