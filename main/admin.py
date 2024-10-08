from django.contrib import admin
from main.models import Book, Author, Genre


class AddDeleteViewMixin:

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True


@admin.register(Book)
class BookAdmin(AddDeleteViewMixin, admin.ModelAdmin):
    date_hierarchy = 'date_published'
    list_display = ['title', 'date_published', 'price', 'description']


@admin.register(Author)
class AuthorAdmin(AddDeleteViewMixin, admin.ModelAdmin):
    list_display = ['name', 'brith_date', 'country', 'picture']


admin.site.register(Genre)
