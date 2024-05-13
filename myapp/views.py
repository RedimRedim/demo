from django.shortcuts import render,HttpResponse
from .models import todoitem
# request handler request -> response is being called views.py in Django
# Create your views here.


def home(request):
    return render(request,"home.html")




