from django.shortcuts import render, redirect, reverse
from django.contrib import auth

def index(request):
    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return redirect(reverse('index'))