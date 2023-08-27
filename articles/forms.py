from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm): #ArticleFor 안에 ModelForm을 상속시킨다
    
    class Meta:
        model = Article
        fields = '__all__'

# ModelForm : 폼을 편하게 만들게 해준다
#             내가 보여주고 싶은 

# Meta (클래스) : 예전 필름 카메라를 찍으면 오른쪽 아래 날짜가 찍히는데 
#        그것이 사진의 일정 부분을 가리기 때문에 Meta라고 해서 다른곳에 저장을 한다
#        아이폰에서 사진쯕으로 사진 아래 추가적으로 입력되는 정보라고 생각하면된다.

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
# __all__ 은 
# Comment model에 어울리는 라는 컬럼이 가지고 있는 모든것을 출력하겠다는 의미
        # fields = ('content', )

        exclude = ('article',)

# fields는 필드에 () 추가해서 보여주는것이고 
# exclude는 필드에서 ()를 제거하고 보여주는것