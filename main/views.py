 # 메인 페이지 연결 + 검색 기능 테스트

#from .models import Board
from django.shortcuts import render
from django.views import generic
from django.db.models import Q

# Create your views here.

def MainPage(request) :
    return render(request, "main/index.html")

def api(request) :
    return render(request, "main/api.html")

# class BoardSearch(generic.ListView):
    """내장 뷰 클래스인 ListView 클래스를 상속하여 구현한 사용자 정의 뷰 클래스."""

    # paginate_by = 10

    # ListView는 model, queryset, get_queryset() 중 하나를 반드시 작성해야 한다.
    def get_queryset(self):
        # HttpRequest 객체를 통해 전달받은 검색기준 및 검색어를 변수에 저장.
        search_type = self.request.GET.get('searchType', '')
        search_word = self.request.GET.get('searchWord', '')

        result = None  # 응답할 게시글 데이터를 저장할 변수 선언.
        if search_word:  # 검색기준 및 검색어를 전달받은 경우,
            match search_type:
                case 'title':  # 검색기준이 제목인 경우,
                    # 제목에 검색어가 포함되는 게시글 데이터를 선택.
                    result = Board.objects.filter(title__contains=search_word)
                case 'content':  # 검색기준이 내용인 경우,
                    # 내용에 검색어가 포함되는 게시글 데이터를 선택.
                    result = Board.objects.filter(content__contains=search_word)
                case 'writer':  # 검색기준이 작성자인 경우,
                    # 작성자의 사용자 이름에 검색어가 포함되는 게시글 데이터를 선택.
                    result = Board.objects.filter(writer__username__contains=search_word)
                case _: # 간편 검색 기능 구현 
                    result = Board.objects.filter(
                        Q(title__icontains=search_word) |
                        Q(content__icontains=search_word) |
                        Q(writer__username__icontains=search_word)
                    ).distinct()
        else:  # 검색기준 또는 검색어를 전달받지 못한 경우,
            # 모든 게시글 데이터를 선택.
            result = Board.objects.all()

        # 데이터베이스에서 가져온 게시글 데이터를 반환해서 템플릿에 전달.
        return result

    def get_context_data(self, **kwargs):
        # 요청을 통해 전달받은 검색기준 및 검색어를 다시 템플릿으로 전달한다.
        context = super().get_context_data(**kwargs)
        # search_type = self.request.GET.get('searchType', '')
        search_word = self.request.GET.get('searchWord', '')
        if search_word:
            #context['searchType'] = search_type
            context['searchWord'] = search_word
        return context