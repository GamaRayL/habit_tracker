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

EXPECTED_CREATE_DATA = {
    "id": 1,
    "place": "дом",
    "time_to_start": "12:00:00",
    "action": "делать курсовую",
    "is_positive": False,
    "frequency": 2,
    "reward": "сон",
    "time_to_complete": "00:02:00",
    "is_public": False,
    "user": 1,
    "merge": None
}

# Lists
FREQUENCY_CHOICES = [
    (1, 'Каждый день'),
    (2, 'Каждые 2 дня'),
    (3, 'Каждые 3 дня'),
    (4, 'Каждые 4 дня'),
    (5, 'Каждые 5 дня'),
    (6, 'Каждые 6 дня'),
    (7, 'Каждую неделю'),
]