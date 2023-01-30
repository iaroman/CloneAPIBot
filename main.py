import sysconfig
from telebot import types
import types
import telebot
import configparser

token = '5985528739:AAHfUz2bebAyHf5nlAScQDWCPoBiYw39gII'
bot = telebot.TeleBot("5985528739:AAHfUz2bebAyHf5nlAScQDWCPoBiYw39gII")
@bot.message_handler(content_types=["Поехали"])
def start(message):
    if message.text == "Поехали":
        bot.send_message(message.from_user.id, "Привет, это бот который может решить твое уровнение.Напиши да если ты готов")
        if message.text == "да":
            bot.send_message(message.from_user.id, "Тогда погнали")
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            key_ypovnenie = types.KeyboardButton("Уровнение" )
            key_drobi = types.KeyboardButton("Дроби интерпритатор")
            keyboard.add(key_drobi, key_ypovnenie)


    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши 'уровнение',и я тебе обьясню. ")
    else:
        bot.send_message(message.from_user.id,"Я тебя не понимаю напиши   /help")
@bot.callback_query_handlers(function=lambda call: True)
def callback_worker(call):

    if call.data == "yrovnenie":
        def get_text_messages(kit):
            bot.send_message(kit.from_user.id,"Какого типа вам требуется решить уровнение; * или : или + или - .")
            if kit.text == "*":
                def get_number_messages(XXX):
                    bot.send_message(XXX.from_user.id,
                                     "Каким по счету будет Х 1 или 2.")
                    if XXX == 1:


                        def get_number_messages(m2):
                            bot.send_message(m2.from_user.id,
                                            "Какой будет второй множитель?")
                            def get_number_messages(ans):
                                bot.send_message(ans.from_user.id,
                                                "Какoе произведение?")
                                rovno = "="
                                bot.send_message("1)",ans,"/",m2,)
                                bot.send_message("Ответ", ans / m2 )


    if call.data == "drobi":
        def get_text_messages(message):
            bot.send_message(message.from_user.id,"В разаработке")



bot.polling(none_stop=True, interval=0)


