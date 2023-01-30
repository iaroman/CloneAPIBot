from telebot import types
import types
import telebot
token = '5985528739:AAHfUz2bebAyHf5nlAScQDWCPoBiYw39gII'
bot = telebot.TeleBot("5985528739:AAHfUz2bebAyHf5nlAScQDWCPoBiYw39gII")
@bot.message_handler(content_types=["уровнение"])
def get_text_messages(message):
    if message.text == "уровнениие":
        bot.send_message(message.from_user.id, "Привет, это бот который может решить твое уровнение.Напиши да если ты готов")
        if message.text == "да":
            bot.send_message(message.from_user.id, "Тогда погнали")
            keyboard = types.InlineKeyboardMarkup()
            key_ypovnenie = types.InlineKeyboardButton(text="Уровнение", callback_data="yrovnenie" )
            key_drobi = types.InlineKeyboardButton(text="Дроби интерпритатор", callback_data="drobi")


    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши 'уровнение',и я тебе обьясню. ")
    else:
        bot.send_message(message.from_user.id,"Я тебя не понимаю напиши   /help")
@bot.callback_query_handlers(func=lambda call: True)
def callback_worker(call):

    if call.data == "yrovnenie":
        def get_text_messages(kit):
            bot.send_message(kit.from_user.id,"Какого типа вам требуется решить уровнение; * или : или + или - .")

            if kit.text == "*":
                zapros = int(input("Каким по счету будет X 1 или 2"))
                if zapros == 1:
                    m2 = int(input("Ведите второй множитель"))
                    o1 = int(input("Ведите произведение"))
                    print("x", "*", m2, "=", o1)
                    test1 = input("Мы правильно вели?да или нет .")
                    resh = o1 / m2
                    if test1 != "нет":
                        print("1)", o1, ":", m2, "=", resh)
                        print("Ответ:", resh)
                else:
                    m1 = int(input("Ведите первый множитель"))
                    o1 = int(input("Ведите произведение"))
                    print(m1, "*", "x", "=", o1)
                    test1 = input("Мы правильно вели?да или нет .")
                    resh = o1 / m1
                    if test1 != "нет":
                        print("1)", o1, ":", m1, "=", resh)
                        print("Ответ:", resh)


            elif kit == ":":
                zapros = int(input("Каким по счету будет X 1 или 2"))
                if zapros == 1:
                    m2 = int(input("Ведите второй делитель"))
                    o1 = int(input("Ведите разность"))
                    print("x", ":", m2, "=", o1)
                    test1 = input("Мы правильно вели?да или нет .")
                    resh = o1 * m2
                    if test1 != "нет":
                        print("1)", o1, "*", m2, "=", resh)
                        print("Ответ:", resh)
                else:
                    m1 = int(input("Ведите первое делимое"))
                    o1 = int(input("Ведите произведение"))
                    print(m1, "*", "x", "=", o1)
                    test1 = input("Мы правильно вели?да или нет .")
                    resh = o1 / m1
                    if test1 != "нет":
                        print("1)", o1, ":", m1, "=", resh)
                        print("Ответ:", resh)


            elif kit == "-":
                zapros = int(input("Каким по счету будет X 1 или 2"))
                if zapros == 1:
                    m2 = int(input("Ведите второй вычитаемое"))
                    o1 = int(input("Ведите разность"))
                    print("x", "-", m2, "=", o1)
                    test1 = input("Мы правильно вели?да или нет .")
                    resh = o1 - m2
                    if test1 != "нет":
                        print("1)", o1, "-", m2, "=", resh)
                        print("Ответ:", resh)
                else:
                    m1 = int(input("Ведите первое уменьшаемое"))
                    o1 = int(input("Ведите разность"))
                    print(m1, "-", "x", "=", o1)
                    test1 = input("Мы правильно вели?да или нет .")
                    resh = o1 - m1
                    if test1 != "нет":
                        print("1)", o1, "+", m1, "=", resh)
                        print("Ответ:", resh)


            elif kit == "+":
                zapros = int(input("Каким по счету будет X 1 или 2"))
                if zapros == 1:
                    m2 = int(input("Ведите второй слагаемое"))
                    o1 = int(input("Ведите сумму"))
                    print("x", "-", m2, "=", o1)
                    test1 = input("Мы правильно вели?да или нет .")
                    resh = o1 - m2
                    if test1 != "нет":
                        print("1)", o1, "+", m2, "=", resh)
                        print("Ответ:", resh)
                else:
                    m1 = int(input("Ведите первое слагаемое"))
                    o1 = int(input("Ведите сумму"))
                    print(m1, "-", "x", "=", o1)
                    test1 = input("Мы правильно вели?да или нет .")
                    resh = o1 - m1
                    if test1 != "нет":
                        print("1)", o1, "+", m1, "=", resh)
                        print("Ответ:", resh)
    if call.data == "":
        def get_text_messages(message):
            bot.send_message(message.from_user.id,"В разаработке")




bot.polling(none_stop=True, interval=0)


