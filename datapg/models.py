from django.db import models

# Create your models here.
class NumCar(models.Model):
    age = models.CharField(max_length=20)
    num_man = models.IntegerField()
    num_women = models.IntegerField()