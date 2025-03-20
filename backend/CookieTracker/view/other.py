from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_func, logout as logout_func
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

def articles(request):
    return render(request, 'Articles.html')

def exercises(request):
    return render(request, 'exercises.html')

def debloat(request):
    return render(request, 'debloat.html')