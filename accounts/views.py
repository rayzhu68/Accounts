from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

def index(request):
    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfuly been logout!")
    return redirect(reverse('index'))