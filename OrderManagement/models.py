from django.db import models
from Inventory.models import *

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer_reference = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    items_reference = models.ForeignKey(InventoryItem, on_delete=models.SET_NULL,null=True)
    order_number = models.CharField(max_length=50, unique=True)
    quantity = models.IntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,null=True,default='Pending')
    amount = models.DecimalField(max_digits=10, decimal_places=2,null=True,default=0.00)
    gst = models.DecimalField(max_digits=10, decimal_places=2,null=True,default=0.00)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,null=True,default=0.00)

    def __str__(self):
        return f"Order - {self.customer_reference.name} - {self.items_reference.name} - {self.order_number}"