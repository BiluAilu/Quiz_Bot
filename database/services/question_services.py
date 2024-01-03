from bson import ObjectId
from ..models.question_model import Question, questions_collection

from typing import List
async def get_questions(category:str,level:str):
    questions = questions_collection.find({"category":category,"level":level})
    return [Question(**q) async for q in questions]


async def get_question_by_id(question_id:ObjectId) -> Question or None:
    question = await questions_collection.find_one({'_id': question_id})
    return Question(**question) if question else None


async def create_question(**kwargs) -> bool:
    question = await questions_collection.insert_one({ **kwargs})
    return question


async def update_question(question_id:ObjectId, **kwargs) -> Question:
    question = await questions_collection.find_one_and_update({'_id': question_id}, {'$set': kwargs}, return_document=True)
    return Question(**question)


async def approve_question(question_id:ObjectId) -> Question:
    question = await questions_collection.find_one_and_update({'_id': question_id}, {'$set': {'status':"approved"}}, return_document=True)
    return Question(**question)


async def reject_question(question_id:ObjectId, **kwargs) -> Question:
    question = await questions_collection.find_one_and_update({'_id': question_id}, {'$set': {'status':"rejected"}}, return_document=True)
    return Question(**question)

