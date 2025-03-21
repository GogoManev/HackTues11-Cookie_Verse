from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from ..models import Post, Comment
from django.http import Http404

User = get_user_model()

def articles(request):
    return render(request, 'Articles.html')

def exercises(request):
    return render(request, 'exercises.html')

def debloat(request):
    return render(request, 'debloat.html')

def guthealth(request):
    return render(request, 'guthealth.html')