import requests
from django.contrib.auth import get_user

from config.settings import TG_URL, TG_CHAT_ID
from main.models import Habit


def send_msg_to_tg():
    message = 'Hello World!'
    habits = Habit.objects.filter(user=user)
    print(get_user)

    # try:
    #     response = requests.post(TG_URL, json={'chat_id': TG_CHAT_ID, 'text': message})
    #     print(response.text)
    # except Exception as e:
    #     print(e)
