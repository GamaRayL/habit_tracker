from main.models import Habit
from celery import shared_task
from datetime import datetime, timedelta
from main.services.send_msg_to_tg import send_msg_to_tg
from django_celery_beat.models import PeriodicTask, IntervalSchedule


@shared_task
def task_send_msg_to_tg(habit_id):
    send_msg_to_tg(habit_id)


for habit in Habit.objects.all():
    habit_time = datetime.combine(datetime.today(), habit.time_to_start)
    previous_tasks = PeriodicTask.objects.filter(
        name__contains=f'ID задачи {habit.id}'
    )
    previous_tasks.delete()

    if datetime.now() < habit_time:
        # Создаем интервал для повтора
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=habit.frequency,
            period=IntervalSchedule.DAYS,
        )

        # Создаем задачу для повторения
        PeriodicTask.objects.create(
            interval=schedule,
            name=f'ID задачи {habit.id}. Задача: {habit.__str__()}',
            task='main.tasks.task_send_msg_to_tg',
            args=[habit.id],
            start_time=habit_time - timedelta(seconds=15)
        )
