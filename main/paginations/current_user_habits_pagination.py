from rest_framework.pagination import PageNumberPagination


class CurrentUserHabitsPagination(PageNumberPagination):
    """Пагинация привычек текущего пользователя."""
    page_size = 5
    page_size_query_param = 'page_size'
