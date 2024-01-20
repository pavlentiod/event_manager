import pandas as pd
from create_bot import bot
from aiogram import Dispatcher
from all_states import user_States
from keyboards.kb import days_buttons, backb
# from DATA import columns1, columns2
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

# from handlers.admin.A_ST import base1, base2
# base1 = pd.read_csv('base1.csv', index_col=0)
# base2 = pd.read_csv('base2.csv', index_col=0)
base3 = pd.DataFrame(columns=['ID', 'NAME', 'LASTNAME', 'GROUP', 'CONTACT'])
base3.set_index('ID')
""" НАЖАТА КОМАНДА СТАРТ """


async def start(m: Message, state: FSMContext):
    await state.set_state(user_States.USER_MENU[0])
    await bot.send_message(m.from_user.id, 'Привет! Добавить ваши данные в базу?', reply_markup=yes_no())


def yes_no():
    markup = InlineKeyboardMarkup(row_width=2)
    yes = InlineKeyboardButton(text='Да', callback_data='repeat')
    no = InlineKeyboardButton(text='Нет', callback_data='back_to_menu')
    markup.add(yes, no)
    return markup


async def menu(cb: CallbackQuery, state: FSMContext):
    await state.set_state(user_States.USER_MENU[0])
    await bot.send_message(cb.from_user.id, 'Выбери категорию:', reply_markup=user_menu())


def user_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    bt1 = InlineKeyboardButton(text='Информация, разделенная по дням соревнований', callback_data='days_info')
    bt2 = InlineKeyboardButton(text='Поиск потерянных вещей', callback_data='losted')
    bt3 = InlineKeyboardButton(text='Написать организаторам', callback_data='contact')
    bt4 = InlineKeyboardButton(text='Общая информация', callback_data='main_info')
    bt5 = InlineKeyboardButton(text='Справка', callback_data='help')
    bt6 = InlineKeyboardButton(text='Как я сегодня пробежал?', callback_data='autosplit')
    bt7 = InlineKeyboardButton(text='Мои данные ', callback_data='acq')
    bt8 = InlineKeyboardButton(text='Оставить отзыв ', callback_data='feedback')
    markup.add(bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8)
    return markup


""" ЗНАКОМСТВО """


async def acq_1(cb: CallbackQuery, state: FSMContext):
    await bot.send_message(cb.from_user.id, 'Отлично! Введи свое имя')
    await state.set_state(user_States.USE_STATE_ACQ_1[0])


async def acq_name(m: Message, state: FSMContext):
    async with state.proxy() as data:
        data['NAME'] = m.text
    await bot.send_message(m.from_user.id, 'Отлично! Введи свою фамилию')
    await state.set_state(user_States.USE_STATE_ACQ_2[0])


async def acq_lastname(m: Message, state: FSMContext):
    async with state.proxy() as data:
        data['LASTNAME'] = m.text
    await bot.send_message(m.from_user.id, 'Отлично! Введи группу')
    await state.set_state(user_States.USE_STATE_ACQ_3[0])


async def acq_group(m: Message, state: FSMContext, ):
    async with state.proxy() as data:
        data['GROUP'] = m.text
        t = 'Данные пользователя:\n\n' + "\n".join([f'{i}: {data[i]}' for i in data.keys()])
    await bot.send_message(m.from_user.id, t)
    await bot.send_message(m.from_user.id, 'Отлично! Нажми "подтвердить", чтобы добавить даныне в базу',
                           reply_markup=accept_kb())

    # await state.set_state(user_States.USER_MENU[0])


def accept_kb():
    markup = InlineKeyboardMarkup(row_width=1)
    bt1 = InlineKeyboardButton(text='Подтвердить', callback_data='accept')
    bt2 = InlineKeyboardButton(text='Ввести заново', callback_data='repeat')
    return markup.add(bt1, bt2)


async def accept(cb: CallbackQuery, state: FSMContext):
    if cb.data == 'accept':
        await state.set_state(user_States.USER_MENU[0])
        """ ЗАПИСЬ ДАННЫХ В БАЗУ """
        await bot.send_message(cb.from_user.id, 'Отлично! Выбери категорию', reply_markup=user_menu())
    elif cb.data == 'repeat':
        await state.set_state(user_States.USE_STATE_ACQ_1[0])
        await bot.send_message(cb.from_user.id, 'Отлично! Введи свое имя')

""" ИНФА ПО ДНЯМ СОРЕВНОВАНИЙ """



async def choose_day(cb: CallbackQuery, state: FSMContext):
    base1 = pd.read_csv('base1.csv', index_col=0)
    await state.set_state(user_States.USER_DAYS_INFO[0])
    await bot.send_message(cb.from_user.id, 'Выбери день соревнований:',
                           reply_markup=days_buttons(len(base1.index)).add(backb))


async def days_info_categories(cb: CallbackQuery, state: FSMContext):
    await state.set_state(user_States.USER_DAYS_INFO_MENU[0])
    async with state.proxy() as data:
        data['day'] = cb.data
    await bot.send_message(cb.from_user.id, 'Выбери категорию:', reply_markup=days_info_menu(cb.data).add(backb))


def days_info_menu(day):
    markup = InlineKeyboardMarkup(row_width=1)
    # print(base1.loc[day])
    base1 = pd.read_csv('base1.csv', index_col=0)
    for i in base1.columns:
        if i in base1.loc[day].dropna().index.values:
            bt = InlineKeyboardButton(text=i, callback_data=i)
            markup.add(bt)
    return markup


def register_users_handlers(dp: Dispatcher):
    """ Начало, команда /start"""
    dp.register_message_handler(start, commands=['start'], state='*')
    """ Знакомство """
    dp.register_callback_query_handler(acq_1, lambda x: x.data == 'repeat',
                                       state=user_States.USER_MENU[0])
    dp.register_message_handler(acq_name, state=user_States.USE_STATE_ACQ_1[0])
    dp.register_message_handler(acq_lastname, state=user_States.USE_STATE_ACQ_2[0])
    dp.register_message_handler(acq_group, state=user_States.USE_STATE_ACQ_3[0])
    dp.register_callback_query_handler(accept, state=user_States.USE_STATE_ACQ_3[0])
    """ Главное меню и навигация """
    dp.register_callback_query_handler(menu, lambda x: x.data == 'back_to_menu', state=user_States.all())
    # dp.register_callback_query_handler(user_menu, state=user_States.USER_MENU[0])
    """ Информация по дням """
    dp.register_callback_query_handler(choose_day, lambda x: x.data == 'days_info', state=user_States.USER_MENU[0])
    dp.register_callback_query_handler(days_info_categories, state=user_States.USER_DAYS_INFO[0])
