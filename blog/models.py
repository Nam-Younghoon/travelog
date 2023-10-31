from collections.abc import Iterable
from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

class Post(models.Model):
    title = models.CharField('제목', max_length=100)
    # body = models.TextField('내용')
    body = RichTextUploadingField('본문', blank=False, null=False, help_text='파일첨부는 이미지만 지원합니다. 본문내 이미지는 끌어다가 올리거나, 툴바에서 올릴 수 있습니다. 이미지가 너무 크지 않게 조절 해주세요 (추천 사이즈 512)')
    thumbnail_image = models.ImageField(
        '썸네일', upload_to='images/%Y/%m/%d/', blank=True, null=True
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
    
    def get_previous(self):
        return self.get_previous_by_created_at()
    
    def get_next(self):
        return self.get_next_by_created_at()
    
class Category(models.Model):
    type = models.CharField(max_length=10)

    def __str__(self):
        return self.type

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments',
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.message
    
class ReplyComment(models.Model):
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='replys'
    )
    reply_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.reply_message
    
    class Meta:
        ordering = ['-created_at']