from ..models.user_model import User, users_collection


async def get_users() -> list[User]:
    users = users_collection.find()
    return [User(**u) async for u in users]


async def get_user_by_id(id: int) -> User or None:
    user = await users_collection.find_one({'_id': id})
    return User(**user) if user else None


async def create_user(id: int, **kwargs) -> User:
    user = await users_collection.insert_one({'_id': id, **kwargs})
    return await get_user_by_id(user.inserted_id)


async def update_user(id: int, **kwargs) -> User:
    user = await users_collection.find_one_and_update({'_id': id}, {'$set': kwargs}, return_document=True)
    return User(**user)

async def is_admin(id:int)->bool:
    user = await users_collection.find_one({'_id': id})
    return user['is_admin'] == 1