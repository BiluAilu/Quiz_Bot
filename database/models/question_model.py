from pydantic import BaseModel

from database.services.loader import collection
from datetime import datetime
from typing import List

class Question(BaseModel):
    _id: int
    title: str
    choices: List[str]
    answer:str
    user_id: int
    status: str
    category:str
    level:str
    date: datetime

   


questions_collection = collection.question