from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import CommandStart, Command

from .handlers.commands import start_cmd_handler, startapp_handler
from .handlers.inline_queries import inline_query_handler
from .config import settings

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

dp.message.register(start_cmd_handler, CommandStart())
dp.message.register(startapp_handler, Command("startapp"))
dp.inline_query.register(inline_query_handler)

def main():
    dp.run_polling(bot)

if __name__ == '__main__':
    main()
