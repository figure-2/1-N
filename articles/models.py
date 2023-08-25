from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

#댓글 기능을 쓰기 위해 위애 Article과 comment를 연결해 줘야 한다 이걸 관계설정이라고 부른다.
class Comment(models.Model):  # 댓글 기능을 만들어준다.
    content = models.TextField() # 댓글은 제목이 없으니 내용만 넣는 공간을 만들어준다.
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # 내가 연결하고 싶은 모델과 on_deletes는 옵션


    # <용어 설명> 
    # PK : 고유한 값 (ex: id)
    # FK (ForeignKey) : 나의 고유한 값은 아닌데 다른 테이블에 있는 값을 가져와서 저장하는것
