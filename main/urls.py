from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.MainPage, name="index"),
    #path('',TemplateView.as_view(template_name='index.html'))
]