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


class ENEIbot:
    def __init__(self) -> None:
        self.__TOKEN = '5486126731:AAFJV5QVDXuQoLk6RY-GQFpvjruwnDhSrU4'
        self._encuestadores = {}

    def bot_send_text(self, message, userID):
        send_text = f'https://api.telegram.org/bot{self.__TOKEN}/sendMessage?chat_id={userID}&parse_mode=Markdown&text={message}'
        response = requests.get(send_text)
        return response
#Buenas tardes, soy el bot encargado de notificar errores duante la ENEI
p = ENEIbot()
test_bot = p.bot_send_text('One piece', dic['luis'])