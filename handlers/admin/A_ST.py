import pandas as pd
from create_bot import dp, bot
from aiogram import Dispatcher, types
from all_states import admin_states
from keyboards.kb import state_a_buttons, download_menu, make_a_numbers, state_a_edit_base, \
    days_buttons, main_info, main_info_menu, back
from DATA import columns1, columns2
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


base1 = pd.DataFrame()
base2 = pd.DataFrame(columns=columns2, index=['EVENT NAME'])
""" ДОБАВИТЬ ОБЗОР БАЗЫ ДАННЫХ """
""" ВОЗВРАТ В МЕНЮ """


async def navigation(cb: CallbackQuery, state: FSMContext):
    if cb.data == 'a_menu':
        await bot.delete_message(chat_id=cb.from_user.id, message_id=cb.message.message_id)
        await state.set_state(admin_states.A_MENU_STATE[0])
        await bot.send_message(cb.from_user.id, 'Выберите действие:', reply_markup=state_a_buttons())
    elif cb.data == 'back':
        await bot.delete_message(chat_id=cb.from_user.id, message_id=cb.message.message_id)
        await state.set_state(admin_states.A_DOWNLOAD_STEP1[0])
        await bot.send_message(cb.from_user.id, 'Выбери категорию:',
                               reply_markup=days_buttons(len(base1.index)).row(main_info))


""" НАЖАТА КОМАНДА ADMIN """


async def categories(m: Message, state: FSMContext):
    await state.set_state(admin_states.A_MENU_STATE[0])
    await bot.send_message(chat_id=m.from_user.id, text=f'Выбери действие:', reply_markup=state_a_buttons())



""" СОЗДАНИЕ БАЗЫ """


async def create_base(cb: CallbackQuery, state: FSMContext):
    await state.set_state(admin_states.A_EDIT[0])
    await bot.delete_message(chat_id=cb.from_user.id, message_id=cb.message.message_id)
    await bot.send_message(cb.from_user.id,
                           f'Дней соревнований в базе: {len(base1.index)}\n\nВыберите действие:',
                           reply_markup=state_a_edit_base())


""" ДОБАВЛЕНИЕ ДНЕЙ """


async def edit_days(cb: CallbackQuery, state: FSMContext):
    global base1
    await bot.delete_message(chat_id=cb.from_user.id, message_id=cb.message.message_id)
    if str(cb.data) == 'add_days':
        await bot.send_message(cb.from_user.id, 'Укажите число:', reply_markup=make_a_numbers(11))
        await state.set_state(admin_states.A_CREATE_DAYS[0])
    elif str(cb.data) == 'remove_days':
        if len(base1.index) == 0:
            await state.set_state(admin_states.A_EDIT[0])
            await bot.send_message(cb.from_user.id, 'Удалять нечего!')
            await bot.send_message(cb.from_user.id, 'Выберите действие:', reply_markup=state_a_edit_base())
        else:
            await state.set_state(admin_states.A_REMOVE_DAYS[0])
            await bot.send_message(cb.from_user.id, 'Укажите день:',
                                   reply_markup=days_buttons(len(base1.index)))
    elif cb.data == 'remove_base':
        await state.set_state(admin_states.A_EDIT[0])
        base1.drop(labels=base1.index, axis=0, inplace=True)
        base1.to_csv('base1.csv')
        await bot.send_message(cb.from_user.id, 'База очищена!',
                               reply_markup=state_a_edit_base())


async def edit_days_in_df(cb: CallbackQuery, state: FSMContext):
    await state.set_state(admin_states.A_EDIT[0])
    await bot.delete_message(chat_id=cb.from_user.id, message_id=cb.message.message_id)
    global base1
    if cb.data.isdigit():
        base1 = pd.concat([base1, pd.DataFrame(
            columns=columns1,
            index=['day' + str(i) for i in
                   range(len(base1.index) + 1, len(base1.index) + int(cb.data) + 1)])], join='outer',
                          axis=0)
        base1.to_csv('base1.csv')
        await bot.send_message(cb.from_user.id, 'Дни добавлены!', reply_markup=state_a_edit_base())
    elif 'day' in cb.data:
        l_days = len(base1.index)
        base1.drop(axis=0, labels=base1.index[list(base1.index).index(cb.data)], inplace=True)
        base1.reset_index().drop(axis=1, labels=base1.columns[0], inplace=True)
        base1.index = ['day' + str(i) for i in range(1, l_days)]
        base1.to_csv('base1.csv')
        await bot.send_message(cb.from_user.id, 'Дни удалены!', reply_markup=state_a_edit_base())


