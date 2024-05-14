from django.urls import path
from .views import chart_view
from . import views #. it means current folder

urlpatterns = [
    path("", views.home, name="home"),
    path("chart/", chart_view, name="chart"),
]