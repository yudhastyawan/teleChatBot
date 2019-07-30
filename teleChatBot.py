import requests

def bot_sendtext(bot_message):
    bot_token = 'YOUR TOKEN'
    bot_chatID = 'YOUR CHAT ID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    requests.get(send_text)

def bot_sendPhoto(pathPhoto):
    bot_token = 'YOUR TOKEN'
    bot_chatID = 'YOUR CHAT ID'
    files = {
        'chat_id': (None, bot_chatID),
        'photo': (pathPhoto,
                  open(pathPhoto, 'rb')),
    }

    response = requests.post('https://api.telegram.org/bot' + bot_token + '/sendPhoto',
                             files=files)

def bot_sendDocument(pathFile):
    bot_token = 'YOUR TOKEN'
    bot_chatID = 'YOUR CHAT ID'
    files = {
        'chat_id': (None, bot_chatID),
        'document': (pathFile, open(pathFile, 'rb')),
    }

    response = requests.post('https://api.telegram.org/bot' + bot_token + '/sendDocument', files=files)