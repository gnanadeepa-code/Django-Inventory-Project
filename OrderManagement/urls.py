from django.urls import path
from .views import *

urlpatterns = [
    path('customerslist/', CustomerList, name='customerList'), 
    path('customeradd/', CustomerAdd, name='customerAdd'),
    path('deletecustomer/<int:id>/', CutomerDelete, name='customerDelete'),
    path('updatecustomer/<int:id>/', CustomerUpdate, name='customerUpdate'),
    
    path('orderadd/', OrderAdd, name='orderAdd'),
    path('orderlist/', OrderList, name='orderList'),
    path('deleteorder/<int:id>/', OrderDelete, name='orderDelete'),
    path('updateorder/<int:id>/', OrderUpdate, name='orderUpdate'),
]