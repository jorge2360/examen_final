from django.urls import path
from . import views
from .views import index
appname = "home"
urlpatterns = [
    path("", index, name="home"),
]
