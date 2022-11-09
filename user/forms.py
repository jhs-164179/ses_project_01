from django.contrib.auth import forms as auth_forms
from django import forms

class CustomUserCreationForm(auth_forms.UserCreationForm):
    email = forms.EmailField(max_length=50, label='이메일')