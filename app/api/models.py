from django.db import models

# Create your models here.


class Xomashyolar(models.Model):
    name=models.CharField(max_length=250)

class Product(models.Model):
    name=models.CharField(max_length=250)
    
    