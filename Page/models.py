from django.db import models

# Create your models here.
class Form(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)

