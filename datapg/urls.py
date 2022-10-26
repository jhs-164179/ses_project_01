from django.urls import path

from . import views

app_name = "datapg"
urlpatterns = [
    path("",views.chart_page),
]