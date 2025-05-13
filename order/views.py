from django.shortcuts import redirect
from main.permissions import new_order_permission
from order.forms import CommentForm, OrderForm

import telegram


bot = telegram.Bot(token='7545027509:AAFTzyoz5FA0mgL75Lj4nA6VI5MGTBWCF7g')


@new_order_permission(login_url='login')
def new_order(request, pk):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            bot.sendMessage(2095041544, f"Yangi zakaz keldi {form.cleaned_data.get('name', 'book')}")
        else:
            print(form.errors)

    return redirect('home')


@new_order_permission(login_url='login')
def new_comment(request):
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return redirect('kitoblar')