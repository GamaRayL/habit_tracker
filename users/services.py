from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail


def send_confirm_register_mail(self, user, verify_email_url):
    send_mail(
        subject='Поздравляем с регистрацией',
        message=f'Вы зарегистрировались на нашей платформе. '
                f'Для продолжения регистрации перейдите по ссылке '
                f'{get_current_site(self.request)}{verify_email_url}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email]
    )