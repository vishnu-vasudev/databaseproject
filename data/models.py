from statistics import mode
from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.TextField(max_length=20)
    password = models.TextField(max_length=20)

class Department(models.Model):
    dpt_name = models.CharField(max_length=20)

class Student(models.Model):
    stud_name = models.CharField(max_length=20)
    stud_place = models.CharField(max_length=20)
    stud_dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    dob = models.DateField()
    username = models.CharField(max_length=20, default='')
    password = models.CharField(max_length=20, default='')