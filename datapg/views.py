from django.shortcuts import render

# Create your views here.
def datapg_pg(req):
    return render(req, 'datapg/charts.html')