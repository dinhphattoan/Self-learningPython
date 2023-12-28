import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, AuthenticationForm
from django.contrib import messages
import simplejson 
from UserApp.forms import myUserCreationForm

def login_view(request):
  
    if request.method == 'POST':
        data = ""
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(data)
        data="Invalid username or password"
        return HttpResponse(data)
    return render(request, 'login.html')# Create a login.html template for the login form

def logout_view(request):
    logout(request)
    return redirect('default_view')  # Replace 'home' with the name of your home view

def signup_view(request):
    if request.method == 'POST':
        form = myUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = myUserCreationForm()
    return render(request, 'signup.html', {'form': form})  # Create a signup.html template for the signup form

def password_reset_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            # Handle password reset logic
            pass
    else:
        form = PasswordResetForm()

    return render(request, 'password_reset.html', {'form': form})  # Create a password_reset.html template for the password reset form

# Define other views as needed for your application
