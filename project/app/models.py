from django.db import models

class employee(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    dept= models.CharField(max_length=50)

class add_dept(models.Model):
    department=models.CharField(max_length=50)
    h_department=models.CharField(max_length=50)
    
class querys(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    query=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    status=models.CharField(max_length=90,default='pending')
    admin_reply=models.CharField(max_length=9,blank=True)
    