from django.urls import path

from order.views import new_order


urlpatterns = [
    path('order/<int:pk>/', new_order , name='new_order')
]
