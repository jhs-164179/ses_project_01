from django.urls import path
from django.views.generic import TemplateView
from . import views


from datapg import views as dtspg
app_name = 'main' # 메인 주소
urlpatterns = [
    path('test/', views.MainPage, name="mmindex"), # 메인 페이지 주소


    path('', dtspg.data_page, name="index"), # 메인 페이지 주소
    # path('board/', views.BoardSearch.as_view(), name="search"), # 검색 기능 구현 테스트 추후 비활성화
    path('api/', views.api, name="api"), # API 테스트 페이지
]