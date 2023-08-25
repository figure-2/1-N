from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


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
        form = ArticleForm() # 빈종이가 만들고

    context = {
        'form': form,
    } #else 와 if 문에서 다 쓰기 위해 왼쪽으로 이동 

    return render(request, 'form.html', context)