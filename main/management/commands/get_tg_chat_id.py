import requests
from django.core.management import BaseCommand

from config.settings import TG_URL, TG_BOT_TOKEN
from constants import TG_GET_UPDATES, TG_SEND_MESSAGE


class Command(BaseCommand):
    help = 'Команда для получения chat ID из Telegram бота и отправка его обратно.'

    def handle(self, *args, **options):
        try:
            print('Запуск команды...')
            url_get = TG_URL.format(TG_BOT_TOKEN, TG_GET_UPDATES)
            url_post = TG_URL.format(TG_BOT_TOKEN, TG_SEND_MESSAGE)
            data = requests.post(url_get)
            response = data.json()

            if response['result']:
                print('Идет отправка сообщения в Telegram...')
                chat_id = response['result'][-1]['message']['chat']['id']
                requests.post(url_post, json={
                    'chat_id': chat_id,
                    'text': f'На вот, держи свой чат ID: {chat_id}'
                })
                print('Сообщение отправлено.')

        except Exception as e:
            print('Сообщение не отправлено.')
            print(e)
