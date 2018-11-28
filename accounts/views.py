from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm

def index(request):
    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfuly been logout!")
    return redirect(reverse('index'))
    
def login(request):
    login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})
    
    