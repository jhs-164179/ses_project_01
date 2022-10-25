from django.shortcuts import render

# Create your views here.
def chart_page(req):
    return render(req, 'datapg/charts.html')

def map_test(req):
    return render(req, 'datapg/newtest.html')