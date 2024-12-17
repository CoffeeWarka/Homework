from django.http import HttpResponse
from django.shortcuts import render
from select import error

from .forms import UserRegister

def sign_up_by_html(request):
    users = ['Alex', 'John', 'Amy']
    info = {}
    context = {'info': info}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if username in users:
            info['error'] = 'Пользователь уже существует'
        elif int(age)<18:
            info['error'] = 'Вы должны быть старше 18'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        else:
            info['greet'] = f'Приветствуем, {username}'
        return render(request, 'fifth_task/registration_page.html', context)

    return render(request, 'fifth_task/registration_page.html', context)

def sign_up_by_django(request):
    users = ['Alex', 'John', 'Amy']
    info = {}
    context = {'info': info}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username in users:
                info['error'] = 'Пользователь уже существует'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            else:
                info['greet'] = f'Приветствуем, {username}'
                return render(request, 'fifth_task/registration_page.html', context)
    else:
        info = UserRegister()
        context = {'info': info}
        return render(request, 'fifth_task/registration_page.html', context)


    return render(request, 'fifth_task/registration_page.html', context)