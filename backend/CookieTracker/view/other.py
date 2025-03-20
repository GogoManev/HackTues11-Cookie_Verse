from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

def articles(request):
    return render(request, 'Articles.html')

def exercises(request):
    return render(request, 'exercises.html')

@login_required(login_url='/login/')
def newpost(request):
    return render(request, 'newpost.html')