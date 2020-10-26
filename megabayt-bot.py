#1 ИМПОРТ!
import telebot
from telebot import TeleBot
from telebot import types
import apiai
from apiai import ApiAI
import json
import pymysql
from pyzbar.pyzbar import decode
import qrcode
import requests
from PIL import Image
from data_base import *


#Рассылка
name = ''
surname = ''
_is_polling = []
age = 0
yes = 0
no = 0
kids = []
admins = []
password = ['paSSword', '1']
number_squad = 0
#КОНЕЦ
message_special = {}
name_quest = ""
quest_info = []
number_question_in_quest = 0
#ТОКЕН

token=""
bot = telebot.TeleBot(token=token)
#ТОКЕН

#
hide_keyboard = types.ReplyKeyboardRemove()
help_button = types.KeyboardButton('Помощь')

cancel_button = types.KeyboardButton("Отмена")
cancel_keyboard = types.ReplyKeyboardMarkup()
cancel_keyboard.row(cancel_button)

next_button = types.KeyboardButton("Дальше")
next_keyboard = types.ReplyKeyboardMarkup()
next_keyboard.row(next_button)

answer_button = types.KeyboardButton("Дальше")
answer_keyboard = types.ReplyKeyboardMarkup()
answer_keyboard.row(next_button)

opros_button_1 = types.KeyboardButton("Участвовать в опросе")
opros_button_2 = types.KeyboardButton("Посмотреть результаты")
opros_keyboard = types.ReplyKeyboardMarkup()
opros_keyboard.row(opros_button_1)
opros_keyboard.row(opros_button_2)


yes_button = types.KeyboardButton("Да")
no_button = types.KeyboardButton("Нет")
yes_no_markup = types.ReplyKeyboardMarkup()
yes_no_markup.row(yes_button)
yes_no_markup.row(no_button)

is_qr_keyboard = types.ReplyKeyboardMarkup()
is_qr_keyboard.row(yes_button)
is_qr_keyboard.row(no_button)

yes_button_1 = types.KeyboardButton("Подтвердить")
quest_accept_keyaboard = types.ReplyKeyboardMarkup()
quest_accept_keyaboard.row(yes_button_1)
quest_accept_keyaboard.row(cancel_button)

quest_button_1 = types.KeyboardButton("Создать квест")
quest_button_2 = types.KeyboardButton("Учавствовать в квесте")
quest_keyboard_1 = types.ReplyKeyboardMarkup()
quest_keyboard_1.row(quest_button_1)
quest_keyboard_1.row(quest_button_2)

quest_keyboard_2 = types.ReplyKeyboardMarkup()
quest_keyboard_2.row(quest_button_2)

help_keyboard = types.ReplyKeyboardMarkup()
help_keyboard.row(help_button)
break_button = types.KeyboardButton('Поломка')
otryad_button = types.KeyboardButton('Списки отрядов')
rating_button = types.KeyboardButton('Рейтинг отрядов')
timetable_button = types.KeyboardButton('Расписание')
quest_button = types.KeyboardButton('Квесты')
commands_keyboard_1 = types.ReplyKeyboardMarkup()

commands_keyboard_1.row(break_button)

commands_keyboard_2 = types.ReplyKeyboardMarkup()
commands_keyboard_2.row(break_button)
commands_keyboard_2.row(rating_button)
commands_keyboard_2.row(timetable_button)
commands_keyboard_2.row(quest_button)

load = types.KeyboardButton("Загрухить xlsx таблицу")
get = types.KeyboardButton('Получить данные по отряду')
insert = types.KeyboardButton('Добавить данные по отряду')
# update = types.KeyboardButton('Изменить данные по отряду')

edit_rating_but = types.KeyboardButton("Изменить рейтинг отрядов")
veiw_rating_but = types.KeyboardButton('Посмотреть рейтинг отрядов')

rating_keyboard_1 = types.ReplyKeyboardMarkup()
rating_keyboard_1.row(edit_rating_but)
rating_keyboard_1.row(veiw_rating_but)
rating_keyboard_1.row(cancel_button)

rating_keyboard_2 = types.ReplyKeyboardMarkup()
rating_keyboard_2.row(veiw_rating_but)
rating_keyboard_2.row(cancel_button)

squad_keyboard = types.ReplyKeyboardMarkup()
squad_keyboard.row(load)
squad_keyboard.row(get)
squad_keyboard.row(insert)
squad_keyboard.row(cancel_button)

avtoriz = types.KeyboardButton("Авторизироваться")
avtoriz_keyboard = types.ReplyKeyboardMarkup()
avtoriz_keyboard.row(avtoriz)

get_values_1 = types.KeyboardButton("Скачать xlsx таблицу")
get_values_2 = types.KeyboardButton("Получить по конкретному человеку")
get_values_keyboard = types.ReplyKeyboardMarkup()
get_values_keyboard.row(get_values_1)
get_values_keyboard.row(get_values_2)
get_values_keyboard.row(cancel_button)

load_xlsx_table_but = types.KeyboardButton("Загрузить расписание в формате xlsx")
upcoming_event_but = types.KeyboardButton("Показать ближайшее по времени мероприятие")
all_timetable_but = types.KeyboardButton("Показать расписание")

timetable_keyboard_1 = types.ReplyKeyboardMarkup()
timetable_keyboard_1.row(load_xlsx_table_but)
timetable_keyboard_1.row(upcoming_event_but)
timetable_keyboard_1.row(all_timetable_but)
timetable_keyboard_1.row(cancel_button)

timetable_keyboard_2 = types.ReplyKeyboardMarkup()
timetable_keyboard_2.row(upcoming_event_but)
timetable_keyboard_2.row(all_timetable_but)
timetable_keyboard_2.row(cancel_button)
#


#Кнопка
connection = types.KeyboardButton('Связь с кураторами📱')
timetable = types.KeyboardButton('Расписание🧾')
review = types.KeyboardButton('Отзывы🗓')
map = types.KeyboardButton('Карта Байтика🗺')
structure = types.KeyboardButton('Состав отряда📝')
information = types.KeyboardButton('Сказать информацию о тебе🐶')
graduates = types.KeyboardButton('Выпускники👩🏻‍🎓')
details = types.KeyboardButton('Подробности о лагере🏫')
future = types.KeyboardButton('Будущие смены➡️')
raiting = types.KeyboardButton('Рейтинг отрядов📈')#ДОДЕЛАТЬ
bag = types.KeyboardButton('Поломки🛠')#ДОДЕЛАТЬ
menu = types.KeyboardButton('Меню🍕')#ДОДЕЛАТЬ
playlist = types.KeyboardButton('Голосование✅')#ДОДЕЛАТЬ
napravlenie = types.KeyboardButton('Направление💻')#ДОДЕЛАТЬ
vopros = types.KeyboardButton('❓Задать вопрос❔')#ДОДЕЛАТЬ
quests = types.KeyboardButton('Квесты♟')

# main_markup(message) = types.ReplyKeyboardMarkup()

#main_markup(message).row(connection, timetable, review)
##main_markup(message).row(map, structure)
#main_markup(message).row(information, graduates, details)
#main_markup(message).row(future, raiting, menu)
#main_markup(message).row(playlist, napravlenie, vopros)
#main_markup(message).row(bag, quests)
hide = types.ReplyKeyboardRemove()
#Кнопка(к)

#Кнопка1
v1 = types.KeyboardButton('Отряд 1')
v2 = types.KeyboardButton('Отряд 2')
v3 = types.KeyboardButton('Отряд 3')
v4 = types.KeyboardButton('Отряд 4')
v5 = types.KeyboardButton('Отряд 5')
v6 = types.KeyboardButton('Отряд 6')
v = types.KeyboardButton('Назад')

sq1 = types.KeyboardButton("1")
sq2 = types.KeyboardButton("2")
sq3 = types.KeyboardButton("3")
sq4 = types.KeyboardButton("4")
sq5 = types.KeyboardButton("5")
sq6 = types.KeyboardButton("6")
squads = types.ReplyKeyboardMarkup()
squads.row(sq1, sq2, sq3)
squads.row(sq4, sq5, sq6)

