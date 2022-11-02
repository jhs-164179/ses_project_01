from django.urls import path

from .import views

app_name = 'board'
urlpatterns = [
    # 자유게시판 페이지로 이동하는 URL 패턴.
    path('free/', views.free_board, name='free'),
    
    # 자유게시판 게시글 상세 페이지로 이동하는 URL 패턴.
    path('<int:board_id>/', views.detail, name='detail'),
    
    path('reply/create/<int:board_id>/', views.reply_create, name="reply_create"),
]