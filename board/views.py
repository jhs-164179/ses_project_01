from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render
from django.db.models import Q

from .models import Board, Reply

# 자유게시판 페이지로 이동.
class FreeBoardListView(generic.ListView):

    # 내가 지정한 템플릿 이름
    template_name = 'board/free_board.html'

    # 페이지 제한 수
    paginate_by = 10

    def get_queryset(self):
        search_type = self.request.GET.get('searchType', '')
        search_word = self.request.GET.get('searchWord', '')

        result = None
        if search_word: # search_type and
            match search_type:
                case 'title':
                    result = Board.objects.filter(title__icontains=search_word)
                case 'content':
                    result = Board.objects.filter(content__icontains=search_word)
                case 'writer':
                    result = Board.objects.filter(writer__username__icontains=search_word)
                case _: # 간편 검색 기능 구현 
                    result = Board.objects.filter(
                        Q(title__icontains=search_word) |
                        Q(content__icontains=search_word) |
                        Q(writer__username__icontains=search_word)
                    ).distinct()
        else:
            result = Board.objects.all()           
        return result.order_by('-date')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_type = self.request.GET.get('searchType','')
        search_word = self.request.GET.get('searchWord','')
        if search_type and search_word:
            context['searchType'] = search_type
            context['searchWord'] = search_word
        return context


class NoticeBoardListView(generic.ListView):

    template_name = 'board/notice_board.html'

    paginate_by = 10

    def get_queryset(self):
        search_type = self.request.GET.get('searchType', '')
        search_word = self.request.GET.get('searchWord', '')

        result = None
        if search_word: # search_type and
            match search_type:
                case 'title':
                    result = Board.objects.filter(title__icontains=search_word)
                case 'content':
                    result = Board.objects.filter(content__icontains=search_word)
        
                case _: # 간편 검색 기능 구현 
                    result = Board.objects.filter(
                        Q(title__icontains=search_word) |
                        Q(content__icontains=search_word)
                    ).distinct()
        else:
            result = Board.objects.filter(writer_id = 2)           
        return result.order_by('-date')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_type = self.request.GET.get('searchType','')
        search_word = self.request.GET.get('searchWord','')
        if search_type and search_word:
            context['searchType'] = search_type
            context['searchWord'] = search_word
        return context


class FreeBoardDetailView(generic.DetailView):
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        board = Board.objects.get(pk=pk)
        board.count += 1
        board.save()
        return Board.objects.filter(pk=pk)


# 자유게시판에서 글 작성.
class FreeBoardCreateView(LoginRequiredMixin, generic.CreateView):
    model = Board
    fields = ['title', 'content']
    login_url = reverse_lazy('user:login')

    template_name = "board/board_form.html"

    def form_valid(self, form):
        form.instance.writer = self.request.user
        form.save()
        return redirect(reverse_lazy('board:free'))


@login_required(login_url=reverse_lazy('user:login'), redirect_field_name='/board/free/')


def reply_create(request, board_id):

    content = request.POST.get('content', '')
    user = request.user
    Reply.objects.create(content=content, writer=user, board_id=board_id)

    return redirect(reverse('board:detail', kwargs={'pk':board_id}))


def board_delete(request, pk) :
    
    board = Board.objects.get(pk=pk)
    board.delete()
    # board.save()
    return redirect(reverse('board:free'))

def board_edit(request, pk) :

    context = {'board' : Board.objects.get(pk = pk)}
    return render(request, 'board/board_edit.html', context)

def edit_complete(request, pk) :

    board = Board.objects.get(pk=pk)
    title = request.POST.get('title', '')
    content = request.POST.get('content', '')
    board.title = title
    board.content = content
    board.save()
    return redirect(reverse('board:detail', kwargs={'pk':pk}))

def reply_delete(request, pk) :
    board_id = request.POST.get('boardid', '')
    reply = Reply.objects.get(pk=pk)
    reply.delete()
    return redirect(reverse('board:detail', kwargs={'pk': board_id }))


def reply_edit(request, pk) :

    reply_id = request.POST.get('replyid', )
    reply = Reply.objects.get(pk=reply_id)
    content = request.POST.get('reply_rewrite_'+reply_id, '')
    print(reply_id)
    print(content)
    reply.content = content
    reply.save()
    return redirect(reverse('board:detail', kwargs={'pk':pk}))