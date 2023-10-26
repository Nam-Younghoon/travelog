from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField('제목', max_length=100)
    # body = models.TextField('내용')
    body = RichTextUploadingField('본문', blank=False, null=False)
    thumbnail_image = models.ImageField(
        '썸네일', upload_to='images/%Y/%m/%d/', blank=True, null=True
    )
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, verbose_name='카테고리', 
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
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