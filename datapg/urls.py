from django.urls import path

from . import views

app_name = "datapg"
urlpatterns = [
    # path("",views.chart_page, name="datapage"),
    path("",views.data_page, name="datapage"),
    path("testt/",views.test_pg),
]