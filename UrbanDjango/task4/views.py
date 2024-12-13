from django.shortcuts import render


def review_temp(request):
    return render(request, 'review.html')

def main_temp(request):
    return render(request, 'main_page.html')

def watchlist_temp(request):
    movie1 = 'Крёстный отец'
    movie2 = 'Список Шиндлера'
    movie3 = 'Хороший, плохой, злой'
    context = {'movie1': movie1, 'movie2': movie2, 'movie3': movie3,
               }
    return render(request, 'watchlist.html', context)

