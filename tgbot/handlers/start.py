from asyncio import sleep

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils.markdown import hlink

from tgbot.config import Config
from tgbot.models.user_tg import UserTG


async def start(message: types.Message, user: UserTG, config: Config) -> None:
    start_text = (
        "Привет!",
        "Я могу <b>убрать одежду</b> с любой фотографии девушки 🥰",
        "Не переживай, все <b>конфиденциально</b> и <b>анонимно</b> 🙈",
        f"Можешь посмотреть на {hlink('примеры', config.misc.photo_examples_url)} 🔞",
        "<b>Отправь мне фотографию</b> девушки и я уберу с нее одежду 👙"
    )

    for text in start_text:
        await user.send_chat_action(types.ChatActions.TYPING)
        await sleep(2)
        await user.send_message(text)


def register(dp: Dispatcher) -> None:
    dp.register_message_handler(start, CommandStart())
