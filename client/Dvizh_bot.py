import telebot
from telebot import types


BOT_TOKEN = "8483705345:AAHoNkx4LxJCy_XCnYEao9-Cry5cZ7dxWAs"
SUPPORT_USERNAME = "@nikiairo"

bot = telebot.TeleBot(BOT_TOKEN)

# Приветствие
WELCOME_TEXT = """
Хэй! Ты в официальном боте DVIZH FRANKFURT 🧨🙌

ЧИТАЙ ИНФУ И УВИДИМСЯ НА ДВИЖЕ  😎👇
"""

# Информация о событии
EVENT_INFO = """🔥БОЛЬШОЙ СБОР

Уже 27.09 в 18:00 стартует наш большой сбор — и это будет ночь, которую не захочется забывать. Лес, костёр, гитара, песни Коржа, маршмеллоу, шашлыки, гриль у реки, красивые закаты и виды — всё до самого утра. Да, мы гуляем всю ночь! 🌙🔥

Представь:
✨ тёплая, ламповая, бесценная атмосфера 
✨ фирменные наклейки с нашим логотипом
✨ бир-понг, шум, суета и энергия до потолка
✨ гитара, костёр, маршмеллоу и аромат шашлыков
✨ энергия на всю ночь — гуляем до утра, кайфуем и поём
✨ файеры, костер и единомышленники рядом, что еще нужно для невероятной ночи 

💸 Взнос: 20 евро с человека 

Так же, мы берем: пару палаток, газовый гриль, подушки, пледы, так что даже если нет палатки и захочешь поспать, мы с радостью предоставим тебе место 


📦 Что брать с собой:
✔ хорошее настроение (обязательно)
✔ друзей (чем больше, тем веселее)
✔ тёплую одежду
✔ палатки — если есть, возьми обязательно с собой!

📍 Локация выдаётся сразу после оплаты.
💳 Оплатить можно по немецкой или украинской карте — мы сделали всё, чтобы оплатить было удобно каждому.

Так что отмечай дату, собирай команду и приходи. Это будет ночь Франкфурта — ночь свободы, костра, шашлыков, Коржа, фаеров, красивых закатов и настоящего драйва! 🚀
"""

# Реквизиты оплаты
PAYMENT_DETAILS = f"""Оплата участия:

💳 Реквизиты для оплаты:

Укр Карта: 5355 2800 4940 7032 (ПУМБ)
Sparkasse: DE56 5105 0015 0656 2446 13

После оплаты отправьте скриншот организатору 👉 {SUPPORT_USERNAME}

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