markup1 = types.ReplyKeyboardMarkup()

markup1.row(v1, v2, v3, v4)
markup1.row(v5, v6, v)
#Кнопка1(к)


select_number_squad_keyboard = types.ReplyKeyboardMarkup()
select_number_squad_keyboard.row(sq1, sq2, sq3)
select_number_squad_keyboard.row(sq4, sq5, sq6)


#Кнопка2
o1 = types.KeyboardButton('Полина')
o2 = types.KeyboardButton('Асия')
o3 = types.KeyboardButton('Данил')
o4 = types.KeyboardButton('Аделя')
o5 = types.KeyboardButton('Дарья')
o6 = types.KeyboardButton('Артур')
o7 = types.KeyboardButton('Камиля(фотограф)')
o8 = types.KeyboardButton('Виолета')
o9 = types.KeyboardButton('Назад')

markup2 = types.ReplyKeyboardMarkup()

markup2.row(o1, o2, o3)
markup2.row(o4, o5, o6)
markup2.row(o7, o8, o9)
#Кнопка2(к)


#Кнопка3
fut = types.KeyboardButton('Зимние каникулы 2020. С 2 по 8 января')
fut1 = types.KeyboardButton('Летние каникулы 2020. С 1 июня до 25 августа')

markup3 = types.ReplyKeyboardMarkup()

markup3.row(fut)
markup3.row(fut1)
#Кнопка3(к)

#Кнопка4
rai1 = types.KeyboardButton('Добавить баллы')
rai2 = types.KeyboardButton('Посмотреть баллы')

markup4 = types.ReplyKeyboardMarkup()

markup4.row(rai1, rai2)
#Кнопка4(к)

#Кнопка5 День домашних животных
golos = types.KeyboardButton('Да')
golos1 = types.KeyboardButton('Нет')
golos3 = types.KeyboardButton('Свой вариант')

markup5 = types.ReplyKeyboardMarkup()

markup5.row(golos, golos1)
markup5.row(golos3)
#Кнопка5(к)

#Кнопка6
nap = types.KeyboardButton('Python')
nap1 = types.KeyboardButton('Sas-сервис')
nap2 = types.KeyboardButton('DVR')

markup6 = types.ReplyKeyboardMarkup()

markup6.row(nap, nap2)
markup6.row(nap1)
#Кнопка6(к)


#Кнопка7
p1 = types.KeyboardButton('Python-1')
p2 = types.KeyboardButton('Python-2')
p3 = types.KeyboardButton('Python-3')

markup7 = types.ReplyKeyboardMarkup()

markup7.row(p1, p2, p3)
#Кнопка7(к)


#Кнопка8
s1 = types.KeyboardButton('S-1')
s2 = types.KeyboardButton('S-2')
s3 = types.KeyboardButton('S-3')

markup8 = types.ReplyKeyboardMarkup()

markup8.row(s1, s2, s3)
#Кнопка8(к)


#Кнопка9
vr1 = types.KeyboardButton('VR-1')
vr2 = types.KeyboardButton('VR-2')
dvr = types.KeyboardButton('DVR')

markup9 = types.ReplyKeyboardMarkup()

markup8.row(vr1, vr2, dvr)
#Кнопка9(к)

dobav = types.KeyboardButton('Добавить рейтинг')
posmotr = types.KeyboardButton('Посмотреть рейтинг')

markup10 = types.ReplyKeyboardMarkup()

markup10.row(dobav, posmotr)



def main_markup(message):
    avtoriz = types.KeyboardButton("Авторизироваться")
    connection = types.KeyboardButton('Связь с кураторами📱')
    timetable = types.KeyboardButton('Расписание🧾')
    review = types.KeyboardButton('Отзывы🗓')
    map = types.KeyboardButton('Карта Байтика🗺')
    structure = types.KeyboardButton('Состав отряда📝')
    information = types.KeyboardButton('Сказать информацию о тебе🐶')
    graduates = types.KeyboardButton('Выпускники👩🏻‍🎓')
    details = types.KeyboardButton('Подробности о лагере🏫')
    future = types.KeyboardButton('Будущие смены➡️')
    raiting = types.KeyboardButton('Рейтинг отрядов📈')#ДОДЕЛАТЬ
    bag = types.KeyboardButton('Поломки🛠')#ДОДЕЛАТЬ
    menu = types.KeyboardButton('Меню🍕')#ДОДЕЛАТЬ
    playlist = types.KeyboardButton('Голосование✅')#ДОДЕЛАТЬ
    napravlenie = types.KeyboardButton('Направление💻')#ДОДЕЛАТЬ
    vopros = types.KeyboardButton('❓Задать вопрос❔')#ДОДЕЛАТЬ
    quests = types.KeyboardButton('Квесты♟')

    lvl = int(get_lvl_position(message.chat.id))
    

    if lvl == 0:
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.row(connection, review, graduates)
        keyboard.row(details, future, vopros)
        keyboard.row(avtoriz)
        return keyboard

    elif lvl == 1:
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.row(connection, review, graduates)
        keyboard.row(details, future, vopros)
        keyboard.row(menu)
        return keyboard

    elif lvl == 2:
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.row(connection, timetable, review)
        keyboard.row(map, graduates, details)
        keyboard.row(future, raiting, bag)
        keyboard.row(menu, playlist, napravlenie)
        keyboard.row(vopros, quests)
        return keyboard

    elif lvl >= 3:
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.row(connection, timetable, review)
        keyboard.row(map, graduates, details)
        keyboard.row(future, raiting, bag)
        keyboard.row(menu, playlist, napravlenie)
        keyboard.row(vopros, quests, structure)
        return keyboard


def raiting_keyboard_is(message):

    lvl = int(get_lvl_position(message.chat.id))
    
    edit_rating_but = types.KeyboardButton("Изменить рейтинг отрядов")
    veiw_rating_but = types.KeyboardButton('Посмотреть рейтинг отрядов')

    if 1 < lvl < 3:
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.row(veiw_rating_but)
        return keyboard
    else:
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.row(veiw_rating_but)
        keyboard.row(edit_rating_but)
        return keyboard


def quest_keyboard_is(message):
    lvl = int(get_lvl_position(message.chat.id))
    
    quest_button_1 = types.KeyboardButton("Создать квест")
    quest_button_2 = types.KeyboardButton("Учавствовать в квесте")

    if 1 < lvl < 3:
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.row(quest_button_2)
        return keyboard
    else:
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.row(quest_button_1)
        keyboard.row(quest_button_2)
        return keyboard


#start
@bot.message_handler(commands=['start'])
def start_message(message):
    if not is_avtorize(message.chat.id):
                bot.send_message(message.chat.id,  'Добро пожаловать в чат-бот.\n'
                                      'Если у вас есть доступ к аккаунту участника лагеря, то нажми на кнопку "Авторизация" и введите 8-ти значный код.\n'
                                      'Если нет, то вам доступны эти функции:\n'
                                      '- Выпускники.\n'
                                      '- Будущие смены.\n'
                                      '- Подробности о лагере.\n'
                                      '- Отзывы.\n'
                                      '- Связь с куратором.\n'
                                      'Выбирите что вас интересует.v', 
                                 reply_markup=main_markup(message))
    bot.register_next_step_handler(message, q)



#Kod
#def


