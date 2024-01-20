import json
import logging
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
import time

bot = Bot(token='TOKEN')
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
mrk = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text='Ну и где снова этот гомосексуал?', callback_data='where'))
p = {365441836: 'tema', 232706431: 'pasha'}
comm = {'last_loc_tema': {"latitude": 10.750442, "longitude": 106.662022},
        'last_loc_pasha': {"latitude": 10.750442, "longitude": 106.662022}}


async def start(m: types.Message):
    await bot.send_message(m.from_user.id,
                           'Здарова! Ну надеюсь пашок тебе всё  объяснил, правила простые:\n\n1. Труселя свои грязные не разбрасывать\n2. Информацию обновлять не раз, сука, в месяц',
                           reply_markup=mrk)


async def remind(m: types.Message):
    await bot.send_message(chat_id=365441836,
                           text='Муся! Я уже все морги обзвонил, тебя нигде нет, к сожалению :( \n\nГеометочкой поделись пожалуйста...')
    await bot.send_message(chat_id=232706431,
                           text='Муся! Я уже все морги обзвонил, тебя нигде нет, к сожалению :( \n\nГеометочкой поделись пожалуйста...')


async def start_ps(m: types.Message):
    await bot.delete_my_commands()
    await bot.set_my_commands([types.BotCommand('whe_a_u_broo', 'брооо, ты где?? :)')])
    await bot.set_my_commands([types.BotCommand('last_loc_pasha', '{"latitude": 60.000633, "longitude": 30.355768}'),
                               types.BotCommand('last_loc_tema', '{"latitude": 60.000633, "longitude": 30.355768}')],
                              language_code='czn')


async def search_gomo(cb: types.CallbackQuery):
    await bot.send_message(cb.from_user.id, 'Включаю сканер бжжжжжжжжжжж.....')
    time.sleep(4)
    await bot.send_message(cb.from_user.id, 'Последний раз я эту суку видел где-то тут:')
    # comm =  {i.command: json.loads(str(i.description).replace("'", '"')) for i in
    #          await bot.get_my_commands(language_code='xy')}
    comm.update({i.command: json.loads(str(i.description).replace("'", '"')) for i in
                 await bot.get_my_commands(language_code='czn')})
    # await bot.send_message(cb.from_user.id, comm)
    loc = comm[f'last_loc_{p[cb.from_user.id]}']
    await bot.send_location(chat_id=cb.from_user.id, latitude=loc['latitude'], longitude=loc['longitude'])
    # await bot.send_location(chat_id=cb.from_user.id, latitude=59.939098, longitude=30.315868)
    mrk = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
        KeyboardButton(text='Сегодня я тут', request_location=True))
    await bot.send_message(cb.from_user.id, 'Я своё дело сделал, поведуй теперь куда пизды приехать вручить',
                           reply_markup=mrk)


async def loc_save(m: types.Message):
    await bot.send_message(chat_id=m.from_user.id, text='Ахахахах, коллекторам я уже скинул, спс',
                           reply_markup=types.ReplyKeyboardRemove())
    if m.from_user.id == 365441836:
        await bot.set_my_commands(commands=[types.BotCommand('last_loc_pasha', str(m.location))], language_code='czn')
    elif m.from_user.id == 232706431:
        await bot.set_my_commands(commands=[types.BotCommand('last_loc_tema', str(m.location))], language_code='czn')

async def send_loco(m: types.Message):
    mrk = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text='Отправить локо📍', request_location=True))
    await bot.send_message(m.from_user.id, 'Отправь локацию, нажав на кнопку!', reply_markup=mrk)

dp.register_message_handler(start, commands=['start', 'whe_a_u_broo'])
dp.register_message_handler(send_loco, commands=['send_location'])
dp.register_message_handler(remind, commands=['rem'])
dp.register_message_handler(start_ps, commands=['start_ps'])
dp.register_callback_query_handler(search_gomo, lambda x: x.data == 'where')
dp.register_message_handler(loc_save, content_types=['location'])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    logging.warning('Bye!')


