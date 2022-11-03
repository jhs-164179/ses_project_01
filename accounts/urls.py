from django.urls import path
from .views import register, login, logout
app_name = 'accounts' # 메인 주소
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
