from django.urls import path
from main.views import  ShopView, home_view, book_view,  contact_view, CreateBookView


urlpatterns = [
    
    path('', home_view, name='home'),
    path('book/<int:id>/', book_view, name='books'),
    path('shop/',ShopView.as_view(), name='shop'),
    path('contact/',contact_view, name='kitoblar'),
    path('create/', CreateBookView.as_view(), name='add')
]
