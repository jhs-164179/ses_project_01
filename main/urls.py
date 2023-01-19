from django.urls import path
from django.views.generic import TemplateView
from . import views

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from datapg import views as dataviews

app_name = 'main' # 메인 주소
urlpatterns = [
    path('', dataviews.data_page, name="datapage"), # 메인 페이지 주소
    path('', views.MainPage, name="index"), # 메인 페이지 주소
    path('api/', views.api, name="api"), # API 테스트 페이지
]