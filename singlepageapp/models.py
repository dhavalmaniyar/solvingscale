from django.db import models
from django.utils import timezone
# Create your models here.

class Inquiry(models.Model):
    name=models.CharField(max_length=30)
    mobile=models.IntegerField()
    email=models.EmailField(max_length=256)
    inquiry=models.CharField(max_length=50)
    pay=models.CharField(max_length=100)
    need=models.TextField()
    date=models.DateField(default=timezone.now())
