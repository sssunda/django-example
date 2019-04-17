from django.db import models

# Create your models here.
class Post(models.Model):
    REGION_CHOICE = (
        ('Africa', '아프리카'),
        ('Europe', '유럽'),
        ('Oceania', '오세아니아'),
        ('Asia', '아시아'),
        ('North America', '북아메리카'),
        ('South America', '남아메리카'),
    )
    title = models.CharField(max_length=100, verbose_name = '제목', help_text='포스팅 제목을 입력해주세요. 최대 100자 내외')
    content = models.TextField(verbose_name= '내용')
    region = models.CharField(max_length=20, choices=REGION_CHOICE, default = 'Asia')
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    tag_set = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now = True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name