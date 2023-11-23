import requests
from django.contrib.auth import get_user

from config.settings import TG_URL, TG_CHAT_ID
from main.models import Habit


def send_msg_to_tg():
    # message = 'Hello World!'
    # habits = Habit.objects.filter(user=user)
    # print(get_user)
    print(TG_URL)

    try:
        response = requests.post(TG_URL, json={'chat_id': 132093023, 'text': 'Маруся это твой чат ID 132093023, для регистрации. Привет от Гамида и спокойной ночи!)'})
        print(response.text)
    except Exception as e:
        print(e)

    # try:
    #     url = 'https://api.telegram.org/bot6795892672:AAEuABnRXf7MIXPhUMXqSl2rtMOdhaq8Mfg/getUpdates'
    #     # print(TG_URL)
    #     response = requests.post(url)
    #     print(response.json()['result'][-1]['message']['chat'])
    # except Exception as e:
    #     print(e)

