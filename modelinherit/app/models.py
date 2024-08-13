from django.db import models

# Create your models here.
class MainModel(models.Model):
    Studentname=models.CharField(max_length=100)
    Teachername=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Password=models.CharField(max_length=100)
