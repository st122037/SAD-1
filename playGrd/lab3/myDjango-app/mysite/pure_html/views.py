from django.shortcuts import render
from django.template import loader


def index (request):
    return render(request, 'index.html')

def index1 (request):
    return render(request, 'index1.html')

def index2(request):
    return render(request, 'index2.html')

def index3 (request):
    return render(request, 'index3.html')