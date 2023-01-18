from django import forms
from board.models import Board

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content']

