from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(verbose_name="닉네임", max_length=50, unique=True, help_text='닉네임은 고유합니다!')
    email = models.EmailField(verbose_name="이메일", unique=True)




