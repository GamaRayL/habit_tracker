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
    "id": 2,
    "place": "дом",
    "time_to_start": "12:00:00",
    "action": "делать курсовую",
    "is_positive": False,
    "frequency": 2,
    "reward": "сон",
    "time_to_complete": "00:02:00",
    "is_public": True,
    "user": 1,
    "merge": None
}

EXPECTED_DATA = {
    "id": 5,
    "place": "дом",
    "time_to_start": "12:00:00",
    "action": "делать курсовую",
    "is_positive": False,
    "frequency": 2,
    "reward": "сон",
    "time_to_complete": "00:02:00",
    "is_public": True,
    "user": 4,
    "merge": None
}

EXPECTED_CURRENT_HABIT_LIST = {
    "count": 1,
    "next": None,
    "previous": None,
    "results": [
        {
            "id": 3,
            "place": "дом",
            "time_to_start": "12:00:00",
            "action": "делать курсовую",
            "is_positive": False,
            "frequency": 2,
            "reward": "сон",
            "time_to_complete": "00:02:00",
            "is_public": True,
            "user": 2,
            "merge": None
        }
    ]
}

EXPECTED_UPDATE_DATA = {
    "id": 6,
    "place": "дом",
    "time_to_start": "14:00:00",
    "action": "делать зарядку",
    "is_positive": False,
    "frequency": 2,
    "reward": "сок",
    "time_to_complete": "00:01:00",
    "is_public": True,
    "user": 5,
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
    (10, 'Каждую неделю'),
]
