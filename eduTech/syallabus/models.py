from django.db import models
import django

class Books(models.Model):
    bookname = models.CharField(max_length=240)
    author = models.CharField(max_length=230)
    published = models.DateField(default= django.utils.timezone.now)
    cost = models.IntegerField(null=True)
