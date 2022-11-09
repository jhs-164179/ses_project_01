from django.urls import path

from . import views

app_name = "datapg"

urlpatterns = [
    path("",views.data_page, name="datapage"),    
]