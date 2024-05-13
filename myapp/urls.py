from django.urls import path
from . import views #. it means current folder

urlpatterns = [
    path("", views.home, name="home"),

]