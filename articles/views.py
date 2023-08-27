from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'index.html', context)

def create(request):
    # get 요청을 하면 빈종이가 날라온다 그 다음에 post작업을 한다
    # 그러면 create 함수에는 else가 먼저 동작을 하고 if 문이 실행이 된다

        # if문을 get으로 먼저 하는게 아니라 post로 
        # 먼저 받는 이유는 장고에서 delete와 update를 안쓸려고 해서 
        # 공식적으로 지원을 하지 않는다

    if request.method == 'POST': # 데이터를 수정한다?
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')

    else:
        form = ArticleForm()
        # 빈종이가 만들고

    context = {
        'form': form,
    }
    #else 와 if 문에서 다 쓰기 위해 왼쪽으로 이동 
    # else는 form을 출력하는 부분
    # if ansdms data를 저장하는 부분

    return render(request, 'form.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)
    comment_form = CommentForm()

    # comment 목록

    # # 첫번째 방법
    # comment_list = Comment.objects.filter(article=article)
    # # 앞에 있는 article은 article/model.py 의 article에서 가져온것이고 
    # # 뒤에 있는 article은 바로 위에 있는 article에서 가져온것

    # # 두번째 방법
    # comment_list = article.comment_set.all()

    # 세번째 방법
    # html 코드에서 article.comment_set.all 로 사용
    # 추가적으로 line 63번째 주석 처리하고 사용

    context = {
        'article': article,
        'comment_form': comment_form,
        # 'comment_list': comment_list,
    }

    return render(request, 'detail.html', context)

# 댓글을 작성하기 위한 순서
def comment_create(request, article_id):
    # 사용자가 입력한 정보를 form에 입력
    comment_form = CommentForm(request.POST)

    # 유효성 검사
    if comment_form.is_valid():
        # form을 저장 => 추가로 넣어야 하는 데이터를 넣기 위해 저장 멈취! (중간 저장 느낌?)
        comment_form.save(commit=False)


        # 첫번째 방법.
        # # article_id를 기준으로 article objects를 가져와서
        # article = Article.objects.get(id=article_id)
        # # article 컬럼에 추가
        # comment.article = article

        # # 두번째 방법
        # # 사이트 속도 저하를 막기 위해 숫자 값을 하나로 저장하는 방법
        comment.article_id = article_id



        # 저장
        comment.save()

        return redirect('articles:detail', id=article_id)
    
def comment_delete(request, article_id, id):
    comment = Comment.objects.get(id=id)

    comment.delete()

    return redirect('articles:detail', id=article_id)