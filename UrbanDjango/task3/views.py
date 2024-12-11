from django.shortcuts import render

# Create your views here.
def review_temp(request):
    return render(request, 'review.html')

def main_temp(request):
    return render(request, 'main_page.html')

def watchlist_temp(request):
    return render(request, 'watchlist.html')
