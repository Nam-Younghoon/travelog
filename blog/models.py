from collections.abc import Iterable
from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField('제목', max_length=100)
    # body = models.TextField('내용')
    body = RichTextUploadingField('본문', blank=False, null=False, help_text='본문내 이미지는 끌어다가 올리거나, 파일 첨부를 클릭하여 올릴 수 있습니다. 이미지가 너무 크지 않게 조절 해주세요')
    thumbnail_image = models.ImageField(
        '썸네일', upload_to='images/%Y/%m/%d/', blank=True, null=True, default='default_gray.png'
    )
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, verbose_name='카테고리', 
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    tags = models.ManyToManyField(
        'Tag', blank=True
    )
    views_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    
class Category(models.Model):
    type = models.CharField(max_length=10)

    def __str__(self):
        return self.type

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name