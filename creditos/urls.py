from django.urls import path
from . import views

urlpatterns = [
    path("", views.creditos, name="creditos"),
]
