from ..models.user_model import User, users_collection
from bson import ObjectId
from ..models.question_model import Question, questions_collection
from typing import List


async def get_users() -> List[User]:
    users = users_collection.find()
    return [User(**u) async for u in users]


async def get_user_by_id(id: int) -> User or None:
    user = await users_collection.find_one({'_id': id})
    return User(**user) if user else None
async def is_blocked(id: int) -> User or None:
    user = await users_collection.find_one({'_id': id})
    print(user)
    return 0 if user['status'] else 1
    # return User(**user) if user else None


async def create_user(id: int, **kwargs) -> User:
    user = await users_collection.insert_one({'_id': id, **kwargs})
    return await get_user_by_id(user.inserted_id)


async def update_user(id: int, **kwargs) -> User:
    user = await users_collection.find_one_and_update({'_id': id}, {'$set': kwargs}, return_document=True)
    return User(**user)

async def is_admin(id:int)->bool:
    user = await users_collection.find_one({'_id': id})
    return user['is_admin'] == 1

async def get_contributor_questions(id:int)->List[Question]:
    questions_cursor = questions_collection.find({"user_id": id})
    questions = await questions_cursor.to_list(length=None)
    return [Question(**q) for q in questions]