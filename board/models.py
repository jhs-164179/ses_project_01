from django.db import models
from django.utils import timezone
from django.contrib.auth import models as auth_models

class Board(models.Model):
    
    title = models.CharField(max_length=50, verbose_name='제목')
    content = models.TextField(max_length=3000, verbose_name='내용')
    date = models.DateTimeField(default=timezone.now)
    count = models.IntegerField(default=0)
    writer = models.ForeignKey(auth_models.User, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f'{self.title}'

class Reply(models.Model):

    board = models.ForeignKey(Board, on_delete=models.DO_NOTHING)
    content = models.TextField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)
    writer = models.ForeignKey(auth_models.User, on_delete=models.DO_NOTHING)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.board.title}-{self.content}'