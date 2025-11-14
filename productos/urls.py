from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar_productos, name="listar_productos"),
    path("agregar/", views.agregar_producto, name="agregar_producto"),
    path("editar/<int:id>/", views.editar_producto, name="editar_producto"),
]
