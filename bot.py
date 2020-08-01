import telebot
import prod
t = prod.tamagochi()
users = [] 
chat = set()
tamag = {}
token = "1320476697:AAHq6ifXzVUn3ZRmqnTzz2-iKtwaqhe3SLc"
bot = telebot.TeleBot(token=token)
@bot.message_handler(content_types=['text'])
def ech(message):
    global t
    text = message.text
    user_id = message.chat.id
    chat.add(user_id)
    if not user_id in chat :
        bot.send_message(user_id,"(Ловелин) : Привет,меня зовут Ловелин")
        bot.send_photo(user_id,'https://ltdfoto.ru/images/2020/08/01/LOVELAN1.png')
        bot.send_message(user_id,"(Диктор) :Что-бы покормить её напиши /feed")
        bot.send_message(user_id,"(Диктор) :Что-бы пойти погулять с ней напиши /walk")
        bot.send_message(user_id,"(Диктор) :Что-бы дать ей попить напиши /drink")
        bot.send_message(user_id,"(Диктор) :Что-бы уложить  её спат напиши /sleep")
    else:
        bot.send_message(user_id,"(Диктор) :Что-бы покормить её напиши /feed")
        bot.send_message(user_id,"(Диктор) :Что-бы пойти погулять с ней напиши /walk")
        bot.send_message(user_id,"(Диктор) :Что-бы дать ей попить напиши /drink")
        bot.send_message(user_id,"(Диктор) :Что-бы уложить  её спат напиши /sleep")
        text = message.text
        user_id = message.chat.id
        if text == "/drink" :
            t.drink()
            bot.send_message(user_id,t.thirst)
            bot.send_message(user_id,"Это потребность Ловелин к воде")
            bot.send_photo(user_id,'https://ltdfoto.ru/images/2020/08/01/LOVELIN2.jpg')
        elif text == "/walk" :
            t.takeawalk()
            bot.send_message(user_id,t.walk)
            bot.send_message(user_id,"Это потребность Ловелин к гулянке")
            bot.send_photo(user_id,'https://ltdfoto.ru/images/2020/08/01/LOVELIN3.png')
        elif text == "/sleep" :
            t.sleep()
            bot.send_message(user_id,t.sleepiness)
            bot.send_message(user_id,"Это потребность Ловелин ко сну")
        elif text == "/feed" :
            t.feed()
            bot.send_message(user_id,t.hunger)
            bot.send_message(user_id,"Это потребность Ловелин к еде")
        elif text == "/heal" :
            t.healthc()
            bot.send_message(user_id,t.health)
            bot.send_message(user_id,"Это потребность Ловелин к востановлнию жизней")
    if t.hunger >= 48 :
        bot.send_message(user_id,"Я голодна покорми меня!!!!!!!")
        bot.send_message(user_id,"Я голодна покорми меня!!!!!!!")
        bot.send_message(user_id,"Я голодна покорми меня!!!!!!!")
        bot.send_message(user_id,"Я голодна покорми меня!!!!!!!")
        bot.send_message(user_id,"Я голодна покорми меня!!!!!!!")
        bot.send_message(user_id,"Я голодна покорми меня!!!!!!!")
        bot.send_message(user_id,"Я голодна покорми меня!!!!!!!")
        bot.send_message(user_id,"Я голодна покорми меня!!!!!!!")
    elif t.sleepiness >= 48 :
        bot.send_message(user_id,"Я хочу спать уложи меня спать пожалуйста!!!!!!")
        bot.send_message(user_id,"Я хочу спать уложи меня спать пожалуйста!!!!!!")
        bot.send_message(user_id,"Я хочу спать уложи меня спать пожалуйста!!!!!!")
        bot.send_message(user_id,"Я хочу спать уложи меня спать пожалуйста!!!!!!")
        bot.send_message(user_id,"Я хочу спать уложи меня спать пожалуйста!!!!!!")
        bot.send_message(user_id,"Я хочу спать уложи меня спать пожалуйста!!!!!!")
        bot.send_message(user_id,"Я хочу спать уложи меня спать пожалуйста!!!!!!")
        bot.send_message(user_id,"Я хочу спать уложи меня спать пожалуйста!!!!!!")
    elif t.walk >= 48 :
        bot.send_message(user_id,"Я хочу гулять,пошли погуляем!!!!!!")
        bot.send_message(user_id,"Я хочу гулять,пошли погуляем!!!!!!")
        bot.send_message(user_id,"Я хочу гулять,пошли погуляем!!!!!!")
        bot.send_message(user_id,"Я хочу гулять,пошли погуляем!!!!!!")
        bot.send_message(user_id,"Я хочу гулять,пошли погуляем!!!!!!")
        bot.send_message(user_id,"Я хочу гулять,пошли погуляем!!!!!!")
        bot.send_message(user_id,"Я хочу гулять,пошли погуляем!!!!!!")
        bot.send_message(user_id,"Я хочу гулять,пошли погуляем!!!!!!")
        bot.send_message(user_id,"Я хочу гулять,пошли погуляем!!!!!!")
    elif t.thirst >= 48 :
        bot.send_message(user_id,"ДАЙТЕ ВОДЫ !!!!!!!!!!!!!!!")
        bot.send_message(user_id,"ДАЙТЕ ВОДЫ !!!!!!!!!!!!!!!")
        bot.send_message(user_id,"ДАЙТЕ ВОДЫ !!!!!!!!!!!!!!!")
        bot.send_message(user_id,"ДАЙТЕ ВОДЫ !!!!!!!!!!!!!!!")
        bot.send_message(user_id,"ДАЙТЕ ВОДЫ !!!!!!!!!!!!!!!")
        bot.send_message(user_id,"ДАЙТЕ ВОДЫ !!!!!!!!!!!!!!!")
        bot.send_message(user_id,"ДАЙТЕ ВОДЫ !!!!!!!!!!!!!!!")
        bot.send_message(user_id,"ДАЙТЕ ВОДЫ !!!!!!!!!!!!!!!")
        bot.send_message(user_id,"ДАЙТЕ ВОДЫ !!!!!!!!!!!!!!!")
        bot.send_message(user_id,"ДАЙТЕ ВОДЫ !!!!!!!!!!!!!!!")
        bot.send_message(user_id,"ДАЙТЕ ВОДЫ !!!!!!!!!!!!!!!")
        bot.send_message(user_id,"ДАЙТЕ ВОДЫ !!!!!!!!!!!!!!!")
    user_id = message.chat.id
    tamag[user_id] = message.text
    bot.send_message(user_id,"Голод = "+ str(t.hunger)+"\n Потребность ко сну : " + str(t.sleepiness))
    bot.send_message(user_id,"Потребность к гулянке = " + str(t.walk) +"\n Потребность к питью =" + str(t.thirst))
    def add_user(message):
        user_id = message.chat.id
        if user_id not in users:
            users.append(user_id)
    while True:
        for user_id in users:
            t.update()
        time.sleep(2)
bot.polling(none_stop=True)
                                                                