@bot.message_handler(content_types=['text'])
#Связь с кураторами
def q(message):
    if message.text == 'Связь с кураторами📱':
        bot.send_message(message.chat.id, 'Выбери отряд, в котором ты состоишь', reply_markup=markup2)
        bot.register_next_step_handler(message, w)
    
    elif message.text == "Авторизироваться":
        if is_avtorize(message.chat.id):
            bot.send_message(message.chat.id, "Вы уже авторизированы", reply_markup=hide_keyboard)
        else:
            bot.send_message(message.chat.id, "Введите ваш индификатор", reply_markup=hide_keyboard)
            bot.register_next_step_handler(message, avtorize_indificator)

    elif message.text == 'Расписание🧾':
        bot.send_message(message.chat.id, 'Расписание на 18.11.2019:\n'
                                          '8.45 зарядка\n'
                                           '9.00 завтрак\n'
                                            '9.40 оргсбор\n'
                                            '10.30-13.00 занятия\n'
                                            '13.30 обед\n'
                                            '14.00 веревочный курс\n'
                                            '16.30 полдник\n'
                                            '15.00-16.00 тихий час\n'
                                            '16.30 полдник\n'
                                            '17.35 тренинг в 1а(сас)\n'
                                            '18.30 ужин\n'
                                            '20.30 гостевание', reply_markup=main_markup(message))
        bot.send_message(message.chat.id, 'Что-то ещё?')
        bot.register_next_step_handler(message, q)

    elif message.text == 'Отзывы🗓':
        bot.send_message(message.chat.id, "Дата пребывания в лагере: 30.05.2016\nДобрый вечер! Буквально только что приехали из вашего лагеря, "
                         "отпраздновав выпускной наших деток из садика. Очень понравилось! Огромное спасибо всем организаторам. "
                         "Впервые задумались всерьез отправить детей на летнее время в лагерь на отдых. Отдельное огромное и душевное "
                         "спасибо хочется сказать ребятам, которые шикарно делают свое дело. Молодцы! От ворот встретили и сразу "
                         "погрузили всех нас в сказку, чудесно провели всю программу и проводили до автобуса при прощании. "
                         "Ни разу не вышли из образа! Дети визжали от восторга. Родители до сих пор аплодируют стоя! "
                         "Огромное спасибо! (Мы даже имен их не спросили. Отблагодарите от нас, пожалуйста пиратов "
                         "Джека Воробья и еще одного капитана.....))))! )Успехов и процветания всем вам - особенного "
                         "строения души людям, которые работают с детьми и у которых так здорово это получается. "
                         "Высокая гора.д/сад Бэлэкэч родители Фантазеров.")
        bot.send_photo(message.chat.id, 'https://baytik-kazan.ru/kcfinder/upload/images/1%282%29.jpg')
        bot.send_message(message.chat.id, 'Что-то ещё?')
        bot.register_next_step_handler(message, q)

    elif message.text == 'Успехи ребят🏆':
        bot.send_message(message.chat.id, 'Вафин Амир Аделевич.🙎🏻‍♂️\n'
                                  '❓Кто же он такой?❓\n'
                                  'Это очеень хороший человек, который за свои 22 года добился очень много.\n'
                                  '💰Когда он учился в 10-ом классе, он со своей командой написали IT-проект, который продали за 1 000 000 рублей.💵\n'
                                  'Замечу что это случилось после неских поездок в лагерь "Байтик".\n'
                                  'Если хотите узнать больше об Амире, то вот его инстаграм: https://www.instagram.com/vafinamir/ . Вы ему также можете написать в direct.')
        bot.send_message(message.chat.id, 'Чем могу ещё помощь?', reply_markup=main_markup(message))
        bot.send_photo(message.chat.id, 'https://sun9-18.userapi.com/c855636/v855636889/137ce5/1raOUWylZG8.jpg')
        bot.send_message(message.chat.id, 'Что-то ещё?')
        bot.register_next_step_handler(message, q)

    elif message.text == 'Карта Байтика🗺':
        bot.send_photo(message.chat.id, "http://fest.krutushka.ru/data/viewers/map2016-big.jpg")
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=main_markup(message))
        bot.register_next_step_handler(message, q)

    elif message.text == 'Состав отряда📝':
        bot.send_message(message.chat.id, 'Что именно вы хотите?', reply_markup=squad_keyboard)

    elif message.text == "Сказать информацию о тебе🐶":
        bot.send_message(message.chat.id, 'Напиши своё ФИО полностью в И.П.', reply_markup=hide)
        bot.register_next_step_handler(message, i)


    elif message.text == 'Выпускники👩🏻‍🎓':
        bot.send_message(message.chat.id, 'https://sun9-18.userapi.com/c855636/v855636889/137ce5/1raOUWylZG8.jpg')
        bot.send_message(message.chat.id, 'Вафин Амир Аделевич.🙎🏻‍♂')
        bot.send_message(message.chat.id, 'Чем могу ещё помощь?', reply_markup=main_markup(message))
        bot.register_next_step_handler(message, q)

    elif message.text == 'Подробности о лагере🏫':
        bot.send_message(message.chat.id, 'Проект предусматривает проведение смен, на которых участники занимаются проектной деятельностью и развивают цифровые компетенции.'
                         'Педагогами - экспертами и тренерами являются практики бизнес-сферы и успешные предприниматели, которые профессионально ведут школьников к запланированным результатам.'
                         'Работа ведется в команде от трёх до пяти человек. А по окончанию смены каждая из них проходит трёхэтапный конкурсный отбор, где представляет работающий прототип IT-продукта.'
                         'На первом этапе все команды презентуют свои проекты экспертам в учебных группах. Лучшие два проекта от группы проходят на следующий этап, где их ожидает расширенное жюри и разбор со стороны других команд.'
                         'Завершается смена защитой приобретенных компетенций в формате Фестиваля проектов, куда приглашаются победители предыдущего этапа. Фестиваль будет проходить в Технопарке высоких технологий '
                         '«ИТ парк» (г.Казань). На этом этапе участники представляют свои проекты приглашенным экспертам из числа представителей учебных заведений, министерств, предприятий IT-сферы, потенциальных инвесторов, представителей бизнес-инкубаторов.')
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=main_markup(message))
        bot.register_next_step_handler(message, q)


    elif message.text == 'Будущие смены➡️':
        bot.send_message(message.chat.id, 'Выбери смены которые тебя интересуют', reply_markup=markup3)
        bot.register_next_step_handler(message, p)

    elif message.text == 'Рейтинг отрядов📈':
        bot.send_message(message.chat.id, 'Вы хотите добавить или посмотреть рейтинг', reply_markup=raiting_keyboard_is(message))
        bot.register_next_step_handler(message, choose)

    elif message.text == 'Меню🍕':
        bot.send_message(message.chat.id, 'ЗАВТРАК:\nКаша молочная овсяная\nЙогурт\nМасло сливочное\nБатон\nЧай с '
                                          'сахаром\nОБЕД:\nОвощная нарезка\nСуп лапша\nРис опущенный\nГовядина тушёная\n'
                                          'Говядина тушёная с черносливом\nКомпот из сухофруктов\nХлеб\nПОЛДНИК:\nСок '
                                          'фруктовый\nПеченье Сормовское\nФрукт\nУЖИН:\nОвощная нарезка\nГречка '
                                          'рассыпчатая\nКотлеты куриные\nЧай сладкий с лионом\nХлеб сельский\n2-ОЙ УЖИН\nКоктейл молочный')
        bot.send_message(message.chat.id, 'Чем могу помощь ещё?', reply_markup=main_markup(message))
        bot.register_next_step_handler(message, q)

    elif message.text == '❓Задать вопрос❔':
        bot.send_message(message.chat.id, 'Хорошо. Задай мне вопрос который тебя интересует. Если хочешь закончить диалог, напиши "Назад"')
        bot.register_next_step_handler(message, send_message23)

    elif message.text == 'Поломки🛠':
        bot.send_message(message.chat.id, 'Опишите вашу проблему.', reply_markup=cancel_keyboard)
        bot.register_next_step_handler(message, location_w)
    elif message.text == 'Направление💻':
        bot.send_message(message.chat.id, 'Выбери направление', reply_markup=markup6)
        bot.register_next_step_handler(message, p1)
    elif message.text == "Голосование✅":
        bot.send_message(message.chat.id, "Хочешь ли ты хеллоуин?", reply_markup=opros_keyboard)
        bot.register_next_step_handler(message, poll_1)
    elif message.text == "Результаты опроса":
        poll_results(message)
    elif message.text == "Квесты♟":
        bot.send_message(message.chat.id, "Что именно вы хотите?", reply_markup=quest_keyboard_is(message))
    elif message.text == "Создать квест":
        constructor_quest(message)
    elif message.text == "Учавствовать в квесте":
        bot.send_message(message.chat.id, "Доступные квесты:", reply_markup=create_list_quests())
        bot.register_next_step_handler(message, just_quest)
    elif message.text == "Загрухить xlsx таблицу":
        bot.send_message(message.chat.id, "Отправте таблицу с отрядами:")
        bot.register_next_step_handler(message, get_table_base)
    elif message.text == "Получить данные по отряду":
        bot.send_message(message.chat.id, "Что именно вы хотите получить?", reply_markup=get_values_keyboard)
    elif message.text == "Скачать xlsx таблицу":
        get_xlsx_table()
        with open("Отряд.xlsx", "rb") as f:
            bot.send_document(message.chat.id, f)
    elif message.text == "Получить по конкретному человеку":
        bot.send_message(message.chat.id, "Введите данные в формате ФИО")
        bot.register_next_step_handler(message, get_values_table_2)
    elif message.text == "Добавить данные по отряду":
        bot.send_message(message.chat.id, "Введите номер комнаты, номер отряда, ФИО, дату рождения, пол, адрес, ФИО родителя и телефон. \n\nПримечание:\nДанные необходимо вводить через запятую\nПример:\n101, 1, Иванов Иван Иванович, 11.11.2005, м, Москва, Петров Петр Петрович, +7 ********")
        bot.register_next_step_handler(message, add_values_table)
    else:
        bot.send_message(message.chat.id, 'Добро пожаловать в чат-бот.\n'
                                      'Если у вас есть доступ к аккаунту участника лагеря, то выберите меню "Мой код" и введите 6-ти значный код.\n'
                                      'Есл нет, то вам доступны эти функции:\n'
                                      '- Выпускники.\n'
                                      '- Будущие смены.\n'
                                      '- Подробности о лагере.\n'
                                      '- Отзывы.\n'
                                      '- Связь с куратором.\n'
                                      'Выбирите что вас интересует.', reply_markup=main_markup(message))
        bot.register_next_step_handler(message, q)


