from pyexpat import model
from tkinter import CASCADE
from django.db import models


# Create your models here.
class Seller(models.Model):
    s_name = models.CharField(max_length=20)
    s_email = models.CharField(max_length=40)
    s_password = models.CharField(max_length=20) 

class Product(models.Model):
    pd_name = models.CharField(max_length=20)
    pd_price = models.IntegerField()
    pd_image = models.ImageField(upload_to = 'images/')
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)