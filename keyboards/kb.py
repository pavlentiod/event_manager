import pandas as pd
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
from DATA import columns1, columns2

base1 = pd.read_csv('base1.csv', index_col=0)
""" ADMIN STATE """
main_info = InlineKeyboardButton(text="Общая информация", callback_data='main_info')
backb = InlineKeyboardButton(text='Вернуться в меню', callback_data='back_to_menu')

def back():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton(text='Загрузить еще', callback_data='back'),
               InlineKeyboardButton(text='Вернуться в главное меню', callback_data='a_menu'))
    return markup


def state_a_edit_base():
    markup = InlineKeyboardMarkup(row_width=1)
    bt1 = InlineKeyboardButton(text='Добавить дни', callback_data='add_days')
    bt2 = InlineKeyboardButton(text='Удалить дни', callback_data='remove_days')
    bt3 = InlineKeyboardButton(text='Очистить базу', callback_data='remove_base')
    bt_m = InlineKeyboardButton(text='Меню', callback_data='a_menu')
    markup.add(bt1, bt2, bt3, bt_m)
    return markup


# print(state_a_edit_base()[:5])
def make_a_numbers(p):
    numbers_markup = InlineKeyboardMarkup(row_width=5)
    for i in range(1, p):
        btn = InlineKeyboardButton(text=str(i), callback_data=str(i))
        numbers_markup.insert(btn)
    return numbers_markup


def days_buttons(p):
    days_markup = InlineKeyboardMarkup(row_width=5)
    for i in range(1, p + 1):
        btn = InlineKeyboardButton(text='day' + str(i), callback_data='day' + str(i))
        days_markup.insert(btn)
    return days_markup


def state_a_buttons():
    admin_markup = InlineKeyboardMarkup(row_width=1)
    btn0 = InlineKeyboardButton(text='РЕДАКТИРОВАТЬ БАЗУ', callback_data='edit_data')
    btn1 = InlineKeyboardButton(text='ЗАГРУЗКА ДАННЫХ ДЛЯ КАТЕГОРИЙ', callback_data='download_data')
    btn1_2 = InlineKeyboardButton(text='ОБЗОР БАЗЫ', callback_data='data_review')
    btn2 = InlineKeyboardButton(text='РАССЫЛКА ПО ВСЕМ УЧАСТНИКАМ', callback_data='newsletter')
    btn3 = InlineKeyboardButton(text='ПРОСМОТР ОБРАЩЕНИЙ ОТ УЧАСТНИКОВ', callback_data='contacts')
    admin_markup.add(btn0, btn1, btn1_2, btn2, btn3)
    return admin_markup




def download_menu():
    admin_markup = InlineKeyboardMarkup(row_width=1)
    for i in columns1:
        admin_markup.add(InlineKeyboardButton(text=i, callback_data=i))
    bt_m = InlineKeyboardButton(text='Меню', callback_data='a_menu')
    return admin_markup.add(bt_m)


def main_info_menu():
    main_info = InlineKeyboardMarkup(row_width=1)
    for i in columns2:
        main_info.add(InlineKeyboardButton(text=i, callback_data=i))
    return main_info


""" STATE2 ВЫБОР КНОПОК МЕНЮ """
menu_buttons_text = ['1. STATE3 - ЗНАКОМСТВО', '2. STATE4 - ИНФО ПО КАЖДОМУ ДНЮ', '3. STATE5 - СПРАВКА',
                     '4. STATE6 - НАПИСАТЬ ОРГАМ',
                     '5. STATE7 - ОБЩАЯ ИНФА О СТАРТЕ', '6. STATE8 - ПОИСК ПОТЕРЯННЫХ ВЕЩЕЙ',
                     '7. STATE9 - ОТЗЫВЫ СПОРТСМЕНОВ']



def state2_buttons(menu_buttons_list: list):
    state2_inline_buttons = InlineKeyboardMarkup(row_width=1)
    for i in base1.columns:
        state2_inline_buttons.add(InlineKeyboardButton(text=i, callback_data=i))
    return state2_inline_buttons


