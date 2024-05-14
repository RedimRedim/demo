from django.contrib import admin
from .models import todoitem, Sales

# Register your models here.
admin.site.register(todoitem)
@admin.register(Sales)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('orderDate', 'totalOrders', 'completedOrders', 'totalAmount', 'ratio', 'completedTime')

