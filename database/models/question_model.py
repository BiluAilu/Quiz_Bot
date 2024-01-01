from pydantic import BaseModel

from ..loader import collection
from datetime import datetime
from typing import

class Question(BaseModel):
    _id: int
    title: str
    choices: List[str]
    answer:str
    user_id: str
    status: int
    category:str
    date: datetime

   


questions_collection = collection.question