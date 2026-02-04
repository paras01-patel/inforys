from django.db import models

class employee(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    dept= models.CharField(max_length=50)
 
 
 