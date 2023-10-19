from django.db import models
import datetime

class Books(models.Model):
    bookname = models.CharField(max_length=240)
    author = models.CharField(max_length=230)
    published = models.DateField(default=datetime.date.today())
    cost = models.IntegerField(null=True)
