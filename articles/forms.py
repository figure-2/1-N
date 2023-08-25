from django import forms
from .models import Article

class ArticleForm(forms.ModelForm): #ArticleFor 안에 ModelForm을 상속시킨다
    class Meta:
        model = Article
        fields = '__all__'


# ModelForm : 폼을 편하게 만들게 해준다
#             내가 보여주고 싶은 

# Meta (클래스) : 예전 필름 카메라를 찍으면 오른쪽 아래 날짜가 찍히는데 
#        그것이 사진의 일정 부분을 가리기 때문에 Meta라고 해서 다른곳에 저장을 한다
#        아이폰에서 사진쯕으로 사진 아래 추가적으로 입력되는 정보라고 생각하면된다.