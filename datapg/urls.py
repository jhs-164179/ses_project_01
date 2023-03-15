from django.urls import path

from . import views

app_name = "datapg"
urlpatterns = [
    # path("",views.chart_page, name="datapage"),
    path("",views.data_page, name="datapage"),
    path("pr/",views.pr_pg, name='project'),
    path("pr_2/",views.pr_pg_2, name='project_2'),
    path("items/",views.items, name='items'),
]