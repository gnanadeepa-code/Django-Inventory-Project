from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from .models import User

# Create your views here.
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/orders/customerslist/')

    context = {
        "error": ""
    }
    if request.method == 'POST':
        print(request.POST)
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            print("Authenticated role:", user.role)
            login(request, user)
            if user.role != 2:
                print("Logged in role:", user.role)
                return redirect('/orders/orderlist/')
            elif user.role == 2:
                print("Logged in role:", user.role)
                return redirect('/orders/customerslist/')
        else:
            context["error"] = "* Invalid username or password."
            print("Invalid credentials")
    return render(request, 'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('/')

def signupPage(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        age = request.POST.get('age')

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': '* Username already exists.'})
        
        new_user = User(username=username, first_name=firstname, last_name=lastname, email=email, age=age)
        new_user.set_password(password)
        new_user.save()
        print("User created successfully")
        return redirect('/')
    return render(request, 'signup.html')