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
    
    

