from django.db import models

# Create your models here.
class loginModel(models.Model):
    email=models.EmailField(max_length=23)
    password=models.CharField(max_length=22)

class registerModel(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=20)