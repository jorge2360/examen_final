from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar_categorias, name="listar_categorias"),
    path("agregar/", views.agregar_categoria, name="agregar_categoria"),
    path("editar/<int:id>/", views.editar_categoria, name="editar_categoria"),
]
