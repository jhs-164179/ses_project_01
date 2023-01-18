from .models import User
from django.http import HttpResponse
from django.contrib import auth
# from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm
from django.shortcuts import render, redirect

"""
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
""" 

def register(request):
    if request.method == "GET":
        return render(request, 'accounts/register.html')
    elif request.method == "POST":
        username = request.POST.get('username', None)
        useremail = request.POST.get('email', None)
        password = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)
                        
        err_data = {}   

        if not(username and useremail and password and password2):
            err_data['error'] = '모든 값을 입력해주세요.'
            return render(request, 'accounts/register.html', err_data)
        elif password != password2:
            err_data['error'] = '비밀번호가 다릅니다.'
            return render(request, 'accounts/register.html', err_data)
        elif User.objects.filter(user_name=request.POST['username']).exists():
            err_data['error'] = '이미 가입된 닉네임이 있습니다.'
            return render(request, 'accounts/register.html', err_data)
        elif User.objects.filter(user_email=request.POST['email']).exists():
            err_data['error'] = '이미 가입된 이메일이 있습니다.'
            return render(request, 'accounts/register.html', err_data)
        else:
            user = User(
                user_name=username,
                user_email=useremail,
                user_pw = make_password(password),
            )
            user.save()

        return redirect('/accounts/login/')
        

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_name
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')

    