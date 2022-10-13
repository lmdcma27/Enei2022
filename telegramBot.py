#https://api.telegram.org/
#https//core.telegram.org/bots/api

#botname : eneiBot
#username : @chanoYwicho_bot
#Token para el bot @chanoYwicho_bot
#token = '5486126731:AAFJV5QVDXuQoLk6RY-GQFpvjruwnDhSrU4'


#{"ok":true,"result":[{"update_id":475662859,"message":{"message_id":7,"from":{"id":5532347205,"is_bot":false,"first_name":
# "luciano","language_code":"es"},"chat":{"id":5532347205,"first_name":"luciano","type":"private"},"date":1665588791,"text":
# "/start","entities":[{"offset":0,"length":6,"type":"bot_command"}]}}]}

#https://api.telegram.org/bot5486126731:AAFJV5QVDXuQoLk6RY-GQFpvjruwnDhSrU4/getUpdates

from bs4 import BeautifulSoup  #del módulo bs4, necesitamos BeautifulSoup
import requests
import schedule


dic ={'cristian':'1284302283', 'luis':'1410000448'}


def bot_send_text(bot_message, bot_chatID):
    
    bot_token = '5700827288:AAEW8yE5wN88xSi7kkNwV_scWBh8S4Ijyeo'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response
#Buenas tardes, soy el bot encargado de notificar errores duante la ENEI
test_bot = bot_send_text('One piece', dic['luis'])