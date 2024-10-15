from aiogram.types import CallbackQuery
from aiogram import Router, F

from models.chatgpt import Chatbot

chat = Chatbot()
router = Router()


@router.callback_query(F.data == 'new')
async def create_new_chat(callback: CallbackQuery):
    chat.clear(callback.from_user.id)
    await callback.message.answer(text='Новый чат успешно создан')


@router.callback_query(F.data == 'info')
async def send_info(callback: CallbackQuery):
    await callback.message.answer(text='Как пользоватся ботом? В боте есть комманды /info и /new. Команда /new '
                                       'позволяет создать новый чат с ChatGPT, а /info нужна для понимания функционла '
                                       'бота. По мере развития бота, будут появлятся новые пояснения')