""" ЗАГРУЗКА ДАННЫХ, ВОЗВРАЩАЕТ ВЫБОР ДНЯ """


async def download(cb: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=cb.from_user.id, message_id=cb.message.message_id)
    await state.set_state(admin_states.A_DOWNLOAD_STEP1[0])
    await bot.send_message(cb.from_user.id,
                           'Выбери день для загрузки данных, либо загрузите общую информацию\n\nЧтобы загрузить информацию по дням, сначала добавьте их в разделе "РЕДАКТИРОВАТЬ БАЗУ"',
                           reply_markup=days_buttons(len(base1.index)).row(main_info))


""" ВЫБРАН ДЕНЬ, ВОЗВРАЩАЕТ ВЫБОР КАТЕГОРИИ """


async def download_cat(cb: CallbackQuery, state: FSMContext):
    await state.set_state(admin_states.A_DOWNLOAD_STEP2[0])
    await bot.delete_message(chat_id=cb.from_user.id, message_id=cb.message.message_id)
    async with state.proxy() as data:
        data['day'] = {'day': str(cb.data)}
    await bot.send_message(cb.from_user.id, 'Выбери категорию:',
                           reply_markup=download_menu())


async def main_info_download(cb: CallbackQuery, state: FSMContext):
    await state.set_state(admin_states.A_DOWNLOAD_STEP2[0])
    await bot.delete_message(chat_id=cb.from_user.id, message_id=cb.message.message_id)
    await bot.send_message(cb.from_user.id, 'Выбери категорию:',
                           reply_markup=main_info_menu())


format_for_downloading_val = ['https://ссылка_на_сплиты\nлибо файл в формате htm/html',
                              "https://ссылка_на_стартовые_протоколы\nлибо файл в формате htm/html",
                              "59.934411, 30.306245\n\nПример отправки координат", "https://ссылка_на_gps_трансляцию",
                              "https://ссылка_на_онлайн_результаты"]

# format_for_downloading = {base1.columns[i]: format_for_downloading_val[i] for i in range(5)}

""" ВЫБОР КАТЕГОРИИ ДЛЯ ЗАГРУЗКИ НА ОПРЕДЕЛЕННЫЙ ДЕНЬ """


async def download_cat_hendlers(cb: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=cb.from_user.id, message_id=cb.message.message_id)
    await state.set_state(admin_states.A_DOWNLOAD_STEP3[0])
    async with state.proxy() as data:
        day = data['day']['day']
        data['day']['category'] = str(cb.data)
    await bot.send_message(cb.from_user.id,
                           f'Отлично! Пришли ссылку для {list(base1.index).index(day) + 1}го дня\n\nВажно! В сообщении должна быть только информация такого формата:\n\n{format_for_downloading_val[list(base1.columns).index(cb.data)]}')


async def main_info_cat_hendlers(cb: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=cb.from_user.id, message_id=cb.message.message_id)
    async with state.proxy() as data:
        data['category'] = cb.data
    await state.set_state(admin_states.A_DOWNLOAD_MAIN_INFO[0])
    await bot.send_message(cb.from_user.id,
                           f'Важно! В сообщении должна быть только информация такого формата:\n\n"FORMAT"')


""" ПОЛУЧЕНИЕ ЗАГРУЖАЕМЫХ ДАННЫХ И ЗАПИСЬ """


async def catch_download_data(m: Message, state: FSMContext):
    async with state.proxy() as data:
        cat = data['day']['category']
        day = data['day']['day']
    base1.loc[day][cat] = m.text
    base1.to_csv('base1.csv')
    await bot.send_message(m.from_user.id,
                           f'Поздравляю! данные для {list(base1.index).index(day) + 1}го дня в категории "{cat}" загружены',
                           reply_markup=back())


async def catch_main_info_data(m: Message, state: FSMContext):
    async with state.proxy() as data:
        cat = data['category']
    base2.loc['EVENT NAME'][cat] = m.text
    base2.to_csv('base2.csv')
    await bot.send_message(m.from_user.id,
                           f'Поздравляю! данные в категории "{cat}" загружены',
                           reply_markup=back())


""" ОБЗОР БАЗЫ """


