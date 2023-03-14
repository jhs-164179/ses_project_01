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
        # cursor.execute("SELECT * FROM test1 ORDER BY two DESC")
        # data4 = cursor.fetchall()
        cursor.execute("SELECT * FROM test2")
        data5 = cursor.fetchall()
        # cursor.execute("SELECT lat,lng FROM clustercenter")
        # data6= cursor.fetchall()
        

    return render(req, 'datapg/charts.html', {
        'col1_title': '남성',
        'col2_title': '여성',
        'row_data': data1,
        'row_data2': data2,
        'row_data3': data3,
        # 'row_data4': data4,
        'row_data5': data5
        # 'row_data6': data6
    })

def pr_pg(req):
    import pymysql
    # 127.0.0.1
    db = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='1234',db='hongboard',charset='utf8')
    cursor = db.cursor()
    
    with db:
        cursor.execute("SELECT lat,lng FROM clustercenter")
        data6= cursor.fetchall()

    return render(req, 'datapg/pr.html', {
        'row_data6': data6
    })

def pr_pg_2(req):
    # 체크박스 형식을 선택하면 컬럼을 선택하여 학습 및 배포할 수 있게끔..
    # if req.method == 'POST':
    #     form = req.POST

    #     print(form)
    #     print(len(form))


    return render(req, 'datapg/pr_2.html')