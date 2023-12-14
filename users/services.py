from django.conf import settings
from django.core.mail import EmailMessage


def send_confirm_register_mail(user, absolute_verify_email_url):
    """Отправка письма со ссылкой для подтверждения почты пользователя"""
    message = (f'Вы зарегистрировались на нашей платформе. '
               f'Для продолжения регистрации перейдите по '
               f'<a href="{absolute_verify_email_url}">ссылке</a>')

    email = EmailMessage(
        subject='Поздравляем с регистрацией',
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email],
    )
    email.content_subtype = 'html'
    email.send()
