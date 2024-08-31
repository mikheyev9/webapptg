from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

from tg_bot.config import settings
from tg_bot.logging_config import logger


async def start_cmd_handler(message: types.Message):
    logger.info(f"Received /start command from {message.from_user.username}")
    web_app_button = InlineKeyboardButton(text="Open WebApp",
                                          web_app=WebAppInfo(url=settings.WEBAPP_HOST))
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[web_app_button]])
    await message.answer("Привет! Нажми на кнопку, чтобы открыть WebApp.",
                         reply_markup=keyboard)


async def startapp_handler(message: types.Message):
    text = message.text
    args = text.split(maxsplit=1)[1] if len(text.split(maxsplit=1)) > 1 else ""
    params = {arg.split("=")[0]: arg.split("=")[1] for arg in args.split("&") if "=" in arg}
    profile_username = params.get("profile")
    profile_url = f"{settings.WEBAPP_HOST}/profile?username={profile_username}"
    web_app_button = InlineKeyboardButton(text="Open Profile WebApp",
                                          web_app=WebAppInfo(url=profile_url))
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[web_app_button]])
    await message.answer(f"Нажмите на кнопку ниже, чтобы открыть профиль {profile_username} в WebApp.",
                         reply_markup=keyboard)
    logger.info(f"Handled /startapp command with profile {profile_username}")