from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BTN_GET_LAST = InlineKeyboardButton('Предыдущие показания', callback_data='get_last')
BTN_GET_CURRENT = InlineKeyboardButton('Текущие показания', callback_data='get_current')
BTN_INPUT = InlineKeyboardButton('Ввод показаний', callback_data='input_meters')
MAIN_MENU = InlineKeyboardMarkup().add(BTN_GET_LAST, BTN_GET_CURRENT, BTN_INPUT)