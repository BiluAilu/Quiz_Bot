import asyncio 

from aiogram import Dispatcher

from bot.bot_instance import bot
from bot.handlers.message.message_handlers import message_router
from bot.handlers.message.user_message_handlers import user_router
from bot.handlers.registration.user_registration_handler import user_registration_router 
from bot.handlers.registration.quiz_process_handler import quiz_taking_router 
from bot.handlers.registration.question_registration_handler import question_registration_router 
# from bot.callbacks.callback import callback_router


def register_routers(dp: Dispatcher) -> None:
    """Registers routers"""

    dp.include_router(user_registration_router)
    dp.include_router(question_registration_router)
    dp.include_router(user_router)
    dp.include_router(quiz_taking_router)
    dp.include_router(message_router)




    # callback routers
    # dp.include_router(callback_router)





async def main() -> None:
    """The main function which will execute our event loop and start polling."""
    try:
        dp = Dispatcher()

        print('Bot Starting....')
        register_routers(dp)
        print("Polling ....")
        
        await dp.start_polling(bot)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    asyncio.run(main())