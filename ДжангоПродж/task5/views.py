from django.http import HttpResponse
from django.shortcuts import render
from select import error

from .forms import UserRegister

def sign_up_by_html(request):
    users = [
        {'username':' Alex', 'password': 'qwertyuio', 'age': 23},
        {'username':' John', 'password': 'rainbowbutterfly', 'age': 50},
        {'username':' Amy', 'password': '123456789', 'age': 18},]
    info = {}
    context = {'info': info}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age)<18:
            info['error'] = 'Вы должны быть старше 18'
        elif username == [user for user in users]:
            info['error'] = 'Пользователь уже существует'
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
    else:
        info = UserRegister()
        context = {'info': info}


    return render(request, 'fifth_task/registration_page.html', context)