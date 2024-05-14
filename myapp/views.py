from django.shortcuts import render,HttpResponse
from .models import todoitem
from myapp.models import Sales
from datetime import date, time
# request handler request -> response is being called views.py in Django
# Create your views here.


def home(request):
    return render(request,"home.html")

sales_data = Sales(
    orderDate=date(2024, 5, 1),
    totalOrders=3000,
    completedOrders=2500,
    totalAmount=1325828,
    ratio='83%',
    completedTime=time(hour=0, minute=1, second=15)
)
sales_data.save()




