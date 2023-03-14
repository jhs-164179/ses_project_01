import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pr_01.settings")

django.setup()

from datapg.models import NumCar, NumEvCar, NumEvCar2, ClusterCenter

data = None
file_dir = 'datapg/datafile/'


def read_data(file_dir, table_name):
    with open(file_dir + f'{table_name}.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        global data
        data = list(reader)
    return


def csv_to_db(table_name, class_name, bulk_list):
    class_name.objects.bulk_create(bulk_list)

    with open(file_dir + f'{table_name}.csv', 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
    return


def add_numcar():
    read_data(file_dir, 'numcar')
    if not data:
        return print('Nothing to update')

    arr = []
    for row in data:
        arr.append(NumCar(
            age=row[0],
            num_man=row[1],
            num_women=row[2]
        ))

    csv_to_db('numcar', NumCar, arr)
    return print('NumCar table updated')


def add_numevcar():
    read_data(file_dir, 'numevcar')
    if not data:
        return print('Nothing to update')

    arr = []
    for row in data:
        arr.append(NumEvCar(
            region=row[0],
            num_evcar=int(float(row[1])),
            percent=int(float(row[2]))
        ))

    csv_to_db('numevcar', NumEvCar, arr)
    return print('NumEvCar table updated')


def add_numevcar2():
    read_data(file_dir, 'numevcar2')
    if not data:
        return print('Nothing to update')

    arr = []
    for row in data:
        arr.append(NumEvCar2(
            region2=row[0],
            num_evcar2=int(float(row[1])),
            percent2=int(float(row[2]))
        ))

    csv_to_db('numevcar2', NumEvCar2, arr)
    return print('NumEvCar table updated')


def add_cluster_center(): # 인덱스 컬럼명은 제외해야 함!
    read_data('datapg/final_data/', 'clustering_center')
    if not data:
        return print('Nothing to update')
    arr = []
    for row in data:
        arr.append(ClusterCenter(
            lng=row[0],
            lat=row[1]
        ))

    csv_to_db('clustercenter', ClusterCenter, arr)
    return print('ClusterCenter table updated')


add_numcar()
add_numevcar()
add_numevcar2()
add_cluster_center()
