from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def func_temp(request):
    return render(request, 'def_view.html')


class class_temp(TemplateView):
    template_name = 'class_view.html'