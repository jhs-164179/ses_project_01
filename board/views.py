from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Board

# class FreeBoardView(request):
    
def free_board(request):
    
    board_list = Board.objects.order_by('-date')
    context = {'board_list' : board_list }

    return render(request, 'board/free_board.html', context)



def detail(request, board_id):

    board = get_object_or_404(Board, pk=board_id)
    context = {'board': board}
    return render(request, 'board/board_detail.html', context)


def reply_create(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    board.reply_set.create(content=request.POST.get('content'), date=timezone.now())
    
    return redirect('board:detail', board_id=board.id)
