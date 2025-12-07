from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')
def CustomerList(request):
    try:
        customers = Customer.objects.all()
        context = {
            'customers': customers
        }
        return render(request, 'customersList.html', context)
    except Customer.DoesNotExist:
        return render(request, '404.html', status=404)
    
@login_required(login_url='/')   
def CustomerAdd(request):
    context = {
        'customer_form': CustomerForm()
    }
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            print("Customer added successfully!", form)
            context['success_message'] = "Customer added successfully!"
        else:
            context['customer_form'] = form  # Return the form with errors
    return render(request, 'customers.html', context)

@login_required(login_url='/')
def CutomerDelete(request, id):
    try:
        customer = Customer.objects.get(id=id)
        customer.delete()
        return redirect('/orders/customerslist/')
    except Customer.DoesNotExist:
        return render(request, '404.html', status=404)

@login_required(login_url='/')   
def CustomerUpdate(request, id):
    try:
        customer = Customer.objects.get(id=id)
        if request.method == 'POST':
            form = CustomerForm(request.POST, instance=customer)
            if form.is_valid():
                form.save()
                return redirect('/orders/customerslist/')
        else:
            form = CustomerForm(instance=customer)
        context = {
            'customer_form': form
        }
        return render(request, 'customers.html', context)
    except Customer.DoesNotExist:
        return render(request, '404.html', status=404)

@login_required(login_url='/')
def OrderAdd(request):
    context = {
        'order_form': OrderForm()
    }
    if request.method == 'POST':
        form = OrderForm(request.POST)
        print("Form Data Received:", request.POST)
        selected_item = InventoryItem.objects.get(id=request.POST.get('items_reference'))
        print("Selected Item ID:", selected_item)
        print("Selected Item Amount:", selected_item.amount, "GST:", selected_item.gst)
        amount = float(request.POST.get('quantity'))* float(selected_item.amount) if selected_item else None
        gst = (amount * float(selected_item.gst))/100 if selected_item else None
        print("Amount:", amount, "GST:", gst)
        total_amount = amount + gst if amount is not None and gst is not None else None
        print("Total Amount:", total_amount)
        if form.is_valid():
            print("Form is valid:")
            new_order = Order(
                customer_reference=form.cleaned_data['customer_reference'],
                items_reference=form.cleaned_data['items_reference'],
                order_number=form.cleaned_data['order_number'],
                quantity=form.cleaned_data['quantity'],
                amount=amount,
                gst=gst,
                total_amount=total_amount
            )
            new_order.save()
            print("Order added successfully!")
            context['success_message'] = "Order added successfully!"
            return redirect('/orders/orderlist/')
        else:
            print("Form is invalid:", form.errors)
            context['order_form'] = form  # Return the form with errors
    return render(request, 'orders.html', context)

@login_required(login_url='/')
def OrderList(request):
    try:
        orders = Order.objects.all()
        context = {
            'orders': orders
        }
        return render(request, 'orderLists.html', context)
    except Order.DoesNotExist:
        return render(request, '404.html', status=404)

@login_required(login_url='/')
def OrderUpdate(request, id):
    try:
        order = Order.objects.get(id=id)
        if request.method == 'POST':
            form = OrderForm(request.POST, instance=order)
            selected_item = InventoryItem.objects.get(id=request.POST.get('items_reference'))
            print("Selected Item ID:", selected_item)
            print("Selected Item Amount:", selected_item.amount, "GST:", selected_item.gst)
            amount = float(request.POST.get('quantity'))* float(selected_item.amount) if selected_item else None
            gst = (amount * float(selected_item.gst))/100 if selected_item else None
            print("Amount:", amount, "GST:", gst)
            total_amount = amount + gst if amount is not None and gst is not None else None
            print("Total Amount:", total_amount)
            if form.is_valid():
                print("Form is valid:")
                order_filtered = Order.objects.filter(id=id)
                order_filtered.update(
                    customer_reference=form.cleaned_data['customer_reference'],
                    items_reference=form.cleaned_data['items_reference'],
                    order_number=form.cleaned_data['order_number'],
                    quantity=form.cleaned_data['quantity'],
                    amount=amount,
                    gst=gst,
                    total_amount=total_amount
                )
                return redirect('/orders/orderlist/')
        else:
            form = OrderForm(instance=order)
        context = {
            'order_form': form
        }
        return render(request, 'orders.html', context)
    except Order.DoesNotExist:
        return render(request, '404.html', status=404)

@login_required(login_url='/')
def OrderDelete(request, id):
    try:
        order = Order.objects.get(id=id)
        order.delete()
        return redirect('/orders/orderlist/')
    except Order.DoesNotExist:
        return render(request, '404.html', status=404)