from django.shortcuts import render
from django.http import HttpResponse
import csv

from .models import NumCar

# Create your views here.
def chart_page(req):
    return render(req, 'datapg/charts.html')

def test(req):
    return render(req, 'datapg/testtt.html')

data = None
file_dir = 'datapg/datafile/'
def read_data(table_name):
    with open(file_dir + f'{table_name}.csv','r',encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        global data
        data = list(reader)
    return

def csv_to_db(table_name, class_name, bulk_list):
    class_name.objects.bulk_create(bulk_list)

    with open(file_dir + f'{table_name}.csv','w',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
    return

def add_numcar(req):
    read_data('numcar')
    if not data:
        return HttpResponse('Nothing to update')

    arr = []
    for row in data:
        arr.append(NumCar(
            age = row[0],
            num_man = row[1],
            num_women = row[2]
        ))
    
    csv_to_db('numcar',NumCar,arr)
    return HttpResponse('NumCar table updated')


def column_chart(req):
    import pymysql
    # 127.0.0.1
    db = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='1234',db='pr_01',charset='utf8')
    cursor = db.cursor()

    with db:
        cursor.execute("USE pr_01")
        cursor.execute("SELECT age, num_man, num_women FROM numcar")
        data1 = cursor.fetchall()

    return render(req, 'datapg/charts.html', {
        'col1_title': '남성',
        'col2_title': '여성',
        'row_data': data1
    })