def avtorize_indificator(message):
    t = check_indificator(message.text, message.chat.id)
    if t == "Вы успешно авторизовались":
        x = commands_keyboard_1 if int(get_lvl_position(message.chat.id)) >= 1 else commands_keyboard_2
        bot.send_message(message.chat.id, t, reply_markup=x)
    else:
        bot.send_message(message.chat.id, t)

telebot
def get_values_table_2(message):
    try:
        bot.send_message(message.chat.id, get_values_table_1(message.text.split()))
    except:
        bot.send_message(message.chat.id, "Произошла непредвиденная ошибка")


def add_values_table(message):
    try:
        bot.send_message(message.chat.id, new_values_table_1(message.text.split(",")))
    except:
        bot.send_message(message.chat.id, "Произошла непредвиденная ошибка")


def get_table_xls(message):
    try:
        file_info = bot.get_file(message.document.file_id)
        f = open(r'base.xlsx', "wb")
        file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))
        f.write(file.content)
        f.close()
        bot.send_message(message.chat.id, new_all_values_table_1("base.xlsx"))
    except:
        bot.send_message(message.chat.id, "Произошла непредвиденная ошибка")


def get_table_base(message):
    get_table_xls(message)


#Сами кураторы
def w(message):
    if message.text == 'Полина':
        bot.send_message(message.chat.id, "Напиши ей в телеграмме по этому номеру +7", reply_markup=hide)
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=main_markup(message))

    elif message.text == 'Асия':
        bot.send_message(message.chat.id, "Напиши ей в телеграмме по этому номеру +7 917 257-81-66", reply_markup=hide)
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=main_markup(message))

    elif message.text == 'Данил':
        bot.send_message(message.chat.id, "Напиши ему в телеграмме по этому номеру +7 937 616-49-39", reply_markup=hide)
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=main_markup(message))

    elif message.text == 'Аделя':
        bot.send_message(message.chat.id, "Напиши ей в телеграмме по этому номеру +7 953 496-66-10", reply_markup=hide)
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=main_markup(message))

    elif message.text == 'Дарья':
        bot.send_message(message.chat.id, "Напиши ей в телеграмме по этому номеру + 7 965 585-71-19", reply_markup=hide)
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=main_markup(message))

    elif message.text == 'Артур':
        bot.send_message(message.chat.id, "Напиши ему в телеграмме по этому номеру +7 967 360-26-83", reply_markup=hide)
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=main_markup(message))

    elif message.text == 'Камиля(фотограф)':
        bot.send_message(message.chat.id, "Напиши ей в телеграмме по этому номеру +7 987 267-05-77", reply_markup=hide)
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=main_markup(message))

    elif message.text == 'Виолета':
        bot.send_message(message.chat.id, "Напиши ей в телеграмме по этому номеру +7 999 145-40-28", reply_markup=hide)
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=main_markup(message))

    elif message.text == 'Назад':
        bot.send_message(message.chat.id, 'Ок', reply_markup=main_markup(message))
    #else:
     #   bot.send_message(message.chat.id, 'Я тебя не понимаю(', reply_markup=main_markup(message))



#Расписание
def e(message):
    if message.text == 'Расписание🧾':
        bot.send_message(message.chat.id, 'Расписание на 18.11.2019:\n'
                                          '8.45 зарядка\n'
                                           '9.00 завтрак\n'
                                            '9.40 оргсбор\n'
                                            '10.30-13.00 занятия\n'
                                            '13.30 обед\n'
                                            '14.00 веревочный курс\n'
                                            '16.30 полдник\n'
                                            '15.00-16.00 тихий час\n'
                                            '16.30 полдник\n'
                                            '17.35 тренинг в 1а(сас)\n'
                                            '18.30 ужин\n'
                                            '20.30 гостевание', reply_markup=main_markup(message))
        bot.send_message(message.chat.id, 'Что-то ещё?')
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю(', reply_markup=main_markup(message))



#Отзывы
def r(massage):
    if message.text == 'Отзывы🗓':
        bot.send_message(message,chat.id, "Дата пребывания в лагере: 30.05.2016\nДобрый вечер! Буквально только что приехали из вашего лагеря, "
                         "отпраздновав выпускной наших деток из садика. Очень понравилось! Огромное спасибо всем организаторам. "
                         "Впервые задумались всерьез отправить детей на летнее время в лагерь на отдых. Отдельное огромное и душевное "
                         "спасибо хочется сказать ребятам, которые шикарно делают свое дело. Молодцы! От ворот встретили и сразу "
                         "погрузили всех нас в сказку, чудесно провели всю программу и проводили до автобуса при прощании. "
                         "Ни разу не вышли из образа! Дети визжали от восторга. Родители до сих пор аплодируют стоя! "
                         "Огромное спасибо! (Мы даже имен их не спросили. Отблагодарите от нас, пожалуйста пиратов "
                         "Джека Воробья и еще одного капитана.....))))! )Успехов и процветания всем вам - особенного "
                         "строения души людям, которые работают с детьми и у которых так здорово это получается. "
                         "Высокая гора.д/сад Бэлэкэч родители Фантазеров.")
        bot.send_photo(message.chat.id, 'https://baytik-kazan.ru/kcfinder/upload/images/1%282%29.jpg')
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=main_markup(message))



