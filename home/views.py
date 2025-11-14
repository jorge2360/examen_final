from django.shortcuts import render

def index(request):
    return render(request, "home/index.html")

def creditos(request):
    return render(request, "home/creditos.html")
