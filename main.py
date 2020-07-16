import telebot
import configure 
from telebot import types
 
bot = telebot.TeleBot(configure.config['token']);
@bot.message_handler(commands=['help'])
def help(message):
    
        bot.send_message(message.from_user.id, "Напиши /start, если хочешь провести вечер за просмотром фильма, но не знаешь что посмотреть!)");

@bot.message_handler(commands=['start'])
def start(message):
    global isRunning
    isRunning = False
    if isRunning == False:
        markup_inline = types.InlineKeyboardMarkup()
        item_fantasy = types.InlineKeyboardButton(text = 'Фэнтези', callback_data = 'fantasy')
        item_detective = types.InlineKeyboardButton(text = 'Детектив', callback_data = 'detective')
        item_comics = types.InlineKeyboardButton(text = 'Комиксы', callback_data = 'comics')
        item_drama = types.InlineKeyboardButton(text = 'Драмма', callback_data = 'drama')
    
        markup_inline.add(item_drama, item_comics, item_detective, item_fantasy)
        bot.send_message(message.chat.id, 'Отлично! Давайте начнем с жанра, какой предпочитаешь?', 
                            reply_markup = markup_inline
                        )  
        isRunning = True
@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item_ok = types.KeyboardButton("Отличный фильм, пойду посмотрю!")
    item_no = types.KeyboardButton("Нет, пожалуй хочу еще один")
    markup_reply.add(item_ok, item_no)
    if call.data == 'fantasy':
            bot.send_message(call.message.chat.id, 'Если ты настоящий ценитель кинематогрофа, ты знаешь, что лучше фильма тебе не найти - The Lord of the Rings. The Return of the King. Вот ссылка - https://www.kinopoisk.ru/film/3498/', 
                            reply_markup = markup_reply
                        )  
    elif call.data == 'detective':
            bot.send_message(call.message.chat.id, 'Мой любимый фильм из таких - Murder on the Orient Express. Вот ссылка - https://www.kinopoisk.ru/film/817969/', 
                            reply_markup = markup_reply
                        )
    elif call.data == 'comics':
            bot.send_message(call.message.chat.id, 'Мой любимый фильм из таких - Doctor Strange. Вот ссылка - https://www.kinopoisk.ru/film/409600/', 
                            reply_markup = markup_reply
                        )
    elif call.data == 'drama':
            bot.send_message(call.message.chat.id, 'Мой любимый фильм из таких - Green Book. Вот ссылка - https://www.kinopoisk.ru/film/1108577/', 
                            reply_markup = markup_reply
                        )
@bot.message_handler(content_types = ['text'])
def get_text(message):
    if message.text == "Нет, пожалуй хочу еще один":
            bot.send_message(message.chat.id, 'Ухх, значит видел уже как Гендальф Балрога сразил, ну ладно, вот тебе еще - The Hobbit: An Unexpected Journey.  Вот ссылка - https://www.kinopoisk.ru/film/278522/')
            bot.send_message(message.chat.id, 'Любишь больше динамики в фильме? Тогда лови - Now You See Me. Вот ссылка - https://www.kinopoisk.ru/film/522892/')
            bot.send_message(message.chat.id, 'Не нравится Кибербич? Тогда понравится Тони Старк! - Iron Man. Вот ссылка - https://www.kinopoisk.ru/film/61237/')
            bot.send_message(message.chat.id, 'Лучший фильм для настоящих мужчин - The Wolf of Wall Street. Вот ссылка - https://www.kinopoisk.ru/film/462682/')
    if message.text == "Отличный фильм, пойду посмотрю!":
         bot.send_message(message.chat.id, 'Приятного просмотра, заходи когда захочешь!')
         isRunning = False
bot.polling(none_stop=True, interval=0)