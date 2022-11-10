# from django.contrib.auth import models as auth_models
# from django.db import models
# from django.utils import timezone


# Create your models here.
# class MainBoard(models.Model):
#     """게시글을 표현하기 위한 모델 클래스."""
#     # verbose_name은 관리자 페이지에서 나타낼 필드 이름 지정임 
#     title = models.CharField(max_length=50, verbose_name='제목')  # 제목.
#     content = models.TextField(max_length=3000, verbose_name='내용')  # 내용.
#     date = models.DateTimeField(default=timezone.now)  # 작성일.
#     count = models.IntegerField(default=0)  # 조회수.
#     mainwriter = models.ForeignKey(auth_models.User, on_delete=models.DO_NOTHING)  # 작성자.
    # writer = models.ForeignKey(auth_models.User, on_delete=models.DO_NOTHING)  # 작성자.