#подробности о лагере
def pod(massage):
    if message.text == 'Подробности о лагере🏫':
        bot.send_message(message.chat.id,
                         'Проект предусматривает проведение смен, на которых участники занимаются проектной деятельностью и развивают цифровые компетенции.'
                         'Педагогами - экспертами и тренерами являются практики бизнес-сферы и успешные предприниматели, которые профессионально ведут школьников к запланированным результатам.'
                         'Работа ведется в команде от трёх до пяти человек. А по окончанию смены каждая из них проходит трёхэтапный конкурсный отбор, где представляет работающий прототип IT-продукта.'
                         'На первом этапе все команды презентуют свои проекты экспертам в учебных группах. Лучшие два проекта от группы проходят на следующий этап, где их ожидает расширенное жюри и разбор со стороны других команд.'
                         'Завершается смена защитой приобретенных компетенций в формате Фестиваля проектов, куда приглашаются победители предыдущего этапа. Фестиваль будет проходить в Технопарке высоких технологий '
                         '«ИТ парк» (г.Казань). На этом этапе участники представляют свои проекты приглашенным экспертам из числа представителей учебных заведений, министерств, предприятий IT-сферы, потенциальных инвесторов, представителей бизнес-инкубаторов.')
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=main_markup(message))





#Успехи ребят
def t(message):
    if message.text == 'Успехи ребят🏆':
        bot.send_photo(message.chat.id, 'https://sun9-18.userapi.com/c855636/v855636889/137ce5/1raOUWylZG8.jpg')
        bot.send_message(message.chat.id, 'Вафин Амир Аделевич.🙎🏻‍♂️\n'
                                  '❓Кто же он такой?❓\n'
                                  'Это очеень хороший человек, который за свои 22 года добился очень много.\n'
                                  '💰Когда он учился в 10-ом классе, он со своей командой написали IT-проект, который продали за 1 000 000 рублей.💵\n'
                                  'Замечу что это случилось после неских поездок в лагерь "Байтик".\n'
                                  'Если хотите узнать больше об Амире, то вот его инстаграм: https://www.instagram.com/vafinamir/ . Вы также можете написать ему в direct.')
        bot.send_message(message.chat.id, 'Чем могу ещё помощь?', reply_markup=main_markup(message))


#Карта Байтика
def y(message):
    if message.text == 'Карта Байтика🗺':
        bot.send_photo(message.chat.id, "http://fest.krutushka.ru/data/viewers/map2016-big.jpg")
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=main_markup(message))



#Состав отряда
def u(message):
    if message.text == 'Отряд 1':
        bot.send_message(message.chat.id, 'Отряд 1', reply_markup=main_markup(message))
        bot.send_photo(message.chat.id, 'https://sun9-71.userapi.com/c858420/v858420180/103344/DF-cdXM1UT8.jpg')

    elif message.text == 'Отряд 2':
        bot.send_message(message.chat.id, 'Отряд 2', reply_markup=main_markup(message))
        bot.send_photo(message.chat.id, 'https://sun9-31.userapi.com/c858420/v858420180/103354/3ZaMk0NySnA.jpg')

    elif message.text == 'Отряд 3':
        bot.send_message(message.chat.id, 'Отряд 3', reply_markup=main_markup(message))
        bot.send_photo(message.chat.id, 'https://sun9-41.userapi.com/c858420/v858420180/10335c/IIZEzBK-dZo.jpg')

    elif message.text == 'Отряд 4':
        bot.send_message(message.chat.id, 'Отряд 4', reply_markup=main_markup(message))
        bot.send_photo(message.chat.id, 'https://sun9-43.userapi.com/c858420/v858420180/103364/x0xMvkrt4LI.jpg')

    elif message.text == 'Отряд 5':
        bot.send_message(message.chat.id, 'Отряд 5', reply_markup=main_markup(message))
        bot.send_photo(message.chat.id, 'https://sun9-19.userapi.com/c858420/v858420180/10336c/-YcSOi2_G2Q.jpg')

    elif message.text == 'Отряд 6':
        bot.send_message(message.chat.id, 'Отряд 6', reply_markup=main_markup(message))
        bot.send_photo(message.chat.id, 'https://sun9-34.userapi.com/c858420/v858420180/103374/CXU11e_-XHA.jpg')



#Сказать информацию о тебе
def i(message):
    if message.text == 'Зарипова Динара':
        bot.send_message(message.chat.id, 'Ты живёшь в корпусе №7. В комнате 21. Твои вожатые это Руслан и Асия', reply_markup=main_markup(message))


#Выпускники
def o(message):
    if message.text == 'Выпускники👩🏻‍🎓':
        bot.send_photo(message.chat.id, 'https://sun9-18.userapi.com/c855636/v855636889/137ce5/1raOUWylZG8.jpg')
        bot.send_message(message.chat.id, 'Вафин Амир Аделевич.🙎🏻‍♂')
        bot.send_message(message.chat.id, 'Чем могу ещё помощь?', reply_markup=main_markup(message))


#Будущие смены
def p(message):
    if message.text == 'Зимние каникулы 2020. С 2 по 8 января':
        bot.send_message(message.chat.id, 'Даты: с 3 по 9 января 2020 года\nВозраст: 7-17 лет\nСтоимость: 16 500 рублей\nПроживание: 7 корпус\n'
                                       'Участники проекта разместятся в комфортабельном седьмом корпусе с 4-х и 6-ти местными комнатами со всеми удобствами. На каждом этаже есть площадки, на которых будут проходить  мастер-классы и отрядные мероприятия.\n'
                                       'Новогодние каникулы всегда таят в себе что-то волшебное и сказочное, а  когда их можно провести в компании друзей в живописном месте, то отдых превращается в чудо. Традиционно, с боем курантов в лагере «Байтик» наступает '
                                       'Зимняя сказка, и каждый день наполняется незабываемыми событиями.\n'
                                       'О программе  смены:\n'
                                       'Программа смены разнообразна.\n'
                                       'Каждый участник  найдет для себя интересные и полезные занятия. Мероприятия будут проходить как всем лагерем  так и делиться по возрастам. \n'
                                       'Необычная тематика, опытные вожатые  обеспечат яркий отдых и безопасность. Профильные мастер-классы и занятия дадут много новых  знаний и впечатлений.\n'
                                       'Помимо этого, ребят ждут:\n'
                                       '- увлекательные квесты,  приключенческие "вертушки", вечерние  шоу-программы и дискотеки. До последнего момента тема смены остается в секрете!!!\n'
                                       '- новогодний и рождественский праздники, встреча с Дедом Морозом и его друзьями\n'
                                       '- командно-спортивная игра «Лазертаг» (за доп.оплату )\n'
                                       '- зимние забавы (катание на коньках, лыжах, санках)  и спортивные мероприятия на свежем воздухе\n- катание на санях, запряженных лошадьми.')
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=main_markup(message))
        bot.register_next_step_handler(message, q)

    elif message.text == 'Летние каникулы 2020. С 1 июня до 25 августа':
        bot.send_message(message.chat.id, 'Приехав в наш лагерь,  ребенок выбирает интересующую его область  и ежедневно в первой половине дня посещает занятия по выбранному направлению. У нас 9  профильных направлений на выбор:\n\n'

                                            'IT-технологии\n'
                                            'Робототехника\n'
                                            'Английский язык\n'
                                            'Нарды\n'
                                            'Театральное искусство\n'
                                            'Архитектура и дизайн\n'
                                            'Маленькая леди\n'
                                            'Хореография\n'
                                            'Кулинарная школа\n\n'
                                            'Во второй половине дня предусмотрены студиные занятия также на выбор ребенка более 20 студий, точный перечень становится ивестен в первые дни смены. Среди них различные спортивные, вокальные, хореографические, компьютерные и другие студии.')
        bot.send_message(message.chat.id, 'Что-то ещё', reply_markup=main_markup(message))
        bot.register_next_step_handler(message, q)

#Рейтинг
def fgghj(message):
    if message.text == 'Добавить рейтинг':
        bot.send_message(message.chat.id, 'Выбери нужный тебе отряд"')
        bot.register_next_step_handler(message, select_number_squad)

    elif message.text == 'Посмотреть рейтинг':
        bot.send_message(message.chat.id, 'Топ 6 по рейтенгу:\n'
                                          '1. 6 отряд - 45 балл\n'
                                          '2. 5 отряд - 31 балл\n'
                                          '3. 3 отряд - 10 баллов\n'
                                          '4. 1 отряд - 7 баллов\n'
                                          '5. 4 отряд - 3 балла\n'
                                          '6. 2 отряд - 0 баллов')


