from core.buttons import new_chat

from models.chatgpt import Chatbot

from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.enums import ParseMode

chat = Chatbot()
router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(text="Вас  приветствует бот %Такой-то%", reply_markup=new_chat)


@router.message(F.text)
async def answer(message: Message):
    user_id, message_from_user = message.from_user.id, message.text
    response = chat.send_message(user_id=user_id, message= message_from_user)
    await message.answer(text=response, parse_mode=ParseMode.MARKDOWN)
