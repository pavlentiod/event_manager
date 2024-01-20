from aiogram.utils.helper import Helper, HelperMode, ListItem


class admin_states(Helper):
    mode = HelperMode.snake_case
    A_MENU_STATE = ListItem()
    A_EDIT = ListItem()
    A_CREATE_DAYS = ListItem()
    A_REMOVE_DAYS = ListItem()
    A_DOWNLOAD_STEP1 = ListItem()
    A_DOWNLOAD_STEP2 = ListItem()
    A_DOWNLOAD_STEP3 = ListItem()
    A_DOWNLOAD_MAIN_INFO = ListItem()
    NEWSLETTER_STATE = ListItem()
    """
    РАССЫЛКА ПО ВСЕМ УЧАСТНИКАМ
    ПРИНЯТЬ СООБЩЕНИЕ, РАЗОСЛАТЬ В ЦИКЛЕ ПО ВСЕМ ID
    """
    CONTACT_STATE = ListItem()
    """
    ПРОСМОТР ОБРАЩЕНИЙ ОТ УЧАСТНИКОВ
    ВОЗМОЖНОСТЬ ОТВЕТА НА ОБРАЩЕНИЕ, КОТОРОЕ ПРИДЕТ УЧАСТНИКУ В ЛИЧКУ
    """


class user_States(Helper):
    mode = HelperMode.snake_case

    USE_STATE0 = ListItem()
    """ """
    USE_STATE_ACQ_1 = ListItem()
    """ """
    USE_STATE_ACQ_2 = ListItem()
    """ """
    USE_STATE_ACQ_3 = ListItem()
    """ """
    # USE_STATE_ACQ_AC = ListItem()
    """ """
    USER_MENU = ListItem()
    """"""
    USER_LOSTED = ListItem()
    """"""
    USER_CONTACT = ListItem()
    """"""
    USER_MAIN_INFO = ListItem()
    """"""
    USER_AUTOSPLIT = ListItem()
    """"""
    USER_FEEDBACK = ListItem()
    """"""
    USER_DAYS_INFO = ListItem()
    """ """
    USER_DAYS_INFO_MENU = ListItem()
    """ """



