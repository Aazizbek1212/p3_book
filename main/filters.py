from django_filters import FilterSet

from main.models import Book


class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = ['aouthors', 'genre']
