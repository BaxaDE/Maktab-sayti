from django.shortcuts import render
from .models import Rahbariyat,Tadbirlar

# Create your views here.
def my_func(request):
    queryset = Rahbariyat.objects.all()
    context = {
        'Rahbariyat':queryset,
    }
    return render(request,'homepage.html',context)
def my_func_1(request):
    queryset = Tadbirlar.objects.all()
    context = {
        'Tadbirlar':queryset,
    }
    return render(request,'homepage.html',context)
