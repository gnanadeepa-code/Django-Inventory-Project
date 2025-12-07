from django.shortcuts import render, redirect
from .forms import * 
from .models import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
""" def InventoryItemsPage(request):
    context = {
        'items_form': Inventory_ItemForm()
    }
    if request.method == 'POST':
        form = Inventory_ItemForm(request.POST)
        if form.is_valid():
            form.save()
            print("Inventory item added successfully!",form)
            context['success_message'] = "Inventory item added successfully!"
        else:
            context['items_form'] = form  # Return the form with errors
    return render(request, 'inventoryitems.html', context)

def InventoryItemListPage(request):
    try:
        item = InventoryItem.objects.all()
        context = {
            'items': item
        }
        return render(request, 'inventoryLists.html', context)
    except InventoryItem.DoesNotExist:
        return render(request, '404.html', status=404)
    
def DeleteInventoryItem(request, id):
    try:
        item = InventoryItem.objects.get(id=id)
        item.delete()
        return redirect('/inventory/inventoryitemsList/')
    except InventoryItem.DoesNotExist:
        return render(request, '404.html', status=404)
      

def UpdateInventoryItem(request, id): 
    try:
        item = InventoryItem.objects.get(id=id)
        if request.method == 'POST':
            print("Processing POST request for item:", item)
            form = Inventory_ItemForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('/inventory/inventoryitemsList/')
        else:
            print("Rendering update form for item:", item)
            form = Inventory_ItemForm(instance=item)
        context = {
            'items_form': form
        }
        return render(request, 'inventoryitems.html', context)
    except InventoryItem.DoesNotExist:
        return render(request, '404.html', status=404) """
    

class InventoryItemView(LoginRequiredMixin, View):
    login_url = '/'
    def get(self, request):
        print("Handling GET request for InventoryItemView class")
        try:
            context = {
                'items_form': Inventory_ItemForm()
            }
            print("Rendering inventoryitems.html with context:", context)
            return render(request, 'inventoryitems.html', context)
        except InventoryItem.DoesNotExist:
            return render(request, '404.html', status=404)
        
    def post(self, request):
        # Handle any POST requests if necessary
        print("Handling POST request for InventoryItemView class with id:", id)
        form=Inventory_ItemForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/inventory/inventoryitemsList/')
       
        
class InventoryItemListView(LoginRequiredMixin, View):
    login_url = '/'
    def get(self, request):
        print("Handling GET request for InventoryItemListView class")
        try:
            item = InventoryItem.objects.all()
            context = {
                'items': item
            }
            print("Rendering inventoryLists.html with context:", context)
            return render(request, 'inventoryLists.html', context)
        except InventoryItem.DoesNotExist:
            return render(request, '404.html', status=404)
        
class InventoryItemDeleteView(LoginRequiredMixin, View):
    login_url = '/'
    def get(self, request, id):
        print("Handling GET request for InventoryItemDeleteView class with id:", id)
        try:
            item = InventoryItem.objects.get(id=id)
            item.delete()
            return redirect('/inventory/inventoryitemsList/')
        except InventoryItem.DoesNotExist:
            return render(request, '404.html', status=404) 
        
class InventoryItemUpdateView(LoginRequiredMixin, View):
    login_url = '/'
    def get(self, request, id):
        print("Handling GET request for InventoryItemUpdateView class with id:", id)
        try:
            item = InventoryItem.objects.get(id=id)
            form = Inventory_ItemForm(instance=item)
            context = {
                'items_form': form
            }
            print("Rendering inventoryitems.html with context:", context)
            return render(request, 'inventoryitems.html', context)
        except InventoryItem.DoesNotExist:
            return render(request, '404.html', status=404)
        
    def post(self, request, id):
        print("Handling POST request for InventoryItemUpdateView class with id:", id)
        try:
            item = InventoryItem.objects.get(id=id)
            form = Inventory_ItemForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('/inventory/inventoryitemsList/')
            context = {
                'items_form': form
            }
            print("Rendering inventoryitems.html with context:", context)
            return render(request, 'inventoryitems.html', context)
        except InventoryItem.DoesNotExist:
            return render(request, '404.html', status=404)
        