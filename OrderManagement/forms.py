from django.forms import ModelForm
from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone','address']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer_reference', 'items_reference', 'order_number', 'quantity']