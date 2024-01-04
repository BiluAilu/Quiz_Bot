from bson import ObjectId
from ..models.question_model import Question, questions_collection

from typing import List
async def get_questions(category:str,level:str):
    # Define your query parameters
    query_params = {"category":category,"level":level}

    # Perform a query with parameters, random sample, and limit
    pipeline = [
        {"$match": query_params},  # Match documents based on your criteria
        {"$sample": {"size": 5}},  # Adjust the size based on your requirements
        {"$limit": 5}  # Limit the number of documents to 5
    ]
    
    questions = questions_collection.aggregate(pipeline)
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

