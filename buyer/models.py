from django.db import models
from django.forms import CharField

class Buyer(models.Model):
    email = models.CharField(max_length=30)
    name = models.TextField(max_length=30)
    phone = models.BigIntegerField()
    password = models.CharField(max_length=20)
