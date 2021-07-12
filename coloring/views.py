from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def rec_easy(request):
    return render(request, 't2/rec_easy.html')

def rec_hard(request):
    return render(request, 't2/rec_hard.html')

def color_easy(request):
    return render(request, 't2/color_easy.html')

def color_hard(request):
    return render(request, 't2/color_hard.html')

def info(request):
    return render(request, 't2/info.html')
