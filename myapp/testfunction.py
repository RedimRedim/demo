from myapp.models import Sales

#generete all SalesData
def all_sales_data():
    all_sales = Sales.objects.all()
    orderDate = [sale.orderDate.isoformat() for sale in all_sales]
    totalOrders = [sale.totalOrders for sale in all_sales]
    completedOrders = [sale.completedOrders for sale in all_sales]
    totalAmount = [round(float(sale.totalAmount), 2) for sale in all_sales]
    ratio = [sale.ratio for sale in all_sales]
    completedTime = [sale.completedTime for sale in all_sales]

    context = {
        'orderDate': orderDate,
        'totalOrders': totalOrders,
        'completedOrders': completedOrders,
        'totalAmount': totalAmount,
        'ratio': ratio,
        'completedTime': completedTime}

    return context