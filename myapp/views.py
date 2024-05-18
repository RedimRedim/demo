from django.shortcuts import render,HttpResponse
from .models import todoitem, Sales
from datetime import date, time
import  matplotlib.pyplot as plt
from io import BytesIO
import base64
from .testfunction import all_sales_data

def home(request):
    context = all_sales_data()
    return render(request,"home.html", context)

def generate_chart():
    # Get data from database
    orders = Sales.objects.all().order_by('orderDate')
    dates = [order.orderDate for order in orders]
    total_orders = [order.totalOrders for order in orders]
    completed_orders = [order.completedOrders for order in orders]
    total_amount = [order.totalAmount for order in orders]

    # create plot
    plt.figure(figsize=(10, 6))
    plt.plot(dates, total_orders, label='Total Orders')
    plt.plot(dates, completed_orders, label='Completed Orders')
    plt.plot(dates, total_amount, label='Total Amount')

    plt.xlabel('Date')
    plt.ylabel('Count/Amount')
    plt.title('Orders Data')
    plt.legend()

    # Save plot as image in memory
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode image as base64
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return graphic

def chart_view(request):
    chart = generate_chart()
    return render(request, 'chart.html', {'chart': chart})


'''sales_data = Sales(
    orderDate=date(2024, 5, 1),
    totalOrders=3000,
    completedOrders=2500,
    totalAmount=1325828,
    ratio='83%',
    completedTime=time(hour=0, minute=1, second=15)
)
sales_data.save()

sales = Sales.objects.all()
for sale in sales:
    print(sale)'''


