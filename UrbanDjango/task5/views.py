from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
import os

# Create your views here.

users = ['Андрей', 'Руслан', 'Миша', 'Маша', 'bolivar']
info_s = {}

def sign_up_by_django(request):
    if request.method == 'POST':
        info=info_s
        user_flag=False
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            in_user=username in users
            if password == repeat_password:
                if age>=18:
                    if in_user == False:
                        user_flag = True
                    else:
                        info['error'] = 'Пользователь уже существует'
                else:
                    info['error'] = 'Вы должны быть старше 18'
            else:
                info['error']='Пароли не совпадают!'

            if user_flag:
                message = (f'Приветствуем, {username}!')
                print(message)
            else:
                message = info['error']
            return HttpResponse(message)

        else:
            form = UserRegister()
            info['form'] = form
        return render(request, 'fifth_task/registration_page.html', info)

def sign_up_by_html(request):
    if request.method == 'POST':
        info=info_s
        user_flag=False
        user_have = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        in_user = username in users
        if password == repeat_password:
            if age >= 18:
                if in_user == False:
                    user_flag = True
                else:
                    info['error'] = 'Пользователь уже существует'
            else:
                info['error'] = 'Вы должны быть старше 18'
        else:
            info['error'] = 'Пароли не совпадают!'

        if user_flag:
            message = (f'Приветствуем, {username}!')
            print(message)
        else:
            message = info['error']
            print(message)
        return HttpResponse(message)
    return render(request, 'fifth_task/registration_page.html')


