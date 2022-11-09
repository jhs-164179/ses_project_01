from django.urls import path

from . import views

app_name = "datapg"

urlpatterns = [
<<<<<<< HEAD
    path("",views.data_page, name="datapage"),    
=======
    # path("",views.chart_page, name="datapage"),
    path("",views.data_page, name="datapage"),
    path("testt/",views.test_pg),
>>>>>>> ccb1ca1d9ca9808b8eae18d310b8cc52cb50322f
]