
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from importlib import import_module


# SessionStore = import_module(settings.SESSION_ENGINE).SessionStore

class User(models.Model):
    user_name = models.CharField(max_length=64)
    user_email = models.EmailField(max_length=64)
    user_pw = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'community_user'
        verbose_name = '커뮤니티 사용자'
        verbose_name_plural = '커뮤니티 사용자'

