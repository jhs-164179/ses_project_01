from django.urls import path

from .import views

app_name = 'board'
urlpatterns = [
    # 자유게시판 페이지로 이동.
    path('free/', views.FreeBoardListView.as_view(), name='free'),
    
    # 자유게시판에서 글 작성.
    path('write/', views.FreeBoardCreateView.as_view(), name='create'),

    # 공지사항 페이지로 이동.
    path('notice/', views.NoticeBoardListView.as_view(), name='notice'),
    
    # 글 상세 페이지 조회.
    path('<int:pk>/', views.FreeBoardDetailView.as_view(), name='detail'),
    
    # 댓글 작성.
    path('<int:board_id>/reply/write/', views.reply_create, name="reply_create"),

    # 게시글 삭제
    path('<int:pk>/delete/', views.board_delete, name="delete"),

    # 게시글 수정 페이지
    path('<int:pk>/edit/', views.board_edit, name='edit'),

    # 게시글 수정 적용
    path('<int:pk>/edit_complete/', views.edit_complete, name="edit_complete"),

    # 댓글 삭제
    path('<int:pk>/reply_delete/', views.reply_delete, name="reply_delete"),

     # 댓글 수정
    path('<int:pk>/reply_edit/', views.reply_edit, name="reply_edit"),

]