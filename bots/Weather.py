import telegram, requests, json, os

TOKEN = os.environ['TOKEN']
bot = telegram.Bot(TOKEN)

def telegramButtom(chat_id, text = 'Ob-havoni bilish uchin bosing'):
    keyboard = [[telegram.KeyboardButton('Weather 🌦', request_location  = True)]]
    RKM = telegram.ReplyKeyboardMarkup(keyboard, resize_keyboard = True)
    bot.sendMessage(chat_id, text, reply_markup = RKM, protect_content = True)

def weather(lat, lon, API_key):
    url = f'https://api.openweathermap.org/data/2.5/weather'
    r = requests.get(url, params={'lat':lat, 'lon':lon, 'appid':API_key})
    data = r.json()
    return data

def dataText(data):
    state = data['sys']['country']#davlat
    city = data['name']#shahar
    speed = data['wind']['speed']#shamol
    pressure = data['main']['pressure']#bosim
    humidity = data['main']['humidity']#namlik
    base = data['base']#manba
    temp_min = data['main']['temp_min']#pas harorat
    temp_max = data['main']['temp_max']#pas harorat

    data_text = f"----ob-havo----\n\
    Davlat 🗽-----------{state},\n\
    Shaxart 🏙-----------{city},\n\
    Kundizi ☀️---------{temp_max - 273}C🌡,\n\
    Kechasi 🌙---------{temp_min - 273}C🌡,\n\
    shamol tezligi 💨---{speed}m/s,\n\
    havo namligi 💦-----{humidity},\n\
    havo bosimi 🎈------{pressure}\n\
    xabar beradi 🗣-----{base}".title()

    return data_text

s = ''
while True:
    updat = bot.getUpdates()
    update_id = updat[-1].update_id
    chat_id = updat[-1].message.chat.id
    l = updat[-1].message.location
    text = updat[-1].message.text

    if text == '/start' and s != update_id:
        bot.sendMessage(chat_id, 'Xush kelibsiz')
        s = update_id

    elif l != None and s != update_id:
        lat = str(l.latitude)
        lon = str(l.longitude)
        API_key = os.environ['API_key']

        d = weather(lat, lon, API_key)
        text = dataText(d)
        bot.sendMessage(chat_id, text)
        telegramButtom(chat_id)
        s = update_id

    elif s != update_id:
        bot.sendMessage(chat_id, 'So\'ralmagan malumot')
        s = update_id