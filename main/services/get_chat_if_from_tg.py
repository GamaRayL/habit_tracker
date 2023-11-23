import requests

from config.settings import TG_URL, TG_BOT_TOKEN
from constants import TG_GET_UPDATES, TG_SEND_MESSAGE


def get_chat_id_from_tg():
    # try:
    #     response = requests.post(TG_URL, json={'chat_id': 132093023, 'text': 'Маруся это твой чат ID 132093023, для регистрации. Привет от Гамида и спокойной ночи!)'})
    #     print(response.text)
    # except Exception as e:
    #     print(e)

    try:
        url_get = TG_URL.format(TG_BOT_TOKEN, TG_GET_UPDATES)
        url_post = TG_URL.format(TG_BOT_TOKEN, TG_SEND_MESSAGE)
        data = requests.post(url_get)
        response = data.json()
        if response['result']:
            chat_id = response['result'][-1]['message']['chat']['id']
            requests.post(url_post, json={'chat_id': chat_id, 'text': f'Твой чат ID {chat_id}'})
    except Exception as e:
        print(e)