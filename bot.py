from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
from aiogram.utils.helper import Helper, HelperMode, ListItem
from create_bot import dp
from handlers.admin import A_ST
from handlers.user import USER
from messages import MESSAGES
import tracemalloc

tracemalloc.start()


async def reset_state(m: types.Message):
    await dp.current_state().reset_state()
    await m.reply(text='state reset')

dp.register_message_handler(reset_state, commands=['reset'], state='*')
A_ST.reg_admin_handlers(dp)
USER.register_users_handlers(dp)


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown, skip_updates=True)