def select_number_squad(message):
    pass



#Поломки



#Меню
def a(message):
    if message.text == 'Меню🍕':
        bot.send_message(message.chat.id, 'ЗАВТРАК:\nКаша молочная овсяная\nЙогурт\nМасло сливочное\nБатон\nЧай с '
                                          'сахаром\nОБЕД:\nОвощная нарезка\nСуп лапша\nРис опущенный\nГовядина тушёная\n'
                                          'Говядина тушёная с черносливом\nКомпот из сухофруктов\nХлеб\nПОЛДНИК:\nСок '
                                          'фруктовый\nПеченье Сормовское\nФрукт\nУЖИН:\nОвощная нарезка\nГречка '
                                          'рассыпчатая\nКотлеты куриные\nЧай сладкий с лионом\nХлеб сельский\n2-ОЙ УЖИН\nКоктейл молочный')
        bot.send_message(message.chat.id, 'Что-тоещё?', reply_markup=main_markup(message))


#Голосование
def poll_1(message):
    global yes, no
    if message.text == 'Участвовать в опросе':
        bot.send_message(message.chat.id, "Выбери вариант ответа", reply_markup=yes_no_markup)
        bot.register_next_step_handler(message, poll)
    elif message.text == 'Посмотреть результаты':
        results = "'За' проголосовало " + str(yes) + " человек\n" + "'Против' " + str(no) + ' человек'
        bot.send_message(message.chat.id, results, reply_markup=main_markup(message))


def poll(message):
    global yes, no, _is_polling
    if message.chat.id not in _is_polling:
        if message.text == 'Да':
            yes += 1
        elif message.text == 'Нет':
            no += 1
        _is_polling.append(message.chat.id)
        bot.send_message(message.chat.id, 'Твой голос учтен', reply_markup=main_markup(message))
    else:
        bot.send_message(message.chat.id, "Извини, но ты уже голосовал", reply_markup=main_markup(message))

    
# Направления

def p1(message):
    if message.text == 'Python':
        bot.send_message(message.chat.id, 'Выбери группу', reply_markup=markup7)
        bot.register_next_step_handler(message, p2)
    elif message.text == 'Sas-сервис':
        bot.send_message(message.chat.id, 'Выбери группу', reply_markup=markup8)
        bot.register_next_step_handler(message, p2)
    elif message.text == 'DVR':
        bot.send_message(message.chat.id, 'Выбери группу', reply_markup=markup9)
        bot.register_next_step_handler(message, p2)


def p2(message):
    if message.text == 'Python-1':
        bot.send_message(message.chat.id, 'Преподаватель-Хакимов Роман\nНомер телефона-89503100100\nЗанятия проходят в 7 корпусе в кабинете №214', reply_markup=main_markup(message))
    elif message.text == 'Python-2':
        bot.send_message(message.chat.id, 'Преподаватель-Каскаров Родион\nНомер телефона-89061100743\nЗанятия проходят в 7 корпусе в кабинете №213', reply_markup=main_markup(message))
    elif message.text == 'Python-3':
        bot.send_message(message.chat.id, 'Преподаватель-Лотфуллин Камиль\nНомер телефона-89856660205\nЗанятия проходят в холле 7 корпуса', reply_markup=main_markup(message))
    if message.text == 'S-1':
        bot.send_message(message.chat.id,'Преподаватель-Хакимов Роман\nНомер телефона-89503100100\nЗанятия проходят в 7 корпусе в кабинете №214',
                                 reply_markup=main_markup(message))
    elif message.text == 'S-2':
        bot.send_message(message.chat.id,
                                 'Преподаватель-Хакимов Роман\nНомер телефона-89503100100\nЗанятия проходят в 7 корпусе в кабинете №214',
                                 reply_markup=main_markup(message))
    elif message.text == 'S-3':
        bot.send_message(message.chat.id,
                                 'Преподаватель-Хакимов Роман\nНомер телефона-89503100100\nЗанятия проходят в 7 корпусе в кабинете №214',
                                 reply_markup=main_markup(message))
    if message.text == 'VR-1':
        bot.send_message(message.chat.id,
                                 'Преподаватель-Хакимов Роман\nНомер телефона-89503100100\nЗанятия проходят в 7 корпусе в кабинете №214',
                                 reply_markup=main_markup(message))
    elif message.text == 'VR-2':
        bot.send_message(message.chat.id,
                                 'Преподаватель-Хакимов Роман\nНомер телефона-89503100100\nЗанятия проходят в 7 корпусе в кабинете №214',
                                 reply_markup=main_markup(message))
    elif message.text == 'D-VR':
        bot.send_message(message.chat.id,
                                 'Преподаватель-Хакимов Роман\nНомер телефона-89503100100\nЗанятия проходят в 7 корпусе в кабинете №214',
                                 reply_markup=main_markup(message))



def location_w(message):
    print('location_success')
    print(message.text)
    if message.text == "Отмена":
        bot.send_message(message.chat.id,
                         "Список команд:\n1)Работа с списками отрядов.\n2)Получать данные о поломках.\n3)Работать с рейтингом отрядов.\n4)Отправлять вам расписание.")
        return
    bot.send_message(message.chat.id, 'Опишите место, где произошла поломка:\n1)Корпус.\n2)Номер комнаты.')
    bot.register_next_step_handler(message, photo_w)
    message_special[message.chat.id] = [message.text]


def photo_w(message):
    print('info_success')
    if message.text == "Отмена":
        bot.send_message(message.chat.id,
                         "Список команд:\n1)Работа с списками отрядов.\n2)Получать данные о поломках.\n3)Работать с рейтингом отрядов.\n4)Отправлять вам расписание.")
        return
    bot.send_message(message.chat.id, 'Прикрепите фото поломки.')
    message_special[message.chat.id].append(message.text)
    bot.register_next_step_handler(message, info_w)


def info_w(message):
    print('photo_success')
    if message.text == "Отмена":
        bot.send_message(message.chat.id,
                         "Список команд:\n1)Работа с списками отрядов.\n2)Получать данные о поломках.\n3)Работать с рейтингом отрядов.\n4)Отправлять вам расписание.")
        return
    bot.send_message(message.chat.id, 'Хорошо, скоро мы устраним эту проблему.', reply_markup=main_markup(message))
    
    bot.send_message(-355601262, "\n".join(message_special[message.chat.id]))
    try:
        file_info = bot.get_file(message.photo[0].file_id)
        bot.send_photo(-355601262, message.photo[0].file_id)
    except:
        bot.send_message(-355601262, "Ошибка при отправке фотографии")
    message_special[message.chat.id] = []

def unknown_error(message):
    bot.send_message(message.chat.id, 'Неизветная ошибка, попробуйте позже',
                     reply_markup=hide_keyboard)


@bot.message_handler(content_types=['voice'])
def voice_fail(message):
    bot.send_message(message.chat.id, 'Извини, я не принимаю голосовые сообщения. Попробуй перейти в меню "Помощь"',
                     reply_markup=help_keyboard)


@bot.message_handler(content_types=['photo'])
def message_for_photo(message):
    bot.send_message(message.chat.id, 'Зачем ты скидываешь мне это фото? Попробуй перейти в меню "Помощь"',
                     reply_markup=help_keyboard)


@bot.message_handler(content_types=['location'])
def location_message(message):
    bot.send_message(message.chat.id, 'Зачем ты отправил мне своё местоположение? Перейди в меню "Помощь"',
                     reply_markup=help_keyboard)


