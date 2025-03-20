from django.shortcuts import render

# Create your views here.s
from django.contrib.auth import get_user_model

User = get_user_model()


def index(request):
    return render(request, 'index.html')
