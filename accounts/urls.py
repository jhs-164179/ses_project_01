from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import register, login

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(next_page="/") , name='logout'),
]
