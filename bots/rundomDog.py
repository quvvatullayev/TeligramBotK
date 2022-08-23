import telegram,requests
import os,json
TOKEN = os.environ['TOKEN']
bot = telegram.Bot(TOKEN)

def getUpdets():
    update = bot.getUpdates()
    text = update[-1].message.text
    chaId = update[-1].message.chat.id
    updetId = update[-1].update_id
    return text, chaId, updetId

def teligramButtom(chaId):
    keyboer = [[telegram.KeyboardButton('start rundom 🐱'), telegram.KeyboardButton('start rundom 🐶')]]
    RKM = telegram.ReplyKeyboardMarkup(keyboer, resize_keyboard = True)
    bot.sendMessage(chaId, 'Rasim tanlash uchin boshlang', reply_markup=RKM)

s = ''
while True:
    text, chaId, updetId = getUpdets()
    if s != updetId:

        if text == '/start':
            bot.sendMessage(chaId, 'Hush kelibsiz rundom dig and cit botga')
            s = updetId

        if text == 'start rundom 🐱':
            url = 'https://aws.random.cat/meow'
            catJson = requests.get(url)
            catJson = catJson.json()
            cat = catJson['url']
            bot.sendPhoto(chaId,cat)
            s = updetId

        elif text == 'start rundom 🐶':
            url = 'https://random.dog/woof.json'
            dogJson = requests.get(url)
            dogJson = dogJson.json()
            dog = dogJson['url']
            bot.sendPhoto(chaId,dog)
            s = updetId

        teligramButtom(chaId)

        s = updetId