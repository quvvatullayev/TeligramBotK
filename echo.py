import telegram, os,json

TOKEN = os.environ['TOKEN']
bot = telegram.Bot(TOKEN)

def getUpdets():
    update = bot.getUpdates()
    chaId = update[-1].message.chat.id
    updetId = update[-1].update_id
    return chaId, updetId

s = ''
while True:
    chaId, updetId = getUpdets()
    if s != updetId:
        data = bot.getUpdates()
        basData = data[-1].message

        if basData.text != None:
            text = basData.text
            bot.sendMessage(chaId, text)
            s = updetId


        elif basData.document != None:
            document = basData.document.file_id
            bot.sendDocument(chaId,document)
            s = updetId


        elif basData.video_note != None:
            video_note = basData.video_note.file_id
            bot.sendVideoNote(chaId, video_note)
            s = updetId


        elif basData.voice != None:
            voice = basData.voice
            bot.sendVoice(chaId, voice)
            s = updetId


        elif basData.video != None:
            video = basData.video.file_id
            bot.sendVideo(chaId, video)
            s = updetId


        elif basData.audio != None:
            audio = basData.audio.file_id
            bot.sendAudio(chaId, audio)
            s = updetId


        elif basData.sticker != None:
            sticker = basData.sticker.file_id
            bot.sendSticker(chaId, sticker)
            s = updetId


        elif basData.dice != None:
            emoji = basData.dice.emoji
            bot.sendDice(chaId, emoji)
            s = updetId


        elif basData.photo != None:
            photo = basData.photo[0]['file_id']
            bot.sendPhoto(chaId, photo)
            s = updetId
