from django.urls import path
from .views import register, login, logout
from .import views
app_name = 'accounts'


app_name = "accounts"

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
