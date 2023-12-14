from main.models import Habit
from rest_framework.serializers import ValidationError


class HabitValidator:
    """Валидатор привычки"""
    def __init__(self, reward_field, merge_field, is_positive_field):
        self.reward_field = reward_field
        self.merge_field = merge_field
        self.is_positive_field = is_positive_field

    def __call__(self, value):
        is_positive = value.get(self.is_positive_field)
        reward = value.get(self.reward_field)
        merge = value.get(self.merge_field)

        if is_positive and (reward or merge):
            raise ValidationError(
                'У приятной привычки не может быть reward(вознаграждения)'
                ' или merge(связанной привычки)!'
            )

        if is_positive:
            return True

        if reward and merge:
            raise ValidationError(
                'Нельзя одновременно выбрать merge(приятную привычку) '
                'и reward(вознаграждение)!'
            )

        if not reward and not merge:
            raise ValidationError(
                'Необходимо указать merge(приятную привычку) '
                'или reward(вознаграждение)!'
            )

        if not reward:
            try:
                habit = Habit.objects.get(pk=merge.pk)
                if not habit.is_positive:
                    raise ValidationError('Привычка не является приятной!')
            except Habit.DoesNotExist:
                raise ValidationError('Привычка не найдена!')
