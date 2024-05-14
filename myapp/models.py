from django.db import models


# Create your models here.

class todoitem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class Sales(models.Model):
    orderDate = models.DateField()
    totalOrders = models.IntegerField()
    completedOrders = models.IntegerField()
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    ratio = models.CharField(max_length=10)
    completedTime = models.TimeField()

    def __str__(self):
        return f"Sales data for {self.orderDate}"
    
    
    

'''order_data = [
    {'orderDate': '2024-05-01', 'totalOrders': 3000, 'completedOrders': 2500, 'totalAmount': 1325828, 'ratio': '83%', 'completedTime': '00:01:15'},
    {'orderDate': '2024-05-02', 'totalOrders': 3500, 'completedOrders': 2800, 'totalAmount': 1459823, 'ratio': '80%', 'completedTime': '00:01:20'},
    {'orderDate': '2024-05-03', 'totalOrders': 4000, 'completedOrders': 3500, 'totalAmount': 1675893, 'ratio': '87.5%', 'completedTime': '00:01:10'},
]'''