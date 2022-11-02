from django.db import models
from django.utils import timezone

class Board(models.Model):
    
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=3000)
    date = models.DateTimeField(default=timezone.now)
    count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.title}'

class Reply(models.Model):

    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.board.title}-{self.content}'