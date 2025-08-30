import telebot
from telebot import types


BOT_TOKEN = "8483705345:AAHoNkx4LxJCy_XCnYEao9-Cry5cZ7dxWAs"
SUPPORT_USERNAME = "@nikiairo"

bot = telebot.TeleBot(BOT_TOKEN)

# Приветствие
WELCOME_TEXT = """Привет! 👋
Добро пожаловать в сообщество фанатов Коржа во Франкфурте! 🇩🇪🎵

Мы собираемся на крутой движ, где всегда весело и музыка на максимуме! 🎤🔥
"""

# Информация о событии
EVENT_INFO = """ℹ️Информация о предстоящих событиях:

⏳06.09 DVIZH QUEST
🌉 В 16:00 стартуем в центре города, выполняем задания квеста и финишируем на GrillPlatz с мясом, пивом и тусой 🍖🍻🔥

🎯 Тебя ждут подсказки, движ, соревнование и главный приз — фирменная футболка DVIZH FRANKFURT 🏆

💸 Квест бесплатный, сбор после — по 15€.

Хочешь участвовать? 

Переходи в канал 👉 https://t.me/dwizhfrankfurt/30
"""

# Реквизиты оплаты
PAYMENT_DETAILS = f"""Оплата участия:

💳 Реквизиты для оплаты:

Укр Карта: 5355280049407032 (ПУМБ)
Sparkasse: DE 56510500150656244613

После оплаты отправьте скриншот в организатору 👉 {SUPPORT_USERNAME}

"""

# FAQ
FAQ_TEXT = """❓ Часто задаваемые вопросы:

1️⃣ Зачем этот бот?  

- Бот создан, чтобы было проще организовывать большие сборы и дальнейшие поездки

2️⃣ Почему оплата на карту?   

- Каждую встречу организаторы делают закупы за свой счет, в основном это сумма варьируется от 300-500€ (не говоря уже о других крупных событиях)


3️⃣ За что я скидываюсь?   

- На встречах вы получаете: Безалкогольные напитки (вода,фанта,пепси,кола,спрайт), Пару бутылок пива, Шашлык, Овощи ,Жареную картошка, Маршмэлоу, Булочки/тосты, Нарезка (сыр,колбаса)

4️⃣ Я могу не скидываться?

-Да, конечно. Вы можете брать с собой еду и напитки самостоятельно, и приходить к нам за вайбом и компанией.

Убедительно просим,если вы берете еду и напитки с собой, сообщите пожалуйста нам и уважайте друг друга. Если вы не скидываетесь, не берите ничего со стола и из напитков, так вы показывает свое неуважение к организатором и к другим людям которые скинулись!

"""


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn_info = types.InlineKeyboardButton("ℹ️ Информация о событии", callback_data="info")
    btn_pay = types.InlineKeyboardButton("💳 Оплатить участие", callback_data="pay")
    btn_support = types.InlineKeyboardButton("📞 Контакты поддержки", callback_data="support")
    btn_faq = types.InlineKeyboardButton("❓ FAQ", callback_data="faq")
    markup.add(btn_info)
    markup.add(btn_pay)
    markup.add(btn_support)
    markup.add(btn_faq)

    bot.send_message(message.chat.id, WELCOME_TEXT, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "info":
        markup = types.InlineKeyboardMarkup()
        btn_back = types.InlineKeyboardButton("⬅️ Назад в меню", callback_data="back")
        markup.add(btn_back)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=EVENT_INFO,
                              reply_markup=markup)

    elif call.data == "pay":
        markup = types.InlineKeyboardMarkup()
        btn_back = types.InlineKeyboardButton("⬅️ Назад в меню", callback_data="back")
        markup.add(btn_back)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=PAYMENT_DETAILS,
                              reply_markup=markup)

    elif call.data == "support":
        markup = types.InlineKeyboardMarkup()
        btn_back = types.InlineKeyboardButton("⬅️ Назад в меню", callback_data="back")
        markup.add(btn_back)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=f"📩 Связаться с поддержкой: {SUPPORT_USERNAME}",
                              reply_markup=markup)

    elif call.data == "faq":
        markup = types.InlineKeyboardMarkup()
        btn_back = types.InlineKeyboardButton("⬅️ Назад в меню", callback_data="back")
        markup.add(btn_back)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=FAQ_TEXT,
                              reply_markup=markup)

    elif call.data == "back":
        start(call.message)  # возвращаем в меню


print("🤖 Бот запущен...")
bot.polling(none_stop=True)

###  powered by VI  ###