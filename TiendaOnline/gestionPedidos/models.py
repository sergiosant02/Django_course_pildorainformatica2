from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()

class Item(models.Model):
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    price = models.IntegerField()

class Order(models.Model):
    name = models.IntegerField()
    date = models.DateField()
    shipped = models.BooleanField()
