from django.core.management import BaseCommand

from main.services.send_msg_to_tg import send_msg_to_tg


class Command(BaseCommand):
    def handle(self, *args, **options):
        send_msg_to_tg()