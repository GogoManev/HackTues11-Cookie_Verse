from django.shortcuts import render

# Create your views here.s
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

User = get_user_model()

def index(request):
    return render(request, 'index.html')
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)  # Check user credentials
        if user is not None:
            login(request, user)  # Logs in the user
            return redirect('index')  # Redirect to homepage
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')
def home(request):
    return render(request, "index.html", {"user": request.user})