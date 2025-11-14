from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from categorias.models import Categoria

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, "productos/listar.html", {"productos": productos})

def agregar_producto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        precio = request.POST.get("precio")
        categoria_id = request.POST.get("categoria")
        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            categoria_id=categoria_id
        )
        return redirect("listar_productos")

    categorias = Categoria.objects.all()
    return render(request, "productos/agregar.html", {"categorias": categorias})

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == "POST":
        producto.nombre = request.POST.get("nombre")
        producto.descripcion = request.POST.get("descripcion")
        producto.precio = request.POST.get("precio")
        producto.categoria_id = request.POST.get("categoria")
        producto.save()
        return redirect("listar_productos")

    categorias = Categoria.objects.all()
    return render(request, "productos/editar.html", {"producto": producto, "categorias": categorias})
