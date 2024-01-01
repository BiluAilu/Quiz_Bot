from pydantic import BaseModel

from ..loader import collection
from datetime import datetime


class User(BaseModel):
    _id: int
    name: str
    phone_number: str
    photo_id: str
    is_admin: int
    date: datetime

   


users_collection = collection.user