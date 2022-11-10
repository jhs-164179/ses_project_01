from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'main' # 메인 주소
urlpatterns = [
    path('', views.MainPage, name="index"), # 메인 페이지 주소
    # path('board/', views.BoardSearch.as_view(), name="search"), # 검색 기능 구현 테스트 추후 비활성화
    path('api/', views.api, name="api"), # API 테스트 페이지
    #path('',TemplateView.as_view(template_name='index.html'))
]