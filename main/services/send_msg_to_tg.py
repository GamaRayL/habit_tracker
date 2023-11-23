import requests
from users.models import User
from constants import TG_SEND_MESSAGE
from config.settings import TG_URL, TG_BOT_TOKEN


def send_msg_to_tg():
    users = User.objects.all()
    url_post = TG_URL.format(TG_BOT_TOKEN, TG_SEND_MESSAGE)

    print('Запуск команды...')
    for user in users:
        habits = user.habit.all()
        chat_id = user.tg_chat_id
        for habit in habits:
            message = (f'Место: {habit.place}\n'
                       f'Время начала: {habit.time_to_start}\n'
                       f'Действие: {habit.action}\n'
                       f'Награда: {habit.reward or habit.merge}\n'
                       f'Время на выполнение: {habit.time_to_complete}\n')

            try:
                requests.post(url_post, json={'chat_id': chat_id, 'text': message})
            except Exception as e:
                print(f'Ошибка при отправке сообщения: {e}')
    print('Отправка сообщений закончена.')
