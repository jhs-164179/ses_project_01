from django.urls import path

from . import views

app_name = "datapg"
urlpatterns = [
    # path("",views.chart_page, name="datapage"),
    path("",views.column_chart, name="datapage"),
    path("db/",views.test),
    path('numcar/', views.add_numcar),
]