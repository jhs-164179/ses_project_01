from django.db import models

# Create your models here.
class NumCar(models.Model):
    age = models.CharField(max_length=20)
    num_man = models.IntegerField()
    num_women = models.IntegerField()

    class Meta:
        db_table = 'numcar'

class NumEvCar(models.Model): # 전국 단위 전기차 대수
    region = models.CharField(max_length=20)
    num_evcar = models.IntegerField()
    percent = models.IntegerField()

    class Meta:
        db_table = 'numevcar'

class NumEvCar2(models.Model): # 지방 단위 전기차 대수
    region2 = models.CharField(max_length=20)
    num_evcar2 = models.IntegerField()
    percent2 = models.IntegerField()

    class Meta:
        db_table = 'numevcar2'

class Test1(models.Model):
    one = models.CharField(max_length=20)
    two = models.IntegerField()
    
    class Meta:
        db_table = 'test1'

class Test2(models.Model):
    one = models.CharField(max_length=20)
    two = models.IntegerField()
    
    class Meta:
        db_table = 'test2'