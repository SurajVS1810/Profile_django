from django.db import models

# Create your models here.
class home(models.Model):
    name=models.CharField(max_length=2550)
    education=models.CharField(max_length=2550)
    skills=models.CharField(max_length=2550)
    phone=models.CharField(max_length=2550)
    github=models.CharField(max_length=2550)
    email=models.CharField(max_length=2550)
    linkedin=models.CharField(max_length=2550)
    achievment=models.CharField(max_length=2550)
