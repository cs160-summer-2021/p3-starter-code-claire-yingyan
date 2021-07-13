from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'coloring/index.html')

def home(request):
    return render(request, 'coloring/home.html')

def rec_easy(request):
    return render(request, 'coloring/rec_easy.html')

def rec_hard(request):
    return render(request, 'coloring/rec_hard.html')

def color_easy(request):
    return render(request, 'coloring/color_easy.html')

def color_hard(request):
    return render(request, 'coloring/color_hard.html')

def info(request):
    return render(request, 'coloring/info.html')
