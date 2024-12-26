from django.http import HttpResponse
from django.shortcuts import render
from select import error
from .forms import UserRegister
from .models import Buyer, Game, News
from django.shortcuts import render
from django.core.paginator import Paginator


def cart_temp(request):
    return render(request, 'cart.html')


def main_temp(request):
    return render(request, 'main_page.html')


def gamelist_temp(request):
    gamelist = Game.objects.all()
    context = {'gamelist': gamelist}
    return render(request, 'gamelist.html', context)


def sign_up_by_html(request):
    buyers = Buyer.objects.all()

    info = {}
    context = {'info': info}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        for buyer in buyers:
            if username == buyer.name:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'registration_page.html', context)
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'registration_page.html', context)
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'registration_page.html', context)
        Buyer.objects.create(name=username, age=age)
        info['greet'] = f'Приветствуем, {username}'
        return render(request, 'registration_page.html', context)
    return render(request, 'registration_page.html', context)


def sign_up_by_django(request):
    users = Buyer.objects.all()
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
                return render(request, 'registration_page.html', context)
    else:
        info = UserRegister()
        context = {'info': info}
        return render(request, 'registration_page.html', context)
    return render(request, 'registration_page.html', context)


def news(request):
    all_news = News.objects.all().order_by('-date')
    paginator = Paginator(all_news, 3)
    news_page_number = request.GET.get('page')
    news_page = paginator.get_page(news_page_number)
    return render(request, 'news.html', {'page_obj': news_page})
