from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import User

# Create your views here.

def signup(request):
    if(request.method == 'POST'):
        # Handle the signup logic here
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        if name and email and password1 and password2:
            user = User.objects.create_user(name=name, email=email, password=password1)
            print('User created:', user)

            return redirect('/login')
        else:
            print('Something went wrong')
        
    else:
        print('Just show the form')
    return render(request, 'account/signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        
        if email and password:
            user = authenticate(email=email, password=password)
            if user is not None:
                auth_login(request, user)
                print('Authentication successful')
                return redirect('/')
            else:
                print('Authentication failed')
        else:
            print('Invalid credentials')
    return render(request, 'account/login.html')