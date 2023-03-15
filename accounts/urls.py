from django.urls import path
from django.contrib.auth import views as auth_views
from .views import re_password, renew_password, register, login

app_name = 'accounts'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/',login,name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page="/") , name='logout'),
    path('password/', re_password, name='password'),
    path('renew_password/', renew_password, name='renew_password'),
]
