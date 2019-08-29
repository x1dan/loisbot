from telethon import TelegramClient, events, sync
from telethon.tl.functions.channels import JoinChannelRequest
from modules.lois import Lois

from core.sleep import CountSleep
from colorama import Fore, Back, Style 
import time
import os
import sys

class App():
    def start():
        print(Fore.RED + 'Начинаем авторизацию в телеграмме')
        api_id = os.getenv("API_ID")
        api_hash = os.getenv("API_HASH")
        client = TelegramClient('sessions/'+os.getenv("PHONE"), api_id, api_hash)
        client.start()
        if client.get_me():
            code = Lois.auth()
            print(Fore.GREEN + "Код для авторизации - " + code)
            CountSleep.countdown(t=int(os.getenv("WAIT_AUTH")))
            client.send_message('@loisprobot', code)
            CountSleep.countdown(t=int(os.getenv("WAIT_AUTH")))
            token = Lois.get_token(code)
            print(Fore.GREEN + "Токен авторизации - " + token)
            while True:
                try:
                    CountSleep.countdown(t=int(os.getenv("WAIT_TASKS")))
                    balance = Lois.get_me(token)
                    print(Fore.GREEN + 'Ваш баланс - ' + balance)
                    CountSleep.countdown(t=int(os.getenv("WAIT_TASKS")))
                    tasks = Lois.get_tasks(token)
                    for task in tasks:
                        if task['type'] == 'tg_members':
                            print(Fore.GREEN + 'Подписываемся на - @' + task['item']['attr']['url'])
                            try:
                                client(JoinChannelRequest(task['item']['attr']['url']))
                                CountSleep.countdown(t=int(os.getenv("WAIT_SUBSCRIBE")))
                                client.send_message(os.getenv("USER_NOTIFICATE"), 'Успешная подписка на группу @' + task['item']['attr']['url'])
                                Lois.check_task(token,id=task['id'])
                                CountSleep.countdown(t=int(os.getenv("WAIT_SUBSCRIBE")))
                            except:
                                print(Fore.RED + 'Не удалось подписаться')
                                continue
                except KeyboardInterrupt:
                    print ("Bye")
                    sys.exit()
            



