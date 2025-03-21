from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from ..models import Post
from django.http import Http404

def forum(request):
    return render(request, 'forums.html')