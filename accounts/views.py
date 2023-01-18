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
            return render(request, 'accounts/register.html')
        elif password != password2:
            err_data['error'] = '비밀번호가 다릅니다.'
            return render(request, 'accounts/register.html')
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
            # 로그인 시에 login_id를 입력하지 않으므로 직접 아래의 줄처럼 직접 DB에서 가져온다.
            get_id = User.objects.filter(user_name = form.user_name).values('id')[0]['id']
            request.session['user'] = form.user_name
            request.session['id'] = get_id
            #print(get_id)
            return redirect('/')
    else:
        form = LoginForm()
    print(form.errors)
    return render(request, 'accounts/login.html', {'form': form})

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')

    