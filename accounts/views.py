from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm

def index(request):
    return render(request, 'index.html')
    
@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfuly been logged out!")
    return redirect(reverse('index'))
    
def login(request):
    """return a login page"""
    if request.method=="POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
            else:
                login_form.add_error(None, "Your username or password is incorrect!")
    else:
        login_form = UserLoginForm()
    
    return render(request, 'login.html', {"login_form": login_form})
    
def registration(request):
    """Render the registration page"""
    return render(request, 'registration.html')