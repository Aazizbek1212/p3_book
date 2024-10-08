from django.shortcuts import redirect
from main.permissions import new_order_permission
from order.forms import OrderForm

import telegram


bot = telegram.Bot(token='7208873739:AAFx1jjr2Trd8saP0AfDjkx0LckwrFAD0I0')


@new_order_permission(login_url='login')
def new_order(request, pk):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            print('sdfsdfsf')
            bot.sendMessage(2095041544, f"Yangi zakaz {form.cleaned_data.get('phone_number')}")
        else:
            print(form.errors)

    return redirect('home')
