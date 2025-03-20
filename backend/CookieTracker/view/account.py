from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_func, logout as logout_func
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

def login(request):
    if request.user.is_authenticated:
        return redirect('dms')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_func(request, user)
            return redirect('dms')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
        
    return render(request, 'login.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not email or not username or not password:
            return render(request, 'signup.html', {'error': 'All fields are required.'})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username is already taken.'})
        
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email is already in use.'})

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            login_func(request, user)
            return redirect('index')
        except Exception as e:
            return render(request, 'signup.html', {'error': str(e)})

    return render(request, 'signup.html')

@login_required(login_url='/login/')
def logout(request):
    logout_func(request)
    return redirect('index')