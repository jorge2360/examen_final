from django.shortcuts import render

def creditos(request):
    return render(request, "creditos/creditos.html")