async def data_review(cb: CallbackQuery):
    global base1, base2
    if len(base1.index) == 0:
        await bot.send_message(cb.from_user.id, 'ДОБАВЬТЕ ДАННЫЕ В БАЗУ')
    for i in list(base1.index):
        txt = f'{i}:\n\n' + '\n'.join([f'{j} : {base1.loc[i][j]}' for j in base1.columns])
        await bot.send_message(cb.from_user.id, txt)
    for i in list(base2.index):
        txt = f'{i}:\n\n' + '\n'.join([f'{j} : {base2.loc[i][j]}' for j in base2.columns])
        await bot.send_message(cb.from_user.id, txt)


""" РАССЫЛКА """


async def newsletter(cb: CallbackQuery):
    await bot.delete_message(chat_id=cb.from_user.id, message_id=cb.message.message_id)
    state = dp.current_state()
    await state.set_state(admin_states.NEWSLETTER_STATE[0])
    await bot.send_message(cb.from_user.id, 'Напиши сообщение для рассылки')


async def catch_newsletter(m: Message, state: FSMContext):
    await state.set_state(admin_states.A_MENU_STATE[0])
    await bot.send_message(m.from_user.id, 'Сейчас всем все разошлю! Чего желаете?', reply_markup=state_a_buttons())


""" ОБРАЩЕНИЯ ОТ УЧАСТНИКОВ """


async def contacts(cb: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=cb.from_user.id, message_id=cb.message.message_id)
    await state.set_state(admin_states.CONTACT_STATE[0])
    await bot.send_message(cb.from_user.id, 'Сообщения от участников:',
                           reply_markup=InlineKeyboardMarkup().add(
                               InlineKeyboardButton(text='Меню', callback_data='a_menu')))


def reg_admin_handlers(dp: Dispatcher):
    """ НАВИГАЦИЯ """
    dp.register_callback_query_handler(navigation, lambda c: c.data in ['a_menu', 'back'],
                                       state=admin_states.all())
    dp.register_message_handler(categories, commands=['admin'], state='*')

    """ РЕДАКТИРОВАНИЕ БАЗЫ """
    dp.register_callback_query_handler(create_base, lambda c: c.data == 'edit_data', state=admin_states.A_MENU_STATE[0])
    dp.register_callback_query_handler(edit_days, state=admin_states.A_EDIT[0])
    dp.register_callback_query_handler(edit_days_in_df, state=admin_states.A_CREATE_DAYS + admin_states.A_REMOVE_DAYS)
    """ ЗАГРУЗКА ДАННЫХ В БАЗУ ПО ДНЯМ """
    dp.register_callback_query_handler(download, lambda c: c.data == 'download_data',
                                       state=admin_states.A_MENU_STATE[0])
    dp.register_callback_query_handler(download_cat, lambda c: c.data in list(base1.index),
                                       state=admin_states.A_DOWNLOAD_STEP1[0])
    dp.register_callback_query_handler(download_cat_hendlers, lambda c: c.data in list(base1.columns),
                                       state=admin_states.A_DOWNLOAD_STEP2[0])
    dp.register_message_handler(catch_download_data, state=admin_states.A_DOWNLOAD_STEP3[0])
    """ ЗАГРУЗКА ОБЩЕЙ ИНФОРМАЦИИ """
    dp.register_callback_query_handler(main_info_download, lambda c: c.data == 'main_info',
                                       state=admin_states.A_DOWNLOAD_STEP1[0])
    dp.register_callback_query_handler(main_info_cat_hendlers, lambda c: c.data in columns2,
                                       state=admin_states.A_DOWNLOAD_STEP2[0])
    dp.register_message_handler(catch_main_info_data, state=admin_states.A_DOWNLOAD_MAIN_INFO[0])
    """ ОБЗОР БАЗЫ """
    dp.register_callback_query_handler(data_review, lambda c: c.data == 'data_review',
                                       state=admin_states.A_MENU_STATE[0])
    """ РАССЫЛКА """
    dp.register_callback_query_handler(newsletter, lambda c: c.data == 'newsletter', state=admin_states.A_MENU_STATE[0])
    dp.register_message_handler(catch_newsletter, state=admin_states.NEWSLETTER_STATE[0])
    """ ОБРАЩЕНИЯ """
    dp.register_callback_query_handler(contacts, lambda c: c.data == 'contacts', state=admin_states.A_MENU_STATE[0])
