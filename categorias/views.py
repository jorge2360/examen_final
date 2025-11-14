from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, "categorias/listar.html", {"categorias": categorias})

def agregar_categoria(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        Categoria.objects.create(nombre=nombre, descripcion=descripcion)
        return redirect("listar_categorias")
    return render(request, "categorias/agregar.html")

def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == "POST":
        categoria.nombre = request.POST.get("nombre")
        categoria.descripcion = request.POST.get("descripcion")
        categoria.save()
        return redirect("listar_categorias")
    return render(request, "categorias/editar.html", {"categoria": categoria})
