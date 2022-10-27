from django.shortcuts import render

# Create your views here.
def chart_page(req):
    return render(req, 'datapg/charts.html')

def test_page(req):
    return render(req, 'datapg/testtt.html')