def send_message23(message):
    request = apiai.ApiAI('a3121094db294780a1525cbb93725ea6').text_request()  # токен DialogFlow
    request.lang = 'ru'
    request.session_id = 'session_1'  # сюда можно писать что захотите
    request.query = message.text
    response = json.loads(request.getresponse().read().decode('utf-8'))
    answer = str(response['result']['fulfillment']['speech'])
    if answer != '':
        bot.send_message(message.chat.id, answer)
        bot.register_next_step_handler(message, send_message23)
    elif message.text == 'Назад':
        bot.send_message(message.chat.id, 'Хорошо\nВыбирите что хотите?', reply_markup=main_markup(message)
                         )
        bot.register_next_step_handler(message, q)
    else:
        bot.send_message(message.chat.id, 'Прости, но я тебя не понимаю😓\n'
                                          'Напиши /start или /help и я тебе обязательно постораюсь помощь)')


def create_list_quests(keyboard=True):
    db = pymysql.connect(host='127.0.0.1',
                         user='root',
                         password='',
                         db='mega_bait_bot',
                         charset='utf8mb4')
    cursor = db.cursor()
    cursor.execute("SELECT name FROM quest WHERE 1")
    x = cursor.fetchall()
    if keyboard:
        list_quest_keyboard = types.ReplyKeyboardMarkup()
        for i in x:
            list_quest_keyboard.row(types.KeyboardButton(i[0]))
        return list_quest_keyboard
    else:
        t = []
        for i in x:
            t.append(i[0])
        return t


def just_quest(message):
    if message.text.strip() in create_list_quests(keyboard=False):
        db = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             db='mega_bait_bot',
                             charset='utf8mb4')
        cursor = db.cursor()
        cursor.execute("SELECT id FROM quest WHERE name='{0}'".format(message.text.strip()))
        x = cursor.fetchall()
        id_quest = str(x[0][0])
        cursor.execute(
            "INSERT INTO quest_player(id_user, quest_id) VALUES('{0}', '{1}')".format(str(message.chat.id), id_quest))
        db.commit()
        bot.send_message(message.chat.id, "Подтвердите участие в квесте", reply_markup=quest_accept_keyaboard)
        bot.register_next_step_handler(message, game_quest)


def game_quest(message):
    if message.text != "Отмена":
        db = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             db='mega_bait_bot',
                             charset='utf8mb4')
        cursor = db.cursor()
        cursor.execute("SELECT quest_id, number_task FROM quest_player WHERE id_user='{0}'".format(message.chat.id))
        x = cursor.fetchall()
        print(x)
        id_quest = x[0][0]
        number_task = x[0][1]
        cursor.execute("SELECT question FROM quest_task WHERE id_quest='{0}' and id='{1}'".format(str(id_quest), str(number_task)))
        print("SELECT question FROM quest_task WHERE id_quest='{0}' and id='{1}'".format(str(id_quest), str(number_task)))
        result = cursor.fetchall()
        print(result)
        bot.send_message(message.chat.id, result[0][0], reply_markup=hide_keyboard)
        bot.register_next_step_handler(message, get_qr_code)
    else:
        x = commands_keyboard_1 if int(get_lvl_position(message.chat.id)) >= 1 else commands_keyboard_2
        bot.send_message(message.chat.id, "Принято", reply_markup=x)


def analiz_answer_text(message):
    db = pymysql.connect(host='127.0.0.1',
                         user='root',
                         password='',
                         db='mega_bait_bot',
                         charset='utf8mb4')
    cursor = db.cursor()
    #result_text = 
    print(result_text)
    cursor.execute("SELECT id FROM quest_task WHERE answer='{0}'".format(result_text))
    result_1 = int(cursor.fetchall()[0][0])
    cursor.execute("SELECT number_task FROM quest_player WHERE id_user='{0}'".format(str(message.chat.id)))
    result_2 = int(cursor.fetchall()[0][0])
    print(result_1 - result_2)
    if result_1 - result_2 == 0:
        pass

def get_qr_code(message):
    db = pymysql.connect(host='127.0.0.1',
                         user='root',
                         password='',
                         db='mega_bait_bot',
                         charset='utf8mb4')
    cursor = db.cursor()
    file_info = bot.get_file(message.photo[0].file_id)
    f = open(r'test.jpg', "wb")
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))
    f.write(file.content)
    f.close()
    result_text_1 = analiz_qr_code("test.jpg")
    result_text = ""
    for p in [int(i) for i in result_text_1.split()]:
        result_text += chr(p)
    print(result_text)
    cursor.execute("SELECT id FROM quest_task WHERE answer='{0}'".format(result_text))
    result_1 = int(cursor.fetchall()[0][0])
    cursor.execute("SELECT number_task FROM quest_player WHERE id_user='{0}'".format(str(message.chat.id)))
    result_2 = int(cursor.fetchall()[0][0])
    print(result_1 - result_2)
    if result_1 - result_2 == 0:
        #cursor.execute("SELECT id FROM quest_task WHERE id_quest='{0}'".format(str(message.chat.id)))
        #result_3 = int(cursor.fetchall()[0][0])
        # f result_1 ==
        bot.send_message(message.chat.id, "Отлично! А теперь ответь на вопрос:", reply_markup=answer_keyboard)
        cursor.execute("UPDATE quest_player SET number_task='{0}' WHERE id_user ='{1}'".format(str(result_1 + 1), str(message.chat.id)))
        db.commit()
        bot.register_next_step_handler(message, game_quest)
    else:
        bot.send_message(message.chat.id, "Ты нашел не тот QR-код. Давай по новой")
        bot.register_next_step_handler(message, game_quest)


def generate_qr_code(message):
    db = pymysql.connect(host='127.0.0.1',
                         user='root',
                         password='',
                         db='mega_bait_bot',
                         charset='utf8mb4')
    cursor = db.cursor()
    cursor.execute("SELECT id FROM quest WHERE name='{0}'".format(name_quest.strip()))
    id_quest = int(cursor.fetchall()[0][0])
    x = []
    y = {}
    print("---------")
    for i in range(number_question_in_quest + 1):
        cursor.execute("SELECT answer FROM quest_task WHERE id='{0}' and id_quest='{1}'".format(str(i + 1), str(id_quest)))
        try:
            x.append(cursor.fetchall()[0][0])
        except:
            pass
    for j, i in enumerate(x):
        t = ""
        for p in i:
            t += str(ord(p)) + " "
        img = qrcode.make(t)
        img.save("qr{0}.png".format(str(j)))
        y["qr{0}.png".format(str(j))] = i

    for i, j in y.items():
        print(i)
        with open(i, 'rb') as f:
            bot.send_photo(message.chat.id, f, caption=j)
    bot.send_message(message.chat.id, "Создание квеста оконченно", reply_markup=main_markup(message))


def analiz_qr_code(img):
    return decode(Image.open(img))[0][0].decode("utf-8")


def constructor_quest(message):
    bot.send_message(message.chat.id, "Введите название квеста:")
    bot.register_next_step_handler(message, step_create_1)


def step_create_1(message):
    global name_quest
    db = pymysql.connect(host='127.0.0.1',
                               user='root',
                               password='',
                               db='mega_bait_bot',
                               charset='utf8mb4')
    cursor = db.cursor()
    name_quest = message.text
    cursor.execute("""INSERT INTO quest(name) VALUES('{0}')""".format(message.text))
    db.commit()
    bot.send_message(message.chat.id, "Введите количество заданий")
    bot.register_next_step_handler(message, step_create_2)


def step_create_2(message):
    global number_question_in_quest
    n = int(message.text)
    number_question_in_quest = int(message.text)
    bot.send_message(message.chat.id, "Введите подсказку для нахождения QR-кода/ключа")
    try:
        bot.register_next_step_handler(message, step_question_1)
    except:
        bot.send_message(message.chat.id, "Ошибка. Введите количество заданий")
        bot.register_next_step_handler(message, step_create_2)


