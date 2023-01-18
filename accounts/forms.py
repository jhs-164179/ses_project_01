from django import forms
from .models import User
from django.contrib.auth.hashers import check_password
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User as us


class LoginForm(forms.Form):
    useremail = forms.EmailField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        }, max_length=64, label="Email")
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },widget=forms.PasswordInput, label = "Password")


    def clean(self):
        cleaned_data = super().clean()
        useremail = cleaned_data.get('useremail')
        password = cleaned_data.get('password')

        if useremail and password:
            try:
                user = User.objects.get(user_email = useremail)
            except User.DoesNotExist:
                self.add_error("useremail", "아이디가 존재하지 않습니다.")
                return

            if not check_password(password, user.user_pw):
                self.add_error("password", "비밀번호가 일치하지 않습니다.")
            else:
                self.user_name = user.user_name
 
        
        
        


# class UserForm(UserCreationForm):
#     email = forms.EmailField(label="이메일")

#     class Meta:
#         model = User
#         fields = ("username", "password1", "password2", "email")