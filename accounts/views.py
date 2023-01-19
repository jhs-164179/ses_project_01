from .models import User
from django.http import HttpResponse
from django.contrib import auth
# from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

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

    if request.session.get('user') is not None or request.session.get('id') is not None :
        return redirect('/')
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
    return render(request, 'accounts/login.html', {'form': form})

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
        del(request.session['id'])
    return redirect('/')

# 비밀번호 변경

def re_password(request):
    #request.session['error'] = ''
    #return redirect(reverse('accounts:password'))
    return render(request, 'accounts/password.html')

def renew_password(request):
    
    if request.session.get('user') is None or request.session.get('id') is None :
        messages.success(request, '로그인 후 비밀번호 변경이 가능합니다.')
        return redirect(reverse('accounts:password'))
    
    lastpassword = request.POST.get('lastpass')
    renewpassword1 = request.POST.get('newpass1')
    renewpassword2 = request.POST.get('newpass2')
    get_pw = User.objects.filter(id = request.session.get('id')).values('user_pw')[0]['user_pw']
    print(get_pw)

    # 데이터를 일회성으로 전달하기 위해서는 session에 저장하기 보단 
    # django의 messages 기능을 이용한다.
    # redirect일때 유용하게 사용 가능

    if lastpassword == '' or renewpassword1 == '' or renewpassword2 == '' :
        messages.success(request, '비밀번호란은 비워둘 수 없습니다.')
        #request.session['error'] = '바꿀 비밀번호란은 비워둘 수 없습니다.'
        return redirect(reverse('accounts:password'))
    elif len(renewpassword1) < 8 or len(renewpassword2) < 8:
        messages.success(request, '바꿀 비밀번호는 8자리 이상이어야 합니다.')
        #request.session['error'] = '바꿀 비밀번호는 8자리 이상이어야 합니다.'
        return redirect(reverse('accounts:password'))
    elif not check_password(lastpassword, get_pw):
        messages.success(request, '기존 비밀번호가 일치하지 않습니다.')
        #request.session['error'] = '기존 비밀번호가 일치하지 않습니다.'
        return redirect(reverse('accounts:password'))
    elif renewpassword1 != renewpassword2 :
        messages.success(request, '바꿀 비밀번호가 일치하지 않습니다.')
        #request.session['error'] = '바꿀 비밀번호가 일치하지 않습니다.'
        return redirect(reverse('accounts:password'))
    elif lastpassword == renewpassword1 or lastpassword == renewpassword2 :
        messages.success(request, '바꿀 비밀번호가 기존 비밀번호와 같습니다.')
        #request.session['error'] = '바꿀 비밀번호가 기존 비밀번호와 같습니다.'
        return redirect(reverse('accounts:password'))
    else :
        #request.session['error'] = ''
        repass = User.objects.get(id = request.session.get('id'))
        repass.user_pw = make_password(renewpassword2)
        repass.save()
        del(request.session['user'])
        del(request.session['id'])
        return redirect('/')
