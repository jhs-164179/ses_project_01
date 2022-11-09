from .models import User
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            if AuthUser.objects.filter(username=request.POST['username']).count() <= 0:
                user = AuthUser.objects.create_user(
                                                username=request.POST['username'],
                                                password=request.POST['password1']),
                if user != None:
                    user = auth.authenticate(request, username=request.POST['username'], password=request.POST['password1'])
                    auth.login(request, user)
                    return redirect('/')

    return render(request, 'accounts/register.html')
    


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('/')

    