ADMIN = 'администратор'
MEMBER = 'участник'

# TG Methods
TG_GET_UPDATES = 'getUpdates'
TG_SEND_MESSAGE = 'sendMessage'

# Dictionary
NULLABLE = {'null': True, 'blank': True}

USER_ROLES = {
    'admin': ADMIN,
    'member': MEMBER
}

FREQUENCY_CHOICES = [
    (1, 'Каждый день'),
    (2, 'Каждые 2 дня'),
    (3, 'Каждые 3 дня'),
    (4, 'Каждые 4 дня'),
    (5, 'Каждые 5 дня'),
    (6, 'Каждые 6 дня'),
    (7, 'Каждую неделю'),
]