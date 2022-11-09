from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def data_page(req):
    import pymysql
    # 127.0.0.1
    db = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='1234',db='hongboard',charset='utf8')
    cursor = db.cursor()
    # datapg_numcar 로 변경
    with db:
        cursor.execute("SELECT age, num_man, num_women FROM numcar")
        data1 = cursor.fetchall()
        cursor.execute("SELECT * FROM numevcar ORDER BY num_evcar DESC")
        data2 = cursor.fetchall()
        cursor.execute("SELECT * FROM numevcar2")
        data3 = cursor.fetchall()
        cursor.execute("SELECT * FROM test1 ORDER BY two DESC")
        data4 = cursor.fetchall()
        cursor.execute("SELECT * FROM test2")
        data5 = cursor.fetchall()
        

    return render(req, 'datapg/charts.html', {
        'col1_title': '남성',
        'col2_title': '여성',
        'row_data': data1,
        'row_data2': data2,
        'row_data3': data3,
        'row_data4': data4,
        'row_data5': data5
    })

def test_pg(req):
    return render(req, 'datapg/testtt.html')