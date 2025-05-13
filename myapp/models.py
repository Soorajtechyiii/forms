from django.db import models

class Employee(models.Model):
    empid=models.IntegerField(null=True)
    empname=models.CharField(max_length=100)
    empaddress=models.CharField(max_length=200)
