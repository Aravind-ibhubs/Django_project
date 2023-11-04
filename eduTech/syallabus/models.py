from django.db import models
import django

class Books(models.Model):
    bookname = models.CharField(max_length=240)
    author = models.CharField(max_length=230)
    published = models.DateField(default= django.utils.timezone.now)
    cost = models.IntegerField(null=True)

class Member(models.Model):
    firstname = models.TextField(max_length=200)
    lastname = models.TextField(max_length=200)
    phone = models.IntegerField(null=True)
    
    def __str__(self):
        return f"{firstname} {lastname}"
    