class useStates(Helper):
    mode = HelperMode.snake_case

    PRE_A_STATE = ListItem()
    """
    ВВОД КОЛ-ВА ДНЕЙ СОРЕВНОВАНИЙ
    """
    A_STATE = ListItem()
    """
    ADMIN STATE
    1. ЗАГРУЗКА ДАННЫХ ДЛЯ КАТЕГОРИЙ
    2. РАССЫЛКА ПО ВСЕМ УЧАСТНИКАМ
    3. ПРОСМОТР ОБРАЩЕНИЙ ОТ УЧАСТНИКОВ
    
    СНАЧАЛА ИДЕТ ЗАГРУЗКА ДАННЫХ ПО КАТЕГОРИЯМ, БОТ АВТОМАТИЧЕСКИ ИСПОЛЬЗУЕТ ТОЛЬКО ЗАПОЛНЕННЫЕ КАТЕГОРИИ
    """

    STATE1 = ListItem()
    """
     Юзер нажал команду старт:
     1. Перейти к состоянию STATE2(главное меню)
     2. Перейти к состоянию STATE3(знакомство)
    """
    STATE2 = ListItem()
    """ 
    Юзер в главном меню:
    Клавиатура, возможность перехода к:
    1. STATE3 - ЗНАКОМСТВО
    2. STATE4 - ИНФО ПО КАЖДОМУ ДНЮ
    3. STATE5 - СПРАВКА
    4. STATE6 - НАПИСАТЬ ОРГАМ
    5. STATE7 - ОБЩАЯ ИНФА О СТАРТЕ
    6. STATE8 - ПОИСК ПОТЕРЯННЫХ ВЕЩЕЙ
    7. STATE9 - ОТЗЫВЫ СПОРТСМЕНОВ
    """
    STATE3 = ListItem()
    """
    ЗНАКОМСТВО:
    1. ПРОВЕРКА НАЛИЧИЯ СПОРТСМЕНА В БАЗЕ
    2. ПОКАЗ ПРОФИЛЯ ПРИ НАЛИЧИИ
    3. ВОЗМОЖНОСТЬ ИЗМЕНИТЬ ИНФУ ПРОФИЛЯ
    4. СВЯЗКА ФУНКЦИЙ ЗНАКОМСТВА -> STATE3_1 -> STATE3_2 -> STATE3_3
    5. АВТОМАТИЧЕСКИЙ ВЫХОД В ГЛАВНОЕ МЕНЮ  
    """
    STATE4 = ListItem()
    """ 
    ВЫБОР ИНФОРМАЦИИ ПО ДНЯМ СОРЕВНОВАНИЙ:
    
    ДНИ СОРЕВНОВАНИЙ:
    STATE4_1, STATE4_2, STATE4_3, STATE4_4, STATE4_N
    
    ПОДСОСТОЯНИЯ:
    ST_REZ РЕЗУЛЬТАТЫ 
    ST_SPLITS СПЛИТЫ 
    ST_SPLIT_LEADERS ЛИДЕРЫ НА ПЕРЕГОНАХ ST_SPLIT_LEADERS
    ST_GRADES ЛИДЕРЫ ПО ОЦЕНКЕ 
    ST_GROUP_REVIEW ОБЗОР ПЕРЕГОНОВ ОДНОЙ ГРУППЫ С ОПЦИЯМИ 
    ST_START СТАРТОВЫЕ ПРОТОКОЛЫ 
    ST_TECH_INFO ТЕХНИЧЕСКАЯ ИНФОМАЦИЯ 
    ST_ONLINE_RES ССЫЛКА НА ОНЛАЙН РЕЗЫ 
    ST_GPS_LINK ССЫЛКА НА GPS ТРАНСЛЯЦИЮ 
    ST_LOCATION МЕТКА СО СТАРТОМ
    """
    STATE5 = ListItem()
    """
    ОПИСАНИЕ КОМАНД И АВТОМАТИЧЕСКИЙ ВЫХОД ОБРАТНО В МЕНЮ
    """
    STATE6 = ListItem()
    """ 
    ФОРМА ДЛЯ ОБРАЩЕНИЯ К ОРГАНИЗАТОРАМ, ОТПРАВКА ИМ СООБЩЕНИЯ В ЛИЧКУ
    1. ИСПОЛЬЗОВАНИЕ ФУНКЦИЙ ЗНАКОМСТВА, ЧТОБЫ ЗАРЕГЕСТРИРОВАТЬ СООБЩЕНИЕ
    2. ПРИКРЕПЛЕНИЕ К ТЕКСТУ ОБРАЩЕНИЯ + КОНТАКТЫ ДЛЯ ОБРАТНОЙ СВЯЗИ(МОЖНО ОТПРАВЛЯТЬ ОБРАТНО ПО ID)
    """
    STATE7 = ListItem()
    """
    1. БЮЛЛЕТЕНЬ
    2. САЙТ ОРГАНИЗАТОРОВ
    3. СХЕМА ЦЕНТРА СОРЕВНОВАНИЙ
    4. ЗАЯВКА
    5. ФОТОГРАФИИ
    """
    STATE8 = ListItem()
    """
    1. ПРОСМОТР ПОТЕРЯННЫХ ВЕЩЕЙ
    2. ОСТАВИТЬ ЗАПИСЬ О НАХОДКЕ(+ ПРИКРЕПЛЕНИЕ ДАННЫХ ДЛЯ СВЯЗИ, ПОДТЯНУТЬ ЗНАКОМСТВО)
    """
    STATE9 = ListItem()
    """
    ОСТАВИТЬ ОТЗЫВ(ПОДТЯНУТЬ ЗНАКОМСТВО)
    """
    """ПОДСОСТОЯНИЯ"""
    """ STATE4 """
    ST_REZ = ListItem()
    """ 
    1. КНОПКА ВЫБОРА ГРУППЫ
    2. ОБРАЩЕНИЕ К БАЗЕ СО СПЛИТАМИ
    """
    ST_SPLITS = ListItem()
    """
    1. КНОПКА ВЫБОРА ГРУППЫ
    2. ОБРАЩЕНИЕ К БАЗЕ СО СПЛИТАМИ
    """
    ST_SPLIT_LEADERS = ListItem()
    """
    1. КНОПКА ВЫБОРА ПЕРЕГОНА
    2. ОБРАЩЕНИЕ К БАЗЕ СО СПЛИТАМИ
    3. ВЫБОР КОГО ВКЛЮЧАТЬ В ЛИДЕРЫ
    """
    ST_GRADES = ListItem()
    """
    1. КНОПКА ВЫБОРА ГРУППЫ
    2. ОБРАЩЕНИЕ К БАЗЕ СО ОЦЕНКАМИ
    """
    ST_GROUP_REVIEW = ListItem()
    """
    1. КНОПКА ВЫБОРА ГРУППЫ
    2. ОБРАЩЕНИЕ К БАЗЕ СО СПЛИТАМИ
    3. ВЫБОР КОГО ВКЛЮЧАТЬ В ЛИДЕРЫ
    """
    ST_START = ListItem()
    """
    1. КНОПКА ВЫБОРА ГРУППЫ
    2. ОБРАЩЕНИЕ К БАЗЕ СО СТАРТОВЫМИ
    """
    ST_TECH_INFO = ListItem()
    """
    ОБРАЩЕНИЕ К ФАЙЛАМ ТЕХ.ИНФО
    """
    ST_ONLINE_RES = ListItem()
    """
    ОБРАЩЕНИЕ К ССЫЛКАМ НА ОНЛАЙН РЕЗЫ
    """
    ST_GPS_LINK = ListItem()
    """
    ОБРАЩЕНИЕ К ССЫЛКАМ НА ТРАНСЛЯЦИЮ
    """
    ST_LOCATION = ListItem()
    """
    ОБРАЩЕНИЕ К СПИСКУ МЕСТ
    """

    """ STATE3 """
    ST_NAME = ListItem()
    """ 
    1. ЗАПИСЬ ИМЕНИ И ID В БАЗУ
    2. УСТАНОВКА СЛЕД. СОСТОЯНИЯ -> ST_LASTNAME
    """
    ST_LASTNAME = ListItem()
    """ 
    1. ЗАПИСЬ ФАМИЛИИ В БАЗУ
    2. УСТАНОВКА СЛЕД. СОСТОЯНИЯ -> ST_GROUP
    """
    ST_GROUP = ListItem()
    """ 
    1. ЗАПИСЬ ГРУППЫ В БАЗУ
    2. ПРОВЕРКА ДАННЫХ ПОЛЬЗОВАТЕЛЕМ:
    НЕТ - ВОЗВРАТ В НАЧАЛО ЗНАКОМСТВА
    ДА - ВОЗВРАТ В ГЛАВНОЕ МЕНЮ, ЛИБО ФУНКЦИЮ КОТОРАЯ ВЫЗВАЛА STATE3
    """

    """ A_STATE """
    DOWLOAD_STATE = ListItem()
    """
    ЗАГРУЗКА ДАННЫХ ПО КАТЕГОРИЯМ
    1. ПОКАЗАТЬ КАТЕГОРИИ, ПРИНЯТЬ ДАННЫЕ С УКАЗАНИЕМ НА ФОРМАТ
    """
