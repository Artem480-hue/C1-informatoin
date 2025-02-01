import telebot
from telebot import types

token = '7924584184:AAGugrc_FCyM6i-C-PlZZxUeMwKsyJRZSIs'
bot = telebot.TeleBot(token)

# Главная клавиатура
def main_menu_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Купить курсы💵")
    item2 = types.KeyboardButton("О нас👥")
    item3 = types.KeyboardButton("Отзывы👨‍🎓")
    markup.add(item1, item2, item3)
    return markup

# Отзывы
reviews = [
    {
        "author": "Александр Шестаков",
        "course": "Основы программирования на языке Java для школьников",
        "text": "Программирование открывает мир удивительных возможностей. Java пригодится в любом проекте, даже при создании сайта. Мне нравится создавать что-нибудь полезное и я, очень рад что пошел именно на эти курсы, советую всем!"
    },
    {
        "author": "Екатерина Смирнова",
        "course": "Курс Microsoft Office для школьников",
        "text": "Курс очень помог мне разобраться с офисными программами, теперь я легко делаю презентации и документы. Рекомендую!"
    },
    {
        "author": "Иван Петров",
        "course": "Курс по веб-разработке",
        "text": "Крутой курс! Теперь я могу делать свои сайты. Спасибо преподавателям за терпение и помощь!"
    }
]

@bot.message_handler(commands=['start'])
def start_message(message):
    # Отправляем фото
    with open('photo-p1.jpg', 'rb') as photo:  # Замените 'photo-p1.jpg' на фактическое имя файла
        bot.send_photo(message.chat.id, photo)

    # Отправляем приветственное сообщение
    bot.send_message(message.chat.id,
                     'Привет, бот создан нашими учениками @xzwsn и @artemonsos! p.s.: нажмите сюда для начала полной работы кнопок: /button',
                     reply_markup=main_menu_markup())

@bot.message_handler(commands=['button'])
def button_keyboard(message):
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=main_menu_markup())

@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Купить курсы💵":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        course_names = [
            "Программирование на языке Python / 11-17 лет",
            "Программирование на Roblox / 9-13 лет",
            "Программирование на языке Java / 11-14 лет",
            "Веб-разработка. Создание сайтов / 13-17 лет",
            "Системное администрирование / 11-17 лет",
            "Microsoft Office (подготовка презентаций, работа с Word и Excel) / 10 - 12 лет",
            "Юный программист / 7-10 лет",
            "В главное меню"
        ]
        for course in course_names:
            markup.add(types.KeyboardButton(course))
        bot.send_message(message.chat.id, "Выберите курс для покупки:", reply_markup=markup)
    elif message.text in [
        "Программирование на языке Python / 11-17 лет",
        "Программирование на Roblox / 9-13 лет",
        "Программирование на языке Java / 11-14 лет",
        "Веб-разработка. Создание сайтов / 13-17 лет",
        "Системное администрирование / 11-17 лет",
        "Microsoft Office (подготовка презентаций, работа с Word и Excel) / 10 - 12 лет",
        "Юный программист / 7-10 лет"
    ]:
        payment_info = "Для покупки курса скиньте 5000 рублей на номер: +79270033517 Сбер с сообщением -Хочу купить курсы- а также ваш ник в телеграмм, и наш модератор примет вашу заявку и выдаст вам доступ к занятиям!"
        bot.send_message(message.chat.id, payment_info, reply_markup=main_menu_markup())
    elif message.text == "О нас👥":
        text = (
            "Информация о нас:\n"
            "Мы Самарская ИТ компания «Современные технологии», созданная в 2009 году. www.sov-teh.ru\n"
            "Ключевые направления деятельности: программирование, внедрение и системная интеграция.\n\n"
            "В 2012 году Учебный Центр «Современные Технологии» начал обучать ИТ-специалистов, учитывая растущий спрос на рынке труда.\n"
            "В течение более 7 лет центр проводит курсы для взрослых и детей в г. Самара и является ведущим учебным центром Фирмы «1С».\n"
            "Основная специализация — обучение программистов и пользователей по программным продуктам 1С, с акцентом на качественное очное образование.\n"
            "Особой гордостью является проект «1C:Клуб программистов для школьников», в котором обучилось более 4 тысяч участников в Самаре и около 13 тысяч по всей России.\n"
            "Центр тщательно отбирает лучших наставников и преподавателей для обеспечения высокого уровня обучения."
        )
        bot.send_message(message.chat.id, text, reply_markup=main_menu_markup())
    elif message.text == "Отзывы👨‍🎓":
        show_review(message, 0)  # Начинаем с первого отзыва
    elif message.text == "В главное меню":
        bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=main_menu_markup())

def show_review(message, index):
    review = reviews[index]
    text = f"Отзыв от {review['author']}\n" \
           f"Курс: {review['course']}\n\n" \
           f"{review['text']}"

    markup = types.InlineKeyboardMarkup()

    # Создаем кнопки "Назад" и "Вперед" в одном ряду
    row = []
    if index > 0:
        row.append(types.InlineKeyboardButton("⬅️ Назад", callback_data=f"review_prev_{index}"))
    if index < len(reviews) - 1:
        row.append(types.InlineKeyboardButton("➡️ Вперед", callback_data=f"review_next_{index}"))

    if row:
        markup.add(*row)  # Добавляем кнопки в одну строку

    # Добавляем кнопку "Добавить отзыв"
    markup.add(types.InlineKeyboardButton("Добавить отзыв", callback_data="add_review"))

    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('review_'))
def review_callback(call):
    action, index_str = call.data.split('_')[1:]
    index = int(index_str)

    if action == 'prev':
        index = max(0, index - 1)
    elif action == 'next':
        index = min(len(reviews) - 1, index + 1)

    show_review(call.message, index)
    bot.answer_callback_query(call.id)  # Обязательно нужно ответить на callback

@bot.callback_query_handler(func=lambda call: call.data == "add_review")
def add_review_callback(call):
    bot.send_message(call.message.chat.id, "Чтобы написать отзыв отправьте отзыв ему @artemonsos")
    bot.answer_callback_query(call.id)  # Обязательно нужно ответить на callback

# Запуск бота
bot.polling(none_stop=True)
