from django.urls import path

from order.views import new_comment, new_order


urlpatterns = [
    path('order/<int:pk>/', new_order, name='new_order'),
    path('comment/', new_comment, name='comment')
]
