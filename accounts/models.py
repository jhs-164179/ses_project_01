
from django.db import models
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

# class UserSession(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False)
#     session_key = models.CharField(max_length=40, editable=False)
#     created_at = models.DateTimeField(auto_now_add=True)

# def kicked_my_other_sessions(sender, request, user, **kwargs):
#     for user_session in UserSession.objects.filter(user=user):
#         session_key = user_session.session_key
#         session = SessionStore(session_key)
#         # session.delete()
#         session['kicked'] = True
#         session.save()
#         user_session.delete()

#     session_key = request.session.session_key
#     UserSession.objects.create(user=user, session_key=session_key)

# user_logged_in.connect(kicked_my_other_sessions, dispatch_uid='user_logged_in')    