# state2_inline_buttons = state2_buttons()

""" STATE3 ЗНАКОМСТВО"""


def state3_buttons():
    state3_inline_buttons = InlineKeyboardMarkup(row_width=1)
    accept = InlineKeyboardButton(text='Знакомство ДА', callback_data='acq_yes')
    not_accept = InlineKeyboardButton(text='Знакомство НЕТ', callback_data='acq_no')
    state3_inline_buttons.add(accept, not_accept)
    return state3_inline_buttons


# state3_inline_buttons = state3_buttons()

""" STATE4 ВЫБОР ДНЯ СОРЕВНОВАНИЙ """

# days = ['day1', 'day2', 'day3', 'dayN']

days = list(base1.index)




# state4_menu_inline_buttons = state4_menu_buttons()
""" STATE4 ВЫБОР КАТЕГОРИИ """

state4_categories_list = ['ST_REZ РЕЗУЛЬТАТЫ', 'ST_SPLITS СПЛИТЫ',
                          'ST_SPLIT_LEADERS ЛИДЕРЫ НА ПЕРЕГОНАХ ST_SPLIT_LEADERS',
                          'ST_GRADES ЛИДЕРЫ ПО ОЦЕНКЕ', 'ST_GROUP_REVIEW ОБЗОР ПЕРЕГОНОВ ОДНОЙ ГРУППЫ С ОПЦИЯМИ',
                          'ST_START СТАРТОВЫЕ ПРОТОКОЛЫ', 'ST_TECH_INFO ТЕХНИЧЕСКАЯ ИНФОМАЦИЯ',
                          'ST_ONLINE_RES ССЫЛКА НА ОНЛАЙН РЕЗЫ', 'ST_GPS_LINK ССЫЛКА НА GPS ТРАНСЛЯЦИЮ',
                          'ST_LOCATION МЕТКА СО СТАРТОМ']


def state4_categories_buttons(state4_categories_list: list):
    days_cat = InlineKeyboardMarkup(row_width=1)
    for i in state4_categories_list:
        cat_button = InlineKeyboardButton(text=i, callback_data=i)
        days_cat.insert(cat_button)
    return days_cat


# state4_categories = state4_categories_buttons()

""" STATE7 ОБЩАЯ ИНФОРМАЦИЯ """

general_info_list = ['1. БЮЛЛЕТЕНЬ', '2. САЙТ ОРГАНИЗАТОРОВ', '3. СХЕМА ЦЕНТРА СОРЕВНОВАНИЙ', '4. ЗАЯВКА',
                     '5. ФОТОГРАФИИ']


# print([i.strip() for i in s.split('\n')])

def state7_categories_buttons(general_info_list: list):
    info_cat = InlineKeyboardMarkup(row_width=1)
    for i in general_info_list:
        cat_button = InlineKeyboardButton(text=i, callback_data=i)
        info_cat.insert(cat_button)
    return info_cat


# state7_general_info_buttons = state7_categories_buttons()

""" КНОПКИ ВЫБОРА ГРУППЫ """


def groups_buttons(group_list: list):
    group_markup = InlineKeyboardMarkup(row_width=3)
    for i in group_list:
        gr_bnt = InlineKeyboardButton(text=i, callback_data=i)
        group_markup.insert(gr_bnt)
    return group_markup


""" КНОПКИ ВЫБОРА ПЕРЕГОНА """


def routes_buttons(routes: list):
    routes_markup = InlineKeyboardMarkup(row_width=2)
    for i in routes:
        btn = InlineKeyboardButton(text=i, callback_data=i)
        routes_markup.insert(btn)


""" ПОДТВЕРЖДЕНИЕ ЗНАКОМСТВА """


def acq_asseption():
    accept_markup = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text='Следующий шаг', callback_data='next')
    btn2 = InlineKeyboardButton(text='Подтверждение', callback_data='accept')
    accept_markup.add(btn1, btn2)
    return accept_markup
