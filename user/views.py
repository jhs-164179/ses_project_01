from django.contrib.auth import forms
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from .forms import CustomUserCreationForm


class UserCreateView(generic.CreateView):

    form_class = CustomUserCreationForm
    template_name = 'user/user_form.html'
    success_url = reverse_lazy('user:login')