def step_question(message):
    db = pymysql.connect(host='127.0.0.1',
                         user='root',
                         password='',
                         db='mega_bait_bot',
                         charset='utf8mb4')
    cursor = db.cursor()
    print(name_quest)
    cursor.execute("SELECT id FROM quest WHERE name='{0}'".format(name_quest.strip()))
    x = cursor.fetchall()
    print(x)
    id_quest = int(x[0][0])
    cursor.execute("SELECT id FROM quest_task WHERE id_quest='{0}'".format(id_quest))
    bot.send_message(message.chat.id, "Введите подсказку для нахождения QR-кода/ключа", reply_markup=hide_keyboard)
    bot.register_next_step_handler(message, step_question_1)


def step_question_1(message):
    quest_info.append(message.text)
    db = pymysql.connect(host='127.0.0.1',
                         user='root',
                         password='',
                         db='mega_bait_bot',
                         charset='utf8mb4')
    cursor = db.cursor()
    cursor.execute("SELECT id FROM quest WHERE name='{0}'".format(name_quest))
    id_quest = int(cursor.fetchall()[0][0])
    cursor.execute("SELECT id FROM quest_task WHERE id_quest='{0}'".format(id_quest))
    t = cursor.fetchall()
    print(t)
    try:
        i = int(t[-1][-1])
    except:
        i = 1
    bot.send_message(message.chat.id, "Введите вопрос {0}".format(str(i)))
    bot.register_next_step_handler(message, step_answer)


def step_answer(message):
    quest_info.append(message.text)
    db = pymysql.connect(host='127.0.0.1',
                         user='root',
                         password='',
                         db='mega_bait_bot',
                         charset='utf8mb4')
    cursor = db.cursor()
    cursor.execute("SELECT id FROM quest WHERE name='{0}'".format(name_quest))
    id_quest = int(cursor.fetchall()[0][0])
    cursor.execute("SELECT id FROM quest_task WHERE id_quest='{0}'".format(id_quest))
    bot.send_message(message.chat.id, "Введите ответ на вопрос")
    bot.register_next_step_handler(message, step_create)


def step_create(message):
    global quest_info
    quest_info.append(message.text)
    db = pymysql.connect(host='127.0.0.1',
                         user='root',
                         password='',
                         db='mega_bait_bot',
                         charset='utf8mb4')
    cursor = db.cursor()
    cursor.execute("SELECT id FROM quest WHERE name='{0}'".format(name_quest))
    id_quest = cursor.fetchall()[0][0]
    quest_info.append(id_quest)
    print(quest_info)
    cursor.execute("SELECT id FROM quest_task WHERE id_quest='{0}'".format(id_quest))
    t = cursor.fetchall()
    print(t)
    try:
        i = int(t[-1][-1])
    except:
        i = 1
    quest_info.insert(0, i + 1)
    print(quest_info)
    cursor.execute("""INSERT INTO quest_task(id, qr, question, answer, id_quest) VALUES('{0}', '{1}', '{2}', '{3}', '{4}')""".format(*quest_info))
    db.commit()
    print(int(quest_info[0]), number_question_in_quest)
    if int(quest_info[0]) <= number_question_in_quest:
        bot.send_message(message.chat.id, "Вопрос успешно создан", reply_markup=next_keyboard)
        bot.register_next_step_handler(message, step_question)
    else:
        bot.send_message(message.chat.id, "Квест успешно создан. Желаете сгенерировать QR коды?", reply_markup=is_qr_keyboard)
        bot.register_next_step_handler(message, is_qr_code)
    quest_info = []


def db_dict():
    conn = pymysql.connect(host='127.0.0.1',
                               user='root',
                               password='',
                               db='mega_bait_bot',
                               charset='utf8mb4')

    cursor = conn.cursor()
    cursor.execute("""SELECT number_squad, rating FROM rating_squad""")
    data = cursor.fetchall()
    print(data)
    db = {}
    for i in data:
        db[str(i[0])] = int(i[1])
    return db


def db_in_sql(db):
    conn = pymysql.connect(host='127.0.0.1',
                               user='root',
                               password='',
                               db='mega_bait_bot',
                               charset='utf8mb4')

    cursor = conn.cursor()
    cursor.execute("DELETE FROM rating_squad")
    for i, j in db.items():
        cursor.execute("INSERT INTO rating_squad(number_squad, rating) VALUES('{0}', '{1}')".format(i, j))
    conn.commit()
    conn.close()


def choose(message):
    if message.text == 'Изменить рейтинг отрядов':
        if int(get_lvl_position(message.chat.id)) >= 1:
            bot.send_message(message.chat.id, 'У какого отряда вы хотите изменить рейтинг?', reply_markup=select_number_squad_keyboard)
            bot.register_next_step_handler(message, get_squad)
        else:
            bot.send_message(message.chat.id, "У вас недостаточно прав для использования этой команды")
            bot.register_next_step_handler(message, choose)
    elif message.text == 'Посмотреть рейтинг отрядов':
        veiw_rating(message)
    elif message.text == "Отмена":
        bot.send_message(message.chat.id, 'Добро пожаловать в чат-бот.\n'
                                      'Если у вас есть доступ к аккаунту участника лагеря, то выберите меню "Мой код" и введите 6-ти значный код.\n'
                                      'Есл нет, то вам доступны эти функции:\n'
                                      '- Выпускники.\n'
                                      '- Будущие смены.\n'
                                      '- Подробности о лагере.\n'
                                      '- Отзывы.\n'
                                      '- Связь с куратором.\n'
                                      'Выбирите что вас интересует.', reply_markup=main_markup(message))
    else:
        bot.send_message(message.chat.id, 'Я не понимаю', reply_markup=hide_keyboard)


def get_squad(message):
    global number_squad
    db = db_dict()
    try:
        number_squad = message.text.strip()
    except ValueError:
        bot.send_message(message.chat.id, "Такого отряда не существует!")
        return
    if number_squad in db.keys():
        bot.send_message(message.chat.id, "Укажите, насколько вы хотите изменить рейтинг.")
        bot.register_next_step_handler(message, change_rating)
    else:
        bot.send_message(message.chat.id, "Такого отряда не существует!")


def change_rating(message):
    try:
        db = db_dict()
        print(db)
        msg = int(message.text)

        conn = pymysql.connect(host='127.0.0.1',
                               user='root',
                               password='',
                               db='mega_bait_bot',
                               charset='utf8mb4')

        cursor = conn.cursor()
        cursor.execute(
            """SELECT number_squad, rating FROM rating_squad""")
        data = cursor.fetchall()
        print(data)
        db[number_squad] += msg
        bot.send_message(message.chat.id, f'Теперь рейтинг {number_squad} отряда равен {str(db[number_squad])}')
        db_in_sql(db)
    except ValueError:
        bot.send_message(message.chat.id, "Рейтинг должен быть целым числом.")


def add_squad_rating(number):
    conn = pymysql.connect(host='127.0.0.1',
                               user='root',
                               password='',
                               db='mega_bait_bot',
                               charset='utf8mb4')

    cursor = conn.cursor()
    for i in range(number):
        cursor.execute("""INSERT INTO rating_squad(number_squad, rating) VALUES('{0}', '0')""".format(i))
    conn.commit()
    conn.close()


def delete_squad_rating(value=None):
    conn = pymysql.connect(host='127.0.0.1',
                               user='root',
                               password='',
                               db='mega_bait_bot',
                               charset='utf8mb4')

    cursor = conn.cursor()
    if value:
        cursor.execute("""DELETE FROM rating_squad WHERE squad_number='{0}'""".format(value))
    else:
        cursor.execute("DELETE FROM rating_squad WHERE 0")


def veiw_rating(message):
    db = db_dict()
    s = "Рейтинг отрядов:\n"
    for i, j in db.items():
        s += f"{int(i)} отряд: {j}\n"
    bot.send_message(message.chat.id, s, reply_markup=hide_keyboard)


def is_qr_code(message):
    if message.text == "Да":
        bot.send_message(message.chat.id, "Начинаю генерацию, это может занять некоторое время", reply_markup=hide_keyboard)
        generate_qr_code(message)
    else:
        bot.send_message(message.chat.id, "Создание квеста оконченно", reply_markup=main_markup(message))


bot.polling(none_stop=True)
