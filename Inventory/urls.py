from django.urls import path
from .views import *

urlpatterns = [
    # Function-Based Views
   # path('inventoryitems/', InventoryItemsPage, name='inventoryitems'), 
   # path('inventoryitemsList/', InventoryItemListPage, name='inventoryitemLists'), 
   # path('deleteinventoryitem/<int:id>/', DeleteInventoryItem, name='deleteinventoryitem'),
   # path('updateinventoryitem/<int:id>/', UpdateInventoryItem, name='updateinventoryitem'),
    
    # Class-Based Views
    path('inventoryitems/', InventoryItemView.as_view(), name='inventoryitems'), 
    path('inventoryitemsList/', InventoryItemListView.as_view(), name='inventoryitemLists'), 
    path('deleteinventoryitem/<int:id>/', InventoryItemDeleteView.as_view(), name='deleteinventoryitem'),
    path('updateinventoryitem/<int:id>/', InventoryItemUpdateView.as_view(), name='updateinventoryitem'),
   
]