from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

new_chat = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Создать новый чат', callback_data='new')],
                                                 [InlineKeyboardButton(text='Что может этот бот',
                                                                       callback_data='info')]])
