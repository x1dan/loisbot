import requests
import json
import telethon
from colorama import Fore, Back, Style 
class Lois():
    def auth():
        print(Fore.RED + 'Начинаем авторизацию на lois.pro')
        r = requests.get("https://api.lois.pro/v1/auth/tg")
        body = json.loads(r.text)
        return body['code']
    def get_token(code):
        print(Fore.RED + 'Получаем токен с lois.pro')
        r = requests.put("https://api.lois.pro/v1/auth/tg",json={"code": code})
        body = json.loads(r.text)
        return body['token']
    def get_me(token):
        print(Fore.RED + 'Получаем баланс пользователя')
        r = requests.get("https://api.lois.pro/v1/me",headers={
            "Authorization": "Bearer " + token,
        })
        body = json.loads(r.text)
        return body['me']['balance']
    def get_tasks(token):
        print(Fore.RED + 'Получаем задания')
        r = requests.get("https://api.lois.pro/v1/tasks",headers={
            "Authorization": "Bearer " + token,
        })
        body = json.loads(r.text)
        return body['tasks']
    def check_task(token,id):
        print(Fore.RED + 'Проверяем задание - ' + str(id) )
        r = requests.put("https://api.lois.pro/v1/tasks/" + str(id),json={"type": "tg_members"},headers={
            "Authorization": "Bearer " + token,
        })
        body = json.loads(r.text)
        return body

        


