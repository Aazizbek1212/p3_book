from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from django_filters.views import FilterView
from main.filters import BookFilter
from main.forms import AddForm
from .models import Book
from order.forms import OrderForm


def home_view(request):
    book = Book.objects.all()[:4]
    books = Book.objects.all()[:6]
    kitoblar = Book.objects.all()
    return render(request, 'index.html', {'book': book, 'books': books, 'kitob': kitoblar})


def book_view(request, id):
    details = Book.objects.get(pk=id)
    form = OrderForm
    return render(request, 'details.html', {'detail': details, 'form': form})


class ShopView(FilterView):
    model = Book
    template_name = 'shop.html'
    context_object_name = 'kitoblar'
    filterset_class = BookFilter

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search', None)
        if search:
            qs = qs.filter(title__contains=search)
        return qs


def contact_view(request):
    return render(request, 'contact.html')


class CreateBookView(PermissionRequiredMixin, CreateView):
    model = Book
    template_name = 'add.html'
    form_class = AddForm
    permission_required = 'Book.add_book'

    def post(self, request, *args, **kwargs):
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect('add')
