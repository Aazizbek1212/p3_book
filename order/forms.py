from django import forms
from order.models import Coment, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'book' ,'phone_number', 'address', 'city']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Coment
        fields = ['name', 'phone_number', 'text']