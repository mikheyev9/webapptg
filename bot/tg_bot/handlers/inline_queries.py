from aiogram import types
from aiogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                           InlineKeyboardButton, InlineKeyboardMarkup)

from tg_bot.config import settings
from tg_bot.logging_config import logger


async def inline_query_handler(inline_query: types.InlineQuery):
    query = inline_query.query.strip()
    logger.info(f"Received inline query: {query}")

    if query.startswith("profile="):
        username = query.split("=", 1)[-1]
        profile_url_attach = f'https://t.me/{settings.TELEGRAM_BOT_NAME}?startattach={username}'
        profile_url_startapp = f"https://t.me/{settings.TELEGRAM_BOT_NAME}?startapp={username}"
        profile_url = f"{settings.WEBAPP_HOST}/profile?username={username}"

        url_button = InlineKeyboardButton(
            text="Открыть профиль",
            url=profile_url
        )

        keyboard = InlineKeyboardMarkup(inline_keyboard=[[url_button]])
        result = InlineQueryResultArticle(
            id='1',
            title="Отправить профиль",
            input_message_content=InputTextMessageContent(
                message_text=f"Ссылка на открытие в WEB APP (доступно не всем): {profile_url_startapp}\n"
                             f"Нажмите на кнопку ниже, чтобы открыть профиль {username}."
            ),
            reply_markup=keyboard
        )

        await inline_query.answer(results=[result], cache_time=1)
        logger.info(f"Processed inline query for profile: {username}")